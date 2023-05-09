#Grant Funkhouser
#5/8/2023
#Batch Formation GUI
#Allows cataloging of specimens to be shipped out to other facilities
from tkinter import *
from PIL import ImageTk, Image
from datetime import date

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
    window.title("Batch Form")
    window.iconbitmap("icon.ico")
    default()
    
      
    #Buttons and Menus
def default():
    global baseFrame
    baseFrame = LabelFrame(window)
    baseFrame.pack(fill="both", expand = True)
    
    quitButton = Button(baseFrame, text = "Exit", command = window.destroy)
    quitButton.grid(row = 0, column = 2)

    saveButton = Button(baseFrame, text = "Save", command = saveConfirm)
    saveButton.grid(row = 0, column = 3)

    
    global techClick
    techClick = StringVar()
    
    techFrame = LabelFrame(baseFrame, bg = "#b4c0cc", text = "User's Tech Number")
    techFrame.grid(row = 1, column = 0, sticky = W)
    techLabel = Label(techFrame, bg ="#b4c0cc", text = "Tech #")
    techLabel.pack(side = LEFT)
    techOption = OptionMenu(techFrame, techClick, *tech)
    techOption.pack()
    

    global testClick
    testClick = StringVar()

    testFrame = LabelFrame(baseFrame, bg = "#b4c0cc", text = "Requested Test")
    testFrame.grid(row = 4, column = 0, sticky = W)
    testLabel = Label(testFrame, bg = "#b4c0cc", text = "Test")
    testLabel.pack(side = LEFT)
    testOption = OptionMenu(testFrame, testClick, *test)
    testOption.pack(side = LEFT)
    


    global physClick
    physClick = StringVar()

    physFrame = LabelFrame(baseFrame, bg = "#b4c0cc", text = "Authorizing Physician")
    physFrame.grid(row = 2, column = 0, sticky = W)
    physLabel = Label(physFrame, bg = "#b4c0cc", text = "Physician")
    physLabel.pack(side = LEFT)
    physOption = OptionMenu(physFrame, physClick, *phys)
    physOption.pack(side = LEFT)
    


    global labClick
    labClick = StringVar()

    labFrame = LabelFrame(baseFrame, bg = "#b4c0cc", text = "Lab Recieving the Specimen")
    labFrame.grid(row = 3, column = 0, sticky = W)
    labLabel = Label(labFrame, bg = "#b4c0cc", text = "Reference Lab")
    labLabel.pack(side = LEFT)
    labOption = OptionMenu(labFrame, labClick, *lab)
    labOption.pack(side = LEFT)
    

    global tempClick
    tempClick = StringVar()

    tempLabel = Label(testFrame, bg = "#b4c0cc", text = "Required Stability")
    tempLabel.pack(side = LEFT)
    tempOption = OptionMenu(testFrame, tempClick, *temp)
    tempOption.pack(side = LEFT)
    

    global reqClick
    reqClick = StringVar()

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

#Reset Widgets
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
    techString = str(techClick.get())
    testString = str(testClick.get())
    physString = str(physClick.get())
    labString = str(labClick.get())
    tempString = str(tempClick.get())
    reqString = str(reqClick.get())
    resultLine = "[Technician: {0}], [Test: {1}], [Physician: {2}], [Reference Lab: {3}], [Stability Temperature: {4}], [Processng Requirements: {5}]".format(techString,testString,physString,labString,tempString,reqString)
    docuA.write("\n" + "\n")
    docuA.write(resultLine)
    docuA.close()
                
    saveWin = Tk()
    saveWin.title("Confirmation")
    saveLabel = Label(saveWin, text = "Batch Complete")
    saveLabel.pack()
    finButton = Button(saveWin, text = "Finish", command = lambda:[saveWin.destroy(),reset()])
    finButton.pack()
    

if __name__ == "__main__":
    main()
    

