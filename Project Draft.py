from tkinter import *
#Window Creation
window = Tk()
window.geometry("1280x720")
#lists for  drop menus
tech = ["001", "002", "003", "004", "005"]
test = ["Iron Level", "Hemoglobin A1C", "Comprehensive Metabolic Profile", "Basic Metabolic Profile", "Urinalysis"]
phys = ["Dr. Miranda Bailey", "Dr. Frasier Crane", "Dr. John Dorian", "Dr. Gregory House", "Dr. Doogie Howser"]
lab = ["InHouse", "ARUP Lab", "Labcorp", "Mayo Clinic"]
temp = ["Frozen", "Refrigerated", "Ambient"]
req = ["Spin", "NoSpin"]


#function for getting user selection from menu
def drop():
    label = Label(window , text = " ").pack()
    label.config( text = click.get())

#Buttons and Menus
techClick = StringVar()
techFrame = Frame()
techOption = OptionMenu(window, techClick, *tech).pack()
techButton = Button(window , text = "tech#" , command = drop)

testClick = StringVar()
testFrame = Frame()
testOption = OptionMenu(window, testClick, *test).pack()
testButton = Button(window , text = "Test" , command = drop)

physClick = StringVar()
physFrame = Frame()
physOption = OptionMenu(window, physClick, *phys).pack()
physButton = Button(window , text = "Physician" , command = drop)

labClick = StringVar()
labFrame = Frame()
labOption = OptionMenu(window, labClick, *lab).pack()
labButton = Button(window , text = "Lab" , command = drop)

tempClick = StringVar()
tempFrame = Frame()
tempOption = OptionMenu(window, tempClick, *temp).pack()
tempButton = Button(window , text = "Required Temperature" , command = drop)

reqClick = StringVar()
reqFrame = Frame()
reqOption = OptionMenu(window, reqClick, *req).pack()
reqButton = Button(window , text = "Requirements" , command = drop)



window.mainloop()
