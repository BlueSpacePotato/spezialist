import os

def list_dir_without_ds_abs(path: str):
    """
    List directory contents excluding any '.DS_Store' files, returning absolute paths.

    :param path: Filesystem path to the target directory.
    :type path: str
    :return: List of absolute paths for all entries in the directory, excluding '.DS_Store'.
    :rtype: list[str]
    """
    return [os.path.join(path, f) for f in os.listdir(path) if f.lower() != '.ds_store']


def list_dir_without_ds(path: str):
    """
    List directory contents excluding any '.DS_Store' files, returning filenames.

    :param path: Filesystem path to the target directory.
    :type path: str
    :return: List of filenames in the directory, excluding '.DS_Store'.
:rtype: list[str]
    """
    return [f for f in os.listdir(path) if f.lower() != '.ds_store']


def list_dir_without_dot_abs(path: str):
    """
List directory contents excluding hidden files (starting with '.'), returning absolute paths.

:param path: Filesystem path to the target directory.
:type path: str
:return: List of absolute paths for all non-hidden entries in the directory.
:rtype: list[str]
    """
    return [os.path.join(path, f) for f in os.listdir(path) if not f.startswith('.')]


def list_dir_without_dot(path: str):
    """
List directory contents excluding hidden files (starting with '.'), returning filenames.

:param path: Filesystem path to the target directory.
:type path: str
:return: List of filenames in the directory, excluding hidden files.
:rtype: list[str]
    """
    return [f for f in os.listdir(path) if not f.startswith('.')]
    