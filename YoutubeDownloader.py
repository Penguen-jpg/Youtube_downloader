from pytube import YouTube
import tkinter
from tkinter import font
import tkinter.messagebox

def download():
    video = YouTube(link_entry.get())
    # 建立串流(選擇最高解析度)
    stream = video.streams.filter(progressive=True).get_highest_resolution()
    # 下載影片
    stream.download()
    # 顯示訊息
    tkinter.messagebox.showinfo("Information", "下載完成")

# 建立視窗
window = tkinter.Tk()
window.geometry("800x600")
window.title("Youtube影片轉換器")

title = tkinter.Label(window, text="Youtube影片轉換器", width="50", 
                        height="5", font=("微軟正黑體", 25))
title.pack()

# 建立link群組
link_frame = tkinter.Frame(window)
link_frame.pack(side=tkinter.TOP)
link_label = tkinter.Label(link_frame, text="影片網址", 
                        font=("微軟正黑體", 20))
link_label.pack(side=tkinter.TOP)
link_entry = tkinter.Entry(link_frame,width="50") # 讀取連結
link_entry.pack(side=tkinter.LEFT)

# 建立download群組
download_frame = tkinter.Frame(window)
download_frame.pack(side=tkinter.TOP)
download_button = tkinter.Button(download_frame, text="下載", 
                        font=("微軟正黑體", 15), command=download, width="8")
download_button.pack(side=tkinter.LEFT)

# 視窗迴圈
window.mainloop()

