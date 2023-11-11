import tkinter as tk
from MovieTheater import MovieTheater
from FileReader import FileReader
from CinemaApp import CinemaApp

# check if the script is being run as the main program. 
if __name__ == "__main__":
    # Create main application window using tkinter
    root = tk.Tk()
    # Create instance of FileReader class
    file_reader = FileReader("Cinemas.csv")
    # read data from CSV file and create a list of MovieTheater instances
    cinemas = file_reader.read_data()
    # create instance of CinemaApp class, passing the main window "root", and list of cinemas 
    app = CinemaApp(root, cinemas) 
    # start the tkinter main event loop to run the application
    root.mainloop()