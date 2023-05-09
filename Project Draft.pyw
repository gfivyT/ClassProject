#Grant Funkhouser
#5/8/2023
#Batch Formation GUI
#Allows cataloging of specimens to be shipped out to other facilities
from tkinter import *# basic import for tkinter functions
from PIL import ImageTk, Image# import to insert png files
from datetime import date#import to grab current date and time

#lists for  drop menus
tech = ["001", "002", "003", "004", "005"]
test = ["Iron Level", "Hemoglobin A1C", "Comprehensive Metabolic Profile", "Basic Metabolic Profile", "Urinalysis"]
phys = ["Dr. Miranda Bailey", "Dr. Frasier Crane", "Dr. John Dorian", "Dr. Gregory House", "Dr. Doogie Howser"]
lab = ["InHouse", "ARUP Lab", "Labcorp", "Mayo Clinic"]
temp = ["Frozen", "Refrigerated", "Ambient"]
req = ["Spin", "NoSpin"]


#Resets Result File
def erase():
    docuW = open("BatchPrint.txt", "w")
    docuW.write(str(date.today()))
    docuW.close()

#Window Creation
def main():
    erase()
    global window
    window = Tk()
    window.title("Batch Form")#Titles the window
    window.iconbitmap("icon.ico")#Adds a custom picture to the window's icon
    default()
    
      
    #Buttons and Menus
def default():
    global baseFrame#Creates parent frame for widgets
    baseFrame = LabelFrame(window)
    baseFrame.pack(fill="both", expand = True)
    
    quitButton = Button(baseFrame, text = "Exit", command = window.destroy)#Exit button
    quitButton.grid(row = 0, column = 2)

    saveButton = Button(baseFrame, text = "Save", command = saveConfirm)#Save button
    saveButton.grid(row = 0, column = 3)

    
    global techClick#grabs selected value from menu
    techClick = StringVar()
    
    techFrame = LabelFrame(baseFrame, bg = "#b4c0cc", text = "User's Tech Number")
    techFrame.grid(row = 1, column = 0, sticky = W)
    techLabel = Label(techFrame, bg ="#b4c0cc", text = "Tech #")
    techLabel.pack(side = LEFT)
    techOption = OptionMenu(techFrame, techClick, *tech)
    techOption.pack()
    

    global testClick#grabs selected value from menu
    testClick = StringVar()
    #Creates Frame that contains label and option menu
    testFrame = LabelFrame(baseFrame, bg = "#b4c0cc", text = "Requested Test")
    testFrame.grid(row = 4, column = 0, sticky = W)
    testLabel = Label(testFrame, bg = "#b4c0cc", text = "Test")
    testLabel.pack(side = LEFT)
    testOption = OptionMenu(testFrame, testClick, *test)
    testOption.pack(side = LEFT)
    


    global physClick#grabs selected value from menu
    physClick = StringVar()
    c
    physFrame = LabelFrame(baseFrame, bg = "#b4c0cc", text = "Authorizing Physician")
    physFrame.grid(row = 2, column = 0, sticky = W)
    physLabel = Label(physFrame, bg = "#b4c0cc", text = "Physician")
    physLabel.pack(side = LEFT)
    physOption = OptionMenu(physFrame, physClick, *phys)
    physOption.pack(side = LEFT)
    


    global labClick#grabs selected value from menu
    labClick = StringVar()
    #Creates Frame that contains label and option menu
    labFrame = LabelFrame(baseFrame, bg = "#b4c0cc", text = "Lab Recieving the Specimen")
    labFrame.grid(row = 3, column = 0, sticky = W)
    labLabel = Label(labFrame, bg = "#b4c0cc", text = "Reference Lab")
    labLabel.pack(side = LEFT)
    labOption = OptionMenu(labFrame, labClick, *lab)
    labOption.pack(side = LEFT)
    

    global tempClick#grabs selected value from menu
    tempClick = StringVar()
    #Creates Frame that contains label and option menu
    tempLabel = Label(testFrame, bg = "#b4c0cc", text = "Required Stability")
    tempLabel.pack(side = LEFT)
    tempOption = OptionMenu(testFrame, tempClick, *temp)
    tempOption.pack(side = LEFT)
    

    global reqClick#grabs selected value from menu
    reqClick = StringVar()
    #Creates Frame that contains label and option menu
    reqLabel = Label(testFrame, bg = "#b4c0cc", text = "Reqirments")
    reqLabel.pack(side = LEFT)
    reqOption = OptionMenu(testFrame, reqClick, *req)
    reqOption.pack(side = LEFT)

    #Image Insertion
    global picture
    picture = ImageTk.PhotoImage(Image.open("Corner Picture.png"))
    picLabel = Label(baseFrame, image = picture)
    picLabel.grid(row = 0, column = 0, sticky = W)

    
    

    window.mainloop()

#Reset Widgets to default values
def reset():
    techClick.set("")
    testClick.set("")
    physClick.set("")
    labClick.set("")
    tempClick.set("")
    reqClick.set("")
    
#Save Window
def saveConfirm():
    docuA = open("BatchPrint.txt", "a")
    techString = str(techClick.get())#Variables provide strings for write function
    testString = str(testClick.get())
    physString = str(physClick.get())
    labString = str(labClick.get())
    tempString = str(tempClick.get())
    reqString = str(reqClick.get())
    resultLine = "[Technician: {0}], [Test: {1}], [Physician: {2}], [Reference Lab: {3}], [Stability Temperature: {4}], [Processng Requirements: {5}]".format(techString,testString,physString,labString,tempString,reqString)# creates formatted string that provides the text file with a new line of data
    docuA.write("\n" + "\n")
    docuA.write(resultLine)
    docuA.close()
                
    saveWin = Tk()#Second window for save confirmation and required optionmenu reset
    saveWin.title("Confirmation")
    saveLabel = Label(saveWin, text = "Batch Complete")
    saveLabel.pack()
    finButton = Button(saveWin, text = "Finish", command = lambda:[saveWin.destroy(),reset()])#finish button which removes the save window and resets optionmenus
    finButton.pack()
    

if __name__ == "__main__":
    main()
    

