from pytube import YouTube
from tkinter.filedialog import *
from tkinter.messagebox import *
from tkinter import *
from threading import *
downloadBtn={}
font = ('verdana', 20)
file_size = 0

# downloading functions
def startDownload(url):
    global file_size
    path_to_save = askdirectory()
    if path_to_save is None:
        return

    try:
        yt = YouTube(url)
        st = yt.streams.first()
        file_size = st.filesize
        st.download(output_path = path_to_save)
        print("File has been downloaded...")

    except Exception as e:
        print(e)

def btnClicked():
    try:
        downloadBtn['text', ] = "Please wait..."
        downloadBtn['state'] = 'disabled'
        url = urlField.get()
        if url=='':
            return
        print(url)
        thread = Thread(target=startDownload(url,))
        thread.start()
    except Exception as e:
        print(e)

#gui coding
root = Tk()
root.title("My Youtube Downloader")
root.geometry("500x600")

#making url field
urlField = Entry(root, font = font, justify = CENTER)
urlField.pack(side=TOP, fill=X, padx=10)
urlField.focus()

#downloadbutton
DownloadBtn=Button(root, text = "Download Video", font=font, relief="ridge", command=btnClicked)
DownloadBtn.pack(side=TOP, pady=28)

root.mainloop()

# CODE BY: BHAVYA SEHGAL
