from tkinter import * 
from tkinter import filedialog
import shell_commands as sc
import platform


# Selects the folder which contains all the photos that are to be renamed
def getFolder():
    global folder_path
    folder_path = filedialog.askdirectory(initialdir = "~/")
    if folder_path != "":
        label_preview.configure(text="All .jpg files in "+folder_path+" will be renamed")

# Confirms the settings and unlocks the rename button if all the settings have been assigned valid values. 
# Prompts the user to check their settings if any settings have invalid values.
def confirmSettings():
    if folder_path != "" and str(location.get()) != locationList[0] and str(scheme.get()) != schemeList[0]:
        button_rename['state'] = NORMAL
        label_error.configure(text="")
    else:
        label_error.configure(text="ERROR: One or more settings has not been set to a valid selection")

# Checks that proper values are still assigned before beginning the renaming process
# Resets values to their defaults (the Scheme setting remains because it is operating system dependent)
# If any invalid values are found it will prompt the user and disable the button
def renameFiles():
    global folder_path
    if folder_path != "" and str(location.get()) != locationList[0] and str(scheme.get()) != schemeList[0]:
        result = sc.renameFilesShell(scheme, location, folder_path)
        button_rename['state'] = DISABLED
        location.set(locationList[0])
        folder_path = ""
        label_preview.configure(text="All .jpg files in the _____ folder will be renamed")
        label_error.configure(text=result, fg = "green")
    else:
        button_rename['state'] = DISABLED
        label_error.configure(text="ERROR: One or more settings has been changed to an invalid selection")


# Everything bellow, aside from the variables, are GUI settings
window = Tk()
bgColor = "gray20"
txtColor = "gray80"


window.title("CSU East Bay - Batch Rename")
window.geometry("850x260")
window.config(background = "gray50")

header = Frame(window)
setup_buttons = Frame(window)
other_buttons = Frame(window)

header.pack(side="top", fill="both", expand=True)
setup_buttons.pack(fill="both", expand=True)
other_buttons.pack(fill="both", expand=True)
header.config(bg = "gray50")
setup_buttons.config(bg = "gray50")
other_buttons.config(bg = "gray50")

locationList = [
    "Location",
    "Concord",
    "EdenLanding"
]

schemeList = [
    "OS",
    "Windows",
    "Linux"
]


location = StringVar()
scheme = StringVar()
folder_path = ""
location.set(locationList[0])
#Set scheme to current Operating System
scheme.set(platform.system())


label_file_explorer = Label(header,  
                            text = "Batch Rename for PhenoCam", 
                            width = 100, height = 2, 
                            fg = txtColor,
                            bg = bgColor)

label_preview = Label(header,  
                            text = "All .jpg files in the _____ folder will be renamed",
                            width = 100, height = 2,  
                            fg = txtColor,
                            bg = bgColor)

label_error = Label(header,  
                            text = "",
                            width = 100, height = 2,  
                            fg = "red3",
                            bg = bgColor)  


button_explore = Button(setup_buttons,  
                        text = "Select Folder To Rename", 
                        command = getFolder)

location_option = OptionMenu(setup_buttons, 
                        location,
                        *locationList)

location_option.config(width = 18,
                     highlightthickness = 0)

scheme_option = OptionMenu(setup_buttons, 
                        scheme, 
                        *schemeList)

scheme_option.config(width = 18,
                     highlightthickness = 0)

button_confirm = Button(other_buttons,  
                        text = "Confirm Settings", 
                        command = confirmSettings)

button_rename = Button(other_buttons,  
                        text = "Rename Files", 
                        command = renameFiles,
                        state=DISABLED)

label_credits = Label(other_buttons,
                            text = "Created for the PhenoCam project at CSU East Bay by Sean Dixon",
                            width = 100, height = 1,
                            fg = txtColor,
                            bg = bgColor)


label_preview.grid(column = 1, row = 1, pady = (30,0), padx = (75,0))
label_error.grid(column = 1, row = 2)


button_explore.grid(column = 1, row = 1, padx=(150,0))
scheme_option.grid(column = 3, row = 1)
location_option.grid(column = 2, row = 1, padx = 20)

button_confirm.grid(column = 1, row = 1, padx = 385, pady = (25, 5))   
button_rename.grid(column = 1, row = 2, padx = 385, pady = 5)   

label_credits.grid(column = 1, row = 8, pady = (20,20))

window.mainloop()
