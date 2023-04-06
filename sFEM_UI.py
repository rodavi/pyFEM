import tkinter as tk
from tkinter import ttk
import mesh
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure


class sFEMui:

    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title("Simple FEM solver UI v0.1")

        self.theme = ttk.Style()
        #print(self.theme.theme_names())
        self.theme.theme_use("winnative")
        self.__add_menus()
        self.__add_workspace()
        self.__add_treeview()
        self.__add_statebar()

        self.root.grid_columnconfigure(0, weight=0)
        self.root.grid_columnconfigure(1, weight=10)
        self.root.grid_rowconfigure(0, weight=10)
        self.root.grid_rowconfigure(1, weight=0)
    
    def run(self):
        self.root.mainloop()

    def __add_menus(self):
        self.main_menu = sMenu(self.root)
        m_file = self.main_menu.create_tab("File")
        m_edit = self.main_menu.create_tab("Edit")
        m_help = self.main_menu.create_tab("Help")

        self.main_menu.add_command(m_file, "New", shortcut="Ctrl+N")
        self.main_menu.add_separator(m_file)
        self.main_menu.add_command(m_file, "Exit", command= lambda : self.root.destroy())
        self.main_menu.add_command(m_help, "Info", shortcut="Ctrl+I")

    def __add_workspace(self):
        Workspace(self.root, 1, 0)

    def __add_treeview(self):
        HierarchyTree(self.root, 0, 0)

    def __add_statebar(self):
        StateBar(self.root, 0, 1)

class sMenu(tk.Frame):

    def __init__(self, master) -> None:
        self.root = master
        self.main_menu = tk.Menu(self.root)
        self.root.config(menu=self.main_menu)
    
    def create_tab(self, name):
        self.new_menu = tk.Menu(self.main_menu, tearoff=False)
        self.main_menu.add_cascade(menu=self.new_menu, label=name)

        self.root.config(menu=self.main_menu)
        return self.new_menu
    
    def add_command(self, tab, name, command=lambda : "", shortcut=""):
        tab.add_command(
            label=name,
            accelerator=shortcut,
            command=command
        )
    
    def add_separator(self, tab):
        tab.add_separator()


class Workspace(tk.Frame):

    def __init__(self, master, x, y) -> None:
        self.root = master
        self.f_workspace = tk.Frame(self.root, relief=tk.SUNKEN)
        self.f_workspace.grid(column=x, row=y, sticky=tk.N+tk.S+tk.W+tk.E, padx=1, pady=1)
        self.c_workspace = tk.Canvas(self.f_workspace, bg="lightgrey", width=600, height=500)
        self.c_workspace.grid(column=0, row=0, sticky=tk.N+tk.S+tk.W+tk.E, padx=1, pady=1)
        self.f_workspace.grid_columnconfigure(0, weight=1)
        self.f_workspace.grid_rowconfigure(0, weight=1)


class HierarchyTree(tk.Frame):

    def __init__(self, master, x, y) -> None:
        self.root = master
        self.f_hierarchy_tree = tk.Frame(self.root)
        self.f_hierarchy_tree.grid_rowconfigure(0, weight=1)
        self.f_hierarchy_tree.grid(column=x, row=y, sticky=tk.N+tk.S+tk.W+tk.E, padx=1, pady=1)
        self.t_hierarchy = ttk.Treeview(self.f_hierarchy_tree)
        self.t_hierarchy.grid(column=0, row=0, sticky=tk.N+tk.S+tk.W+tk.E, padx=1, pady=1)

        self.s_vertical = tk.Scrollbar(self.f_hierarchy_tree, orient="vertical")
        self.s_vertical.grid(column=1, row=0, sticky=tk.N+tk.S+tk.W+tk.E)

        self.t_hierarchy.config(yscrollcommand=self.s_vertical.set)

        self.s_horizontal = tk.Scrollbar(self.f_hierarchy_tree, orient="horizontal")
        self.s_horizontal.grid(column=0, row=1, sticky=tk.N+tk.S+tk.W+tk.E)

        self.t_hierarchy.config(xscrollcommand=self.s_horizontal.set)

class StateBar(tk.Frame):

    def __init__(self, master, x, y) -> None:
        self.root = master
        self.f_statebar = tk.LabelFrame(self.root, text="")
        self.f_statebar.grid_columnconfigure(0, weight=1)
        self.f_statebar.grid(column=x, row=y, sticky=tk.N+tk.S+tk.W+tk.E, padx=1, pady=1, columnspan=2)
        self.v_state = tk.StringVar()
        self.e_state = tk.Entry(self.f_statebar, state="readonly", textvariable=self.v_state)
        self.e_state.grid(column=0, row=0, sticky=tk.N+tk.S+tk.W+tk.E)
        self.e_state.grid_columnconfigure(0, weight=1)
        self.e_state.grid_rowconfigure(0, weight=2)

    def set_state(self, state):
        self.v_state.set(state)

    def get_state(self):
        return self.v_state.get()
