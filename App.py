from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter.ttk import Combobox
import os
from ClassGenerator import generate_class
from CMakeProjectGenerator import generate_project


def set_folder_path() -> None:
    """
    Open a file dialog to select a folder and set the folder path.

    Returns:
        None
    """
    input_folder = filedialog.askdirectory(initialdir=os.getcwd())
    if input_folder != '':
        selected_folder.set(input_folder)


def create() -> None:
    """
    Create either a project or a class based on the selected option.

    Returns:
        None
    """
    try:
        if selected_option.get() == 0:
            generate_project(selected_folder, text_input)
            messagebox.showinfo("Success", f"Directory '{selected_folder.get()}' created successfully.")

        else:
            generate_class(selected_folder, text_input)
            messagebox.showinfo("Class " + text_input.get(), "created successfully")

    except Exception as e:
        messagebox.showerror("Error", e.args[0])

    except FileExistsError:
        messagebox.showerror("Error", f"Directory '{selected_folder.get()}' already exists.")


def clear_window() -> None:
    """
    Clear all widgets from the window.

    Returns:
        None
    """
    for widget in window_widgets:
        widget.destroy()


def menu():
    """
    Display the menu options.

    Returns:
        None
    """
    clear_window()

    option_label = Label(root, text="Select Option")
    option_label.pack(pady=5)

    options = ["Create Project", "Create Class"]

    selected_option_var = StringVar()

    option_combobox = Combobox(root, textvariable=selected_option_var, values=options, state="readonly")
    option_combobox.pack(pady=10)

    def on_create():
        index = options.index(option_combobox.get())
        selected_option.set(index)
        set_visuals()

    create_button = Button(root, command=on_create, text="Create")
    create_button.pack(pady=5)
    window_widgets.append(option_combobox)
    window_widgets.append(create_button)
    window_widgets.append(option_label)


def set_visuals():
    """
    Set up the visual elements based on the selected option.

    Returns:
        None
    """
    option_string = "Project" if selected_option.get() == 0 else "Class"

    clear_window()

    back_to_menu_button = Button(root, text="Back To Menu", command=menu)
    back_to_menu_button.pack(pady=5)
    window_widgets.append(back_to_menu_button)

    class_label = Label(root, text=option_string + " Name:")
    class_label.pack()
    window_widgets.append(class_label)

    class_name_entry = Entry(root, textvariable=text_input)
    class_name_entry.pack(pady=5)
    window_widgets.append(class_name_entry)

    folder_label = Label(root, text="Folder Path:")
    folder_label.pack()
    window_widgets.append(folder_label)

    folder_path_entry = Entry(root, textvariable=selected_folder)
    folder_path_entry.pack(pady=5)
    window_widgets.append(folder_path_entry)

    folder_button = Button(root, text="Browse", command=set_folder_path)
    folder_button.pack(pady=5)
    window_widgets.append(folder_button)

    create_button = Button(root, text="Create " + option_string, command=create)
    create_button.pack(pady=10)
    window_widgets.append(create_button)


def main():
    """
    Run the main application.

    Returns:
        None
    """
    root.title("Menu")
    menu()
    root.mainloop()


if __name__ == "__main__":
    window_widgets = []
    root = Tk()
    selected_folder = StringVar(value=os.getcwd())
    text_input = StringVar(value="")
    selected_option = IntVar(value=0)
    main()
