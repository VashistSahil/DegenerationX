from tkinter import *
from tkinter import messagebox
import timeit
import time
import mysql.connector
from datetime import date
import random

home= Tk()

width = home.winfo_screenwidth()
height = home.winfo_screenheight()

home.geometry('%dx%d+0+0' % (width,height))
home.title('DX')
home.iconbitmap('dx3.ico')
home.overrideredirect(True)


#Defining functions

def close_enter(event):
    close["bg"]="red3"
def close_leave(event):
    close["bg"]="red"

def contact_enter(event):
    contact["bg"]="grey95"
def contact_leave(event):
    contact["bg"]="white"

def about_enter(event):
    about["bg"]="grey95"
def about_leave(event):
    about["bg"]="white"

def signup1_enter(event):
    signup1["bg"]="blue4"
def signup1_leave(event):
    signup1["bg"]="blue"

def signin_enter(event):
    signin["bg"]="green"
def signin_leave(event):
    signin["bg"]="green3"

def click_contact():
    window3= Tk()
    window3.geometry("1920x1080")

    aaal13= Label(window3, text="Contact us" , font=("Times New Roman",38))
    aaal13.pack()
    
    aaal33= Label(window3, text="(Creator- Sahil Vashist) " , font=("Times New Roman",28))
    aaal33.pack()

    aaal23= Label(window3, text="email: sahil.vashist@outlook.com " , font=("Times New Roman",16))
    aaal23.pack()
    
    aaal43= Label(window3, text="I am always happy to be contacted! " , font=("Times New Roman",16))
    aaal43.pack()

    aaal53= Label(window3, text="  Hope you like my PROJECT :) " , font=("Times New Roman",20))
    aaal53.pack()

    window3.mainloop()

def click_about():
    window= Tk()
    window.geometry("1920x1080")

    aaal1= Label(window, text="About us" , font=("Times New Roman",38))
    aaal1.pack()
    
    aaal3= Label(window, text="(Actually their is only one person running this project!) " , font=("Times New Roman",28))
    aaal3.pack()

    aaal2= Label(window, text="Hello!, My name is Sahil Vashist. If you are reading this, " , font=("Times New Roman",16))
    aaal2.pack()
    
    aaal4= Label(window, text="you must be one of my friends or my Computer Science practical's external checker. " , font=("Times New Roman",16))
    aaal4.pack()

    aaal5= Label(window, text="  Hope you like my PROJECT :) " , font=("Times New Roman",20))
    aaal5.pack()

    window.mainloop()




def click_signup():
    def click_submit_signup():


        flag=0
        mydb = mysql.connector.connect(
              host="localhost",
              user="root",
              passwd="darkbull"
            )
        mycur=mydb.cursor()
        
        try:
            mycur.execute("create database project")
        except:
            print("datbase found")


        try:
            mycur.execute("use project")
        except:
            print("data base not found")

        try:
            mycur.execute(" create table accounts(email_id char(30), username char(20) primary key, password char(30), date_of_joining date)")
        except:
            print("table found")

        
        a= email_enter.get() #email
        b= username_enter.get() #username
        c= password_enter.get() #password
        d= password_re_enter.get() #re password
        #e= tick1.get()

        print("a=",a,"b=",b,"c=",c,"d=",d)


        
        mycur.execute("select email_id from accounts")
        list_of_registered_emails=mycur.fetchall()
        print(list_of_registered_emails)
            
        
        mycur.execute("select username from accounts")
        list_of_registered_usernames=mycur.fetchall()
        print(list_of_registered_usernames)

        lp1=[a]
        lp2=[b]
        f1= tuple(lp1)
        f2= tuple(lp2)

        #print("e=",e)


        #min length yet to do
        if a=="" or b=="" or c=="" or d=="" :
            messagebox.showinfo("Information Not Complete", "Please fill all the details and tick the Terms and Conditions box")
            flag=1

        
        elif f1 in list_of_registered_emails:
            messagebox.showinfo("Email already registered!", "An account from this email already exists. Please try a different Email Id or try Loging In!")
            flag=1

        
        elif f2 in list_of_registered_usernames:
            messagebox.showinfo("Username already registered!", "An account from this Username already exists. Please try a different Username!")
            flag=1
        
        elif c!=d:
            messagebox.showinfo("Passwords do not match!!!", "Passwords do not match! Please Try Again!")
            flag=1


        elif len(b)>20:
            messagebox.showinfo("ERROR","username should not be greater than 20 letters/number/symbols")
            flag=1

        elif len(c)>30:
            messagebox.showinfo("ERROR","password should not be greater than 20 letters/number/symbols")
            flag=1

        elif "@" not in a or "." not in a or " " in a:
            messagebox.showinfo("ERROR", "Enter a valid Email Id")
            flag=1

        if flag==0:
            z=date.today()
            mycur=mydb.cursor()
            data1= "insert into accounts(email_id,username,password,date_of_joining)values(%s,%s,%s,%s)"
            mycur.execute(data1,(a,b,c,z))
            mydb.commit()
            print("success")
            sign_up.destroy()
            

    sign_up= Tk()
    sign_up.geometry("410x410")
    sign_up.configure(background="white")
    sign_up.title('DX')
    sign_up.iconbitmap('dx3.ico')


    titlebar_signup= Frame(sign_up, bg= "green4")

    l1= Label(titlebar_signup, text= "D-Generation X", font=("Times New Roman", 15), fg="white", bg="green4")
    l1.pack()

    abovebody= Frame(sign_up,bg="white")


    l3= Label(abovebody, text=" ",font=("Times New Roman", 10),bg="white")
    l3.pack()

    l2= Label(abovebody, text="Create an Account",font=("Times New Roman", 25),bg="white")
    l2.pack()

    l3= Label(abovebody, text=" ",font=("Times New Roman", 15),bg="white")
    l3.pack()

    body= Frame(sign_up)

    #def TaC1(event):
       # bB1["bg"]="green"
    #def TaC2(event):
        #bB1["bg"]="default"



    username_label= Label(body, text = ("UserName") , font=("Times New Roman",15))
    #username_conditions= Label(body, text = ("min length=4, max length=20") , font=("Times New Roman",5))
    password_label= Label(body, text = ("Password") , font=("Times New Roman",15))
    #password_conditions= Label(body, text = ("min length=4, max length=20") , font=("Times New Roman",5))
    re_password_label= Label(body, text = ("Re-enter Password") , font=("Times New Roman",10))
    email_label= Label(body, text = ("Email-id") , font=("Times New Roman",15))

    username_enter= Entry(body,font=("Times New Roman",15)) #username
    password_enter= Entry(body,font=("Times New Roman",15),show="*") #password
    password_re_enter= Entry(body,font=("Times New Roman",15),show="*") #re check password
    email_enter= Entry(body,font=("Times New Roman",15)) #emailid

    
    aC2= Label(body, text="By signing up I to agree all terms and conditions", fg ="grey31", font=("Times New Roman",8))
    #tick1= IntVar()
    #aC1= Checkbutton(body, text= "I accept all Terms and Conditions", variable= tick1)
    aB1= Button(body, text="SUBMIT", fg ="green",command= click_submit_signup)


    bB1= Label(body, text="I agree that I am not a ROBOT!", fg ="grey31", font=("Courier New",8),bd=0,pady=10)

    email_label.grid(row=0,column=0, sticky=E)
    email_enter.grid(row=0,column=1)
    username_label.grid(row=2,column=0, sticky=E)
    password_label.grid(row=3,column=0, sticky=E)
    re_password_label.grid(row=4,column=0, sticky=E)
    username_enter.grid(row=2,column=1)
    password_enter.grid(row=3,column=1)
    password_re_enter.grid(row=4,column=1)

    #username_conditions.grid(row=5,column=0)
    #password_conditions.grid(row=5,column=1)

    aC2.grid(row=6,columnspan=3)
    #aC1.grid(row=6,columnspan=3)
    bB1.grid(row=7,columnspan=3)
    aB1.grid(row=8,columnspan=3)

    #bB1.bind("<Enter>",TaC1)
    #bB1.bind("<Leave>",TaC2)



    titlebar_signup.pack(side=TOP, fill=X)
    abovebody.pack()
    body.pack()
    sign_up.mainloop()

counter_42=0
flag22=0
n=0
start="X"
def click_signin():
    
    global start
    global n
    global flag22
    global counter_42
    a=username_enter_2.get()
    b=password_enter_2.get()

    username21 = a

    if a=="" or b=="":
        messagebox.showinfo("Incomplete information","Please enter username and password")

    else:
   
        try:
            mydb= mysql.connector.connect(host="localhost", user="root",passwd="darkbull",database="project")
        except:
            messagebox.showinfo("ID not registered", "Please Sign up ")
            
        mycur= mydb.cursor()
        mycur.execute("select username from accounts")
        username_data= mycur.fetchall()
        print(username_data)

        la1=[a]
        ta1=tuple(la1)
        if ta1 in username_data:
            mycur.execute("select password from accounts where username = '{}'".format(a))
            print("username accepted")
            data_password=mycur.fetchall()

            lb1=[b]
            tb1=tuple(lb1)
            if tb1 in data_password:
                ######################
                messagebox.showinfo("logged in","YOU ARE ALL SET TO PLAY!!!!")
                
                

                game_home= Tk()
                
                
                width = game_home.winfo_screenwidth()
                height = game_home.winfo_screenheight()
                
                game_home.geometry('%dx%d+0+0' % (width,height))
                game_home.title('DX')
                game_home.iconbitmap('dx3.ico')
                game_home.overrideredirect(True)


                               
                def close_enter(event):
                    close["bg"]="red3"
                def close_leave(event):
                    close["bg"]="red"
                
                maintitlebar= Frame(game_home,bg="grey11")
                close= Button(maintitlebar, text="CLOSE", bg="red", fg="white",font=("Arial",10), padx=15,pady=0, command= game_home.destroy)
                close.pack(side=RIGHT)
                close.bind("<Enter>",close_enter)
                close.bind("<Leave>",close_leave)
                
                titlebartext= Label(maintitlebar, text= "D-Generation X: World's Best Gaming Platform",bg="grey11",fg="white",padx=6)
                titlebartext.pack(side=LEFT)
                
                def contact_enter(event):
                    contact["bg"]="grey95"
                def contact_leave(event):
                    contact["bg"]="white"
                
                def about_enter(event):
                    about["bg"]="grey95"
                def about_leave(event):
                    about["bg"]="white"
                
                def login1_enter(event):
                    login1["bg"]="blue4"
                def login1_leave(event):
                    login1["bg"]="blue"
                    
                def click_contact():
                    window3b= Tk()
                    window3b.geometry("1920x1080")
                
                    aal13= Label(window3b, text="Contact us" , font=("Times New Roman",38))
                    aal13.pack()
                    
                    aal33= Label(window3b, text="(Creator- Sahil Vashist) " , font=("Times New Roman",28))
                    aal33.pack()
                
                    aal23= Label(window3b, text="email: sahil.vashist@outlook.com " , font=("Times New Roman",16))
                    aal23.pack()
                    
                    aal43= Label(window3b, text="I am always happy to be contacted! " , font=("Times New Roman",16))
                    aal43.pack()
                
                    aal53= Label(window3b, text="  Hope you like my PROJECT :) " , font=("Times New Roman",20))
                    aal53.pack()
                
                    window3b.mainloop()
                
                
                def click_about():
                    window= Tk()
                    window.geometry("1920x1080")#("960x220")
                
                    aal1= Label(window, text="About us" , font=("Times New Roman",38))
                    aal1.pack()
                    
                    aal3= Label(window, text="(Actually their is only one person running this project!) " , font=("Times New Roman",28))
                    aal3.pack()
                
                    aal2= Label(window, text="Hello!, My name is Sahil Vashist. If you are reading this, " , font=("Times New Roman",16))
                    aal2.pack()
                    
                    aal4= Label(window, text="you must be one of my friends or my Computer Science practical's external checker. " , font=("Times New Roman",16))
                    aal4.pack()
                
                    aal5= Label(window, text="  Hope you like my PROJECT :) " , font=("Times New Roman",20))
                    aal5.pack()
                
                    window.mainloop()
                
                
                def b1_enter(event):
                    B1["bg"]="green"
                def b1_leave(event):
                    B1["bg"]="green3"
                
                def b2_enter(event):
                    B2["bg"]="green"
                def b2_leave(event):
                    B2["bg"]="green3"
                
                def b3_enter(event):
                    B3["bg"]="green"
                def b3_leave(event):
                    B3["bg"]="green3"
                    
                def click_logout():
                    game_home.destroy()
                ###################################
                
                def tic_launch():
                    global start
                    global n
                    global flag22
                    root= Tk()

                    
                    width = root.winfo_screenwidth()
                    height = game_home.winfo_screenheight()
                    
                    root.geometry('%dx%d+0+0' % (width,height))
                    root.title('DX')
                    root.iconbitmap('dx3.ico')
                    root.overrideredirect(True)
                    
                    
                    
                    
                    
                    def close_enter(event):
                        close["bg"]="red3"
                    def close_leave(event):
                        close["bg"]="red"
                    
                    def close_is_tictac():
                        root.destroy()
                    
                    

                        
                        
                        
                        
                    maintitlebar= Frame(root,bg="grey11")
                    close= Button(maintitlebar, text="CLOSE", bg="red", fg="white",font=("Arial",10), padx=15,pady=0, command= root.destroy)
                    close.pack(side=RIGHT)
                    close.bind("<Enter>",close_enter)
                    close.bind("<Leave>",close_leave)
                    
                    titlebartext= Label(maintitlebar, text= "D-Generation X: World's Best Gaming Platform",bg="grey11",fg="white",padx=6)
                    titlebartext.pack(side=LEFT)
                    
                        
                    
                    titlebar= Frame(root, bg="white" ,bd=5)
                    
                    name= Label(titlebar, text="D-Generation X", bg="white", font=("Times New Roman",35), fg= "green3")
                    name.pack(side=LEFT)
                    
                    
                    maintitlebar.pack(fill=X)
                    titlebar.pack(fill=X)
                    
                    start="X"
                    
                    n=0
                    
                    
                    flag22=0

                    
                    def restart_tictac():
                        global flag22
                        global n
                        
                        n=0
                        flag22=0
                        b1["text"]=""
                        b2["text"]=""
                        b3["text"]=""
                        b4["text"]=""
                        b5["text"]=""
                        b6["text"]=""
                        b7["text"]=""
                        b8["text"]=""
                        b9["text"]=""
                        
                        print("i am jericho")
                        
                    
                    
                    
                    
                    def win_x():
                        tkbox= Tk()

                        tkbox.geometry('500x540+250+100')
                        #tkbox.overrideredirect(True)
                        tkbox.iconbitmap('dx3.ico')
                        tkbox.title("DX")
                        
                        frame_box_1= Frame(tkbox,bg="black")
                        titlebartext= Label(frame_box_1, text= "D-Generation X: The Worlds best Gaming platform",bg="grey11",fg="white",padx=6)
                        titlebartext.pack(side=LEFT)
                        frame_box_1.pack(fill=X)
                        
                        frame_box_2= Frame(tkbox)
                        spacex2= Label(frame_box_2, text =" ", font=("arial",20))
                        spacex2.pack()
                        messagebox_label= Label(frame_box_2, text= "GAME OVER!",font=("Times New Roman",55),fg="green3")
                        messagebox2_label= Label(frame_box_2, text= "X wins !!!",font=("arial",45),fg="green3")
                        messagebox_label.pack()
                        spacex3= Label(frame_box_2, text =" ", font=("arial",30))
                        spacex3.pack()
                        messagebox2_label.pack()
                        frame_box_2.pack()
                        
                        
                        frame_box_4= Frame(tkbox)
                        spacex4= Label(frame_box_4, text =" ", font=("arial",40))
                        spacex4.pack()
                        restart_tictac2= Button(frame_box_4, text="BACK",font=("Arial",25), bd=5, bg="green3", fg= "white", padx=30, pady=5, height = 1, width = 8, command = tkbox.destroy)
                        restart_tictac2.pack()
                        spacex5= Label(frame_box_4, text =" ", font=("arial",20))
                        spacex5.pack()
                        
                        frame_box_4.pack()
                        tkbox.mainloop()
                    
                    
                    
                    def win_o():
                        tkbox= Tk()

                        tkbox.geometry('500x540+250+100')
                        #tkbox.overrideredirect(True)
                        tkbox.iconbitmap('dx3.ico')
                        tkbox.title("DX")
                        
                        frame_box_1= Frame(tkbox,bg="black")
                        titlebartext= Label(frame_box_1, text= "D-Generation X: The Worlds best Gaming platform",bg="grey11",fg="white",padx=6)
                        titlebartext.pack(side=LEFT)
                        frame_box_1.pack(fill=X)
                        
                        frame_box_2= Frame(tkbox)
                        spacex2= Label(frame_box_2, text =" ", font=("arial",20))
                        spacex2.pack()
                        messagebox_label= Label(frame_box_2, text= "GAME OVER!",font=("Times New Roman",55),fg="green3")
                        messagebox2_label= Label(frame_box_2, text= "O wins !!!",font=("arial",45),fg="green3")
                        messagebox_label.pack()
                        spacex3= Label(frame_box_2, text =" ", font=("arial",30))
                        spacex3.pack()
                        messagebox2_label.pack()
                        frame_box_2.pack()
                        
                        
                        frame_box_4= Frame(tkbox)
                        spacex4= Label(frame_box_4, text =" ", font=("arial",40))
                        spacex4.pack()
                        restart_tictac2= Button(frame_box_4, text="BACK",font=("Arial",25), bd=5, bg="green3", fg= "white", padx=30, pady=5, height = 1, width = 8, command = tkbox.destroy)
                        restart_tictac2.pack()
                        spacex5= Label(frame_box_4, text =" ", font=("arial",20))
                        spacex5.pack()
                        
                        frame_box_4.pack()
                        tkbox.mainloop()
                        
                        
                    def win_draw():
                        tkbox= Tk()

                        tkbox.geometry('500x540+250+100')
                        #tkbox.overrideredirect(True)
                        tkbox.iconbitmap('dx3.ico')
                        tkbox.title("DX")
                        
                        frame_box_1= Frame(tkbox,bg="black")
                        titlebartext= Label(frame_box_1, text= "D-Generation X: The Worlds best Gaming platform",bg="grey11",fg="white",padx=6)
                        titlebartext.pack(side=LEFT)
                        frame_box_1.pack(fill=X)
                        
                        frame_box_2= Frame(tkbox)
                        spacex2= Label(frame_box_2, text =" ", font=("arial",20))
                        spacex2.pack()
                        messagebox_label= Label(frame_box_2, text= "GAME OVER!",font=("Times New Roman",55),fg="green3")
                        messagebox2_label= Label(frame_box_2, text= "It is a draw !!!",font=("arial",45),fg="green3")
                        messagebox_label.pack()
                        spacex3= Label(frame_box_2, text =" ", font=("arial",30))
                        spacex3.pack()
                        messagebox2_label.pack()
                        frame_box_2.pack()
                        
                        
                        frame_box_4= Frame(tkbox)
                        spacex4= Label(frame_box_4, text =" ", font=("arial",40))
                        spacex4.pack()
                        restart_tictac2= Button(frame_box_4, text="BACK",font=("Arial",25), bd=5, bg="green3", fg= "white", padx=30, pady=5, height = 1, width = 8,command = tkbox.destroy)
                        restart_tictac2.pack()
                        spacex5= Label(frame_box_4, text =" ", font=("arial",20))
                        spacex5.pack()

                        
                        frame_box_4.pack()
                        tkbox.mainloop()
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    def click1():
                        global n
                        global flag22
                        if flag22==0:
                            global start
                            if b1["text"]!="X" and b1["text"]!="O":
                                n+=1
                                if start=="X":
                                    b1["text"]="O"
                                    start="O"
                                else:
                                    b1["text"]="X"
                                    start="X"
                            if (b1["text"]=="X" and b2["text"]=="X" and b3["text"]=="X") or (b4["text"]=="X" and b5["text"]=="X" and b6["text"]=="X") or (b7["text"]=="X" and b8["text"]=="X" and b9["text"]=="X") or (b1["text"]=="X" and b5["text"]=="X" and b9["text"]=="X") or (b3["text"]=="X" and b5["text"]=="X" and b7["text"]=="X") or (b1["text"]=="X" and b4["text"]=="X" and b7["text"]=="X") or (b2["text"]=="X" and b5["text"]=="X" and b8["text"]=="X") or (b3["text"]=="X" and b6["text"]=="X" and b9["text"]=="X"):
                                print ("X wins")
                                win_x()
                                flag22=1
                            if (b1["text"]=="O" and b2["text"]=="O" and b3["text"]=="O") or (b4["text"]=="O" and b5["text"]=="O" and b6["text"]=="O") or (b7["text"]=="O" and b8["text"]=="O" and b9["text"]=="O") or (b1["text"]=="O" and b5["text"]=="O" and b9["text"]=="O") or (b3["text"]=="O" and b5["text"]=="O" and b7["text"]=="O") or (b1["text"]=="O" and b4["text"]=="O" and b7["text"]=="O") or (b2["text"]=="O" and b5["text"]=="O" and b8["text"]=="O") or (b3["text"]=="O" and b6["text"]=="O" and b9["text"]=="O"):
                                print ("O wins")
                                win_o()
                                flag22=1
                            if n==9 and flag22==0:
                                print("draw")
                                win_draw()
                    
                                
                    def click2():
                        global n
                        global flag22
                        if flag22==0:
                            global start
                            if b2["text"]!="X" and b2["text"]!="O":
                                n+=1
                                if start=="X":
                                    b2["text"]="O"
                                    start="O"
                                else:
                                    b2["text"]="X"
                                    start="X"
                            if (b1["text"]=="X" and b2["text"]=="X" and b3["text"]=="X") or (b4["text"]=="X" and b5["text"]=="X" and b6["text"]=="X") or (b7["text"]=="X" and b8["text"]=="X" and b9["text"]=="X") or (b1["text"]=="X" and b5["text"]=="X" and b9["text"]=="X") or (b3["text"]=="X" and b5["text"]=="X" and b7["text"]=="X") or (b1["text"]=="X" and b4["text"]=="X" and b7["text"]=="X") or (b2["text"]=="X" and b5["text"]=="X" and b8["text"]=="X") or (b3["text"]=="X" and b6["text"]=="X" and b9["text"]=="X"):
                                print ("X wins")
                                win_x()
                                flag22=1
                            if (b1["text"]=="O" and b2["text"]=="O" and b3["text"]=="O") or (b4["text"]=="O" and b5["text"]=="O" and b6["text"]=="O") or (b7["text"]=="O" and b8["text"]=="O" and b9["text"]=="O") or (b1["text"]=="O" and b5["text"]=="O" and b9["text"]=="O") or (b3["text"]=="O" and b5["text"]=="O" and b7["text"]=="O") or (b1["text"]=="O" and b4["text"]=="O" and b7["text"]=="O") or (b2["text"]=="O" and b5["text"]=="O" and b8["text"]=="O") or (b3["text"]=="O" and b6["text"]=="O" and b9["text"]=="O"):
                                print ("O wins")
                                win_o()
                                flag22=1
                            if n==9 and flag22==0:
                                print("draw")
                                win_draw()
                            
                                
                    def click3():
                        global n
                        global flag22
                        if flag22==0:
                            global start
                            if b3["text"]!="X" and b3["text"]!="O":
                                n+=1
                                if start=="X":
                                    b3["text"]="O"
                                    start="O"
                                else:
                                    b3["text"]="X"
                                    start="X"
                            if (b1["text"]=="X" and b2["text"]=="X" and b3["text"]=="X") or (b4["text"]=="X" and b5["text"]=="X" and b6["text"]=="X") or (b7["text"]=="X" and b8["text"]=="X" and b9["text"]=="X") or (b1["text"]=="X" and b5["text"]=="X" and b9["text"]=="X") or (b3["text"]=="X" and b5["text"]=="X" and b7["text"]=="X") or (b1["text"]=="X" and b4["text"]=="X" and b7["text"]=="X") or (b2["text"]=="X" and b5["text"]=="X" and b8["text"]=="X") or (b3["text"]=="X" and b6["text"]=="X" and b9["text"]=="X"):
                                print ("X wins")
                                win_x()
                                flag22=1
                            if (b1["text"]=="O" and b2["text"]=="O" and b3["text"]=="O") or (b4["text"]=="O" and b5["text"]=="O" and b6["text"]=="O") or (b7["text"]=="O" and b8["text"]=="O" and b9["text"]=="O") or (b1["text"]=="O" and b5["text"]=="O" and b9["text"]=="O") or (b3["text"]=="O" and b5["text"]=="O" and b7["text"]=="O") or (b1["text"]=="O" and b4["text"]=="O" and b7["text"]=="O") or (b2["text"]=="O" and b5["text"]=="O" and b8["text"]=="O") or (b3["text"]=="O" and b6["text"]=="O" and b9["text"]=="O"):
                                print ("O wins")
                                win_o()
                                flag22=1
                            if n==9 and flag22==0:
                                print("draw")
                                win_draw()
                                
                    def click4():
                        global n
                        global flag22
                        if flag22==0:
                            global start
                            if b4["text"]!="X" and b4["text"]!="O":
                                n+=1
                                if start=="X":
                                    b4["text"]="O"
                                    start="O"
                                else:
                                    b4["text"]="X"
                                    start="X"
                            if (b1["text"]=="X" and b2["text"]=="X" and b3["text"]=="X") or (b4["text"]=="X" and b5["text"]=="X" and b6["text"]=="X") or (b7["text"]=="X" and b8["text"]=="X" and b9["text"]=="X") or (b1["text"]=="X" and b5["text"]=="X" and b9["text"]=="X") or (b3["text"]=="X" and b5["text"]=="X" and b7["text"]=="X") or (b1["text"]=="X" and b4["text"]=="X" and b7["text"]=="X") or (b2["text"]=="X" and b5["text"]=="X" and b8["text"]=="X") or (b3["text"]=="X" and b6["text"]=="X" and b9["text"]=="X"):
                                print ("X wins")
                                win_x()
                                flag22=1
                            if (b1["text"]=="O" and b2["text"]=="O" and b3["text"]=="O") or (b4["text"]=="O" and b5["text"]=="O" and b6["text"]=="O") or (b7["text"]=="O" and b8["text"]=="O" and b9["text"]=="O") or (b1["text"]=="O" and b5["text"]=="O" and b9["text"]=="O") or (b3["text"]=="O" and b5["text"]=="O" and b7["text"]=="O") or (b1["text"]=="O" and b4["text"]=="O" and b7["text"]=="O") or (b2["text"]=="O" and b5["text"]=="O" and b8["text"]=="O") or (b3["text"]=="O" and b6["text"]=="O" and b9["text"]=="O"):
                                print ("O wins")
                                win_o()
                                flag22=1
                            if n==9 and flag22==0:
                                print("draw")
                                win_draw()
                            
                    def click5():
                        global n
                        global flag22
                        if flag22==0:
                            global start
                            if b5["text"]!="X" and b5["text"]!="O":
                                n+=1
                                if start=="X":
                                    b5["text"]="O"
                                    start="O"
                                else:
                                    b5["text"]="X"
                                    start="X"
                            if (b1["text"]=="X" and b2["text"]=="X" and b3["text"]=="X") or (b4["text"]=="X" and b5["text"]=="X" and b6["text"]=="X") or (b7["text"]=="X" and b8["text"]=="X" and b9["text"]=="X") or (b1["text"]=="X" and b5["text"]=="X" and b9["text"]=="X") or (b3["text"]=="X" and b5["text"]=="X" and b7["text"]=="X") or (b1["text"]=="X" and b4["text"]=="X" and b7["text"]=="X") or (b2["text"]=="X" and b5["text"]=="X" and b8["text"]=="X") or (b3["text"]=="X" and b6["text"]=="X" and b9["text"]=="X"):
                                print ("X wins")
                                win_x()
                                flag22=1
                            if (b1["text"]=="O" and b2["text"]=="O" and b3["text"]=="O") or (b4["text"]=="O" and b5["text"]=="O" and b6["text"]=="O") or (b7["text"]=="O" and b8["text"]=="O" and b9["text"]=="O") or (b1["text"]=="O" and b5["text"]=="O" and b9["text"]=="O") or (b3["text"]=="O" and b5["text"]=="O" and b7["text"]=="O") or (b1["text"]=="O" and b4["text"]=="O" and b7["text"]=="O") or (b2["text"]=="O" and b5["text"]=="O" and b8["text"]=="O") or (b3["text"]=="O" and b6["text"]=="O" and b9["text"]=="O"):
                                print ("O wins")
                                win_o()
                                flag22=1
                            if n==9 and flag22==0:
                                print("draw")
                                win_draw()
                    
                    def click6():
                        global n
                        global flag22
                        if flag22==0:
                            global start
                            if b6["text"]!="X" and b6["text"]!="O":
                                n+=1
                                if start=="X":
                                    b6["text"]="O"
                                    start="O"
                                else:
                                    b6["text"]="X"
                                    start="X"
                            if (b1["text"]=="X" and b2["text"]=="X" and b3["text"]=="X") or (b4["text"]=="X" and b5["text"]=="X" and b6["text"]=="X") or (b7["text"]=="X" and b8["text"]=="X" and b9["text"]=="X") or (b1["text"]=="X" and b5["text"]=="X" and b9["text"]=="X") or (b3["text"]=="X" and b5["text"]=="X" and b7["text"]=="X") or (b1["text"]=="X" and b4["text"]=="X" and b7["text"]=="X") or (b2["text"]=="X" and b5["text"]=="X" and b8["text"]=="X") or (b3["text"]=="X" and b6["text"]=="X" and b9["text"]=="X"):
                                print ("X wins")
                                win_x()
                                flag22=1
                            if (b1["text"]=="O" and b2["text"]=="O" and b3["text"]=="O") or (b4["text"]=="O" and b5["text"]=="O" and b6["text"]=="O") or (b7["text"]=="O" and b8["text"]=="O" and b9["text"]=="O") or (b1["text"]=="O" and b5["text"]=="O" and b9["text"]=="O") or (b3["text"]=="O" and b5["text"]=="O" and b7["text"]=="O") or (b1["text"]=="O" and b4["text"]=="O" and b7["text"]=="O") or (b2["text"]=="O" and b5["text"]=="O" and b8["text"]=="O") or (b3["text"]=="O" and b6["text"]=="O" and b9["text"]=="O"):
                                print ("O wins")
                                win_o()
                                flag22=1
                            if n==9 and flag22==0:
                                print("draw")
                                win_draw()
                        
                    def click7():
                        global n
                        global flag22
                        if flag22==0:
                            global start
                            if b7["text"]!="X" and b7["text"]!="O":
                                n+=1
                                if start=="X":
                                    b7["text"]="O"
                                    start="O"
                                else:
                                    b7["text"]="X"
                                    start="X"
                            if (b1["text"]=="X" and b2["text"]=="X" and b3["text"]=="X") or (b4["text"]=="X" and b5["text"]=="X" and b6["text"]=="X") or (b7["text"]=="X" and b8["text"]=="X" and b9["text"]=="X") or (b1["text"]=="X" and b5["text"]=="X" and b9["text"]=="X") or (b3["text"]=="X" and b5["text"]=="X" and b7["text"]=="X") or (b1["text"]=="X" and b4["text"]=="X" and b7["text"]=="X") or (b2["text"]=="X" and b5["text"]=="X" and b8["text"]=="X") or (b3["text"]=="X" and b6["text"]=="X" and b9["text"]=="X"):
                                print ("X wins")
                                win_x()
                                flag22=1
                            if (b1["text"]=="O" and b2["text"]=="O" and b3["text"]=="O") or (b4["text"]=="O" and b5["text"]=="O" and b6["text"]=="O") or (b7["text"]=="O" and b8["text"]=="O" and b9["text"]=="O") or (b1["text"]=="O" and b5["text"]=="O" and b9["text"]=="O") or (b3["text"]=="O" and b5["text"]=="O" and b7["text"]=="O") or (b1["text"]=="O" and b4["text"]=="O" and b7["text"]=="O") or (b2["text"]=="O" and b5["text"]=="O" and b8["text"]=="O") or (b3["text"]=="O" and b6["text"]=="O" and b9["text"]=="O"):
                                print ("O wins")
                                win_o()
                                flag22=1
                            if n==9 and flag22==0:
                                print("draw")
                                win_draw()
                                
                    def click8():
                        global n
                        global flag22
                        if flag22==0:
                            global start
                            if b8["text"]!="X" and b8["text"]!="O":
                                n+=1
                                if start=="X":
                                    b8["text"]="O"
                                    start="O"
                                else:
                                    b8["text"]="X"
                                    start="X"
                            if (b1["text"]=="X" and b2["text"]=="X" and b3["text"]=="X") or (b4["text"]=="X" and b5["text"]=="X" and b6["text"]=="X") or (b7["text"]=="X" and b8["text"]=="X" and b9["text"]=="X") or (b1["text"]=="X" and b5["text"]=="X" and b9["text"]=="X") or (b3["text"]=="X" and b5["text"]=="X" and b7["text"]=="X") or (b1["text"]=="X" and b4["text"]=="X" and b7["text"]=="X") or (b2["text"]=="X" and b5["text"]=="X" and b8["text"]=="X") or (b3["text"]=="X" and b6["text"]=="X" and b9["text"]=="X"):
                                print ("X wins")
                                win_x()
                                flag22=1
                            if (b1["text"]=="O" and b2["text"]=="O" and b3["text"]=="O") or (b4["text"]=="O" and b5["text"]=="O" and b6["text"]=="O") or (b7["text"]=="O" and b8["text"]=="O" and b9["text"]=="O") or (b1["text"]=="O" and b5["text"]=="O" and b9["text"]=="O") or (b3["text"]=="O" and b5["text"]=="O" and b7["text"]=="O") or (b1["text"]=="O" and b4["text"]=="O" and b7["text"]=="O") or (b2["text"]=="O" and b5["text"]=="O" and b8["text"]=="O") or (b3["text"]=="O" and b6["text"]=="O" and b9["text"]=="O"):
                                print ("O wins")
                                win_o()
                                flag22=1
                            if n==9 and flag22==0:
                                print("draw")
                                win_draw()
                            
                                
                    def click9():
                        global n
                        global flag22
                        if flag22==0:
                            global start
                            if b9["text"]!="X" and b9["text"]!="O":
                                n+=1
                                if start=="X":
                                    b9["text"]="O"
                                    start="O"
                                else:
                                    b9["text"]="X"
                                    start="X"
                            if (b1["text"]=="X" and b2["text"]=="X" and b3["text"]=="X") or (b4["text"]=="X" and b5["text"]=="X" and b6["text"]=="X") or (b7["text"]=="X" and b8["text"]=="X" and b9["text"]=="X") or (b1["text"]=="X" and b5["text"]=="X" and b9["text"]=="X") or (b3["text"]=="X" and b5["text"]=="X" and b7["text"]=="X") or (b1["text"]=="X" and b4["text"]=="X" and b7["text"]=="X") or (b2["text"]=="X" and b5["text"]=="X" and b8["text"]=="X") or (b3["text"]=="X" and b6["text"]=="X" and b9["text"]=="X"):
                                print ("X wins")
                                win_x()
                                flag22=1
                            if (b1["text"]=="O" and b2["text"]=="O" and b3["text"]=="O") or (b4["text"]=="O" and b5["text"]=="O" and b6["text"]=="O") or (b7["text"]=="O" and b8["text"]=="O" and b9["text"]=="O") or (b1["text"]=="O" and b5["text"]=="O" and b9["text"]=="O") or (b3["text"]=="O" and b5["text"]=="O" and b7["text"]=="O") or (b1["text"]=="O" and b4["text"]=="O" and b7["text"]=="O") or (b2["text"]=="O" and b5["text"]=="O" and b8["text"]=="O") or (b3["text"]=="O" and b6["text"]=="O" and b9["text"]=="O"):
                                print ("O wins")
                                win_o()
                                flag22=1
                            if n==9 and flag22==0:
                                print("draw")
                                win_draw()
                    
                    
                    root2=Frame(root)
                    title22= Label(root2,text=" TIC TAC TOE ",font=("Courier New",48))
                    title22.pack()
                    root2.pack()
                            
                    root3= Frame(root)
                    b1= Button(root3, text="   ", font=("Arial",25), bd=5, bg="orange", fg= "white", padx=30, pady=20, height = 1, width = 2, command= click1)
                    b2= Button(root3, text="   ", font=("Arial",25), bd=5, bg="orange", fg= "white", padx=30, pady=20, height = 1, width = 2, command= click2)
                    b3= Button(root3, text="   ", font=("Arial",25), bd=5, bg="orange", fg= "white", padx=30, pady=20, height = 1, width = 2, command= click3)
                    b4= Button(root3, text="   ", font=("Arial",25), bd=5, bg="orange", fg= "white", padx=30, pady=20, height = 1, width = 2, command= click4)
                    b5= Button(root3, text="   ", font=("Arial",25), bd=5, bg="orange", fg= "white", padx=30, pady=20, height = 1, width = 2, command= click5)
                    b6= Button(root3, text="   ", font=("Arial",25), bd=5, bg="orange", fg= "white", padx=30, pady=20, height = 1, width = 2, command= click6)
                    b7= Button(root3, text="   ", font=("Arial",25), bd=5, bg="orange", fg= "white", padx=30, pady=20, height = 1, width = 2, command= click7)
                    b8= Button(root3, text="   ", font=("Arial",25), bd=5, bg="orange", fg= "white", padx=30, pady=20, height = 1, width = 2, command= click8)
                    b9= Button(root3, text="   ", font=("Arial",25), bd=5, bg="orange", fg= "white", padx=30, pady=20, height = 1, width = 2, command= click9)
                    space1111= Label(root3,text=" ",font=("Arial",25))
                    space1112= Label(root3,text=" ",font=("Arial",25))
                    
                    restart_tictac_33= Button(root3, text= "RESTART", font=("Courier",15), bd=5, bg="green3", fg= "white", padx=30, pady=10, height = 1, width = 2, command= restart_tictac)
                    
                    space1111.grid(row=0)
                    b1.grid(row=2,column=0)
                    b2.grid(row=2,column=1)
                    b3.grid(row=2,column=2)
                    b4.grid(row=3,column=0)
                    b5.grid(row=3,column=1)
                    b6.grid(row=3,column=2)
                    b7.grid(row=4,column=0)
                    b8.grid(row=4,column=1)
                    b9.grid(row=4,column=2)
                    space1112.grid(row=5)
                    restart_tictac_33.grid(row= 6, column = 1)
                    
                    
                    
                    root3.pack()
                    root.mainloop()
                                        
                ####################################   
                
                
                def memory_launch():
                    global counter_42
                    window42= Tk()
                    window42.geometry("1920x1080")
                    
                    
                    width = window42.winfo_screenwidth()
                    height = window42.winfo_screenheight()
                    
                    window42.geometry('%dx%d+0+0' % (width,height))
                    window42.overrideredirect(True)
                    
                    
                    #Defining functions
                    
                    def close_enter(event):
                        close["bg"]="red3"
                    def close_leave(event):
                        close["bg"]="red"
                    
                    
                    
                    #titlebar
                    maintitlebar= Frame(window42,bg="grey11")
                    close= Button(maintitlebar, text="CLOSE", bg="red", fg="white",font=("Arial",10), padx=15,pady=0, command= window42.destroy)
                    close.pack(side=RIGHT)
                    close.bind("<Enter>",close_enter)
                    close.bind("<Leave>",close_leave)
                    
                    titlebartext= Label(maintitlebar, text= "D-Generation X: World's Best Gaming Platform",bg="grey11",fg="white",padx=6)
                    titlebartext.pack(side=LEFT)
                    
                    
                    titlebar= Frame(window42, bg="white" ,bd=5)
                    
                    name= Label(titlebar, text="D-Generation X", bg="white", font=("Times New Roman",35), fg= "green3")
                    name.pack(side=LEFT)
                    
                    
                    
                    colours=["blue","blue","orange","orange","pink","pink","yellow","yellow"]
                    
                    a1=random.choice(colours)
                    colours.remove(a1)
                    a2=random.choice(colours)
                    colours.remove(a2)
                    a3=random.choice(colours)
                    colours.remove(a3)
                    a4=random.choice(colours)
                    colours.remove(a4)
                    a5=random.choice(colours)
                    colours.remove(a5)
                    a6=random.choice(colours)
                    colours.remove(a6)
                    a7=random.choice(colours)
                    colours.remove(a7)
                    a8=random.choice(colours)
                    colours.remove(a8)
                    
                    
                    counter_42=0
                    colour=""
                    block=""
                    
                    def close_is_mem():
                        window42.destroy()
                    
                    def win_mem():
                        tkbox_2= Tk()

                        tkbox_2.geometry('500x540+250+100')
                        #tkbox.overrideredirect(True)
                        tkbox_2.iconbitmap('dx3.ico')
                        tkbox_2.title("DX")
                        
                        frame_box_1_2= Frame(tkbox_2,bg="black")
                        titlebartext_2= Label(frame_box_1_2, text= "D-Generation X: The Worlds best Gaming platform",bg="grey11",fg="white",padx=6)
                        titlebartext_2.pack(side=LEFT)
                        frame_box_1_2.pack(fill=X)
                        
                        frame_box_2_2= Frame(tkbox_2)
                        spacex22= Label(frame_box_2_2, text =" ", font=("arial",20))
                        spacex22.pack()
                        messagebox_label= Label(frame_box_2_2, text= "GAME OVER!",font=("Times New Roman",55),fg="green3")
                        messagebox2_label= Label(frame_box_2_2, text= "YOU WIN !!!",font=("arial",45),fg="green3")
                        messagebox_label.pack()
                        spacex32= Label(frame_box_2_2, text =" ", font=("arial",30))
                        spacex32.pack()
                        messagebox2_label.pack()
                        frame_box_2_2.pack()
                        
                        
                        frame_box_4_2= Frame(tkbox_2)
                        spacex4= Label(frame_box_4_2, text =" ", font=("arial",40))
                        spacex4.pack()
                        restart_tictac2= Button(frame_box_4_2, text="BACK",font=("Arial",25), bd=5, bg="green3", fg= "white", padx=30, pady=5, height = 1, width = 8,command = tkbox_2.destroy)
                        restart_tictac2.pack()
                        spacex5= Label(frame_box_4_2, text =" ", font=("arial",20))
                        spacex5.pack()
                        
                        
                        frame_box_4_2.pack()
                        tkbox_2.mainloop()
                        
                        
                    def restart_mem_game():
                        global colours
                        global counter_42
                        global colour
                        global block
                        global a1
                        global a2
                        global a3
                        global a4
                        global a5
                        global a6
                        global a7
                        global a8
                        
                        counter_42=0
                        colour=""
                        block=""
                        
                        colours=["blue","blue","orange","orange","pink","pink","yellow","yellow"]
                        
                        a1=random.choice(colours)
                        colours.remove(a1)
                        a2=random.choice(colours)
                        colours.remove(a2)
                        a3=random.choice(colours)
                        colours.remove(a3)
                        a4=random.choice(colours)
                        colours.remove(a4)
                        a5=random.choice(colours)
                        colours.remove(a5)
                        a6=random.choice(colours)
                        colours.remove(a6)
                        a7=random.choice(colours)
                        colours.remove(a7)
                        a8=random.choice(colours)
                        colours.remove(a8)
                        
                        
                        
                        
                        b_42_1["bg"]="red"
                        b_42_2["bg"]="red"
                        b_42_3["bg"]="red"
                        b_42_4["bg"]="red"
                        b_42_5["bg"]="red"
                        b_42_6["bg"]="red"
                        b_42_7["bg"]="red"
                        b_42_8["bg"]="red"
                        
                        print("i am jericho")
                        
                    
                    
                    def click_42_1():
                        global counter_42
                        global colour
                        global block
                        global a1
                        if b_42_1["bg"]=="red":
                            b_42_1["bg"]=a1
                            counter_42+=1
                            
                            if counter_42%2!=0:
                                colour=a1
                                block=b_42_1
                    
                            elif a1==colour:
                                b_42_1["bg"]="lawn green"
                                block["bg"]="lawn green"
                            else:            
                                b_42_1["bg"]="red"
                                block["bg"]="red"
                                
                            if b_42_1["bg"]=="lawn green" and b_42_2["bg"]=="lawn green" and b_42_3["bg"]=="lawn green" and b_42_4["bg"]=="lawn green" and b_42_5["bg"]=="lawn green" and b_42_6["bg"]=="lawn green" and b_42_7["bg"]=="lawn green" and b_42_8["bg"]=="lawn green":
                                win_mem()
                    
                    
                    def click_42_2():
                        global counter_42
                        global colour
                        global block
                        global a2
                        if b_42_2["bg"]=="red":
                            b_42_2["bg"]=a2
                            counter_42+=1
                    
                            if counter_42%2!=0:
                                colour=a2
                                block=b_42_2
                            elif a2==colour:
                                b_42_2["bg"]="lawn green"
                                block["bg"]="lawn green"
                            else:
                                b_42_2["bg"]="red"
                                block["bg"]="red"
                            if b_42_1["bg"]=="lawn green" and b_42_2["bg"]=="lawn green" and b_42_3["bg"]=="lawn green" and b_42_4["bg"]=="lawn green" and b_42_5["bg"]=="lawn green" and b_42_6["bg"]=="lawn green" and b_42_7["bg"]=="lawn green" and b_42_8["bg"]=="lawn green":
                                win_mem()
                                
                    
                    
                    def click_42_3():
                        global counter_42
                        global colour
                        global block
                        global a3
                        if b_42_3["bg"]=="red":
                            b_42_3["bg"]=a3
                            counter_42+=1
                    
                            if counter_42%2!=0:
                                colour=a3
                                block=b_42_3
                    
                            elif a3==colour:
                                b_42_3["bg"]="lawn green"
                                block["bg"]="lawn green"
                            else:
                                b_42_3["bg"]="red"
                                block["bg"]="red"
                            if b_42_1["bg"]=="lawn green" and b_42_2["bg"]=="lawn green" and b_42_3["bg"]=="lawn green" and b_42_4["bg"]=="lawn green" and b_42_5["bg"]=="lawn green" and b_42_6["bg"]=="lawn green" and b_42_7["bg"]=="lawn green" and b_42_8["bg"]=="lawn green":
                                win_mem()
                    
                    def click_42_4():
                        global counter_42
                        global colour
                        global block
                        global a4
                        if b_42_4["bg"]=="red":
                            b_42_4["bg"]=a4
                            counter_42+=1
                    
                            if counter_42%2!=0:
                                colour=a4
                                block=b_42_4
                    
                            elif a4==colour:            
                                b_42_4["bg"]="lawn green"
                                block["bg"]="lawn green"
                            else:
                                b_42_4["bg"]="red"
                                block["bg"]="red"
                            if b_42_1["bg"]=="lawn green" and b_42_2["bg"]=="lawn green" and b_42_3["bg"]=="lawn green" and b_42_4["bg"]=="lawn green" and b_42_5["bg"]=="lawn green" and b_42_6["bg"]=="lawn green" and b_42_7["bg"]=="lawn green" and b_42_8["bg"]=="lawn green":
                                win_mem()
                    
                    def click_42_5():
                        global counter_42
                        global colour
                        global block
                        global a5
                        if b_42_5["bg"]=="red":
                            b_42_5["bg"]=a5
                            counter_42+=1
                    
                            if counter_42%2!=0:
                                colour=a5
                                block=b_42_5
                    
                            elif a5==colour:
                                b_42_5["bg"]="lawn green"
                                block["bg"]="lawn green"
                            else:
                                b_42_5["bg"]="red"
                                block["bg"]="red"
                            if b_42_1["bg"]=="lawn green" and b_42_2["bg"]=="lawn green" and b_42_3["bg"]=="lawn green" and b_42_4["bg"]=="lawn green" and b_42_5["bg"]=="lawn green" and b_42_6["bg"]=="lawn green" and b_42_7["bg"]=="lawn green" and b_42_8["bg"]=="lawn green":
                                win_mem()
                    
                    def click_42_6():
                        global counter_42
                        global colour
                        global block
                        global a6
                        if b_42_6["bg"]=="red":
                            b_42_6["bg"]=a6
                            counter_42+=1
                    
                            if counter_42%2!=0:
                                colour=a6
                                block=b_42_6
                    
                            elif a6==colour:
                                b_42_6["bg"]="lawn green"
                                block["bg"]="lawn green"
                            else:
                                b_42_6["bg"]="red"
                                block["bg"]="red"
                            if b_42_1["bg"]=="lawn green" and b_42_2["bg"]=="lawn green" and b_42_3["bg"]=="lawn green" and b_42_4["bg"]=="lawn green" and b_42_5["bg"]=="lawn green" and b_42_6["bg"]=="lawn green" and b_42_7["bg"]=="lawn green" and b_42_8["bg"]=="lawn green":
                                win_mem()
                    
                    def click_42_7():
                        global counter_42
                        global colour
                        global block
                        global a7
                        if b_42_7["bg"]=="red":
                            b_42_7["bg"]=a7
                            counter_42+=1
                    
                            if counter_42%2!=0:
                                colour=a7
                                block=b_42_7
                    
                            elif a7==colour:
                                b_42_7["bg"]="lawn green"
                                block["bg"]="lawn green"
                            else:
                                b_42_7["bg"]="red"
                                block["bg"]="red"
                            if b_42_1["bg"]=="lawn green" and b_42_2["bg"]=="lawn green" and b_42_3["bg"]=="lawn green" and b_42_4["bg"]=="lawn green" and b_42_5["bg"]=="lawn green" and b_42_6["bg"]=="lawn green" and b_42_7["bg"]=="lawn green" and b_42_8["bg"]=="lawn green":
                                win_mem()
                    
                    def click_42_8():
                        global counter_42
                        global colour
                        global block
                        global a8
                        if b_42_8["bg"]=="red":
                            b_42_8["bg"]=a8
                            counter_42+=1
                    
                            if counter_42%2!=0:
                                colour=a8
                                block=b_42_8
                    
                            elif a8==colour:
                                b_42_8["bg"]="lawn green"
                                block["bg"]="lawn green"
                            else:
                                b_42_8["bg"]="red"
                                block["bg"]="red"
                            if b_42_1["bg"]=="lawn green" and b_42_2["bg"]=="lawn green" and b_42_3["bg"]=="lawn green" and b_42_4["bg"]=="lawn green" and b_42_5["bg"]=="lawn green" and b_42_6["bg"]=="lawn green" and b_42_7["bg"]=="lawn green" and b_42_8["bg"]=="lawn green":
                                win_mem()
                        
                    
                              
                    
                    
                    game=Frame(window42)
                    
                    b_42_1=Button(game, text="    ", font=("ARIAL", 30), padx=100,pady=100,bg="red",command=click_42_1)
                    b_42_2=Button(game, text="    ", font=("ARIAL", 30), padx=100,pady=100,bg="red",command=click_42_2)
                    b_42_3=Button(game, text="    ", font=("ARIAL", 30), padx=100,pady=100,bg="red",command=click_42_3)
                    b_42_4=Button(game, text="    ", font=("ARIAL", 30), padx=100,pady=100,bg="red",command=click_42_4)
                    b_42_5=Button(game, text="    ", font=("ARIAL", 30), padx=100,pady=100,bg="red",command=click_42_5)
                    b_42_6=Button(game, text="    ", font=("ARIAL", 30), padx=100,pady=100,bg="red",command=click_42_6)
                    b_42_7=Button(game, text="    ", font=("ARIAL", 30), padx=100,pady=100,bg="red",command=click_42_7)
                    b_42_8=Button(game, text="    ", font=("ARIAL", 30), padx=100,pady=100,bg="red",command=click_42_8)
                    restart_mem_42= Button(game, text= "START", font=("Courier",15), bd=5, bg="green3", fg= "white", padx=30, pady=10, height = 1, width = 2, command= restart_mem_game)
                    spacex42= Label(game, text= '', font= ("arial",20))
                    
                    b_42_1.grid(row=0,column=0)
                    b_42_2.grid(row=0,column=1)
                    b_42_3.grid(row=0,column=2)
                    b_42_4.grid(row=0,column=3)
                    b_42_5.grid(row=1,column=0)
                    b_42_6.grid(row=1,column=1)
                    b_42_7.grid(row=1,column=2)
                    b_42_8.grid(row=1,column=3)
                    spacex42.grid(row=2)
                    restart_mem_42.grid(row=3,column=1,columnspan=2)
                    
                    
                    
                    
                    
                    
                    
                    maintitlebar.pack( fill=X)
                    titlebar.pack( fill=X)
                    game.pack()
                    window42.mainloop()
                                       

                    
                    
                    
                #################################
                
                def click_it_launch():
                    global username21
                    
                    mydb21= mysql.connector.connect(host="localhost", user="root", passwd="darkbull",database="project")
                    mycur21= mydb21.cursor()
                    try:
                        mycur21.execute("create table history_3(username char(20), score float(50), date_of_score date)")
                        trya="no_user"
                        tryb=9999999999
                        mycur21.execute("insert into history_3 (username,score)values('{}',{})".format(trya,tryb))
                        mydb21.commit()
                    except:
                        print("table found")
                    
                    #try:
                    mycur21.execute("select min(score) from history_3")
                    highscore21=mycur21.fetchone()
                    high_score21=highscore21[0]
                    #except:
                    #    print("problem")
                    print(high_score21)    
                    
                    
                    
                    window21= Tk()
                   
                    width = window21.winfo_screenwidth()
                    height = window21.winfo_screenheight()
                    
                    window21.geometry('%dx%d+0+0' % (width,height))
                    window21.overrideredirect(True)


                    window21.iconbitmap('dx3.ico')
                    window21.title("DX")
                    
                    
                    time_print=0
                    flag21=0
                    boom21=0
                    timer=0
                    list21=[]
                    
                    def close_enter(event):
                        close["bg"]="red3"
                    def close_leave(event):
                        close["bg"]="red"
                    
                    def start():
                        global username21
                        global timer
                        global count
                        global flag21
                        global list21
                        global high_score21
                        timer=0
                        score["text"]=0
                        flag21=1
                        time.sleep(1)    
                        bbL1["text"]= "Begin"
                        count=0
                        list21=[]
                        
                    
                    def click():
                        global timer
                        global flag21
                        global count
                        global boom21
                        global high_score21
                        if flag21==1:
                            count+=1
                            score["text"]=count
                            if count==10:
                                boom21=1
                                flag21=0
                            
                            
                    def timerstart():
                        #global username21
                        username21="previous user"
                        global time_print
                        global high_score21
                        global list21
                        global timer
                        global flag21
                        global boom21
                        #print(username21)
                        #global 
                        boom21=0
                        timer=0
                        time=0
                        if flag21==1 and boom21==0 :
                            timer = timeit.default_timer()
                            click()
                            timer += timeit.default_timer()
                            #print(timer)
                            list21.append(timer)
                            
                        
                    
                        if boom21==1:
                            
                            global high_score21
                            time=list21[9]-list21[0]
                            time_print = time
                            bbL6["text"]= time_print
                            #print('Time: ', time)
                            mycur21.execute("select min(score) from history_3")
                            highscore21=mycur21.fetchone()
                            high_score21=highscore21[0]
                            if time<high_score21:
                                high_score21=time
                                bbL4["text"]=high_score21
                            tz= date.today()
                            mycur21.execute("insert into history_3 (username , score, date_of_score)values('{}',{},'{}')".format(username21,time,tz))
                            mydb21.commit()
                            timer=0
                            
                        
                        
                        
                            
                        
                    
                    maintitlebar= Frame(window21,bg="grey11")
                    close= Button(maintitlebar, text="CLOSE", bg="red", fg="white",font=("Arial",10), padx=15,pady=0, command= window21.destroy)
                    close.pack(side=RIGHT)
                    close.bind("<Enter>",close_enter)
                    close.bind("<Leave>",close_leave)
                    
                    titlebartext= Label(maintitlebar, text= "D-Generation X: World's Best Gaming Platform",bg="grey11",fg="white",padx=6)
                    titlebartext.pack(side=LEFT)
                    
                    body21= Frame(window21)
                    
                    main_button= Button(body21, text="CLICK ME !!!", font=("Courier New", 48), padx=30, pady=30, bd=5 , fg="white", bg="green2",command=timerstart)
                    main_button.pack()
                    
                    counter= Label(body21, text= "Clicks", font=("Georgia",28))
                    counter.pack()
                    
                    score= Label(body21, text= "0", font=("Courier New",28))
                    score.pack()
                    
                    start= Button(body21, text="start",font=("Courier",20),padx=5,pady=5,bg="green",fg="snow",command=start)
                    start.pack()
                    
                    bbL1=Label(body21, text= "", font=("Georgia",28))
                    bbL1.pack()
                    
                    bbL2= Label(body21, text= "How much time do you take for 10 CLICKS?", font=("Helvetica",28))
                    bbL2.pack()
                    
                    bbL3= Label(body21, text= "High score", font=("Helvetica",28),fg="green3")
                    bbL3.pack()
                    
                    bbL4= Label(body21, text= high_score21, font=("Helvetica",28),fg="green")
                    bbL4.pack()
                    
                    bbL5= Label(body21, text= "Your Score", font=("Helvetica",28),fg="green3")
                    bbL5.pack()
                    
                    bbL6= Label(body21, text= time_print, font=("Helvetica",28),fg="green")
                    bbL6.pack()
                    
                    
                    maintitlebar.pack(side=TOP, fill=X)
                    
                    
                    
                    body21.pack()
                    window21.mainloop()

                
                
                
                
                
                
                
                ##################################
                
                
                titlebar= Frame(game_home, bg="white" ,bd=5)
                
                name= Label(titlebar, text="D-Generation X", bg="white", font=("Times New Roman",35), fg= "green3")
                name.pack(side=LEFT)
                
                login1= Button(titlebar, text="LOG OUT", font=("Times New Roman",16), bg="blue", fg="white",bd=0, padx=10,command=click_logout)
                login1.pack(side=RIGHT)
                login1.bind("<Enter>",login1_enter)
                login1.bind("<Leave>",login1_leave)
                
                
                contact= Button(titlebar, text="Contact Us", font=("Times New Roman",15), bg="white", fg="grey",bd=0, padx=10, command= click_contact)
                contact.pack(side=RIGHT)
                contact.bind("<Enter>",contact_enter)
                contact.bind("<Leave>",contact_leave)
                
                about= Button(titlebar, text="About us", font=("Times New Roman",15), bg="white", fg="grey",bd=0, padx=10,command=click_about)
                about.pack(side=RIGHT)
                about.bind("<Enter>",about_enter)
                about.bind("<Leave>",about_leave)
                
                
                
                
                
                body=Frame(game_home)
                L01= Label(body, text=" ",font=("Courier New",35))
                L11= Label(body, text="SELECT THE GAME YOU WANT TO PLAY!",font=("Courier New",35),fg="green3")
                L21= Label(body, text=" ",font=("Courier New",35))
                
                B1= Button(body, text="Tic Tac Toe",bg="green3",fg="white",padx=5,pady=5,font=("Times New Roman",35),command=tic_launch)
                B1.bind("<Enter>",b1_enter)
                B1.bind("<Leave>",b1_leave)
                
                
                B2= Button(body, text="Memory",bg="green3",fg="white",padx=5,pady=5,font=("Times New Roman",35), command= memory_launch)
                B2.bind("<Enter>",b2_enter)
                B2.bind("<Leave>",b2_leave)
                
                
                B3= Button(body, text="Click It",bg="green3",fg="white",padx=5,pady=5,font=("Times New Roman",35),command=click_it_launch)
                B3.bind("<Enter>",b3_enter)
                B3.bind("<Leave>",b3_leave)
                
                
                    
                
                L01.grid(row=0,columnspan=6)
                L11.grid(row=1,columnspan=6)
                L21.grid(row=2,columnspan=6)
                B1.grid(row=3,column=1)
                B2.grid(row=3,column=2)
                B3.grid(row=3,column=3)

                
                
                
                
                
                
                
                
                maintitlebar.pack(side=TOP, fill=X)
                titlebar.pack(side=TOP, fill=X)
                body.pack()
                game_home.mainloop()
            



                
            else:
                messagebox.showinfo("error","Username and Password do not match")
        else:
            messagebox.showinfo("error","account not registered, please SIGN UP")
            
            
        

    






#titlebar
maintitlebar= Frame(home,bg="grey11")
close= Button(maintitlebar, text="CLOSE", bg="red", fg="white",font=("Arial",10), padx=15,pady=0, command= home.destroy)
close.pack(side=RIGHT)
close.bind("<Enter>",close_enter)
close.bind("<Leave>",close_leave)

titlebartext= Label(maintitlebar, text= "D-Generation X: World's Best Gaming Platform",bg="grey11",fg="white",padx=6)
titlebartext.pack(side=LEFT)


titlebar= Frame(home, bg="white" ,bd=5)

name= Label(titlebar, text="D-Generation X", bg="white", font=("Times New Roman",35), fg= "green3")
name.pack(side=LEFT)

signup1= Button(titlebar, text="SIGN UP", font=("Bookman Old Style",20), bg="blue", fg="white",bd=0, padx=5, command= click_signup)
signup1.pack(side=RIGHT)
signup1.bind("<Enter>",signup1_enter)
signup1.bind("<Leave>",signup1_leave)


contact= Button(titlebar, text="Contact Us", font=("Times New Roman",15), bg="white", fg="grey",bd=0, padx=10, command= click_contact)
contact.pack(side=RIGHT)
contact.bind("<Enter>",contact_enter)
contact.bind("<Leave>",contact_leave)

about= Button(titlebar, text="About us", font=("Times New Roman",15), bg="white", fg="grey",bd=0, padx=10,command=click_about)
about.pack(side=RIGHT)
about.bind("<Enter>",about_enter)
about.bind("<Leave>",about_leave)



mainbody=Frame(home)
space= Label(mainbody, text="      ", font=("Arial",30))
space2= Label(mainbody, text="     ",font=("Arial",30))

mainbody1= Frame(mainbody)
space11= Label(mainbody1, text= "", font=("Times New Roman",70))

body1= Frame(mainbody1)
L1= Label(body1, text= "SIGN IN", font=("Georgia",48),fg="green3")
L2= Label(body1, text= "TO PLAY" , font=("Georgia",48),fg="green3")
L3= Label(body1, text= " Play.Sleep.Repeat ", font=("Courier New",28),fg="black",pady=30)
L1.pack()
L2.pack()
L3.pack()

body2= Frame(mainbody1)
username_label_2= Label(body2, text = ("UserName") , font=("Times New Roman",25),fg="green")
password_label_2= Label(body2, text = ("Password") , font=("Times New Roman",25),fg="green")
username_enter_2= Entry(body2,font=("Times New Roman",25)) 
password_enter_2= Entry(body2,font=("Times New Roman",25), show="*")
signin= Button(body2,text= "SIGN IN" ,font=("Verdana",20),fg="white",bg="green3",bd=0,command=click_signin)
signin.bind("<Enter>",signin_enter)
signin.bind("<Leave>",signin_leave)
space114= Label(body2, text= "      ", font=("Courier New",8),fg="black")
username_label_2.grid(row=0,column=0, sticky=E)
password_label_2.grid(row=1,column=0, sticky=E)
username_enter_2.grid(row=0,column=1)
password_enter_2.grid(row=1,column=1)
space114.grid(row=2,columnspan=2)
signin.grid(row=3,columnspan=2)


body1.pack()
body2.pack()
space11.pack()



mainbody2= Frame(mainbody)
I= PhotoImage(file="dx3.png")
L1= Label(mainbody2,image=I)

L1.pack()



mainbody1.grid(row=0,column=1)
space.grid(row=0,column=2)
space2.grid(row=0,column=0)
mainbody2.grid(row=0,column=3)










#Main Packing()
maintitlebar.pack( fill=X)
titlebar.pack( fill=X)
mainbody.pack()
home.mainloop()

