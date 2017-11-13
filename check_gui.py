import sys
from tkinter import *
from src.settings import *
from check import startCheck
from src.inputplayer import Player

gui_err_msg = []
lblLst = []

def checkPlayer():
    '''
    DESCRIPTION:    Calling the check.py script to perfrom a player check.
    INPUT:          None
    OUTPUT:         None
    '''
    setBasicLabelBg(lblLst)
    if checkInputs():
        player = Player(txtName.get(), txtServer.get(), txtRegion.get())
        startCheck(player)


def checkInputs():
    '''
    TODO:           Implementation
    DESCRIPTION:    Checks if all nesessary fields are filled
    INPUT:          None
    OUTPUT:         None
    '''
    if txtName.get() == "" :
        lblName["fg"] = "red"
        return False
    if txtServer.get() == "":
        lblServer["fg"] = "red"
        return False
    if not txtRegion.get() in Player.supportedRegions:
        lblRegion["fg"] = "red"
        return False
    return True


def setBasicLabelBg(lstLabel):
    for lbl in lstLabel:
        lbl["fg"] = "black"

#-----------------
#   Properties
widget_pady = 5
frame_padding = 20
entryLength = 30
#-----------------
#   GUI Build
root = Tk()

##--------------
## Initialzing
mainFrame = Frame(root, width=400)
mainFrame.pack(padx=frame_padding, pady=frame_padding)
mainFrame.master.title("WoW-Player-Check")

lblName = Label(mainFrame, text="Player:")
lblLst.append(lblName)
txtName = Entry(mainFrame)
txtName.focus_set()

lblServer = Label(mainFrame, text="Server:")
lblLst.append(lblServer)
txtServer = Entry(mainFrame)

lblRegion = Label(mainFrame, text="Region:")
lblLst.append(lblRegion)
txtRegion = Entry(mainFrame)
txtRegion.delete(0,END)
txtRegion.insert(0, "EU")

lblBlizzapi = Label(mainFrame, text="Blizzard API-Key:")
txtBlizzapi = Entry(mainFrame,width=entryLength)
txtBlizzapi.delete(0,END)
txtBlizzapi.insert(0, BLIZZARD_APIKEY)
txtBlizzapi["state"] = "disabled"

lblWarcraftlogsapi = Label(mainFrame, text="Warcraftlogs API-Key:")
txtWarcraftlogsapi = Entry(mainFrame, width=entryLength)
txtWarcraftlogsapi.delete(0,END)
txtWarcraftlogsapi.insert(0, WARCRAFTLOGS_APIKEY)
txtWarcraftlogsapi["state"] = "disabled"

btnCheck = Button(mainFrame, text="Check", command=checkPlayer)

##--------------
## Positioning
lblName.grid(row=0, column=0, pady=widget_pady, sticky=E)
txtName.grid(row=0, column=1, pady=widget_pady, sticky=W)

lblServer.grid(row=1, column=0, pady=widget_pady, sticky=E)
txtServer.grid(row=1, column=1, pady=widget_pady, sticky=W)

lblRegion.grid(row=2, column=0, pady=widget_pady, sticky=E)
txtRegion.grid(row=2, column=1, pady=widget_pady, sticky=W)

lblBlizzapi.grid(row=3, column=0, pady=widget_pady, sticky=E)
txtBlizzapi.grid(row=3, column=1, pady=widget_pady, sticky=W)

lblWarcraftlogsapi.grid(row=4, column=0, pady=widget_pady, sticky=E)
txtWarcraftlogsapi.grid(row=4, column=1, pady=widget_pady, sticky=W)

btnCheck.grid(row=5, columnspan=2, pady=widget_pady)


root.mainloop()
