from random import randint

class Train: 
    train_no= ""
    fro= ""
    too= ""

    def __init__(self,train_no,fro,to):
        self.train_no = train_no
        self.fro = fro
        self.to = to

    def Book(self):
        # self.fro = fro
        # self.to = to
        print(f"The train is booked! Train no {self.train_no} \n From: {self.fro} \n To: {self.to}")

    def Book_Status(self):
        print(f"The train is booked! Train no {self.train_no}")

    def Booking_Fare(self):
        print(f"The train is booked! Train no {self.train_no} \n From: {self.fro} \n To: {self.to} \nTicket Fare : {randint(100, 900)}")


# Create object
First_book = Train(121212212,"karachi", "Lahore")

First_book.Book()
First_book.Book_Status()
First_book.Booking_Fare()
