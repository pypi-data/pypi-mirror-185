"""
NAME
anawindow

DESCRIPTION
Analysis window of the luminescence time drive data parser.

This module is part of the user interface of the LumParsing package for working with luminescence time drive data.
The Analysis window is controlled by the Main_window.
This window deals with the analysis of signals. Ao: moving and removing, saving
a file of multiple signals, exporting, fitting to a curve.
All data operations use the use modules from the parsertools folder in this package, whereas user
interactions are described below.

The class AnaFrame describes the interactions of the Analysis window.
The window has two subframes that are described in separate modules:
AnaToolFrame        Tools for interacting with data. User notes, list of signals in the file and options for what type
                    of plot to show (Left side of the Frame)
FitOptionsFrame     Extra options to create a fit of one or more signals to the selected function type. Obtained
                    parameters are saved and shown and can be plotted too. (Right side of the Frame)

StdRedirector is used to redirect output from print statements to a widget in the application
Plotting of data and export and saving are controlled directly by AnaFrame

CLASSES
AnaFrame (Subclass of tk.Frame)
"""

import sys
import lumparser.parsertools as pt
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import tkinter as tk
from tkinter import N, S, W, E, TOP, LEFT, X, BOTH, END
try:
    import importlib.resources as resources
except ImportError:
    # Try backported to PY<37 `importlib_resources`.
    import importlib_resources as resources
from . import config
from .anawindow_subframes.anatoolframe import AnaToolFrame
from .anawindow_subframes.fitoptionsframe import FitOptionsFrame
from .stdredirector import StdRedirector


class AnaFrame(tk.Frame):

    def __init__(self, parent, controller, signalgroup=None):
        # link the frame to the parent frame and controller for interactions with
        # the main frame
        self.parent = parent
        self.controller = controller

        # takes the signalgroup object that was given as an argument and stores it
        # in an attribute for use within this class. The signalgroup contains all
        # the data and data operations.
        group = signalgroup
        if group is None:
            no_data = [{"time": 0.0, "value": 0.0}, {"time": 0.1, "value": 1.0}]
            no_signal = pt.Signal("No signals", no_data, "No file")
            group = pt.SignalGroup([no_signal], self.controller.default_name, notes="Empty")
        self.signalgroup = group
        # self.signalgroup.fits = {}

        # initiate the frame and start filling it up
        tk.Frame.__init__(self, self.parent)
        self.create_output_menu()   # Create custom option in menubar

        # make sure the analysis window fills the entire main window
        self.main_window = tk.PanedWindow(self)
        self.main_window.pack(fill=BOTH, expand=1)
        self.main_window.grid_columnconfigure(1, weight=1)
        self.main_window.grid_rowconfigure(0, weight=1)

        # create the overall layout of the screen:
        # tools on the left, plot and terminal in the middle and extra options
        # on the right
        self.tools = AnaToolFrame(self.main_window, self, borderwidth=5)
        self.tools.grid(row=0, rowspan=2, column=0, sticky="nswe", pady=2)
        self.tools.grid_columnconfigure(0, weight=1)

        plotframe = tk.LabelFrame(self.main_window, borderwidth=1, text="View")
        plotframe.grid(row=0, column=1, sticky="nswe", pady=2, padx=2)

        terminal_frame = tk.Frame(self.main_window)
        terminal_frame.grid(row=1, column=1, sticky=N + S + W + E, pady=10)

        self.extra_options = FitOptionsFrame(self.main_window, self)
        self.extra_options.grid(row=0, rowspan=2, column=2, pady=2, sticky=N + S + W + E)

        # middle part of the screen: plot and terminal
        ## plot
        self.title_text = tk.StringVar()
        self.title_text.set("-no signal selected-")
        plot_top = tk.Frame(plotframe)
        plot_top.pack(side=TOP, fill=BOTH)
        self.file_title = tk.Label(plot_top, textvariable=self.title_text)
        self.file_title.pack(side=LEFT, expand=1)
        self.fig = plt.figure()
        self.canvas = FigureCanvasTkAgg(self.fig, master=plotframe)
        toolbar = NavigationToolbar2Tk(self.canvas, plotframe)
        toolbar.update()
        self.canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
        toolbar.pack(side=TOP, fill=X)
        plt.xlabel("time [s]")
        plt.ylabel("Intensity [RLU]")

        ## terminal
        terminal_frame.columnconfigure(0, weight=1)
        scrollb = tk.Scrollbar(terminal_frame, )
        scrollb.grid(row=0, column=1, sticky=N + S + E + W)
        self.textout = tk.Text(terminal_frame, width=90, height=15)
        self.textout.grid(row=0, column=0, sticky=N + W + S + E)
        scrollb.config(command=self.textout.yview)
        sys.stdout = StdRedirector(self.textout)
        # standard welcome message
        print("Welcome to the Gaussia Luciferase data analysis interface")

    def create_output_menu(self):
        """Fill output menu in main window with custom input."""
        # create a custom output menu in the menubar at the top of the main window
        self.outputmenu = tk.Menu(self.controller.menubar)
        self.outputmenu.add_command(label="Export dataset", command=self.launch_export)
        self.outputmenu.add_command(label="Save dataset", command=self.save_set)
        self.outputmenu.add_command(label="Save dataset as", command=self.launch_save_as)
        self.outputmenu.add_separator()
        self.outputmenu.add_command(label="Change saving location", command=lambda: self.controller.launch_change_directory())

    def show_custom(self):
        """Show plot of selected X and Y parameters."""
        self.title_text.set("Custom plot")
        plt.clf()
        x_name = self.extra_options.x_var.get()
        y_name = self.extra_options.y_var.get()
        x = []
        y = []
        for signal in self.signalgroup:
            try:
                x.append(float(getattr(signal, x_name)))
            except AttributeError:
                pass
            try:
                y.append(float(getattr(signal, y_name)))
            except AttributeError:
                pass
        plt.xlabel(x_name)
        plt.ylabel(y_name)
        plt.scatter(x, y)
        plt.tight_layout()
        plt.gcf().canvas.draw()

    def show_all(self):
        """Plot all signals in the file."""
        self.title_text.set("All signals in dataset")
        signals = [signal for signal in self.signalgroup]
        self.plot(signals)

    def show_selected(self):
        """Plot the selected signal."""
        self.title_text.set("Selected signals")
        indices = self.tools.browser_box.curselection()
        signals = self.signalgroup.get_at(indices, seq=True)
        self.plot(signals)

    def plot(self, signals):
        """Plot the given signals in the selected plot type."""
        plt.clf()  # clear the current plot
        plottype = self.tools.active_plot.get()  # look up which plot type is selected
        # dependent on plot type, plot the data of the given signals.
        names = []  # store the names of the signals here, to use for legend
        if plottype == "signals":  # plot signal data for given signals
            # label the axes
            plt.xlabel("Time (s)")
            plt.ylabel("Light intensity (RLU)")
            # for each signal, retrieve the data to plot and remember name
            for signal in signals:
                x, y = pt.get_xy(signal.signal_data)
                plt.plot(x, y)
                names.append(signal.name)
        elif plottype == "integrated":  # plot integrated data for given signals
            # label the axes
            plt.xlabel("Time (s)")
            plt.ylabel("Integrated light intensity (RLU*s)")
            # for each signal, retrieve the data to plot and remember name
            for signal in signals:
                x, y = pt.get_xy(signal.integrated_data)
                plt.plot(x, y)
                names.append(signal.name)
        elif plottype == "fit":  # plot created fit and original data for given signals
            if len(signals) == 1 and len(signals[0].fit_data) == 0:
                self.tools.active_plot.set("integrated")
            # label the axes
            plt.xlabel("Time (s)")
            plt.ylabel("Integrated light intensity (RLU*s)")
            # for each signal, retrieve the data to plot and remember name
            for signal in signals:
                self.title_text.set("Fit of %s" % signal.name)
                # first plot original signal data
                x, y = pt.get_xy(signal.integrated_data)
                plt.plot(x, y)
                names.append(signal.name)
                # then plot the latest created fit of that data to a model curve
                fx, fy = pt.get_xy(signal.fit_data)
                plt.plot(fx, fy)
                names.append("Fit of %s" % signal.name)
        # display the names of plotted signals in the legend and adjust plot size
        plt.legend(names, loc=(1.04, 0))
        plt.tight_layout()
        plt.gcf().canvas.draw()

    def launch_export(self):
        """
        Open new window with export options.

        Type of data to export can be selected. Call check_type after choosing
        to display type dependent settings.

        Call export_files when finished.
        """
        # make a str variable that can be tracked
        self.export_type = tk.StringVar()
        # as a default, the currently displayed plot is exported
        self.export_type.set(self.tools.active_plot.get())
        # create window layout and fields
        self.export_window = tk.Toplevel()
        self.export_window.title("Export data to csv - settings")
        label2 = tk.Label(self.export_window, text="Plot type:  ")
        label2.grid(row=1, column=0, columnspan=2, sticky=W)
        # let user select different plot type if desired
        self.type_options = tk.OptionMenu(self.export_window, self.export_type,
                                          "signals", "parameters", "fit")
        self.type_options.grid(row=1, column=2, columnspan=2, sticky=N + S + E + W)

        # let user set filename for export file, default is same name as previously
        self.export_name = tk.StringVar()
        self.export_name.set(self.signalgroup.filename.replace(".parsed", ".csv"))
        self.export_type.trace("w", self.check_type)    # check_type upon change
        label3 = tk.Label(self.export_window, text="File name:  ")
        label3.grid(row=2, column=0, columnspan=2, sticky=W)
        name_entry = tk.Entry(self.export_window, textvariable=self.export_name)
        name_entry.grid(row=2, column=2, columnspan=2, sticky=N + S + E + W)

        # create fields for extra options if signal data is exported
        # hide these by default, show when export_type="signals"
        # this is checked when export type is changed, in check_type
        self.export_normal = tk.BooleanVar(value=True)
        self.export_normal_option = tk.Checkbutton(self.export_window, text="Include normal data",
                                                   variable=self.export_normal)
        self.export_normal_option.grid(row=3, column=2, columnspan=2, sticky=W)
        self.export_normal_option.grid_remove()
        self.export_int = tk.BooleanVar(value=False)
        self.export_int_option = tk.Checkbutton(self.export_window, text="Include integrated data",
                                                variable=self.export_int)
        self.export_int_option.grid(row=4, column=2, columnspan=2, sticky=W)
        self.export_int_option.grid_remove()
        # check what type is selected when to window is opened, to decide whether
        # to display extra options
        self.check_type()

        # save button to wrap up export, calls export_files
        export_button = tk.Button(self.export_window, text="Save",
                                  command=lambda *args: self.export_files(self.export_name.get()))
        export_button.grid(row=5, column=3, sticky=N + S + E + W)

    def check_type(self, *args):
        """Display extra options in export window when export type is "signals"""
        if self.export_type.get() == "signals":
            self.export_normal_option.grid()
            self.export_int_option.grid()
        else:
            self.export_normal_option.grid_remove()
            self.export_int_option.grid_remove()

    def export_files(self, exportname):
        """Export files based on user input, close export window."""
        data_directories = resources.open_text(config, 'data_directories.txt')
        for line in data_directories.read().splitlines():
            if line.startswith("csv_folder"):
                label, csv_folder = line.split("=")
        if self.export_type.get() == "signals":
            normal = self.export_normal.get()
            inte = self.export_int.get()
            self.signalgroup.export_csv(exportname, csv_folder,
                                        normal=normal, integrate=inte)
        elif self.export_type.get() == "fit":
            fit_type = self.extra_options.curve_name.get()
            self.signalgroup.export_csv(exportname, csv_folder, normal=0, integrate=1, fit=1)
        elif self.export_type.get() == "parameters":
            self.signalgroup.export_parameters(exportname, csv_folder)
        print("Exported as %s" % exportname)
        self.export_window.destroy()

    def save_set(self):
        """Simple save of file under current name. Run save_as if necessary"""
        data_directories = resources.open_text(config, 'data_directories.txt')
        for line in data_directories.read().splitlines():
            if line.startswith("parsed_folder"):
                label, parsed_folder = line.split("=")
        if self.signalgroup.filename.startswith(self.controller.default_name):
            self.launch_save_as()
        else:
            print("Saving...")
            self.signalgroup.notes = self.tools.browser_notes.get(1.0, END)
            self.signalgroup.save(parsed_folder)
            print("Saved dataset as %s" % self.signalgroup.filename)

    def launch_save_as(self):
        """
        Open window for saving file. User can input filename.

        Call save_as to finish.
        """
        self.save_window = tk.Toplevel()
        self.save_window.title("Save - settings")
        self.save_name = tk.StringVar(value=self.signalgroup.filename)
        label = tk.Label(self.save_window, text="File name:  ")
        label.grid(row=2, column=0, columnspan=2, sticky=W)
        name_entry = tk.Entry(self.save_window, textvariable=self.save_name)
        name_entry.grid(row=2, column=2, columnspan=2, sticky=N + S + E + W)

        save_button = tk.Button(self.save_window, text="Save",
                                command=lambda *args: self.save_as(self.save_name.get()))
        save_button.grid(row=5, column=3, sticky=N + S + E + W)
        self.save_window.bind('<Return>', lambda *args: self.save_as(self.save_name.get()))

    def save_as(self, new_name):
        """Save file under name input by user, then close save window."""
        data_directories = resources.open_text(config, 'data_directories.txt')
        for line in data_directories.read().splitlines():
            if line.startswith("parsed_folder"):
                label, parsed_folder = line.split("=")
        old_name = self.signalgroup.filename
        index = self.controller.windownames.index(old_name)
        # save
        self.signalgroup.notes = self.tools.browser_notes.get(1.0, END)
        self.signalgroup.change_filename(new_name)
        new_name = self.signalgroup.filename    # make sure the two names are the same to prevent errors
        print("Changed filename to {}".format(self.signalgroup.filename))
        self.signalgroup.save(parsed_folder)
        # rename the window #
        if new_name != old_name:
            self.controller.windownames[index] = new_name
            self.controller.windows[new_name] = self.controller.windows.pop(old_name)
        self.controller.show_frame(new_name)
        self.create_output_menu()   # menu somehow lost when renaming window
        # finish
        print("Saved dataset as %s" % self.signalgroup.filename)
        self.save_window.destroy()
