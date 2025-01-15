import csv
import pandas as pd
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import filedialog, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class Home(Frame):
    def __init__(self, master, show_login_callback):
        super().__init__(master)
        self.master = master
        self.file_path = None
        self.show_login_callback = show_login_callback
        self.invert_graph = BooleanVar()

        self.light_bg = '#f0f0f0'
        self.light_button = '#008CBA'
        self.text_color = '#000000'

        self.configure(bg=self.light_bg)

        self.title_label = Label(self, text="Select a file to plot a graph :)",
                                 font=("Arial", 16),
                                 bg=self.light_bg,
                                 fg=self.text_color)
        self.title_label.pack(pady=10)

        self.browse_button = Button(self, text="Browse CSV File",
                                     command=self.browse_file,
                                     bg=self.light_button,
                                     fg='white',
                                     relief=RAISED)
        self.browse_button.pack(pady=10)

        self.file_label = Label(self, text="No file selected",
                                bg=self.light_bg,
                                fg=self.text_color)
        self.file_label.pack(pady=10)

        self.invert_checkbox = Checkbutton(self,
                                           text="Invert Graph",
                                           variable=self.invert_graph,
                                           bg=self.light_bg,
                                           fg=self.text_color,
                                           selectcolor=self.light_button,
                                           activebackground=self.light_bg,
                                           activeforeground=self.text_color,command=self.plot_graph_invert)
        self.invert_checkbox.pack(pady=5)

        self.submit_button = Button(self, text="Submit and Plot Graph",
                                     command=self.plot_graph,
                                     state=DISABLED,
                                     bg=self.light_button,
                                     fg='white',
                                     relief=RAISED)
        self.submit_button.pack(pady=10)

        self.logout_button = Button(self, text="Logout",
                                     command=self.logout,
                                     bg='#ff4444',
                                     fg='white',
                                     relief=RAISED)
        self.logout_button.pack(pady=10)

        self.pack(padx=20, pady=20)

    def browse_file(self):
        self.file_path = filedialog.askopenfilename(
            filetypes=[("CSV Files", "*.csv")],
            title="Select a CSV File"
        )

        if self.file_path:
            self.file_label.config(text=f"Selected File: {self.file_path}")
            self.submit_button.config(state=NORMAL)
        else:
            self.file_label.config(text="No file selected")
            self.submit_button.config(state=DISABLED)

    def plot_graph(self):
        if not self.file_path:
            messagebox.showerror("Error", "No file selected!")
            return

        try:
            df = pd.read_csv(self.file_path)

            if len(df.columns) < 2:
                messagebox.showerror("Error", "CSV must have at least two columns to plot!")
                return

            x = df[df.columns[0]]
            y = df[df.columns[1]]

            plt.style.use('dark_background')

            plt.figure(figsize=(8, 6))
            plt.plot(x, y, marker='o', color='green', linewidth=2)
            plt.title("Graph from CSV Data", fontsize=14, pad=20, color='white')
            plt.xlabel(df.columns[0], color='white')
            plt.ylabel(df.columns[1], color='white')
            plt.grid(True, linestyle='--', alpha=0.5)
            plt.tight_layout()

            plt.show()

        except Exception as e:
            messagebox.showerror("Error", f"Failed to plot graph: {e}")

    def logout(self):
        if messagebox.askyesno("Logout", "Are you sure you want to logout?"):
            self.show_login_callback()
    
    def plot_graph_invert(self):
        if not self.file_path:
            messagebox.showerror("Error", "No file selected!")
            return

        try:
            df = pd.read_csv(self.file_path)

            if len(df.columns) < 2:
                messagebox.showerror("Error", "CSV must have at least two columns to plot!")
                return

            x = df[df.columns[0]]
            y = df[df.columns[1]]

            if self.invert_graph.get():
                y = -y

            fig = Figure(figsize=(6, 4), dpi=100)
            ax = fig.add_subplot(111)
            ax.plot(x, y, marker='o', color='green', linewidth=2)

            ax.set_title("Graph from CSV Data (Inverted)" if self.invert_graph.get() else "Graph from CSV Data", fontsize=12)
            ax.set_xlabel(df.columns[0], fontsize=10)
            ax.set_ylabel(df.columns[1], fontsize=10)
            ax.grid(True, linestyle='--', alpha=0.5)
            ax.set_facecolor('black')
            ax.spines['bottom'].set_color('white')
            ax.spines['top'].set_color('white')
            ax.spines['left'].set_color('white')
            ax.spines['right'].set_color('white')
            ax.tick_params(colors='white')

            if hasattr(self, 'canvas'):
                self.canvas.get_tk_widget().destroy()

            self.canvas = FigureCanvasTkAgg(fig, master=self)
            self.canvas.draw()
            self.canvas.get_tk_widget().pack(pady=10)

        except Exception as e:
            messagebox.showerror("Error", f"Failed to plot graph: {e}")
