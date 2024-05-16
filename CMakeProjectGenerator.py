from FileUtils import write_file, create_directory


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


def generate_include_cmake_lists(project_name):
    return f'''\
target_include_directories({project_name} PRIVATE ${{CMAKE_CURRENT_LIST_DIR}})
'''


def generate_project(project_name, project_path):
    try:
        project_file_name = project_name.get().title().replace(' ', '')

        # The main folder where all project files stored
        root_folder = project_path.join(project_file_name)

        # Generate all folders
        create_directory(root_folder)
        create_directory(root_folder.join('include'))
        create_directory(root_folder.join('src'))
        create_directory(root_folder.join('resources'))

        try:
            # Create CMakeLists.txt file for each folder.
            write_file(root_folder.join('CMakeLists.txt'), generate_cmake_lists(project_file_name))
            write_file(root_folder.join('src', 'CMakeLists.txt'), generate_source_cmake_lists(project_file_name))
            write_file(root_folder.join('include', 'CMakeLists.txt'), generate_include_cmake_lists(project_file_name))
            write_file(root_folder.join('resources', 'CMakeLists.txt'), '')

            # Create main.cpp file.
            write_file(root_folder.join('src', 'main.cpp'), generate_main())

        except OSError as e:
            raise ProjectGenerationError(f"Error creating project: {str(e)}")

    except Exception as e:
        raise ProjectGenerationError(f"An unexpected error occurred: {str(e)}")


class ProjectGenerationError(Exception):
    pass
