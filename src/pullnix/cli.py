from pathlib import Path

from . import repository
from .config import load_config


def ensure_root_dir(root):
    if not root.exists():
        root.mkdir()


def ensure_updated_repo(repo, root):
    updated = False
    changed_files = []

    repo_path = root / repo.name
    if not repo_path.exists():
        repository.clone(repo, repo_path)
        updated = True
    else:
        changed_files = repository.update(repo, repo_path)
        if changed_files:
            updated = True
    return changed_files, updated


def cli(config_path="/etc/pullnix.yml"):
    config = load_config(config_path)

    root = Path(config.root)

    ensure_root_dir(root)

    for repo in config.repos:
        changed_files, updated = ensure_updated_repo(repo, root)
        print(f"updated: {updated}, changed files: {', '.join(changed_files)}")
