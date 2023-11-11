import tkinter as tk
from tkinter import ttk

# GUI application for managing and displaying information about cinemas and ticket sales. 
class CinemaApp:
    # initialize CinemaApp class with a tkinter root window and a list of cinemas.  
    def __init__(self, root, cinemas):
        self.root = root
        self.cinemas = cinemas
        self.root.title("Cinema Ticket Sales")
        root.iconbitmap("theatericon.ico")
        self.root.geometry("800x600")
        self.root.configure(bg="gold")
        
        # Create a style for the Treeview
        style = ttk.Style()
        style.configure("Treeview.Heading", font=("times new roman", 10, "bold"))
        style.configure("Treeview", font=("times new roman", 10))

        # Heading label of the application
        headingLabel = tk.Label(root, text="Cinema Ticket Sales", font=("times new roman", 30, "bold"),
                                bg="maroon", fg="gold", bd=12, relief="groove")
        headingLabel.pack(fill="x")
        
        # Frame for the top section (Combobox, ticket entry, Update)
        top_frame = tk.Frame(root, bg="gold", bd=12, relief="groove")
        top_frame.pack(fill="x")

        # Combobox to select a cinema from the list of cinemas
        self.cinema_choice = ttk.Combobox(top_frame, values=[cinema.name for cinema in cinemas])
        self.cinema_choice.set("Select Cinema") # initial value in Combobox 
        self.cinema_choice.pack(side="left")
        self.cinema_choice.bind("<<ComboboxSelected>>", self.update_cinema_info)

        # labels and entry fields for number of sold tickets for each category
        
        tk.Label(top_frame, text="Adult Ticket Sales:", font=("times new roman", 8, "bold"),
                 bg="gold", fg="maroon").pack(side="left", padx=10, pady=5)
        self.adult_tickets_entry = tk.Entry(top_frame, bd=4, textvariable=tk.StringVar(value="0"), width=5)
        self.adult_tickets_entry.pack(side="left")

        tk.Label(top_frame, text="Senior Ticket Sales:", font=("times new roman", 8, "bold"),
                 bg="gold", fg="maroon").pack(side="left", padx=10, pady=5)
        self.senior_tickets_entry = tk.Entry(top_frame, bd=4, textvariable=tk.StringVar(value="0"), width=5)
        self.senior_tickets_entry.pack(side="left")

        tk.Label(top_frame, text="Children Ticket Sales:", font=("times new roman", 8, "bold"), 
                 bg="gold", fg="maroon").pack(side="left", padx=10, pady=5)
        self.child_tickets_entry = tk.Entry(top_frame, bd=4, textvariable=tk.StringVar(value="0"), width=5)
        self.child_tickets_entry.pack(side="left")
        
        # Frame for Updating and displaying cinema information
        self.update_button = tk.Button(top_frame, text="Update", font=("times new roman", 8, "bold"), 
                                       bd=4, relief="groove", command=self.calculate_and_display_info)
        self.update_button.pack(side="right")

        # Frame for the Information Label
        left_frame = tk.Frame(root)
        left_frame.pack(side="left", fill="both", padx=10, pady=10, expand=True)

        # Label to display information about the selected cinema. 
        self.cinema_info_label = tk.Label(left_frame, text="", font=("times new roman", 10, "bold"),
                                           fg="gold", bg="maroon", bd=4, relief="groove", justify="left")
        self.cinema_info_label.pack(fill="both")

        # Frame for the Treeview widget for sorted cinemas
        treeview_frame = tk.Frame(left_frame)
        treeview_frame.pack(side="left", fill="both", padx=10, pady=10, expand=True)

        self.cinema_order_label = tk.Label(treeview_frame, text="Cinemas in order of Occupied Seats (Descending)", 
                                            font=("times new roman", 10, "bold"), fg="gold", bg="maroon", justify="left")
        self.cinema_order_label.pack(fill="x")

        # Treeview widget with columns for cinema details.
        self.cinema_treeview = ttk.Treeview(treeview_frame, columns=("Cinema", "Ticket Revenue", "Occupied Seats"), show="headings")

        # Column headings for Treeview
        self.cinema_treeview.heading("Cinema", text="Cinema")
        self.cinema_treeview.heading("Ticket Revenue", text="Ticket Revenue")
        self.cinema_treeview.heading("Occupied Seats", text="Occupied Seats")

        # Configure column widths and alignments for the Treeview. 
        self.cinema_treeview.column("Cinema", width=200, anchor="center")
        self.cinema_treeview.column("Ticket Revenue", width=200, anchor="center")
        self.cinema_treeview.column("Occupied Seats", width=200, anchor="center")

        self.cinema_treeview.pack(fill="both", expand=True)

    # Update the information label with details about the selected cinema
    def update_cinema_info(self, event):
        selected_cinema_name = self.cinema_choice.get()
        selected_cinema = next((cinema for cinema in self.cinemas if cinema.name == selected_cinema_name), None)
        if selected_cinema:
            info = f"{selected_cinema.name}\n\nTotal Seats: {selected_cinema.total_seats}\n\nTicket Prices:\n"
            for category, price in selected_cinema.prices.items():
                info += f"{category}: {price} kr\n"
            self.cinema_info_label.config(text=info)

    # Update sold tickets count, calculate and display cinema information, and update the sorted cinemas. 
    def calculate_and_display_info(self):
        selected_cinema_name = self.cinema_choice.get()
        selected_cinema = next((cinema for cinema in self.cinemas if cinema.name == selected_cinema_name), None)
        if selected_cinema:
            
            try:
                adult_tickets = int(self.adult_tickets_entry.get())
                senior_tickets = int(self.senior_tickets_entry.get())
                child_tickets = int(self.child_tickets_entry.get())

            # handling non integer inputs
            except ValueError:
                self.cinema_info_label.config(text="Invalid input. Please enter valid integer values.")
                return
            
            total_tickets = adult_tickets + senior_tickets + child_tickets
            
            # if tickets sold more than seats available
            if total_tickets > selected_cinema.total_seats:
                self.cinema_info_label.config(text="Invalid input. Total tickets sold cannot exceed total seats or be negative.")
                return
            
            # if inputs are negative
            if adult_tickets < 0 or senior_tickets < 0 or child_tickets < 0:
                self.cinema_info_label.config(text="Invalid input. Please enter non-negative integer values.")
                return
            
            # Update the sold_tickets attribute with user input
            selected_cinema.sold_tickets["Adults"].set(int(float(self.adult_tickets_entry.get())))
            selected_cinema.sold_tickets["Seniors"].set(int(float(self.senior_tickets_entry.get())))
            selected_cinema.sold_tickets["Children"].set(int(float(self.child_tickets_entry.get())))
            
            # Calculate and display updated information
            selected_cinema_info = f"{selected_cinema.name}\n\nTicket Revenue: {selected_cinema.calculate_revenue()} kr\n"
            selected_cinema_info += f"Occupied Seats: {selected_cinema.calculate_occupancy():.2f}%"
            self.cinema_info_label.config(text=selected_cinema_info)

        # Sort cinemas in order of highest seats occupation (descending)
        sorted_cinemas = sorted(self.cinemas, key=lambda cinema: cinema.calculate_occupancy(), reverse=True)

        # Clear the Treeview (delete every row)
        for item in self.cinema_treeview.get_children():
            self.cinema_treeview.delete(item)

        # Display sorted cinemas in the Treeview
        for cinema in sorted_cinemas:
            self.cinema_treeview.insert("", "end", values=(cinema.name, f"{cinema.calculate_revenue()} kr", 
                                                            f"{cinema.calculate_occupancy():.2f}%"))