# phenocam_rename

# Pheno Batch Rename for CSU East Bay's PhenoCam Project


## About

**Pheno Batch Rename** is designed for use with the CSU East Bay PhenoCam project; 
with it, you can rename all the photos in a given folder to 
the naming scheme used by the processing software.

This application relies on the Linux "rename" utility to change file names. For this application to work on Windows, WSL and Linux are required to be installed on the computer. This is further explained in the Installation instructions below.

Both Windows10 and Linux systems are supported but given the ease of setup, Linux is recommended.

---

## Installation



### Windows 10:


***PYTHON IS REQUIRED https://www.python.org/downloads/***

1. Open PowerShell as an Administrator and run the following code. *PowerShell is pre-installed on Windows, use the windows search to find it.*
>`dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart`
> * What it is: This command will enable WSL v1. WSL is used to run Linux, in this case Ubuntu, from within Windows which this application requires. 
> * *[microsoft documentation](https://docs.microsoft.com/en-us/windows/wsl/install-win10)*
    
2. Restart your computer.

3. Open the Microsoft Store app and search for / install Ubuntu
> * There are a few versions of Ubuntu on the Microsoft Store; *at the time of writing* the prefered version is the one simply titled Ubuntu

4. Launch Ubuntu and follow the prompts to create your account (username and password). *The first time launching Ubuntu could take a few minutes*

5. After creating your account, still in Ubuntu, enter the following command to update Ubuntu. *This could take a few minutes*
>`sudo apt-get update && sudo apt-get upgrade`

6. Still within Ubuntu, enter the following command to download and install the rename utility.
>`sudo apt install rename`

7. Download the files from this repository.

### Linux:

1. Download / Install the rename utility. For example if using Ubuntu or other debian based linux
> `sudo apt install rename`

2. Download / install Python3. For example if using Ubuntu or other debian based linux
> `sudo apt install python3`

3. Download the files from this repository.

---

## Execution

1. **Make sure you have a backup of the data before you rename it.**

2. Launch the application and set the proper values for the batch you are renaming. (Select the folder containing the photos, the location of the phenocam, and the scheme. *Choose the "scheme" that corresponds to your Operating System.*)  


3. When all values have been assigned, click the "Confirm Settings" button; this will unlock the "Rename" button.  

4. Press the "Rename" button to begin the process. It should only take a few seconds to complete.

5. You should see a message that says its completed successfully. Confirm that all the files are renamed before closing the application.

*After renaming files, the selected folder and location values are reset to help prevent mistakes if multiple folders are being worked on in a single sitting.*
