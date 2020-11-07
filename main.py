import tkinter, wikipediaapi
import requests
#Configuring tkinter for size and window
root = tkinter.Tk()
root.geometry('680x420')
root.title("Wikipedia Article gets")

#GLOBALS
article_tab =0
#Configuring wikipedia api\

#configuring language
wiki = wikipediaapi.Wikipedia('en', extract_format=wikipediaapi.ExtractFormat.WIKI)

S = requests.Session()
URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action":"query",
    "format": "json",
    "generator":"random",
    "grnnamespace":"0",
    "rvprop":"content",
    "grnlimit": "7"
}

#Functions 
def get_clicked(val):
    if(not val):
        return
    # print(val)
    for l in root.pack_slaves():
       l.destroy()
    
    page = wiki.article(val)
    article_tab = tkinter.Toplevel(root)
    article_tab.title(page.title)

    scrollbar = tkinter.Scrollbar(article_tab)
    scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)

    article = tkinter.Text(article_tab, font="Courier 11",  yscrollcommand= scrollbar.set)
    article.insert(tkinter.END, page.text)
    article.pack()
  
    scrollbar.config(command=article.yview)
   
    
def get_random_articles():
    for l in root.pack_slaves():
       l.destroy()
    R = S.get(url=URL,params=PARAMS)
    Data = R.json()['query']['pages']
    for d in Data:
        d =  Data[d]
        btn = tkinter.Button(root , text=d['title'], command=lambda i=d['title']:get_clicked(i))
        btn.pack()

#Labels and buttons
lb1 = tkinter.Label(root,text="Click Button to get random wikipedia article(s)")

lb1.place(x=340,y=230, anchor="center")
lb1.configure(font=("Courier",18))


btn1 = tkinter.Button(root ,command=get_random_articles, text="Click")
btn1.place(x=340, y=260, anchor="center")
root.mainloop()