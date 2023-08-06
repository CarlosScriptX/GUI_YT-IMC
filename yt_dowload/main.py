from customtkinter import *
import pytube
import os

window = CTk()
window.title("Video downloader")
window._set_appearance_mode("#262525")
window.geometry("300x450")
window.resizable(False,False)

def destroy(button):
    button.destroy()

def createButton(event=destroy):
    confirm = CTkButton(window,text="ok",font=arial,height=28,width=45,hover_color="green",command=event)
    confirm.place(x=233,y=210)

def buttonSearch():
    namelink = box.get()
    try:
       yt = pytube.YouTube(namelink)
       buttonDowload = CTkButton(window,text="📥    BAIXAR",font=arial,corner_radius=3,fg_color="#067bba",command=buttondownload)
       buttonDowload.place(x=90,y=210)
    except:
        buttonDowload = CTkButton(window,text="📥    BAIXAR",font=arial,corner_radius=3,fg_color="#04354f",state=DISABLED)
        buttonDowload.place(x=90,y=210)

def buttondownload(eventButton=createButton):
    namelink = box.get()
    yt = pytube.YouTube(namelink)
    pastName = f"{os.path.expanduser('~')}/Videos"
    baixar = yt.streams.get_highest_resolution()
    baixar.download(pastName)
    local = CTkLabel(window,text=f"local:{os.path.expanduser('~')}/Videos",bg_color="#1e2021",width=300,height=35,font=arial2)
    local.place(x=0,y=420)
    return eventButton()



#fontes
fonte = CTkFont(family="Arial",size=12)
fontYou = CTkFont(family="Arial",size=44)
fontTube = CTkFont(family="Arial",size=45)
fontDowload = CTkFont(family="Arial",size=30)
arial = CTkFont(family="Arial",size=19)
arial2 = CTkFont(family="Arial",size=16)



#link
box = CTkEntry(window,placeholder_text="cole o link",font=fonte,text_color="white",placeholder_text_color="gray"\
,border_color="white",border_width=1,corner_radius=5,fg_color="#262525")
box.place(x=90,y=175)

#busca
search = CTkButton(window,text="🔎",height=28,width=45,font=arial,text_color="black",corner_radius=3,\
fg_color="#067bba",command=buttonSearch)
search.place(x=233,y=175)

#buttonDowload
buttonDowload = CTkButton(window,text="📥    BAIXAR",font=arial,corner_radius=3,fg_color="#04354f",state=DISABLED)
buttonDowload.place(x=90,y=210)


#you
labelYou = CTkLabel(window,text="you",font=fontYou,text_color="black")
labelYou.place(x=62,y=33)

#tube
buttonTube = CTkButton(window,text="TUBE",fg_color="red",state=DISABLED,font=fontTube,corner_radius=15)
buttonTube.place(x=135,y=33)

#labeldowload
labelDownload = CTkLabel(window,text="Downloader",font=fontDowload)
labelDownload.place(x=92,y=90)

#frame
nameVideo = CTkFrame(window,width=450,height=40,bg_color="#1e2021")
nameVideo.place(x=-1,y=420)

local = CTkLabel(window,text=" ",bg_color="#1e2021")

window.mainloop()
