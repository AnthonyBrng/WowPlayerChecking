from tkinter import *
from settings import *
from subprocess import call

def checkPlayer():
    '''
    DESCRIPTION:    Calling the check.py script to perfrom a player check.
    INPUT:          None
    OUTPUT:         None
    '''
    if checkInputs():
        call(["python3", "check.py", txtName.get(), txtServer.get(), "--region", txtRegion.get()])
    else:
        print("Error!")


def checkInputs():
    '''
    TODO:           Implementation
    DESCRIPTION:    Checks if all nesessary fields are filled
    INPUT:          None
    OUTPUT:         None
    '''
    return True


#-----------------
#   Properties
widget_pady = 5
frame_padding = 20

#-----------------
#   GUI Build
root = Tk()

##--------------
## Initialzing
mainFrame = Frame(root, width=400)
mainFrame.pack(padx=frame_padding, pady=frame_padding)

lblName = Label(mainFrame, text="Player:")
txtName = Entry(mainFrame)

lblServer = Label(mainFrame, text="Server:")
txtServer = Entry(mainFrame)

lblRegion = Label(mainFrame, text="Region:")
txtRegion = Entry(mainFrame)
txtRegion.delete(0,END)
txtRegion.insert(0, "EU")

lblBlizzapi = Label(mainFrame, text="Blizzard API-Key:")
txtBlizzapi = Entry(mainFrame)
txtBlizzapi.delete(0,END)
txtBlizzapi.insert(0, BLIZZARD_APIKEY)

lblWarcraftlogsapi = Label(mainFrame, text="Warcraftlogs API-Key:")
txtWarcraftlogsapi = Entry(mainFrame)
txtWarcraftlogsapi.delete(0,END)
txtWarcraftlogsapi.insert(0, WARCRAFTLOGS_APIKEY)

btnCheck = Button(mainFrame, text="Check", command=checkPlayer)

##--------------
## Positioning
lblName.grid(row=0, column=0, pady=widget_pady, sticky=E)
txtName.grid(row=0, column=1, pady=widget_pady)

lblServer.grid(row=1, column=0, pady=widget_pady, sticky=E)
txtServer.grid(row=1, column=1, pady=widget_pady)

lblRegion.grid(row=2, column=0, pady=widget_pady, sticky=E)
txtRegion.grid(row=2, column=1, pady=widget_pady)

lblBlizzapi.grid(row=3, column=0, pady=widget_pady, sticky=E)
txtBlizzapi.grid(row=3, column=1, pady=widget_pady)

lblWarcraftlogsapi.grid(row=4, column=0, pady=widget_pady, sticky=E)
txtWarcraftlogsapi.grid(row=4, column=1, pady=widget_pady)

btnCheck.grid(row=5, columnspan=2, pady=widget_pady)

root.mainloop()
