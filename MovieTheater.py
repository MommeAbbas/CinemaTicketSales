import tkinter as tk

# Represents a cinema with attributes for name, setting capacity, ticket prices and sold tickets
class MovieTheater:
    # Initialize instances of the class
    def __init__(self, name, total_seats, adult_price, senior_price, child_price):
        self.name = name # set "name" attribute to the provided name
        self.total_seats = total_seats # set the "total_seats" to the provided total_seats
        
        # dictionary "prices" with ticket prices for each category
        self.prices = {
            "Adults": adult_price,
            "Seniors": senior_price,
            "Children": child_price
        }
        
        # dictionary "sold_tickets" with number of sold tickets for each category
        self.sold_tickets = {
            "Adults": tk.IntVar(), # tracks sold tickets for adults
            "Seniors": tk.IntVar(),
            "Children": tk.IntVar()
        }

    # Calculate and return the total revenue.
    def calculate_revenue(self):
        # Multiply sold tickets with their respective prices and sum them up. 
        revenue = sum(self.sold_tickets[category].get() * self.prices[category] for category in self.prices)
        return revenue

    # Calculate and return occupancy percentage
    def calculate_occupancy(self):
        total_sold_tickets = sum(self.sold_tickets[category].get() for category in self.sold_tickets)
        occupancy = (total_sold_tickets / self.total_seats) * 100
        return occupancy