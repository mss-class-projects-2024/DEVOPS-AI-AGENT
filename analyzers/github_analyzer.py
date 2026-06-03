import tempfile
import shutil
from git import Repo


def clone_repository(repo_url):
    temp_dir = tempfile.mkdtemp()

    print(f"\nCloning Repository...")
    Repo.clone_from(repo_url, temp_dir)

    print("Clone Successful")

    return temp_dir


def cleanup_repository(repo_path):
    shutil.rmtree(repo_path, ignore_errors=True)