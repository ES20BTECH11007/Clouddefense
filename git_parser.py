import github
from github import Github
import xml.etree.ElementTree as ET

g = Github('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')

user = g.get_user('ES20BTECH11007')
repos = user.get_repos()

for repo in repos:
  try:
    pom_files = [f for f in repo.get_contents("") if f.name.lower() == "pom.xml"]
    if not pom_files:
        print("There are no pom.xml files in the repository")
    else:
        for pom_file in pom_files:
            contents = pom_file.decoded_content.decode('utf-8')
            root = ET.fromstring(contents)
            
            for dependency in root.findall('.//{http://maven.apache.org/POM/4.0.0}dependency'):
                group_id = dependency.find('{http://maven.apache.org/POM/4.0.0}groupId').text
                artifact_id = dependency.find('{http://maven.apache.org/POM/4.0.0}artifactId').text
                version_elem = dependency.find('{http://maven.apache.org/POM/4.0.0}version')
                version = version_elem.text if version_elem is not None else "No version specified"
                print(f"{group_id}:{artifact_id} - Version {version}")
  except github.GithubException as e:
      print(f"Error accessing repository")