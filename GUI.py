import tkinter as tk 
from PIL import ImageTk,Image  
import Functions as F 
import Connect as C
import turtle as T
import time 


#creates a cofigures the window
window = tk.Tk()
window.title("TECH LOCATOR")
window.geometry("1500x1500")
#window.configure(background='black')


#resizes images to by a specific factor
def resizeImage(imagePath,factor):
    
    image = Image.open(imagePath) 
    orgWidth, orgHeight = image.size
    n = factor
    newHeight = int(orgHeight* n)
    newWidth = int(orgWidth * n)
    image = image.resize((newWidth,newHeight), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(image)
    
    return img

#creates a frame 
def createPage(root, mainbg):

    container = tk.Frame(root, bg=mainbg)

    return container

#draws cicles with turtle
def drawCircle(T,colour,size,x,y):
    T.penup()
    T.color(colour)
    T.fillcolor(colour)
    T.goto(x,y)                                        
    T.begin_fill()
    T.pendown()
    T.circle(size)
    T.penup()
    T.end_fill()
    T.pendown()

#Introductory Page
def Intro(root):
    space = tk.Canvas(root)
    space.place(x=0,y=0,relwidth=1, relheight=1)
    t = T.RawTurtle(space)
    drawCircle(t,"red",50,25,0)#calling draw circle function
    drawCircle(t,"yellow",50,0,0)
    drawCircle(t,"black",50,-25,0)
    n = 0
    #loop to draw box
    while n < 2:
        t.forward(400)
        t.left(90)
        t.forward(30)
        t.left(90)
        n += 1
    t.penup()
    t.goto(60,0)
    t.write("WELCOME TECH LOCATOR",font=("Arial",12,"bold"))#printing items to screen
    time.sleep(1)


    return mainPage(window,"pexels-photo-1598366.jpeg","The Tech Locator",150)
    
    
    

    
#creates main page of program and returns a the frame container 
def mainPage(root, headerImage, headerText, headerHeight):
    #page = ttk.Frame(root)
    page = tk.Frame(root)
    page.place(x=0, y=0, relwidth=1, relheight=1)

    page1 = tk.Frame(page)
    img = resizeImage("sea.jpg",0.5)
    mp_bg = tk.Label(page1,image = img)
    mp_bg.pack()

    #header = CTK.CTkFrame(page, height=headerHeight)
    #header.pack(fill="x")
    #header.pack_propagate(False)  
   # img = resizeImage(headerImage,0.5)
   # lb = CTK.CTkLabel(header, image=img, width=80, height=80)#,bg="blue")
    #lb.image = img
    #lb.pack(fill="x",expand=True)
    
   #textFrame =  CTK.CTkFrame(header)
    #text = CTK.CTkLabel(textFrame, text=headerText, width=120, height=25, corner_radius=15) #font="times 30 bold underline"
    #text.pack()
   #textFrame.place(relx=0.5, rely=0.5, anchor="center")

    #Footer = tk.Frame(window, bg="black", height=50)#fixed
    #txt = tk .Label(Footer,text="©2019",font="times 20 bold ", fg="white",bg="blue")
    #txt.pack(side="left")
   # txt = tk .Label(Footer,text="YOLO INC.",font="times 20 bold ", fg="white",bg="blue")
   # txt.pack(side="bottom")

    #Footer.pack(side="bottom", fill="x")
    #Footer.pack_propagate(False)

    #containter = createPage(page, "yellow")
    

    return page




#creates a new page
def showPage(root, mainpageb, headerImg, headerText, headerHeight,pageN ):#pageN helps to call display laptops
  
    page = createPage(root, mainpageb)
    page.place(x=0, y=0, relwidth=1, relheight=1)

    
    header = tk.Frame(page, height=headerHeight)
    col = header.cget("background")#getting default background colour for tkinter
    header.pack(fill="x")
    header.pack_propagate(False)

    container = createPage(page, col)
    container.pack(fill="both", expand=True)

    displayLaptops(container, pageN)
    
    bck = tk.Button(header,text="Back",font="times 12 bold ", height=2,command=page.place_forget,bg="black",fg="white")
    bck.pack(side="left")

    img = resizeImage(headerImg,1)
    l1 = tk.Label(header, image=img)#inserting image into header frame
    l1.image = img
    l1.pack(fill="x", expand=True)

    textFrame = tk.Frame(header)#a frame for text in the header
    text = tk.Label(textFrame, text=headerText, font="times 30 bold underline", fg="black")
    text.pack(fill="x")
    textFrame.place(relx=0.5, rely=0.5, anchor="center")

    return 


#calls  showPage function with its parameters and places items on the main page
def createTypes(name, typeImg, headerText, root, height, width, bg, headerHeight,page):
    fr = tk.Frame(root)#frame in container frame of main page

    #configuring a grid system in the container frame for the main page items 
    fr.grid_columnconfigure(0, weight=1)
    fr.grid_columnconfigure(2, weight=1)
    fr.grid_rowconfigure(0, weight=1)
    fr.grid_rowconfigure(4, weight=1)
    fr.grid_rowconfigure(5, weight=1)

    if page == 1:
        notes = tk.Label(fr, text="Searches by Brand,Category and Release Date",font="times 15 bold")
        notes.pack(side="bottom",fill="x")
        

    elif page == 2:
        notes = tk.Label(fr, text="Searches by Brand,Category and Price ",font="times 15 bold")
        notes.pack(side="bottom",fill="x")
        
    if typeImg != None:
        img = resizeImage(typeImg,1)
        lb = tk.Label(fr, image=img, width=width, height=height)
        lb.image = img
        lb.pack(fill="x", expand=True, pady=3)
        btn = tk.Button(fr, text=name, fg="black", font="times 18 bold ",height=2, command=lambda: showPage(window, bg, typeImg, headerText, headerHeight,page))
              
        btn.pack(side="bottom", fill="x")
        
        

    else:
        btn = tk.Button(fr, text=name, bg="black", fg="#fff", height=2,width=35)
        btn.pack(side="bottom", fill="x")

    return fr 




def onselect(event, listSelection, root,page):
    if page == 1:
        info = F.search()

        empty = tk.Label(root, bg="#fff")
        empty.grid(row=3, column=1, sticky=tk.N+tk.S+tk.E+tk.W)


        w = event.widget
        try: 
            index = int(w.curselection()[0])#getting index of selected item
            value = w.get(index)#getting content of selected item at that index
            data = filter(lambda laptop: laptop[1] == value, info)#returning a list of data about laptop selected 
            data = list(data)#changing filter object to a list
        #querying specific info from list
            specs = data[0][2].split("||")
            firstSet = "||".join(specs [:2])
            secondSet = "||".join(specs[2:])
            specs = firstSet + "\n"+secondSet

            listSelection.delete(0,tk.END)
            listSelection.insert(tk.END, "Name: " + data[0][1])
            listSelection.insert(tk.END,"  ")
            listSelection.insert(tk.END, "Specs: " + firstSet)
            listSelection.insert(tk.END, secondSet)
            listSelection.insert(tk.END,"  ")
            listSelection.insert(tk.END, "Category: " + data[0][3])
            listSelection.insert(tk.END,"  ")
            listSelection.insert(tk.END, "Release Date : " + str(data[0][4]))
            img = resizeImage(data[0][5], 0.4)
            lb = tk.Label(root, image=img)
            lb.image = img
            lb.grid(row=3, column=1)
        except:
            pass

    if page == 2:
        info = C.search()

        empty = tk.Label(root, bg="#fff")
        empty.grid(row=3, column=1, sticky=tk.N+tk.S+tk.E+tk.W)

        w = event.widget
        index = int(w.curselection()[0])
        value = w.get(index)
        data = filter(lambda laptop: laptop[1] == value, info) 
        data = list(data)

        listSelection.delete(0,tk.END)
        listSelection.insert(tk.END, "Name: " + data[0][0]+" "+data[0][1])
        listSelection.insert(tk.END, "Category: "+ data[0][2])
        listSelection.insert(tk.END, "Screen size: " + str(data[0][3])+"inch")
        listSelection.insert(tk.END, "Screen Resolution: "+ str(data[0][4]))
        listSelection.insert(tk.END, "CPU: " + str(data[0][5]))
        listSelection.insert(tk.END,"RAM: " + str(data[0][6]))
        listSelection.insert(tk.END, "Memory: " + str(data[0][7]))
        listSelection.insert(tk.END,"GPU: " + data[0][8])
        listSelection.insert(tk.END, "Weight: " + str(data[0][10]))
        listSelection.insert(tk.END, "Price: " + str(int(data[0][11])*5.75)+" " +"cedis")

    
def callSearch(brand, category, release, listNode):
    listNode.delete(0, tk.END)

    brandInfo = brand.get() 
    categoryInfo = category.get()
    releaseInfo = release.get()
    data = F.search(searchword=categoryInfo, brand=brandInfo, releaseDate= releaseInfo)
    
    for x in data:
        listNode.insert(tk.END, x[1])


def callSearch1(brand, category,price, listNode):
    listNode.delete(0, tk.END)

    brandInfo = brand.get()
    categoryInfo = category.get()
    priceInfo = price.get()
    data = C.search(searchword=categoryInfo,brand=brandInfo,price=priceInfo)

    for x in data:
        listNode.insert(tk.END, x[1])
#get items from database  
def createDropMenu(menuitems, menuname, menuframe, labelrow, labelcol, droprow, dropcol):
    brandNames = ["all"]
    brandNames += menuitems
    name = menuname+": "
    brandVar = tk.StringVar(menuframe)# a tkinter control variable, limiting scope of variable to menuframe
    brandVar.set(brandNames[0])#default value

    brand = tk.Label(menuframe, text=name, fg='black', font=("Helvetica", 12, "bold"))
    brand.grid(row=labelrow, column=labelcol, ipady=5, ipadx=5, padx=10, pady=5)
    brandDrop = tk.OptionMenu(menuframe, brandVar, *brandNames)#provides dropdown functionality 
    brandDrop.grid(row=droprow, column=dropcol, ipady=5, ipadx=5, padx=10, pady=5)
    return brandVar#keeps changing based on what is clicked


def Page1(root,page):
    info = F.search()#laptops from database 1
    searchBar = tk.Frame(root, height=10)
    col = searchBar.cget("background")
    
    searchBar.grid(row=0, columnspan=2, sticky=tk.E+tk.W)

    brandlist = F.tableNames()
    brand = createDropMenu(brandlist, "Brand", searchBar, 0, 0, 0, 1)

    categories = ["College", "Business", "Gaming","Travellers"]
    category = createDropMenu(categories, "Category", searchBar, 0, 2, 0, 3)

    years = [2017, 2018, 2019]
    release = createDropMenu(years, "Release Date", searchBar, 0, 4, 0, 5)

    searchBar.columnconfigure(0, weight=1)
    searchBar.columnconfigure(1, weight=1)
    searchBar.columnconfigure(2, weight=1)
    searchBar.columnconfigure(3, weight=1)
    searchBar.columnconfigure(4, weight=1)
    searchBar.columnconfigure(5, weight=1)
    searchBar.columnconfigure(6, weight=2)

    lbl1 = tk.Label(root, text="Laptops:", fg='black',bg=col, font=("Helvetica", 16, "bold"))
    lbl2 = tk.Label(root, text="Details:", fg='black',bg=col, font=("Helvetica", 16,"bold"))
    lbl1.grid(row=1, column=0, sticky=tk.W)
    lbl2.grid(row=1, column=1, sticky=tk.W)

    frm = tk.Frame(root)
    frm.grid(row=2, rowspan=2, column=0, sticky=tk.N+tk.S)
    root.rowconfigure(3, weight=1)
    root.columnconfigure(1, weight=1)

    scrollbar = tk.Scrollbar(frm, orient="vertical")
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    listNodes = tk.Listbox(frm, width=50, yscrollcommand=scrollbar.set, font=("Helvetica", 12))
    listNodes.pack(expand=True, fill=tk.Y)
 
    scrollbar.config(command=listNodes.yview)

    listSelection = tk.Listbox(root, height=10, font=("Helvetica", 12))
    listSelection.grid(row=2, column=1, sticky=tk.E+tk.W+tk.N)
     
    listNodes.bind('<<ListboxSelect>>', lambda e: onselect(e, listSelection, root,page))#with a certain event sequence call this function

    empty = tk.Label(root, bg="#fff")
    empty.grid(row=3, column=1, sticky=tk.N+tk.S+tk.E+tk.W)

    for x in info:
        listNodes.insert(tk.END, x[1])#inserting laptop names

    search = tk.Button(searchBar, text="Search", width=30, bg="blue", fg="#fff", font=("Helvetica", 12, "bold"), command=lambda: callSearch(brand, category, release, listNodes))
    search.grid(row=0, column=6, ipady=5, ipadx=5, padx=10, pady=5)



def Page2(root,page):
    info = C.search()
    searchBar = tk.Frame(root, height=10)
    col = searchBar.cget("background")
    
    searchBar.grid(row=0, columnspan=2, sticky=tk.E+tk.W)

    brandlist = C.uniqueSelect(C.tableNames(),"Company")#select uniquely from Company column
    brand = createDropMenu(brandlist, "Brand", searchBar, 0, 0, 0, 1)

    categories = C.uniqueSelect(C.tableNames(),"Category")
    category = createDropMenu(categories, "Category", searchBar, 0, 2, 0, 3)

    _Price = ["cheap","moderate","expensive"]
    price = createDropMenu(_Price, "Price", searchBar, 0, 4, 0, 5)

    searchBar.columnconfigure(0, weight=1)
    searchBar.columnconfigure(1, weight=1)
    searchBar.columnconfigure(2, weight=1)
    searchBar.columnconfigure(3, weight=1)
    searchBar.columnconfigure(4, weight=1)
    searchBar.columnconfigure(5, weight=1)
    searchBar.columnconfigure(6, weight=2)

    lbl1 = tk.Label(root, text="Laptops:", fg='black',bg=col, font=("Helvetica", 16, "bold"))
    lbl2 = tk.Label(root, text="Details:", fg='black',bg=col, font=("Helvetica", 16,"bold"))
    lbl1.grid(row=1, column=0, sticky=tk.W)
    lbl2.grid(row=1, column=1, sticky=tk.W)

    frm = tk.Frame(root)
    frm.grid(row=2, rowspan=2, column=0, sticky=tk.N+tk.S)
    root.rowconfigure(3, weight=1)
    root.columnconfigure(1, weight=1)

    scrollbar = tk.Scrollbar(frm, orient="vertical")
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    listNodes = tk.Listbox(frm, width=50, yscrollcommand=scrollbar.set, font=("Helvetica", 12))
    listNodes.pack(expand=True, fill=tk.Y)
 
    scrollbar.config(command=listNodes.yview)


    listSelection = tk.Listbox(root, height=10, font=("Helvetica", 12))
    # h = tk.Button(listSelection, text="BUY")
    # h.grid()
    listSelection.grid(row=2, column=1, sticky=tk.E+tk.W+tk.N)
    listNodes.bind('<<ListboxSelect>>', lambda e: onselect(e, listSelection, root,page))#with a certain event sequence call this function

    empty = tk.Label(root, bg="#fff")
    empty.grid(row=3, column=1, sticky=tk.N+tk.S+tk.E+tk.W)

    for x in info:
        listNodes.insert(tk.END, x[1])#inserting laptop names

    search = tk.Button(searchBar, text="Search", width=30, bg="blue", fg="#fff", font=("Helvetica", 12, "bold"), command=lambda: callSearch1(brand, category,price, listNodes))
    search.grid(row=0, column=6, ipady=5, ipadx=5, padx=10, pady=5)


def displayLaptops(root, page):
    if page == 1:
        Page1(root,page)
    elif page == 2:
        Page2(root,page)
    
























   