import time
from abc import ABC, abstractmethod
from tempfile import mkdtemp

from core.db.documents import BaseDocument
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class BaseCrawler(ABC):
    model: type[BaseDocument]

    @abstractmethod
    def extract(self, link: str, **kwargs) -> None: ...