from dictionary import dictionary
from tkinter import*
import random
import time
import copy

from tkinter import *  
from PIL import ImageTk,Image  

from tkinter import messagebox


root = Tk()
root.geometry("1500x650+0+0")
root.configure(background='black')
root.title("Order What You Want")

top = Canvas(root,width = 1600,height=30,bg="black",relief=SUNKEN)
top.grid(row=0, column=0)

f1 = Canvas(root,width = 800,height=600,bg='black',relief=SUNKEN)
image= Image.open("menu.jpg")
image=image.resize((800,550),Image.ANTIALIAS)
img = ImageTk.PhotoImage(image)  
f1.create_image(20, 20, anchor=NW, image=img) 
f1.grid(row=1, column=2)

f2 = Canvas(root ,width = 400,height=700,bg='black',relief=SUNKEN)
f2.grid(row=1,column=0)

label = Label(top, font=( 'aria' ,30, 'bold' ),text="Order What You Want",anchor='n',fg="steel blue",bg='black')
label.grid(row=1,column=0)

label = Label(top, font=( 'aria' ,20, ),text="Eat What You Love",fg="steel blue",anchor='n',bg='black')
label.grid(row=2,column=0)

result = []

def returnEntry(arg=None):
    total = 0
    no_found = []
    items=[]
    count = 0
    result.append(entry.get())
    for i in range(len(result)):
    	for key,value in dictionary.items():
         	items.append(key)

    for i in range(len(result)):
        for key,value in dictionary.items():
            if result[i] == key and result[i] in items:

                label = Label(f2, font=('aria', 15, 'bold'), text=key, fg="steel blue",bg='black', bd=5)
                label.grid(row=6+i, columnspan=3)

                label = Label(f2, font=('aria', 15, 'bold'), text="$ "+str(value), fg="steel blue",bg='black', bd=5)
                label.grid(row=6+i, column=2)

                entry.delete(0,END)

                total += value
            elif result[i] not in items:
            	no_found = []
            	count += 1
            	print("add",no_found)
            	print("count",count)
            	if count == 17:
            		print("result",result)
            		no_found.append(result[i])
            		result.remove(result[i])
            		count = 0
            		print("after",no_found)
            		print("no_found",no_found)
    if len(no_found)> 0:
	    for i in no_found:
	    	if i not in items:
	    		print("i",i)
	    		messagebox.showinfo("Error", "Sorry. We don't have that item. Choose another item.")
	    		entry.delete(0,END)
	    		no_found.pop(0)
	    		if len(result) != 0:
	    			result.remove(i)
	    		print("pop",no_found)
	    
    label = Label(f2, font=( 'aria' ,30, 'bold' ),text="Total: $"+str(total),fg="steel blue",bd=10,bg='black',anchor='w')
    label.grid(row=30,columnspan=3)                

label = Label(f2, font=( 'aria' ,30, 'bold' ),text="Place Your Order",fg="steel blue",bg='black',bd=10,anchor='nw')
label.grid(row=0,columnspan=3)

label = Label(top, font=( 'aria' ,30, 'bold' ),text="Order What You Want",fg="steel blue",bg='black',bd=10,anchor='ne')
label.grid(row=1,column=0)

entry = Entry(f2,font=('ariel' ,20,'bold'), bd=5 ,insertwidth=7 ,bg="white",justify='right')
entry.focus()
entry.bind("<Return>",returnEntry)
entry.grid(columnspan=4) 

root.mainloop()

