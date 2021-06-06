import pickle, os, urllib.request as ur

def displayRecord():
    with ur.urlopen("https://github.com/sukritS009312/availability/blob/main/availability.dat?raw=true") as data:
        recd = pickle.load(data)
        return recd
    
recd = displayRecord()
if len(recd.keys()) == 0:
    print("No Flights Are Scheduled! Come Back Later!\n"+"-"*80)
else:
    print("Here Are The Flights Scheduled-\n"+"="*80)
    for i in recd.keys():
        print(f"Flight No. : {i}\nDeparting Place : {recd[i][0]}\nApproaching Place : {recd[i][1]}\nTime of Departure : {recd[i][2]}\n\
Time to Approach: {recd[i][3]}\nPrice : ₹{recd[i][4]}/-")
        print("-"*80)
   
input("Hit Enter to exit")
