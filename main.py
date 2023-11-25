
# import pygame
# import tkinter as tkr
# from tkinter.filedialog import askdirectory
# import os
#
# musicplayer =tkr.Tk()
# musicplayer.title("Music Player")
# musicplayer.geometry("450x350")
#
#
# directory=askdirectory()
# os.chdir(directory)
# songlist=os.listdir()
# playlist=tkr.Listbox(musicplayer,font="Helvetica 12 Bold",bg="green",selectmode=tkr.SINGLE)
#
# for item in songlist:
#     pos =0
#     playlist.insert(pos,item)
#     pos = pos + 1
#
# pygame.init()
# pygame.mixer.init()
#
# # Adding Buttons
# # def play():
# #     pygame.mixer.music.load(playlist.get(tkr.ACTIVE))
# def play():
#     pygame.mixer.music.load(playlist.get(tkr.ACTIVE))
#     pygame.mixer.music.play()
#
# def pause():
#     pygame.mixer.music.pause()
#
# def unpause():
#     pygame.mixer.music.unpause()
#
# def exitmusicplayer():
#     pygame.mixer.music.stop()
#
#
# Button1 = tkr.Button(musicplayer,width=5,height=3,font="Helvetica 12 Bold",text="Play",command=play,bg="red",fg="white")
# Button2 = tkr.Button(musicplayer,width=5,height=3,font="Helvetica 12 Bold",text="Stop",command=exitmusicplayer,bg="red",fg="white")
# Button3 = tkr.Button(musicplayer,width=5,height=3,font="Helvetica 12 Bold",text="Pause",command=pause,bg="red",fg="white")
# Button4 = tkr.Button(musicplayer,width=5,height=3,font="Helvetica 12 Bold",text="UnPause",command=unpause,bg="red",fg="white")
#
# var = tkr.StringVar()
# songtitle = tkr.Label(musicplayer,font="Helvetica 12 Bold",textvariable=var)
#
# songtitle.pack()
# Button1.pack(fill="x")
# Button2.pack(fill="x")
# Button3.pack(fill="x")
# Button4.pack(fill="x")
#
# playlist.pack(fill="both",expand="yes")
# musicplayer.mainloop()

import pygame
import tkinter as tkr
from tkinter.filedialog import askdirectory
import os

musicplayer = tkr.Tk()
musicplayer.title("Music Player")
musicplayer.geometry("450x350")

directory = askdirectory()
os.chdir(directory)
songlist = os.listdir()
playlist = tkr.Listbox(musicplayer, font=("Helvetica", 12, "bold"), bg="green", selectmode=tkr.SINGLE)

pos = 0
for item in songlist:
    playlist.insert(pos, item)
    pos += 1

pygame.init()
pygame.mixer.init()

# Adding Buttons
def play():
    pygame.mixer.music.load(playlist.get(tkr.ACTIVE))
    pygame.mixer.music.play()

def pause():
    pygame.mixer.music.pause()

def unpause():
    pygame.mixer.music.unpause()

def exitmusicplayer():
    pygame.mixer.music.stop()

Button1 = tkr.Button(musicplayer, width=5, height=3, font=("Helvetica", 12, "bold"), text="Play", command=play, bg="red", fg="white")
Button2 = tkr.Button(musicplayer, width=5, height=3, font=("Helvetica", 12, "bold"), text="Stop", command=exitmusicplayer, bg="red", fg="white")
Button3 = tkr.Button(musicplayer, width=5, height=3, font=("Helvetica", 12, "bold"), text="Pause", command=pause, bg="red", fg="white")
Button4 = tkr.Button(musicplayer, width=5, height=3, font=("Helvetica", 12, "bold"), text="UnPause", command=unpause, bg="red", fg="white")

var = tkr.StringVar()
songtitle = tkr.Label(musicplayer, font=("Helvetica", 12, "bold"), textvariable=var)

songtitle.pack()
Button1.pack(fill="x")
Button2.pack(fill="x")
Button3.pack(fill="x")
Button4.pack(fill="x")

playlist.pack(fill="both", expand="yes")
musicplayer.mainloop()
