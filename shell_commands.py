import subprocess
import os

# Removes the hyphens, underscores and colons as needed using the Rename utility in Linux. 
# Returns a success or error message
def renameFilesShell(scheme, location, folder_path):
    os.chdir(folder_path)
    schemeString = str(scheme.get())
    if schemeString == "Windows":
        subprocess.check_output(["wsl", "rename", "'s/^(.{16})_00/$1/'", "*.jpg" ])
        subprocess.check_output(["wsl", "rename", "'s/^(.{13})_/$1/'", "*.jpg"])
        subprocess.check_output(["wsl", "rename", "'s/-//'", "*.jpg"])
        subprocess.check_output(["wsl", "rename", "'s/-//'", "*.jpg"])
        prependLocation(location)
        return "Batch Rename completed successfully! \n Please confirm all of the files have been renamed before closing this application"
    elif schemeString == "Linux":
        os.system("rename 's/^(.{16}):00/$1/' *.jpg")
        os.system("rename 's/^(.{13})_/$1/' *.jpg")
        os.system("rename 's/://' *.jpg")
        os.system("rename 's/://' *.jpg")
        os.system("rename 's/-//' *.jpg")
        os.system("rename 's/-//' *.jpg")
        prependLocationLinux(location)
        return "Batch Rename completed successfully! \n Please confirm all of the files have been renamed before closing this application"
    else:
        return "ERROR! Something went wrong during the renaming process!"

# Prepends the filename with the designated location
def prependLocation(location):
    if str(location.get()) == "Concord":
        subprocess.check_output(["wsl", "rename", "'s/^/Concord_/'", "*.jpg"])
    elif str(location.get()) == "EdenLanding":
        subprocess.check_output(["wsl", "rename", "'s/^/EdenLanding_/'", "*.jpg"])
    else:
        return "ERROR! Something went wrong during the renaming process!"
        
def prependLocationLinux(location):
    if str(location.get()) == "Concord":
        os.system("rename 's/^/Concord_/' *.jpg")
    elif str(location.get()) == "EdenLanding":
         os.system("rename 's/^/EdenLanding_/' *.jpg")
    else:
        return "ERROR! Something went wrong during the renaming process!"
