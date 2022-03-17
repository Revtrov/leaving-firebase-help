import random
#import the module that generated random stuff
import datetime
#import the module that gets time
from firebase import firebase
#import firebase module
firebase = firebase.FirebaseApplication("https://leaving-cert-test-default-rtdb.europe-west1.firebasedatabase.app/")
#let firebase equal to the firebase at your link ^
ranNum = random.randint(0, 100)
#create a random number between 0 and 100 for sending to you firebase (you will send your data in instead)
data ={
   #what we are sending to fire base
    "randNum":ranNum,
    #send the random number (you can send your data) 
    "timeSigniture":datetime.datetime.now()
    #send the time at which the data was sent (you can use this for graphing etc.) 
}
firebase.post('/folder/',data)
#send the data to your firebase using the post method (function)
#try to avoid folders (leave the quotes in the post blank) as it reduces complexity
