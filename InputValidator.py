import os
from typing import LiteralString


class InvalidInputException(Exception):
    pass


def validate_folder_path(folder_path: LiteralString | str | bytes) -> None:
    """
    Validate the selected folder path.

    Args:
        folder_path (LiteralString | str | bytes): The selected folder path.

    Returns:
        bool: True if the folder path is valid, False otherwise.
        str: Error message if validation fails.
    """
    if not folder_path:
        raise InvalidInputException('Please select a folder.')

    if not os.path.isdir(folder_path):
        raise InvalidInputException('The selected path is not a valid directory.')


def validate_input_text(input_text: str) -> None:
    """
    Validate the input text

    Args:
        input_text (str): The input text to be validated

    Returns:
        bool: True if the input text is not empty, nor contains special characters.
        str: Error message if validation fails, Otherwise empty string.
    """
    if not input_text or not input_text.isalnum():
        raise InvalidInputException('Please enter a valid name.')


def validate_class_name(project_path: LiteralString | str | bytes, class_name: str) -> str:
    """
    Validate the entered name.

    Args:
        project_path (LiteralString | str | bytes): The path to the project's root folder.
        class_name (str): The entered class name.

    Returns:
        bool: True if the class name is valid, False otherwise.
        str: Error message if validation fails, Otherwise the filename string.
    """
    class_file_name = ''.join(word.capitalize() for word in class_name.split(' '))

    validate_input_text(class_file_name)
    validate_cmake_folder(str(project_path))
    if class_file_name + '.h' in os.listdir(str(project_path.join('include'))):
        raise InvalidInputException('The class is already exist.')

    return class_file_name


def validate_project_creation(project_path: LiteralString | str | bytes, project_name: str) -> None:
    """
    Validate if the entered project name could be created.

    Args:
        project_path (LiteralString | str | bytes): The path to the project's root folder.
        project_name (str): The entered project name.

    Returns:
        bool: True if the project name is valid, False otherwise.
        str: Error message if validation fails.
    """
    validate_input_text(project_name)
    validate_folder_path(project_path)


def validate_cmake_folder(folder_path: str) -> None:
    """
    Validates that the folder contains src and include folders,
    and each contains a CMakeLists.txt file.

    Args:
        folder_path (str): The path to the project's main folder.

    Returns:
        bool: True if the folder is a CMake project, False otherwise.
        str: Error message if validation fails, Empty string otherwise.
    """
    if 'src' not in os.listdir(folder_path) or 'include' not in os.listdir(folder_path):
        raise InvalidInputException('Missing src or include folders.')

    if ('CMakeLists.txt' not in os.listdir(folder_path) or 'CMakeLists.txt' not in os.listdir(os.path.join(folder_path,
                                                                                                           'include')) or
            'CMakeLists.txt' not in os.listdir(os.path.join('src'))):
        raise InvalidInputException('Missing CMakeLists.txt file.')
