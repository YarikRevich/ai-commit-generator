import platform

def get_logger_path() -> str:
    """
    Returns a path for the logger specifically
    for the local OS
    """
    os = platform.system()
    if os == "Darwin":
        pass
    elif os == "Linux":
        pass
    elif os == "Windows":
        pass
