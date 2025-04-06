# In the program if we change the name from slf to anything else will it matter 
from random import randint

class Train: 
    train_no= ""
    fro= ""
    too= ""

    def __init__(slf,train_no,fro,to):
        slf.train_no = train_no
        slf.fro = fro
        slf.to = to

    def Book(slf):
        # slf.fro = fro
        # slf.to = to
        print(f"The train is booked! Train no {slf.train_no} \n From: {slf.fro} \n To: {slf.to}")

    def Book_Status(slf):
        print(f"The train is booked! Train no {slf.train_no}")

    def Booking_Fare(slf):
        print(f"The train is booked! Train no {slf.train_no} \n From: {slf.fro} \n To: {slf.to} \nTicket Fare : {randint(100, 900)}")


# Create object
First_book = Train(121212212,"karachi", "Lahore")

First_book.Book()
First_book.Book_Status()
First_book.Booking_Fare()


# As it can be seen the self has been changed to slf and nothing hsppen in the context of 
# execution everything remained same but it is kept self to keep the readability intact 