from abc import ABC, abstractmethod
from typing import Any


class Report(ABC):
    @abstractmethod
    def generate(self, data: Any) -> Any:
        pass

    @abstractmethod
    def display(self, data: Any) -> None:
        pass

    @abstractmethod
    def save(self, data: Any, output_filename: str) -> None:
        pass
