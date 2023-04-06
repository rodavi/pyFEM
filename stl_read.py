import numpy as np
from stl import mesh
from mpl_toolkits import mplot3d
from matplotlib import pyplot
from pathlib import Path
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure


class STLFile:

    def __init__(self, path) -> None:

        self.complete_path = path
        self.mesh = mesh.Mesh.from_file(self.complete_path)

    def show_canvas(self):
        pass

    def show_plt(self):
        # Create a new plot
        self.figure = pyplot.figure()
        self.axes = self.figure.add_subplot(projection='3d')

        self.axes.add_collection3d(mplot3d.art3d.Poly3DCollection(self.mesh.vectors))
        self.axes.grid(False)
        # Auto scale to the mesh size
        scale = self.mesh.points.flatten()
        self.axes.auto_scale_xyz(scale, scale, scale)

        # Show the plot to the screen
        pyplot.show()

path_s = r"\\americas.bmw.corp\homeshare\Mexico\SLP\User\Q502704"
name_s = "/pinza_mitad.stl"
complet_path_s = path_s+name_s
complete_path = Path(complet_path_s)

stl = STLFile(complete_path)
stl.show_plt()