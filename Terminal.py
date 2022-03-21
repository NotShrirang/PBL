#Office Catalogue

from tkinter import *
import os
from datetime import datetime

root = Tk()
root.title("Office Catalogue")

def ClickDone():
    inp=e_name.get()
    datetime_object= datetime.today()
    current_time= datetime.strftime(datetime_object, '%H:%M%p')
    time1 = 34200
    time2=str(datetime.strftime(datetime_object, '%H:%M'))
    # print(time2)
    (h,m)=time2.split(":")
    time3=int(h)*3600+int(m)*60
    diff=time3-time1
    # print(diff)
    File_Late=open("Names_of_Latecomers.txt", "a")
    f=open("Names.txt", "a")
    Label_Disp["text"]="Hello, "+e_name.get()+" !"
    f.write("\n")
    if inp in open("Names.txt").read():
        Label_Disp["text"]="Already in Office!"
        e_name.delete(0, END)
    else:
        f.write(inp+" - "+current_time)
        f.close()
        if diff>0:
            print(time1)
            Label_Disp["text"]="Ohh I see! You're Late! Let's not repeat this!"
            e_name.delete(0, END)
            File_Late=open("Names_of_Latecomers.txt", "a")
            File_Late.write("\n"+inp+" - "+current_time+" - Late")
            File_Late.close()
        else:
            f=open("Names.txt", "a")
            Label_Disp["text"]="Welcome, "+e_name.get()+" !"
            f.write("\n")
            e_name.delete(0, END)
def ClickList():
    f=open("Names.txt", "r")
    Label_Disp["text"]="Present:\n"+str(f.read())
def DispLL():
    File_Late=open("Names_of_Latecomers.txt", "r")
    Label_Disp["text"]="Latecomer today:\n"+str(File_Late.read())
def ClickClr():
    os.remove("Names.txt")
    e_name.delete(0, END)
    Label_Disp["text"]=""
def ClickDelLate():
    os.remove("Names_of_Latecomers.txt")
    e_name.delete(0, END)
    Label_Disp["text"]=""

Label_1 =  Label(root, text = "Welcome!")
Label_1.grid(row=0, column=0, columnspan=2, ipady=0)

Label_Name =  Label(root, text = "Name : ")
Label_Name.grid(row=2, column=0, ipadx=10, ipady=10)

e_name=Entry(root, width=50)
e_name.grid(row=2, column=1, padx=10, pady=10)
e_name.insert(0, "")

Button_Done=Button(root, text="Done!", command=ClickDone, width=50)
Button_Done.grid(row=3, column=0, columnspan=2, pady=10)

Label_Disp =  Label(root, text = "", height=10, )
Label_Disp.grid(row=4, column=0, columnspan=2, ipady=0)

Button_List=Button(root, text="Display Present Persons", command=ClickList, width=40)
Button_List.grid(row=5, column=0, pady=10)

Button_LL=Button(root, text="Display Latecomers' List", command=DispLL, width=40)
Button_LL.grid(row=5, column=1, pady=10)

Button_Clr=Button(root, text="Delete Daily File", command=ClickClr, width=40)
Button_Clr.grid(row=6, column=0)

Button_Del=Button(root, text="Delete Latecomers' File", command=ClickDelLate, width=40)
Button_Del.grid(row=6, column=1)

root.mainloop()

