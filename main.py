import tkinter
import customtkinter
from pytube import YouTube
import sys, os


def createDirectory(name):
    path = sys.path[0] # Take the complete directory to the location where the code is, you can substitute it to the place where you want to save the video.
    if not(os.path.isdir(f'{path}/{name}')): # Check if directory does not exist
        path = os.path.join(sys.path[0], name) # Set the directory to the specified path and the name that was given to it
        os.mkdir(path) # Create a directory
directoryName = 'Video'
createDirectory(directoryName)
path = sys.path[0] # Take the complete directory to the location where the code is, you can substitute it to the place where you want to save the video.

def startDownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink)
        video = ytObject.streams.get_highest_resolution()
        video.download(output_path=f'{path}/{directoryName}')
    except:
        print("YT link is invalid")

# system settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# app frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")

# UI elements
title = customtkinter.CTkLabel(app, text='Insert a youtube link')
title.pack(padx=10, pady=10)

# link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

# Download 
download = customtkinter.CTkButton(app, text="download", command=startDownload)
download.pack(padx=10, pady=10)

# run app
app.mainloop()