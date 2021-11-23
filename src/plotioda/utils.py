import os


def get_full_path(filepath)
    """
    Returns absolute path of file regardless of if
    user YAML input contains absolute or relative path.

    Will fail if path does not exist.

    Args:
        filepath: string path to desired file
    """

    cwd = os.getcwd()
    cwdpath = os.path.join(cwd, filepath)

    if os.path.exists(filepath):
        fullpath = filepath
    elif os.path.exists(cwdpath):
        fullpath = cwdpath
    else:
        raise OSError("File not found.")

    return fullpath
