from abc import ABC, abstractmethod

from app.models.note_models import Note


class NotesLoaderABC(ABC):
    @property
    @abstractmethod
    def folder_path(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def load(self) -> list[Note]:
        raise NotImplementedError


