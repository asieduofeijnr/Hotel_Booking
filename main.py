import pandas as pd

# Read in hotels.csv and set the 'id' column to have dtype str
df = pd.read_csv("hotels.csv", dtype={"id": str})

# Read in cards.csv and convert to a list of dictionaries
df_cards = pd.read_csv("cards.csv", dtype=str).to_dict(orient="records")

# Read in card_security.csv
df_cards_security = pd.read_csv("card_security.csv", dtype=str)


# Define a class called Hotel
class Hotel:
    def __init__(self, hotel_id):
        # Initialize the hotel object with its ID and name
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()

    def book(self):
        """Book a hotel by changing its availability to no"""
        # Set the 'available' column to 'no' for the hotel with this ID
        df.loc[df["id"] == self.hotel_id, "available"] = "no"

        # Save the updated DataFrame to hotels.csv
        df.to_csv("hotels.csv", index=False)

    def available(self):
        """Check if the hotel is available"""
        # Check the 'available' column for the hotel with this ID
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False


# Define a class called ReservationTicket
class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        # Initialize the reservation ticket with the customer's name and hotel object
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        # Generate the reservation ticket message
        content = f"""
        Thank you for your reservation!
        Here are your booking data:
        name: {self.customer_name}
        Hotel name: {self.hotel.name}"""
        return content


# Define a class called Spa, which inherits from ReservationTicket
class Spa(ReservationTicket):
    def book(self):
        # Generate the spa booking message
        content = f"""
        Thank you for your SPA reservation!
        Here are your booking data:
        name: {self.customer_name}
        Hotel name: {self.hotel.name}"""
        return content

    def authenticate(self, given_answer):
        # Check if the customer wants to book a spa
        if given_answer == "yes":
            return True
        else:
            return False


# Define a class called CreditCard
class CreditCard:
    def __init__(self, number):
        # Initialize the credit card with the card number
        self.number = number

    def validate(self, expiration, holder, cvc):
        # Validate the credit card with the provided card data
        card_data = {
            "number": self.number,
            "expiration": expiration,
            "holder": holder,
            "cvc": cvc,
        }

        if card_data in df_cards:
            return True
        else:
            return False


# Define a class called SecureCreditCard, which inherits from CreditCard
class SecureCreditCard(CreditCard):
    def authenticate(self, given_password):
        # Check if the provided password matches the one associated with this credit card number
        password = df_cards_security.loc[
            df_cards_security["number"] == self.number, "password"
        ].squeeze()
        if password == given_password:
            return True
        else:
            return False

    def authenticate(self, given_password):
        password = df_cards_security.loc[
            df_cards_security["number"] == self.number, "password"
        ].squeeze()
        if password == given_password:
            return True
        else:
            return False


# print the hotels dataset
print(df)

# get the ID of the hotel the user wants to book
hotel_id = input("Enter the id of the hotel: ")

# create a Hotel object for the selected hotel
hotel = Hotel(hotel_id)

# check if the selected hotel is available for booking
if hotel.available():
    # create a SecureCreditCard object for the credit card used for payment
    credit_card = SecureCreditCard(number="1234")

    # validate the credit card information
    if credit_card.validate(expiration="12/26", holder="JOHN SMITH", cvc="123"):
        # get the name of the customer and their credit card password
        name = input("Enter your name: ")
        password = input("Please type in your cvc number: ")

        # authenticate the credit card
        if credit_card.authenticate(given_password=password):
            # book the hotel
            hotel.book()

            # generate a reservation ticket for the customer
            reservation_ticket = ReservationTicket(
                customer_name=name, hotel_object=hotel
            )
            print(reservation_ticket.generate())

            # ask the customer if they want to book a spa and authenticate their answer
            spa_booking = Spa(customer_name=name, hotel_object=hotel)
            customer_answer = input("Do you want to book a spa?: ")
            if spa_booking.authenticate(given_answer=customer_answer):
                print(spa_booking.book())
            else:
                print("Thank you have a great day")
        else:
            print("Credit card authentication failed.")
    else:
        print("There was a problem with your payment")
else:
    print("Hotel is not free.")
