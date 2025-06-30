import tempfile
from pathlib import Path

import git
from aws_lambda_powertools import Logger

from core.db.document import RepositoryDocument
from .base import BaseCrawler

logger = Logger(service="llm-twin-course/crawler")


class GithubCrawler(BaseCrawler):
    model = RepositoryDocument

    def __init__(self, ignore_dirs=None, ignore_exts=None) -> None:
        super().__init__()
        if ignore_dirs is None:
            ignore_dirs = {".git", ".idea", "__pycache__"}
        if ignore_exts is None:
            ignore_exts = {".lock", ".png", ".jpg", ".jpeg", ".gif", ".ico"}
        self._ignore_dirs = set(ignore_dirs)
        self._ignore_exts = set(ignore_exts)

    def extract(self, link: str, **kwargs) -> None:
        logger.info(f"Starting scrapping GitHub repository: {link}")
        repo_name = link.rstrip("/").split("/")[-1]

        with tempfile.TemporaryDirectory() as local_temp:
            repo_path = Path(local_temp) / repo_name
            try:
                logger.info(f"Cloning {link} into {repo_path}")
                git.Repo.clone_from(link, repo_path)

                tree = {}
                for item in repo_path.rglob("*"):
                    if any(part in self._ignore_dirs for part in item.parts):
                        continue

                    if item.is_file() and item.suffix not in self._ignore_exts:
                        relative_path = str(item.relative_to(repo_path))
                        try:
                            with item.open("r", encoding="utf-8", errors="ignore") as f:
                                tree[relative_path] = f.read()
                        except Exception as e:
                            logger.warning(f"Could not read file {item}: {e}")

                if not tree:
                    logger.warning(f"No files were extracted from repository: {link}")
                    return

                instance = self.model(
                    name=repo_name, link=link, content=tree, owner_id=kwargs.get("user")
                )
                instance.save()
                logger.info(
                    f"Successfully saved repository {repo_name} to the database."
                )

            except git.GitCommandError as e:
                logger.error(f"Failed to clone repository {link}: {e}")
                raise
            except Exception as e:
                logger.error(
                    f"An unexpected error occurred during crawling of {link}: {e}"
                )
                raise

        logger.info(f"Finished scrapping GitHub repository: {link}")