import os


def generate_cmake_lists(project_name):
    return f'''\
cmake_minimum_required(VERSION 3.16)
project({project_name} LANGUAGES CXX)

set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${{CMAKE_BINARY_DIR}}/bin)
option(BUILD_SHARED_LIBS "Build shared libraries" OFF)

add_executable({project_name} src/main.cpp)
target_compile_features({project_name} PRIVATE cxx_std_17)

add_subdirectory(src)
add_subdirectory(include)
add_subdirectory(resources)

add_custom_command(TARGET {project_name} POST_BUILD
                   COMMAND ${{CMAKE_COMMAND}} -E copy_directory
                       ${{CMAKE_SOURCE_DIR}}/resources $<TARGET_FILE_DIR:{project_name}>/resources)

install(TARGETS {project_name})
'''


def generate_source_cmake_lists(project_name):
    return f'''\
target_sources({project_name} PRIVATE	"main.cpp")
'''


def generate_main():
    return f'''\
#include <iostream>

using namespace std;

int main(){{
    
    cout << "Hello World!" << endl;
    
    return 0;
    
}}    
'''


def generate_includes_cmake_lists(project_name):
    return f'''\
target_include_directories({project_name} PRIVATE ${{CMAKE_CURRENT_LIST_DIR}})
'''


def write_file(name: str, content: str) -> None:
    with open(name, 'w') as out_file:
        out_file.write(content)


def generate_directory(directory_name):
    os.makedirs(directory_name)


def generate_project(project_name, path_name):

    path = path_name.get()
    project_file_name = project_name.get().title().replace(' ', '')

    # Create root folder with CMakeLists.txt file.
    root_folder = str(os.path.join(path, project_file_name))
    generate_directory(root_folder)
    write_file(str(os.path.join(root_folder, 'CMakeLists.txt')), generate_cmake_lists(project_file_name))

    # Create source folder with main and CMakeLists.txt file.
    src_folder = str(os.path.join(path, project_file_name, 'src'))
    generate_directory(src_folder)
    write_file(str(os.path.join(src_folder, 'CMakeLists.txt')), generate_source_cmake_lists(project_file_name))
    write_file(str(os.path.join(src_folder, 'main.cpp')), generate_main())

    # Create includes folder with CMakeLists.txt file.
    include_folder = str(os.path.join(path, project_file_name, 'include'))
    generate_directory(include_folder)
    write_file(str(os.path.join(include_folder, 'CMakeLists.txt')), generate_includes_cmake_lists(project_file_name))

    # Create includes folder with CMakeLists.txt file.
    resources_folder = str(os.path.join(path, project_file_name, 'resources'))
    generate_directory(resources_folder)
    write_file(str(os.path.join(resources_folder, 'CMakeLists.txt')), '')
