import os
import subprocess
import json

PROJECT_DIR = os.path.abspath(os.path.curdir)
REPO_URL = '{{cookiecutter.repo_url}}'
COMPUTE_TYPE = '{{cookiecutter.default_compute}}'
CLONE_DIR = os.path.join(PROJECT_DIR, 'cloned_repo')

# Clone external repo
def clone_repo():
	subprocess.run(['git', 'clone', REPO_URL, CLONE_DIR], check=True)

# Read clusters from cloned repo (adjust path as needed)
def get_clusters():
	clusters_file = os.path.join(CLONE_DIR, 'clusters.json')
	clusters = []
	if os.path.exists(clusters_file):
		with open(clusters_file) as f:
			clusters = json.load(f)
	return clusters

# Generate jobs file based on compute type
def generate_jobs(clusters):
	jobs_path = os.path.join(PROJECT_DIR, 'jobs.yml')
	if COMPUTE_TYPE == 'serverless':
		with open(jobs_path, 'w') as f:
			f.write('jobs:\n  - type: serverless\n')
	else:
		with open(jobs_path, 'w') as f:
			f.write('jobs:\n')
			for cluster in clusters:
				f.write(f"  - type: cluster\n    id: {cluster['id']}\n")

if __name__ == "__main__":
	clone_repo()
	clusters = get_clusters()
	generate_jobs(clusters)
