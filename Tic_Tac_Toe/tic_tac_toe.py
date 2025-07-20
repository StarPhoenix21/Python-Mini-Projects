import tkinter as t
import random

root=t.Tk()
tur=0
def click(event):
    global tur
    tur=1
    button1=event.widget
    n1=str(button1)
    n=n1[-1]
    print(n)
    print(f"turn {tur}")
    if button1["text"]==" ":
        if tur==1:
            button1["text"]='X'
            tur=0
        
    if tur==0:
        while(True):
            bv=["n","2","3","4","6","7","8","9"]
            a=random.choices(bv)
            c=str(a)
            d=c[2]
            # d="1"
            # Win confirm
            if b1["text"]=='O' and b2["text"]=='O' and b3["text"]!='O' and b3["text"]!='X':
                d="3" 
            elif b4["text"]=='O' and b5["text"]=='O' and b6["text"]!='O' and b6["text"]!='X':
                d="6" 
            elif b7["text"]=='O' and b8["text"]=='O' and b9["text"]!='O' and b9["text"]!='X':
                d="9" 
            elif b1["text"]=='O' and b3["text"]=='O' and b2["text"]!='O' and b2["text"]!='X':
                d="2" 
            elif b4["text"]=='O' and b6["text"]=='O' and b5["text"]!='O' and b5["text"]!='X':
                d="5" 
            elif b7["text"]=='O' and b9["text"]=='O' and b8["text"]!='O' and b8["text"]!='X':
                d="8" 
            elif b2["text"]=='O' and b3["text"]=='O' and b1["text"]!='O' and b1["text"]!='X':
                d="1" 
            elif b5["text"]=='O' and b6["text"]=='O' and b4["text"]!='O' and b4["text"]!='X':
                d="4" 
            elif b8["text"]=='O' and b9["text"]=='O' and b7["text"]!='O' and b7["text"]!='X':
                d="7" 
            elif b1["text"]=='O' and b4["text"]=='O' and b7["text"]!='O' and b7["text"]!='X':
                d="7" 
            elif b2["text"]=='O' and b5["text"]=='O' and b8["text"]!='O' and b8["text"]!='X':
                d="8" 
            elif b3["text"]=='O' and b6["text"]=='O' and b9["text"]!='O' and b9["text"]!='X':
                d="9" 
            elif b1["text"]=='O' and b7["text"]=='O' and b4["text"]!='O' and b4["text"]!='X':
                d="4" 
            elif b2["text"]=='O' and b8["text"]=='O' and b5["text"]!='O' and b5["text"]!='X':
                d="5" 
            elif b3["text"]=='O' and b9["text"]=='O' and b6["text"]!='O' and b6["text"]!='X':
                d="6" 
            elif b4["text"]=='O' and b7["text"]=='O' and b1["text"]!='O' and b1["text"]!='X':
                d="1" 
            elif b5["text"]=='O' and b8["text"]=='O' and b2["text"]!='O' and b2["text"]!='X':
                d="2" 
            elif b6["text"]=='O' and b9["text"]=='O' and b3["text"]!='O' and b3["text"]!='X':
                d="3" 
            elif b1["text"]=='O' and b5["text"]=='O' and b9["text"]!='O' and b9["text"]!='X':
                d="9"
            elif b3["text"]=='O' and b5["text"]=='O' and b7["text"]!='O' and b7["text"]!='X':
                d="7" 
            elif b1["text"]=='O' and b9["text"]=='O' and b5["text"]!='O' and b5["text"]!='X':
                d="5" 
            elif b3["text"]=='O' and b7["text"]=='O' and b5["text"]!='O' and b5["text"]!='X':
                d="5"
            elif b5["text"]=='O' and b9["text"]=='O' and b1["text"]!='O' and b1["text"]!='X':
                d="1"
            elif b5["text"]=='O' and b7["text"]=='O' and b3["text"]!='O' and b3["text"]!='X':
                d="3"
            # protect from coner trick
            elif b1["text"]=='X' and b9["text"]=='X' and b2["text"]==" ":
                d="2"
            elif b1["text"]=='X' and b9["text"]=='X' and b4["text"]==" ":
                d="4"
            elif b1["text"]=='X' and b9["text"]=='X' and b6["text"]==" ":
                d="6"
            elif b1["text"]=='X' and b9["text"]=='X' and b8["text"]==" ":
                d="8"
            elif b3["text"]=='X' and b7["text"]=='X' and b2["text"]==" ":
                d="2"
            elif b3["text"]=='X' and b7["text"]=='X' and b4["text"]==" ":
                d="4"
            elif b3["text"]=='X' and b7["text"]=='X' and b6["text"]==" ":
                d="6"
            elif b3["text"]=='X' and b7["text"]=='X' and b8["text"]==" ":
                d="8"
            # not let to win

            elif b1["text"]=='X' and b2["text"]=='X' and b3["text"]!='O':
                d="3"
            elif b4["text"]=='X' and b5["text"]=='X' and b6["text"]!='O':
                d="6"
            elif b7["text"]=='X' and b8["text"]=='X' and b9["text"]!='O':
                d="9"
            elif b1["text"]=='X' and b3["text"]=='X' and b2["text"]!='O':
                d="2"
            elif b4["text"]=='X' and b6["text"]=='X' and b5["text"]!='O':
                d="5"
            elif b7["text"]=='X' and b9["text"]=='X' and b8["text"]!='O':
                d="8"
            elif b2["text"]=='X' and b3["text"]=='X' and b1["text"]!='O':
                d="n"
            elif b5["text"]=='X' and b6["text"]=='X' and b4["text"]!='O':
                d="4"
            elif b8["text"]=='X' and b9["text"]=='X' and b7["text"]!='O':
                d="7"
            elif b1["text"]=='X' and b4["text"]=='X' and b7["text"]!='O':
                d="7"
            elif b2["text"]=='X' and b5["text"]=='X' and b8["text"]!='O':
                d="8"
            elif b3["text"]=='X' and b6["text"]=='X' and b9["text"]!='O':
                d="9"
            elif b1["text"]=='X' and b7["text"]=='X' and b4["text"]!='O':
                d="4"
            elif b2["text"]=='X' and b8["text"]=='X' and b5["text"]!='O':
                d="5"
            elif b3["text"]=='X' and b9["text"]=='X' and b6["text"]!='O':
                d="6"
            elif b4["text"]=='X' and b7["text"]=='X' and b1["text"]!='O':
                d="1"
            elif b5["text"]=='X' and b8["text"]=='X' and b2["text"]!='O':
                d="2"
            elif b6["text"]=='X' and b9["text"]=='X' and b3["text"]!='O':
                d="3"
            elif b1["text"]=='X' and b5["text"]=='X' and b9["text"]!='O':
                d="9"
            elif b3["text"]=='X' and b5["text"]=='X' and b7["text"]!='O':
                d="7"
            elif b1["text"]=='X' and b9["text"]=='X' and b5["text"]!='O':
                d="5"
            elif b3["text"]=='X' and b7["text"]=='X' and b5["text"]!='O':
                d="5"
            elif b5["text"]=='X' and b9["text"]=='X' and b1["text"]!='O':
                d="n"
            elif b5["text"]=='X' and b7["text"]=='X' and b3["text"]!='O':
                d="3"

            # placing to win
            #other then center 
            elif b5["text"]=='X' and b1["text"]!='O' and b1["text"]!='X':
                d="1" 
            elif b5["text"]=='X' and b3["text"]!='O' and b3["text"]!='X':
                d="3" 
            elif b5["text"]=='X' and b7["text"]!='O' and b7["text"]!='X':
                d="7" 
            elif b5["text"]=='X' and b9["text"]!='O' and b9["text"]!='X':
                d="9" 
            # center control
            elif b1["text"]=='X' and b5["text"]!='O' and b5["text"]!='X':
                d="5" 
            elif b2["text"]=='X' and b5["text"]!='O' and b5["text"]!='X':
                d="5" 
            elif b3["text"]=='X' and b5["text"]!='O' and b5["text"]!='X':
                d="5" 
            elif b4["text"]=='X' and b5["text"]!='O' and b5["text"]!='X':
                d="5" 
            elif b6["text"]=='X' and b5["text"]!='O' and b5["text"]!='X':
                d="5" 
            elif b7["text"]=='X' and b5["text"]!='O' and b5["text"]!='X':
                d="5" 
            elif b8["text"]=='X' and b5["text"]!='O' and b5["text"]!='X':
                d="5" 
            elif b9["text"]=='X' and b5["text"]!='O' and b5["text"]!='X':
                d="5"

            if d=="n" and b1["text"]==" ":
             b1["text"]='O'
             tur=1
             break
            elif d=="2" and b2["text"]==" ":
             b2["text"]='O'
             tur=1
             break
            elif d=="3" and b3["text"]==" ":
             b3["text"]='O'
             tur=1
             break
            elif d=="4" and b4["text"]==" ":
             b4["text"]='O'
             tur=1
             break
            elif d=="5" and b5["text"]==" ":
             b5["text"]='O'
             tur=1
             break
            elif d=="6" and b6["text"]==" ":
             b6["text"]='O'
             tur=1
             break
            elif d=="7" and b7["text"]==" ":
             b7["text"]='O'
             tur=1
             break
            elif d=="8" and b8["text"]==" ":
             b8["text"]='O'
             tur=1
             break
            elif d=="9" and b9["text"]==" ":
             b9["text"]='O'
             tur=1
             break
            elif b1["text"]>='O' and b2["text"]>='O' and b3["text"]>='O' and b4["text"]>='O' and b5["text"]>='O' and b6["text"]>='O' and b7["text"]>='O' and b8["text"]>='O' and b9["text"]>='O':
              b4["text"]=""
              b5["text"]=""
              b6["text"]=""
              b1["text"]=""
              b2["text"]=""
              b3["text"]=""
              b7["text"]=""
              b8["text"]=""
              b9["text"]=""
              i=t.Label(root,text="No won",font=("",20))
              i.pack() 
              break
    if b1["text"]=='X' and b2["text"]=='X' and b3["text"]=='X':
          b4["text"]=""
          b5["text"]=""
          b6["text"]=""
          b7["text"]=""
          b8["text"]=""
          b9["text"]=""
          i=t.Label(root,text="X won",font=("",20))
          i.pack()
    elif b4["text"]=='X' and b5["text"]=='X' and b6["text"]=='X':
          b1["text"]=""
          b2["text"]=""
          b3["text"]=""
          b7["text"]=""
          b8["text"]=""
          b9["text"]=""
          i=t.Label(root,text="X won",font=("",20))
          i.pack()  
    elif b7["text"]=='X' and b8["text"]=='X' and b9["text"]=='X':
          b4["text"]=""
          b5["text"]=""
          b6["text"]=""
          b1["text"]=""
          b2["text"]=""
          b3["text"]=""
          i=t.Label(root,text="X won",font=("",20))
          i.pack()
    elif b1["text"]=='X' and b4["text"]=='X' and b7["text"]=='X':
          b8["text"]=""
          b5["text"]=""
          b6["text"]=""
          b9["text"]=""
          b2["text"]=""
          b3["text"]=""
          i=t.Label(root,text="X won",font=("",20))
          i.pack()
    elif b2["text"]=='X' and b5["text"]=='X' and b8["text"]=='X':
          b4["text"]=""
          b9["text"]=""
          b6["text"]=""
          b1["text"]=""
          b7["text"]=""
          b3["text"]=""
          i=t.Label(root,text="X won",font=("",20))
          i.pack()
    elif b3["text"]=='X' and b6["text"]=='X' and b9["text"]=='X':
          b4["text"]=""
          b5["text"]=""
          b8["text"]=""
          b1["text"]=""
          b2["text"]=""
          b7["text"]=""
          i=t.Label(root,text="X won",font=("",20))
          i.pack()
    elif b1["text"]=='X' and b5["text"]=='X' and b9["text"]=='X':
          b4["text"]=""
          b8["text"]=""
          b6["text"]=""
          b7["text"]=""
          b2["text"]=""
          b3["text"]=""
          i=t.Label(root,text="X won",font=("",20))
          i.pack()
    elif b3["text"]=='X' and b5["text"]=='X' and b7["text"]=='X':
          b4["text"]=""
          b8["text"]=""
          b6["text"]=""
          b1["text"]=""
          b2["text"]=""
          b9["text"]=""
          i=t.Label(root,text="X won",font=("",20))
          i.pack()    
    elif b1["text"]=='O' and b2["text"]=='O' and b3["text"]=='O':
          b4["text"]=""
          b5["text"]=""
          b6["text"]=""
          b7["text"]=""
          b8["text"]=""
          b9["text"]=""
          i=t.Label(root,text="O won",font=("",20))
          i.pack()
    elif b4["text"]=='O' and b5["text"]=='O' and b6["text"]=='O':
          b1["text"]=""
          b2["text"]=""
          b3["text"]=""
          b7["text"]=""
          b8["text"]=""
          b9["text"]=""
          i=t.Label(root,text="O won",font=("",20))
          i.pack()  
    elif b7["text"]=='O' and b8["text"]=='O' and b9["text"]=='O':
          b4["text"]=""
          b5["text"]=""
          b6["text"]=""
          b1["text"]=""
          b2["text"]=""
          b3["text"]=""
          i=t.Label(root,text="O won",font=("",20))
          i.pack()
    elif b1["text"]=='O' and b4["text"]=='O' and b7["text"]=='O':
          b8["text"]=""
          b5["text"]=""
          b6["text"]=""
          b9["text"]=""
          b2["text"]=""
          b3["text"]=""
          i=t.Label(root,text="O won",font=("",20))
          i.pack()
    elif b2["text"]=='O' and b5["text"]=='O' and b8["text"]=='O':
          b4["text"]=""
          b9["text"]=""
          b6["text"]=""
          b1["text"]=""
          b7["text"]=""
          b3["text"]=""
          i=t.Label(root,text="O won",font=("",20))
          i.pack()
    elif b3["text"]=='O' and b6["text"]=='O' and b9["text"]=='O':
          b4["text"]=""
          b5["text"]=""
          b8["text"]=""
          b1["text"]=""
          b2["text"]=""
          b7["text"]=""
          i=t.Label(root,text="O won",font=("",20))
          i.pack()
    elif b1["text"]=='O' and b5["text"]=='O' and b9["text"]=='O':
          b4["text"]=""
          b8["text"]=""
          b6["text"]=""
          b7["text"]=""
          b2["text"]=""
          b3["text"]=""
          i=t.Label(root,text="O won",font=("",20))
          i.pack()
    elif b3["text"]=='O' and b5["text"]=='O' and b7["text"]=='O':
          b4["text"]=""
          b8["text"]=""
          b6["text"]=""
          b1["text"]=""
          b2["text"]=""
          b9["text"]=""
          i=t.Label(root,text="O won",font=("",20))
          i.pack() 
    elif b1["text"]>='O' and b2["text"]>='O' and b3["text"]>='O' and b4["text"]>='O' and b5["text"]>='O' and b6["text"]>='O' and b7["text"]>='O' and b8["text"]>='O' and b9["text"]>='O':
          b4["text"]=""
          b5["text"]=""
          b6["text"]=""
          b1["text"]=""
          b2["text"]=""
          b3["text"]=""
          b7["text"]=""
          b8["text"]=""
          b9["text"]=""
          i=t.Label(root,text="No won",font=("",20))
          i.pack() 
root.geometry("500x600")
root.title("TIC-TAE-TOE")
c=t.Canvas(width=800,height=700,bg="lightblue")
f=t.Frame(c)
b1=t.Button(f,text=" ",padx=30,pady=30,font=("",30))
b1.grid(row=0,column=0)
b1.bind("<Button-1>",click)
b2=t.Button(f,text=" ",padx=30,pady=30,font=("",30))
b2.grid(row=0,column=1)
b2.bind("<Button-1>",click)
b3=t.Button(f,text=" ",padx=30,pady=30,font=("",30))
b3.grid(row=0,column=2)
b3.bind("<Button-1>",click)
b4=t.Button(f,text=" ",padx=30,pady=30,font=("",30))
b4.grid(row=1,column=0)
b4.bind("<Button-1>",click)
b5=t.Button(f,text=" ",padx=30,pady=30,font=("",30))
b5.grid(row=1,column=1)
b5.bind("<Button-1>",click)
b6=t.Button(f,text=" ",padx=30,pady=30,font=("",30))
b6.grid(row=1,column=2)
b6.bind("<Button-1>",click)
b7=t.Button(f,text=" ",padx=30,pady=30,font=("",30))
b7.grid(row=2,column=0)
b7.bind("<Button-1>",click)
b8=t.Button(f,text=" ",padx=30,pady=30,font=("",30))
b8.grid(row=2,column=1)
b8.bind("<Button-1>",click)
b9=t.Button(f,text=" ",padx=30,pady=30,font=("",30))
b9.grid(row=2,column=2)
b9.bind("<Button-1>",click)
f.pack()
c.pack()

root.mainloop()
