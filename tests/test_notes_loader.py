from io import StringIO

import pytest

from app.notes_reader.notes_loader import MarkdownNotesLoader


@pytest.fixture(scope="session")
def folder_dir():
    return 42


@pytest.fixture(scope="session")
def note_docker():
    return """
    # Docker

    Multiline Content
    Multiline Content

    #docker#pytest #python
    """


@pytest.fixture(scope="session")
def file_md(note_docker):
    return StringIO(note_docker)


def test_tags_are_normalized():
    tags = ["python", "#pytest", "#python", "Python", "  docker"]

    nl = MarkdownNotesLoader('.', tags)

    assert nl.tags == {"#python", "#pytest", "#docker"}


def test_find_tags_in_multiline_note(note_docker):
    nl = MarkdownNotesLoader('.', [])
    found_tags = nl._MarkdownNotesLoader__find_tags(note_docker)
    assert found_tags == {"#docker", "#pytest", "#python"}