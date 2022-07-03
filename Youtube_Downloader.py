#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from tkinter import *
from pytube import YouTube

root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("ZyckTech-youtube video downloader")


Label(root,text = 'Youtube Video Downloader', font ='arial 20 bold').pack()




##enter link
link = StringVar()

Label(root, text = 'Paste Youtube Link Here:', font = 'arial 15 bold').place(x= 160 , y = 60)
link_enter = Entry(root, width = 70,textvariable = link).place(x = 32, y = 90)



#function to download video


def Downloader():
     
    url =YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text = 'DOWNLOADED', font = 'arial 15').place(x= 180 , y = 210)  


Button(root,text = 'DOWNLOAD NOW', font = 'arial 15 bold' ,bg = 'Blue', padx = 2, command = Downloader).place(x=180 ,y = 150)



root.mainloop()


# In[ ]:





# In[ ]:




