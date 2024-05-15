from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter.ttk import Combobox
import os
from ClassGenerator import generate_class
from CMakeProjectGenerator import generate_project


def get_folder_path():
    """
    Open a file dialog to select a folder and set the folder path.

    Returns:
        None
    """
    selected_folder = filedialog.askdirectory(initialdir=os.getcwd())
    if selected_folder != '':
        folder_path_var.set(selected_folder)


def create():
    """
    Create either a project or a class based on the selected option.

    Returns:
        None
    """
    selected_folder = folder_path_var.get()
    class_name_value = class_name_var.get()
    selected_option = selection_var.get()

    if selected_option == 0:
        try:
            generate_project(folder_path_var, class_name_var)
            messagebox.showinfo("Success", f"Directory '{selected_folder}' created successfully.")
        except FileExistsError:
            messagebox.showerror("Error", f"Directory '{selected_folder}' already exists.")
    else:
        try:
            generate_class(folder_path_var, class_name_var)
            messagebox.showinfo("Class " + class_name_value, "created successfully")
        except Exception as e:
            messagebox.showerror("Error", e.args[0])


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
        selection_var.set(index)
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
    selected_option = selection_var.get()
    option_string = "Project" if selected_option == 0 else "Class"

    clear_window()

    back_to_menu_button = Button(root, text="Back To Menu", command=menu)
    back_to_menu_button.pack(pady=5)
    window_widgets.append(back_to_menu_button)

    class_label = Label(root, text=option_string + " Name:")
    class_label.pack()
    window_widgets.append(class_label)

    class_name_entry = Entry(root, textvariable=class_name_var)
    class_name_entry.pack(pady=5)
    window_widgets.append(class_name_entry)

    folder_label = Label(root, text="Folder Path:")
    folder_label.pack()
    window_widgets.append(folder_label)

    folder_path_entry = Entry(root, textvariable=folder_path_var)
    folder_path_entry.pack(pady=5)
    window_widgets.append(folder_path_entry)

    folder_button = Button(root, text="Browse", command=get_folder_path)
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
    folder_path_var = StringVar(value=os.getcwd())
    class_name_var = StringVar(value="")
    selection_var = IntVar(value=0)
    main()
