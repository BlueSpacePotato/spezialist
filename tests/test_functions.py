import os
import pytest
from spezialist import (
    list_dir_without_ds_abs,
    list_dir_without_ds,
    list_dir_without_dot_abs,
    list_dir_without_dot,
)

def create_files(tmp_path, files):
    """
Helper to create given filenames in tmp_path.
    """
    for name in files:
        file_path = tmp_path / name
        file_path.write_text(f"content of {name}")
    return tmp_path

@pytest.fixture
def sample_dir(tmp_path):
    # Create a mix of normal, hidden, and DS_Store files
    files = ['file1.txt', '.hiddenfile', '.DS_Store', 'file2.log', '.venv']
    return create_files(tmp_path, files)


def test_list_dir_without_ds(tmp_path, sample_dir):
    # Filenames without .DS_Store
    expected = ['file1.txt', '.hiddenfile', 'file2.log', '.venv']
    result = list_dir_without_ds(str(sample_dir))
    assert sorted(result) == sorted(expected)


def test_list_dir_without_ds_abs(sample_dir):
    # Absolute paths without .DS_Store
    result = list_dir_without_ds_abs(str(sample_dir))
    # All returned paths should not end with .DS_Store
    assert all(not p.lower().endswith('.ds_store') for p in result)
    # Should include file1.txt and file2.log, but not .DS_Store
    basenames = [os.path.basename(p) for p in result]
    assert 'file1.txt' in basenames
    assert 'file2.log' in basenames
    assert '.DS_Store' not in basenames


def test_list_dir_without_dot(tmp_path, sample_dir):
    # Filenames without hidden files
    expected = ['file1.txt', 'file2.log']
    result = list_dir_without_dot(str(sample_dir))
    assert sorted(result) == sorted(expected)


def test_list_dir_without_dot_abs(sample_dir):
    # Absolute paths without hidden files
    result = list_dir_without_dot_abs(str(sample_dir))
    # No returned path should have basename starting with .
    basenames = [os.path.basename(p) for p in result]
    assert all(not name.startswith('.') for name in basenames)
    # Should include file1.txt and file2.log
    assert 'file1.txt' in basenames
    assert 'file2.log' in basenames