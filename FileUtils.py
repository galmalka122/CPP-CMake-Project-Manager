import os
from typing import LiteralString


def write_file(file_path: LiteralString | str | bytes, content: LiteralString | str | bytes) -> None:
    with open(file_path, 'w') as out_file:
        out_file.write(content)


def create_directory(directory_name: LiteralString | str | bytes) -> None:
    os.makedirs(directory_name)