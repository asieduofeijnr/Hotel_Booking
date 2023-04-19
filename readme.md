# Hotel Reservation Program :hotel:
This is a Python program that allows a user to book a hotel room, validate their credit card information, and generate a reservation ticket. It also provides an option for booking a spa and authenticating it.


## Getting Started

To get started, download the `hotels.csv`, `cards.csv`, and `card_security.csv` files to your local machine. Then, run the `hotel_booking.py` file in your Python environment.

## Requirements :clipboard:
pandas

## How to Use :rocket:
1. Clone the repository or download the program files.
2. Install the required library by running the following command in your terminal: pip install pandas
3. Run the program in your preferred Python environment.
4. Input the ID of the hotel you wish to book.
5. Input your name and credit card CVC number.
6. If the credit card validation is successful, the hotel will be booked and a reservation ticket will be generated.
7. You will be prompted to book a spa, and if you choose to do so, the spa booking message will be displayed.

## Classes :computer:
Hotel
- This class initializes a hotel object with its ID and name. It also has a book method to change the availability of the hotel to 'no' and a available method to check if the hotel is available.

ReservationTicket
- This class generates a reservation ticket message with the customer's name and the hotel name.

Spa
- This class inherits from ReservationTicket. It has a book method to generate a spa booking message and an authenticate method to check if the customer wants to book a spa.

CreditCard
- This class initializes a credit card object with its number. It has a validate method to check if the provided card data matches the data in the cards.csv file.

SecureCreditCard
- This class inherits from CreditCard. It has an authenticate method to check if the provided password matches the one associated with the credit card number in the card_security.csv file.

