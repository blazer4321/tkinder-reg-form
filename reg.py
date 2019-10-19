from tkinter import*
import pymysql
top=Tk()
top.geometry("1200x1200")
top.title("registration form")
db=pymysql.connect('localhost','root','','ab')
cursor=db.cursor()
NAME= StringVar()
PLACE= StringVar()
AGE= IntVar()
EMAIL= StringVar()
PASSWORD= StringVar()
quali= StringVar()
quali=" "
def database() :
    db=pymysql.connect('localhost','root','','ab')
    cursor=db.cursor()
  
    name=NAME.get()
    place=PLACE.get()
    age=AGE.get()
    email=EMAIL.get()
    password=PASSWORD.get()
    gender=v.get()
    a=var1.get()
    b=var2.get()
    c=var3.get()
    d=var4.get()
    e=var5.get()
    print(name)
    print(place)
    print(age)
    print(email)
    print(password)
    gen=""
    if(gender==1):
     gen="male"
    else:
     gen="female"
    if(a==1):
        quali="10th"
    if(b==1):
        quali+="sslc" if quali==" " else ",sslc"
    if(c==1):
        quali+="diploma" if quali==" " else ",diploma"
    if(d==1):
        quali+="ug" if quali==" " else ",ug"
    if(e==1):
        quali+="pg" if quali==" " else ",pg"
    print(quali)
    sql="insert into `reg`(`name`,`place`,`age`,`email`,`password`,`gender`,`qualification`)values('%s','%s','%d','%s','%s','%s','%s')"%(name,place,age,email,password,gen,quali)
    try:
        cursor.execute(sql)
        db.commit()
        our="values are inserted successfully"
        message=Message(top,text=our,bg='white',width=50,font=("bold",22))
        message.place(x=850,y=620)
    except Exception as a:
        print(a)
        print("error: values are not inserted")
        db.rollback()          
label=Label(top,text="REGISTRATION FORM",width=20,font=("bold",20),bg='red')
label.place(x=450,y=50)
label=Label(top,text="NAME :",width=20,font=("italic",20))
label.place(x=300,y=120)
label=Label(top,text="PLACE :",width=20,font=("italic",20))
label.place(x=300,y=170)
label=Label(top,text="AGE :",width=20,font=("italic",20))
label.place(x=300,y=220)
label=Label(top,text="E-MAIL :",width=20,font=("italic",20))
label.place(x=300,y=270)
label=Label(top,text="PASSWORD:",width=20,font=("italic",20))
label.place(x=300,y=320)
e1=Entry(top,textvar=NAME)
e2=Entry(top,textvar=PLACE)
e3=Entry(top,textvar=AGE)
e4=Entry(top,textvar=EMAIL)
e5=Entry(top,show='*',textvar=PASSWORD)
e1.place(x=540,y=120)
e2.place(x=540,y=170)
e3.place(x=540,y=220)
e4.place(x=540,y=270)
e5.place(x=560,y=320)
v=IntVar()
Radiobutton(top,text='M',variable=v,value=1,font=("bold",20)).place(x=600,y=410)
Radiobutton(top,text='F',variable=v,value=2,font=("bold",20)).place(x=540,y=410)
w=Label(top,text="GENDER :",font=("bold",20)).place(x=400,y=410)
x=Label(top,text="QUALIFICATION :",font=("italic",20)).place(x=410,y=500)
var1=IntVar()
Checkbutton(top,text="10th",variable=var1).place(x=650,y=500)
var2=IntVar()
Checkbutton(top,text="SSLC",variable=var2).place(x=750,y=500)
var3=IntVar()
Checkbutton(top,text="diploma",variable=var3).place(x=850,y=500)
var4=IntVar()
Checkbutton(top,text="ug",variable=var4).place(x=950,y=500)
var5=IntVar()
Checkbutton(top,text="pg",variable=var5).place(x=1050,y=500)
Button=Button(top,text="SUBMIT",width=30,bg='blue',command=database)
Button.place(x=550,y=630)
our="MESSAGE"
message=Message(top,text=our,bg='white',width=50,font=("bold",22))
message.place(x=850,y=620)
top.mainloop()

