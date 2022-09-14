from tkinter import *
from tkinter import messagebox 
from pytube import YouTube
import urllib
from urllib.request import urlopen
from tkinter import filedialog
from moviepy import *
from moviepy.editor import VideoFileClip
import shutil

# Functions 
# Checking internet connection 
def checkLink():
    try:
        #Check connect to the link
        urlopen(str(link.get()), timeout=1)
        return messagebox.showinfo("Connected!", "You can download!")
    except urllib.error.URLError as err:
        return messagebox.showerror(err, "Unable to find the link\nPlease try again later.")

def downloader():
    if str(link.get()) is None:
        return messagebox.showwarning("Warning!","Link video is empty!")
    else:
        # Get user path 
        url = str(link.get())
        # Get selected directory 
        user_dir = directory.cget("text")
        # Download video 
        url = YouTube(str(link.get()))
        video = url.streams.get_highest_resolution().download()
        vid_clip = VideoFileClip(video)
        vid_clip.close()
        shutil.move(video, user_dir)

# Allows user to select a path from the explorer
def select_locs():
    find_locs = filedialog.askdirectory()
    directory.config(text=find_locs)

# UI 
snap = Tk()
snap.resizable(0,0)
snap.title("YouTube Video Downloader")
canvas = Canvas(snap, width=500, height=300)
canvas.pack()

# Image logo 
logo_img = PhotoImage(file="youtube-Logo.png")
logo_img = logo_img.subsample(x=2, y=2) # Resize image
canvas.create_image(250, 57, image=logo_img)
labelVersion = Label(snap, text="Ver. 0.5", font="arial 10 bold").place(x=300, y=110)

# Here is text field to enter a link 
labelLink = Label(snap, text="Link Video: ", font="arial 13 bold").place(x=30, y=130)
link = StringVar()
link_submit = Entry(snap, width=55, textvariable=link).place(x=30, y=155)

# Select path for saving the file 
path_select = Label(snap, text="Download Location:", font="arial 13 bold").place(x=30, y=185)

my_directory = ''
directory = Label(snap, text=my_directory, bg='light grey', font="arial 10 italic")

select_path_btn = Button(snap, text="....", height=1, width= 4, font="arial 9 bold", bg="light grey", padx=1,
        command=select_locs)
canvas.create_window(300, 197, window=directory)
canvas.create_window(457, 195, window=select_path_btn)

Button(snap, text="LINK CHECK", font="arial 15 bold", bg="grey", padx=2,
    command=checkLink, borderwidth=2).place(x=90, y=250)
Button(snap, text="DOWNLOAD", font="arial 15 bold", bg="grey", padx=2,
    command=downloader, borderwidth=2).place(x=250, y=250)

snap.mainloop()