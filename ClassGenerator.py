import os
from FileUtils import write_file
from InputValidator import validate_class_name


def generate_header_content(name: str) -> str:
    return f'''#ifndef {name.capitalize() + '_h'}
#define {name.capitalize() + '_h'}

class {name + '{'}

public:

    {name}() = default;
    ~{name}() = default;

{'};'}

#endif // !{name.capitalize() + '_h'}
'''


def generate_source_content(name: str) -> str:
    return f'''#include "{name + '.h'}"

'''


class ClassGenerationError(Exception):
    pass


def generate_class(folder, class_name):
    try:
        class_filename = validate_class_name(folder.get(), class_name.get())

        header_content = generate_header_content(class_filename)
        source_content = generate_source_content(class_filename)

        # Construct file paths using os.path.join
        header_file_path = os.path.join(folder.get(), 'include', class_filename + '.h')
        source_file_path = os.path.join(folder.get(), 'src', class_filename + '.cpp')

        try:
            write_file(header_file_path, header_content)
            write_file(source_file_path, source_content)

        except OSError as e:
            raise ClassGenerationError(f"Error writing files: {str(e)}")

    except Exception as e:
        raise ClassGenerationError(str(e))
