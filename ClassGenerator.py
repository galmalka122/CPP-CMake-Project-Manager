import os
from CMakeProjectGenerator import write_file


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


def generate_file_name(folder: str, cls_name: str) -> list[str]:

    if folder == '':
        return [0, 'Please select a folder.']

    if 'src' not in os.listdir(folder) or 'include' not in os.listdir():
        return [0, 'src/include directory is missing']

    if cls_name == '':
        return [0, 'Please enter a filename.']

    filename = ' '.join(word.capitalize() for word in cls_name.split(' '))

    if filename + '.h' in os.listdir('./include'):
        return [0, filename + '.h already exists.']

    return [1, filename]


def generate_class(folder, cls_name):

    state, content = generate_file_name(folder.get(), cls_name.get())

    if state == 0:
        raise FileExistsError(content)

    write_file(folder + '/include/' + content + '.h', generate_header_content(content))
    write_file(folder + '/src/' + content + '.cpp', generate_source_content(content))