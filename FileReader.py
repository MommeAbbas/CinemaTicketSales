import csv
from MovieTheater import MovieTheater

# Class for reading and processing CSV data from a file to create MovieTheater instances. 
class FileReader:
    # Constructor method to initialize instances of the class.
    def __init__(self, filename):
        self.filename = filename

    # Read data from a file and create MovieTheater instances.
    def read_data(self):
        try:
            with open(self.filename, mode="r", newline="") as file: 
                reader = csv.DictReader(file) # Create a CSV reader object to read the file as a dictionary.
                cinemas = [] # empty list to store MovieTheater instances.
                 
                for row in reader:
                    cinemas.append(MovieTheater(
                        (row["CinemaName"]), # create MovieTheater instances with data from CSV.
                        int(row["TotalSeats"]), # Convert TotalSeats value to an integer.
                        int(row["AdultPrice"]),
                        int(row["SeniorPrice"]),
                        int(row["ChildPrice"])
                    ))
                
                # Return list of created MovieTheater instances. 
                return cinemas
            
        # Handle cases in which the file is not found. 
        except FileNotFoundError:
            print(f"File '{self.filename}' not found.")
            return [] # return an empty list.
        
        # Handle other exceptions
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return []