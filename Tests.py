


def main():
    import Functions as F
    import GUI as G
    #main page for program
    window = G.window#calling window attribute of GUI
   # mainFrame = G.Intro(window)


    mainFrame = G.mainPage(window,"sea.jpg","The Tech Locator",150)


    #list of items to be placed on the mainpage
    typeList = [("Laptops A","Laptop type.jpg", "grey", 150,1),("Laptops B","Apple-MacBook-Air-928001.jpg", "grey", 150,2)]
    #accumulator variables for columns
    col = 0
    col2 = 0
    

    #looping through list
    for i in typeList:
        #selection statement for arrangement of items on the main page
        if col > 2:
            type2 =  G.createTypes(i[0],i[1], i[0], mainFrame, 200, 250, i[2], i[3],i[4])#creates categories and passes parameters to create new page by the click of a button
            type2.grid(row=1, column=col2, padx=100, pady=10, sticky="nws")
            col2 +=1
        else:
            type1 = G.createTypes(i[0],i[1] , i[0], mainFrame, 200, 250, i[2], i[3],i[4])
            type1.grid(row=0, column=col, padx=100, pady=10, sticky="nws")
            col += 1
    mainFrame.pack(fill="both", expand=True)
    

    
    
    window.mainloop()

if __name__ == '__main__':   
    main()






