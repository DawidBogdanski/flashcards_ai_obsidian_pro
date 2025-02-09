import os

from app.models.note_models import Note
from app.notes_reader.notes_loader_abc import NotesLoaderABC


class NotesLoader(NotesLoaderABC):
    def __init__(self, folder_path: str) -> None:
        self._folder_path = folder_path

    @property
    def folder_path(self) -> str:
        return self._folder_path

    @folder_path.setter
    def folder_path(self, folder_path: str) -> None:
        self._folder_path = folder_path

    def load(self) -> list[Note]:
        notes = []

        for filename in os.listdir(self.folder_path):
            if filename.endswith(".md"):
                file_path = os.path.join(self.folder_path, filename)
                with open(file_path, "r", encoding="utf-8") as file:
