import os


def save_file(filename: str, data: bytes) -> None:
    """Save a file to the local directory."""
    with open(filename, "wb") as out:
        out.write(data)


def delete_file(filename: str) -> None:
    """Delete a file from the local directory."""
    os.remove(filename)
