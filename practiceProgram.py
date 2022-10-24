import practiceClass as p
import csv


shows = {
    "play1":{
        'id':3245,
        'name':'Phantom of the Opera',
        'capacity':65,
        'event_date':'03/01/2023'
    },
    "play2":{
        'id':1548,
        'name':'The Music Man',
        'capacity':45,
        'event_date':'05/15/2023'
    },
    "play3":{
        'id':9587,
        'name':'Hamilton',
        'capacity':124,
        'event_date':'07/21/2023'
    },
    "play4":{
        'id':6254,
        'name':'The Lion King',
        'capacity':89,
        'event_date':'09/29/2023'
    },

}

'''using the above dictionary iterate through it and create an instance of the 
play class that has id 9587
NOTE: Do not hard code the values to create the instance but use
keys and values from the dictionary '''


for key, value in shows.items():
    if value["id"] == 9587:
        showing = p.Play(value["id"],value["name"],value["capacity"],value["event_date"])


'''using the bookings.csv file process only those 
reservations for the same play (9587). Create an 
instance of the Booking class for each customer
that is going to play 9587 - Hamilton. 
if the play reaches capacity print out a 
error message as shown in output.JPG'''


#open the csv file in read mode
infile = open('bookings.csv','r')

#create a csv object from the file object from the step above
reader = csv.reader(infile)

# use a for loop to iterate through each record in the bookings file
next(reader)

for row in reader:
    if row[0] == '9587':
        customer = p.Booking(row[1],row[2])
        p.Play.seats_left(showing, showing.get_Seats())
        if showing.get_Seats() < 0:
            print("***********************************")
            print("Guest Name: ", row[1])
            print("Sorry, show: Hamilton is sold out")
            print("***********************************")
