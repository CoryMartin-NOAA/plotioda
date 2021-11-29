import os


def get_full_path(filepath):
    """
    Returns absolute path of file regardless of if
    user YAML input contains absolute or relative path.

    Will fail if path does not exist.

    Args:
        filepath: string path to desired file
    """

    cwd = os.getcwd()
    cwdpath = os.path.join(cwd, filepath)

    if os.path.exists(os.path.dirname(filepath)):
        fullpath = filepath
    elif os.path.exists(os.path.dirname(cwdpath)):
        fullpath = cwdpath
    else:
        raise OSError("Not a valid path.")

    return fullpath
