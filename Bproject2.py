from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import sqlite3,tkinter.colorchooser
from tkinter.font import * 
import math
################################
tk=Tk()
tk.title("หน้าตาGUI")
t=ttk.Notebook(tk)
gui=Frame(t)
python=Frame(t)
t.add(gui,text="GUI")
t.add(python,text="Python")
t.pack(fill=BOTH,expand=1)

try:
    photo2 = PhotoImage(file="D:\project\พื้นหลัง.png")
    Label(gui,image=photo2 ).place(x=0,y=0,width=1280,height=650)
    Label(python,image=photo2 ).place(x=0,y=0,width=1280,height=650)
except:
    pass


data=sqlite3.connect("D:\project\project2.db")
# a_  ตัวแปรไว้เก็บค่าที่ สามารถแก้ได้
# a_ _ ตัวแปรที่ใช้เก็บค่าจาก a_
# b_  ตัวแปรไว้เก็บค่า ไม่ สามารถแก้ได้
# c_ ลิด
#################################
#                                 กำหนดขนาด หน้า GUI
##############################################################################################################
#สร้างด้าตาเพื่อเก็บข้อมูลของsaveที่ผู้ใช้สร้าง
def data_bate():
    global lon
    try:
        c=data.cursor()
        c.execute(f"""CREATE TABLE "{name_data_a.get()}" (
        "id"	INTEGER,
        "name"	TEXT NOT NULL,
        "box"	TEXT NOT NULL,
        "tex_t"	TEXT NOT NULL,
        "font"	INTEGER NOT NULL,
        "bg"	TEXT NOT NULL,
        "fg"	TEXT NOT NULL,
        "x"	INTEGER NOT NULL,
        "y"	INTEGER NOT NULL,
        "width"	INTEGER NOT NULL,
        "height"	INTEGER NOT NULL,
        "command"	TEXT NOT NULL,
        PRIMARY KEY("id" AUTOINCREMENT)
    );""")
        data.commit()
        c.close()
        data_bate_1()
    except:
        tkinter.messagebox.showinfo("แจ้งคนใช้โปรแกรงจากเจ้าเล่ห์","มีชื่อนี้แล้วอยู่ในระบบ")
        lon=0
#เอาค่าของid1เข้าไปในด้าตาเพื่อไม่ให้มันเป้นค่าว่าง
def data_bate_1():
    global lon
    c=data.cursor()
    c.execute(f"""
    INSERT INTO {name_data_a.get()} 
    ( id,name,box,tex_t,font,bg,fg,x,y,width,height,command) 
    VALUES 
    (1,"GUI" , "-" , "-" , "-" , "-" , "-" , "-" , "-" , "800" , "600" , "-")
    """)
    data.commit()
    c.close()
    _svae_1.set(name_data_a.get())
    name_data_a.set("")
    lon=0

def def_num(S):
    if S.isdigit():
        return True
    return False
nummu = (tk.register(def_num), '%S')
# ถอดรหัสของตัวชื่อที่ให้เข้ามา
def def_code(v):
    r=int(v[7:10])
    return r
# สร้างsave+แจ้งถ้ายังไม่save+ส่งค่าsaveกับคือ    
svae_12=""
size_1=1.4
def def_svae_1(a=0):
    global svae_12,size_1
    if a==1:
        svae_12=_svae_1.get()
        size_1=float(_svae_2.get())
    if svae_12=="":
        tkinter.messagebox.showinfo("แจ้งคนใช้โปรแกรงจากเจ้าเล่ห์","โปรดสร้างSAVE")
        return svae_12
    elif   svae_12=="New File":
        abc()
    else:
        return svae_12
# เป็นส่วนต่อขยายจากการสร้างsave
name_data_a=StringVar()
def abc():
    global lon
    def abc_1(e):
        if name_data_a.get() !="":
            s_namu.append(name_data_a.get())
            data_bate()
        b_button_svae=OptionMenu(gui,_svae_1,*s_namu)
        b_button_svae.place(x=560,y=20,width=74,height=30)
        name_data.destroy()
    if lon==0:
        name_data = LabelFrame(gui, text="name data",padx=5,pady=5)
        name_data.place(x=560,y=20,width=150,height=50)
        ss=Entry(name_data,textvariable=name_data_a)
        ss.pack()
        ss.bind("<Return>", abc_1 )
        b_button_svae.destroy()
        lon=1


#######################################################################################################
# สร้างหน้าพื้นฐานgui
a_width=0
a_height=0
def gui_main_page(e):
    gui_main_page_1()
    try:
        print(str(2)+1)
        # c=data.cursor()
        # c.execute(f"""INSERT INTO {def_svae_1()} ( id,name,box,tex_t,font,bg,fg,x,y,width,height,command) 
        # VALUES (1,"GUI" , "-" , "-" , "-" , "-" , "-" , "-" , "-" , "{a_width}" , "{a_height}" , "-")""")
        # data.commit()
        # c.close()
        # b_gui.place(x=20,y=60,width=int(a_width)/size_1,height=int(a_height)/size_1)
    except :
        c=data.cursor()
        c.execute(f"""UPDATE {def_svae_1()} SET width = "{a_width}" ,height = "{a_height}" WHERE id = 1""")
        data.commit()
        c.close()
        b_gui.place(x=20,y=60,width=int(a_width)/size_1,height=int(a_height)/size_1)
        b_gui.bind("<B1-Motion>",  gui_main_page_3)
        b_gui.bind(" <ButtonRelease-1> ",  gui_main_page_2)
# กำหนดตำแหน่งgui
x_b_gui=20
y_b_gui=60
# หน้า gui ขยับได้ทำให้มันสามารถขยับได้ ยากอยู่
def gui_main_page_3(e):
    global x_b_gui,y_b_gui,lon,x_2,y_2
    b_gui.place(x=int(e.x+x_b_gui), y=int(e.y+y_b_gui)) 
    if lon == 0:
            x_2=e.x
            y_2=e.y
    x_b_gui+=e.x-x_2
    y_b_gui+=e.y-y_2
    lon =1 
# การคืนค่าให้มันเป้นแบบเดิมแล้วก็ทำการปรับค่าใหม่
def gui_main_page_2(e):
    global lon ,x_b_gui,y_b_gui,x_2,y_2
    lon=0
    x_b_gui+=x_2
    y_b_gui+=y_2
    def_svae(e,x_4=1,x_gui=x_b_gui,y_gui=y_b_gui)
# การแปลงค่าขนาดของ หน้าGUIให้มันอยู่ในรู)แบบตัวเลข
def gui_main_page_1():
    global a_height,a_width
    c_width=[]
    c_height=[]
    a_num_1=0
    for i in a_min_page_.get():
        if i.isdigit() == True and a_num_1 ==0 :
            c_width.append(i)
            a_width=''.join(c_width)

        if i.isdigit() == True and a_num_1 ==1 :
            c_height.append(i)
            a_height=''.join(c_height)

        if i.isdigit() == False :
            a_num_1 = 1
# ตกแต่งค่าให้มันมีลูกเล่น
def def_delete (e):
    if a_min_page_.get() == "ขนาดหน้า GUI" :
        b_min_page.delete(0,END)
    elif a_min_page_.get() == "" :
        b_min_page.insert(0,"ขนาดหน้า GUI")

# กำหนดสีตอนกด
def def_color(e):
    b_button_Label["bg"]="#DEB887"
    b_button_Button["bg"]="#DEB887"
    b_button_Entry["bg"]="#DEB887"
    click = e.widget["text"]
    e.widget["bg"]="#E3DED7"
# การบังคับให้มันทำงานตอนที่มันอยู่ค่าsaveeอยู่ในระบบหรือไม่ มีการกำหนดค่า
a_num=b_num=0
def def_app(e):
    global a_width,a_height,a_num
    def_color(e)
    if a_min_page_.get() == "ขนาดหน้า GUI" and _svae_1.get() == "" : 
        a_num=1
    elif a_width!=0 and a_height!=0 : 
        a_num=0
    click = e.widget["text"]
    if a_num ==0:
        def_app_1(click)
# การสร้างเมนูข้างใน
def def_app_1(click):
    global b_num,x_b_gui,y_b_gui
    i=max(box_Dictionaries.values()) + 1
    box_Dictionaries[ box[i] ]= i
    name=box_1[i]
    if click == "Label":
        box[ i ]=Label(gui,text=f"Label{i}",background="#E3DED7")   
    elif click == "Button":
        box[ i ]=Button(gui,text=f"Button{i}",background="#E3DED7")
    elif click == "Entry":
        box[ i ]= Button(gui,text=f"Entry{i}",background="#E3DED7")
    box[ i ].place( x=0/size_1+ x_b_gui+b_num, y=0/size_1+y_b_gui+b_num, width=70/size_1, height=25/size_1)   
    # box[ i ].bind("<Button-1>", def_lon_1)
    box[ i ].bind("<Double-Button-3>", def_delete_1)
    box[ i ].bind("<Button-1>",  def_change)
    box[ i ].bind("<Button-3>",def_change)

    box[ i ].bind("<B1-Motion>",  def_update_1)
    box[ i ].bind(" <ButtonRelease-1> ",  def_update_2)
    box[ i ].bind("<B3-Motion>",  def_update_3)
    box[ i ].bind(" <ButtonRelease-3> ",  def_update_2)
    box[ i ].bind("<Enter>",  def_change_1)
    c=data.cursor()
    c.execute(f"""
    INSERT INTO {def_svae_1()} 
    ( name,box,tex_t,font,bg,fg,x,y,width,height,command) 
    VALUES 
    ("{name}" , "{click}" , "{click}{i}" , 0 , "#E3DED7" , "#000000" , {b_num*size_1} , {b_num*size_1} , 70 , 25 , "ไม่มี")
    """)
    data.commit()
    c.close() 
    d_num_1()

def d_num_1():
    global b_num
    b_num+=10    

#############################################
# กำหนดค่าให้เกิดการกำหนดชื่อได้
box=[]
box_1=[]
box_Dictionaries={"ค่าว่าง":-1}
for i in range(100):
    for i_1 in range(10):
        if len(str(i)) != 3 :
            i="0"+str(i)
        if len(str(i)) == 3 :
            break
    _id="anmeid_"+str(i)
    box.append(_id)
    box_1.append(_id)



######################################################################################################
# ทุกครั้งที่กดจะให้เกิดการแสดงค่าต่างๆ
lon=0
lon_1=0
def def_change(e):
    global a_id,lon,wid,hei,x_1,y_1
    if lon == 0 and lon_1 ==0:
        click = e.widget["text"]
        a_data= data.execute(f""" SELECT * FROM {def_svae_1()} WHERE tex_t ="{click}" """)
        for i in a_data:
            a_te.set(i[3])
            a_fon.set(i[4])
            a_bg.set(i[5])
            a_fg.set(i[6])
            a_x.set(i[7])
            a_y.set(i[8])
            a_wi.set(i[9])
            a_he.set(i[10])
            a_comm.set(i[11])
            b_Button_6["text"]=f"BG\n({a_bg.get()})"
            b_Button_7["text"]=f"FG\n({a_fg.get()})"
            a_id=i[1]
            wid=int(a_wi.get())
            hei=int(a_he.get())
            x_1=float(a_x.get())/size_1
            y_1=float(a_y.get())/size_1
##################################################
def def_change_1(e):
    # if lon == 0 :
    #     click = e.widget["text"]
    #     a_data= data.execute(f""" SELECT * FROM {def_svae_1()} WHERE tex_t ="{click}" """)
    #     for i in a_data:
    #         a_te.set(i[3])
    #         a_fon.set(i[4])
    #         a_bg.set(i[5])
    #         a_fg.set(i[6])
    #         a_x.set(i[7])
    #         a_y.set(i[8])
    #         a_wi.set(i[9])
    #         a_he.set(i[10])
    #         a_comm.set(i[11])
    pass
###################################################
x_1=y_1=x_2=y_2=x_3=y_3=0
examine_1=0
# ส่วนต่อขยายของระบบให้มันขนาดได้ ยาก

def def_update_1(e):
    global wid,hei,x_1,y_1,lon,x_2,y_2,x_3,y_3,examine_1
    click = e.widget["text"]
    r = def_code(a_id)
    box[ r ].place(x=int(e.x+x_1), y=int(e.y+y_1)) 
    a_x.set(math.ceil((x_1+e.x-x_b_gui)*size_1))
    a_y.set(math.ceil((y_1+e.y-y_b_gui)*size_1))
    
    
    if lon == 0:
            x_2=e.x
            y_2=e.y
            delete_La.place(x=1040,y=470,width=100,height=75)
            
    x_1+=e.x-x_2
    y_1+=e.y-y_2
    x_3=e.x+x_1+x_2
    y_3=e.y+y_1+y_2
    lon =1 
    if (1040 <= x_1+wid and  x_1 <= 1140) and (470 <= y_1+hei and y_1 <= 645):
        delete_La["bg"]="#DEB887"
        examine_1=2
    if (1040 >= x_1+wid or  x_3 >= 1140) or (470 >= y_1+hei or y_1 >= 675):
        delete_La["bg"]="#ffffff"
        examine_1=1
# ส่วนต่อให้มันขยายได้
def def_update_3(e):
    global x_1,y_1,lon,x_2,y_2,examine_1
    click = e.widget["text"]
    r = def_code(a_id)
    box[ r ].place(width=e.x,height=e.y)
    if math.ceil((e.x*size_1)) >=0:
        a_wi.set(math.ceil((e.x*size_1)))
    if math.ceil((e.y*size_1)) >=0:
        a_he.set(math.ceil((e.y*size_1)))
    examine_1=1
# ไว้ทำให้อาจารย์ดูกรณี อธิบายไม่รู้เรื่อง
def def_update_4(e):
    print(e.x,e.y)
    # global x_icon,y_icon,lon
    # icon.place(x=e.x+x_icon, y=e.y+y_icon)
    # x_icon+=e.x-20
    # y_icon+=e.y-20
    # # a_Label_1.place(x=x_icon+95,y=y_icon+60,width=100,height=40)
    # # a_Label_2.place(x=x_icon+35,y=y_icon+60,width=100,height=40)
    # # a_Label_3.place(x=x_icon+95,y=y_icon+160,width=100,height=40)
    # # a_Label_4.place(x=x_icon+35,y=y_icon+160,width=100,height=40)
    # # a_Label_5.place(x=x_icon+95,y=y_icon+260,width=230,height=40)
    # # a_Label_8.place(x=980,y=460,width=100,height=40)
    # # a_Label_9.place(x=980,y=510,width=100,height=40)
    # # b_Button_6.place(x=980,y=360,width=100,height=40)
    # # b_Button_7.place(x=1110,y=360,width=100,height=40)
    # # b_Entry_1.place(x=980,y=110,width=100,height=40)
    # # b_Entry_2.place(x=1110,y=110,width=100,height=40)
    # # b_Entry_3.place(x=980,y=210,width=100,height=40)
    # # b_Entry_4.place(x=1110,y=210,width=100,height=40)
    # # b_Entry_5.place(x=980,y=310,width=230,height=40)
    # # b_Entry_8.place(x=1110,y=460,width=100,height=40)
    # # b_Entry_9.place(x=1110,y=510,width=100,height=40)
    # print(e.x,e.y)
# อัพเดตเข้าdata
def def_update_2(e):
    global examine_1
    if examine_1==1:
        global a_id,lon
        c=data.cursor()
        c.execute(f"""UPDATE {def_svae_1()} SET tex_t = "{a_te.get()}", font = "{a_fon.get()}" , 
            bg = "{a_bg.get()}" ,fg = "{a_fg.get()}",
            x="{a_x.get()}",y="{a_y.get()}",width = "{a_wi.get()}" ,height = "{a_he.get()}" ,command="{a_comm.get()}" 
            WHERE name = "{a_id}" """)
        data.commit()
        c.close()
        examine_1=0
        
    elif examine_1==2:
        examine_1=0
        def_delete_1(e)
    delete_La.place(x=1500,y=470,width=100,height=75)
    lon=0
# กำหนดค่าเอง
def def_update(e):
    global a_id,x_b_gui,y_b_gui
    a_data= data.execute(f"""SELECT * FROM {def_svae_1()} WHERE name ="{a_id}" """)
    for i in a_data:
        i = def_code(i[1])
        a=a_te.get()
        a_data_1= data.execute(f"""SELECT tex_t FROM {def_svae_1()} WHERE name !="{a_id}" """)
        for i_1 in a_data_1:
            if a_te.get()==i_1[0]:
                a=a_te.get()+f" ( {i} )"
        box[ i ]["text"]=a
        box[ i ]["bg"]=a_bg.get()
        box[ i ]["fg"]=a_fg.get()
        b_Button_6["text"]=f"BG\n({a_bg.get()})"
        b_Button_7["text"]=f"FG\n({a_fg.get()})"
        a_te.set(a)
        if int(a_fon.get()) > 0:
            try:
                box[ i ]["font"]=Font(family='Times',size=a_fon.get())
            except:
                box[ i ]["font"]=Font(family='Times',size=20)
        box[ i ].place( x=a_x.get()/size_1+ x_b_gui, y=a_y.get()/size_1+y_b_gui, width=a_wi.get()/size_1,height=a_he.get()/size_1) 
        def_update_2(e)
        
##############################################################################################################
_a_=0
# ลบแบบบ้างตัว
def def_delete_1(e):
    # a_da_1=tkinter.messagebox.askquestion("แจ้ง"," ต้องการจะลบใช้หรือไม่")
    a_da_1 ="yes"
    if a_da_1 == "yes":
        click = e.widget["text"]
        a_data= data.execute(f"""SELECT * FROM {def_svae_1()} WHERE tex_t ="{click}" """)
        for i in a_data:
            i_s = def_code(i[1])
            box[ i_s ].destroy()
            c=data.cursor()
            c.execute(f"DELETE FROM {def_svae_1()} WHERE id = {i[0]}")
            data.commit()
            c.close()
# รีค่าใหม่
def def_values():
    for i in box_Dictionaries.values():
        if i != -1:
            box[ i ].destroy()
    box_Dictionaries.clear()
    box_Dictionaries["ค่าว่าง"] = -1
# กำหนดsaveใหม่
def def_svae(e,x_gui=20,y_gui=60,x_4=0):
    global _a_,size_1,x_b_gui,y_b_gui
    def_svae_1(a=1)
    if _a_ == 1:
        def_values()
    try:
        if _svae_1.get() !="":
            a_data= data.execute(f"""SELECT * FROM {def_svae_1(a=1)} WHERE id > 1""")
            for i in a_data:
                i=def_code(i[1])
                box_Dictionaries[ box[i] ]= i 


            a_data= data.execute(f'SELECT * FROM {def_svae_1()} ')
            for data_2 in a_data:
                if data_2[0]==1 and x_4 ==0:
                    x_b_gui=20
                    y_b_gui=60
                    b_min_page.delete(0,END)
                    b_min_page.insert(0,f"{int(data_2[9])}x{int(data_2[10])}")
                    # b_gui.place(x=20,y=60,width=int(data_2[9])/size_1,height=int(data_2[10])/size_1)
                    a_min_page_.set(f"{int(data_2[9])}x{int(data_2[10])}")
                    gui_main_page(e)
                if data_2[0]!=1:
                    i = def_code(data_2[1])

                    if data_2[2] == "Label":
                        box[ i ]=Label(gui,text=f"{data_2[3]}",background=f"{data_2[5]}",fg=data_2[6])   
                    elif data_2[2] == "Button":
                        box[ i ]=Button(gui,text=f"{data_2[3]}",background=f"{data_2[5]}",fg=data_2[6])   
                    elif data_2[2] == "Entry":
                        box[ i ]= Button(gui,text=f"{data_2[3]}",background=f"{data_2[5]}",fg=data_2[6]) 
                    if data_2[4] != 0:
                        try:
                            box[ i ]["font"]=Font(family='Times',size=data_2[4])
                        except:
                            box[ i ]["font"]=Font(family='Times',size=20)
                    box[ i ].place( x=data_2[7]/size_1+ x_gui, y=data_2[8]/size_1+y_gui, width=data_2[9]/size_1, height=data_2[10]/size_1)   
                    # box[ i ].bind("<Button-1>", def_lon_1)
                    box[ i ].bind("<Double-Button-3>", def_delete_1)
                    box[ i ].bind("<Button-1>",  def_change)
                    box[ i ].bind("<Button-3>",def_change)
                    
                    box[ i ].bind("<B1-Motion>",  def_update_1)
                    box[ i ].bind(" <ButtonRelease-1> ",  def_update_2)
                    box[ i ].bind("<B3-Motion>",  def_update_3)
                    box[ i ].bind(" <ButtonRelease-3> ",  def_update_2)
                    box[ i ].bind("<Enter>",  def_change_1)
            _a_=1
    except:
        pass
# กำหนดสี
def color_1(e):
    click = e.widget["text"]
    s=tkinter.colorchooser.askcolor()
    if click==f"BG\n({a_bg.get()})":
        a_bg.set(s[1])
    elif click==f"FG\n({a_fg.get()})":
        a_fg.set(s[1])
    def_update(e)


x_icon=1241
y_icon=0
try:
    photo3 = PhotoImage(file="D:\project\ppp.png")
    icon=Button(gui,image=photo3 )
    icon.place(x=1241,y=0,width=40,height=40)
    icon.bind("<B1-Motion>",  def_update_4)
except:
    pass

a_wi=IntVar()
a_Label_1=Label(gui,background="#FFD700",text="WIDTH",font=Font(family='Geometric Sans',size=15))
a_Label_1.place(x=980,y=60,width=100,height=40)
b_Entry_1=Entry(gui,background="#F0FFFF",textvariable=a_wi,validate='key', vcmd=nummu)
b_Entry_1.place(x=1110,y=60,width=100,height=40)
b_Entry_1.bind("<Return>", def_update )

a_he=IntVar()
a_Label_2=Label(gui,background="#FFD700",text="HEIGHT",font=Font(family='Geometric Sans',size=15))
a_Label_2.place(x=980,y=110,width=100,height=40)
b_Entry_2=Entry(gui,background="#F0FFFF",textvariable=a_he,validate='key', vcmd=nummu)
b_Entry_2.place(x=1110,y=110,width=100,height=40)
b_Entry_2.bind("<Return>", def_update )

a_x=IntVar()
a_Label_3=Label(gui,background="#FFD700",text="X",font=Font(family='Geometric Sans',size=15))
a_Label_3.place(x=980,y=160,width=100,height=40)
b_Entry_3=Entry(gui,background="#F0FFFF",textvariable=a_x,validate='key', vcmd=nummu)
b_Entry_3.place(x=1110,y=160,width=100,height=40)
b_Entry_3.bind("<Return>", def_update )

a_y=IntVar()
a_Label_4=Label(gui,background="#FFD700",text="Y",font=Font(family='Geometric Sans',size=15))
a_Label_4.place(x=980,y=210,width=100,height=40)
b_Entry_4=Entry(gui,background="#F0FFFF",textvariable=a_y,validate='key', vcmd=nummu)
b_Entry_4.place(x=1110,y=210,width=100,height=40)
b_Entry_4.bind("<Return>", def_update )

a_te=StringVar()
a_Label_5=Label(gui,background="#FFD700",text="TEXT",font=Font(family='Geometric Sans',size=15))
a_Label_5.place(x=980,y=260,width=100,height=40)
b_Entry_5=Entry(gui,background="#F0FFFF",textvariable=a_te)
b_Entry_5.place(x=1110,y=260,width=100,height=40)
b_Entry_5.bind("<Return>", def_update )

a_bg=StringVar()
b_Button_6=Button(gui,background="#F0FFFF",text=f"BG\n({a_bg.get()})",font=Font(family='Geometric Sans',size=10))
b_Button_6.place(x=980,y=410,width=100,height=40)
# b_Button_6=Entry(gui,background="#948b82",textvariable=a_bg)
# b_Button_6.place(x=980,y=410,width=100,height=40)
b_Button_6.bind("<Return>", def_update )
b_Button_6.bind("<Button-1>", color_1)

a_fg=StringVar()
b_Button_7=Button(gui,background="#F0FFFF",text=f"FG\n({a_fg.get()})",font=Font(family='Geometric Sans',size=10))
b_Button_7.place(x=1110,y=410,width=100,height=40)
# b_Button_7=Entry(gui,background="#948b82",textvariable=a_fg,)
# b_Button_7.place(x=1110,y=410,width=100,height=40)
b_Button_7.bind("<Return>", def_update )
b_Button_7.bind("<Button-1>", color_1)

a_comm=StringVar()
a_Label_8=Label(gui,background="#FFD700",text="command",font=Font(family='Geometric Sans',size=15))
a_Label_8.place(x=980,y=310,width=100,height=40)
b_Entry_8=Entry(gui,background="#F0FFFF",textvariable=a_comm)
b_Entry_8.place(x=1110,y=310,width=100,height=40)
b_Entry_8.bind("<Return>", def_update )

a_fon=StringVar()
a_Label_9=Label(gui,background="#FFD700",text="FONT",font=Font(family='Geometric Sans',size=15))
a_Label_9.place(x=980,y=360,width=100,height=40)
b_Entry_9=Entry(gui,background="#F0FFFF",textvariable=a_fon,validate='key', vcmd=nummu)
b_Entry_9.place(x=1110,y=360,width=100,height=40)
b_Entry_9.bind("<Return>", def_update )

a_min_page_=StringVar()
b_min_page=Entry(gui,textvariable=a_min_page_,justify = "center",font=20)
b_min_page.place(x=20,y=20,width=163,height=30)
b_min_page.bind("<Return>",gui_main_page )
b_min_page.bind("<Enter>",  def_delete)
b_min_page.bind("<Leave>",  def_delete)

b_min_page.insert(0,"ขนาดหน้า GUI")


b_button_Label=Button(gui,background="#DEB887",text="Label")
b_button_Label.place(x=190,y=20,width=85,height=30)
b_button_Label.bind("<Button-1>", def_app)

b_button_Button=Button(gui,background="#DEB887",text="Button")
b_button_Button.place(x=280,y=20,width=85,height=31)
b_button_Button.bind("<Button-1>", def_app)

b_button_Entry=Button(gui,background="#DEB887",text="Entry")
b_button_Entry.place(x=370,y=20,width=85,height=30)
b_button_Entry.bind("<Button-1>", def_app)
s_namu=["New File"]
a_data= data.execute('SELECT * FROM sqlite_sequence')
for i in a_data:
    s_namu.append(i[0])

_svae_1=StringVar()
b_button_svae=OptionMenu(gui,_svae_1,*s_namu)
b_button_svae.place(x=560,y=20,width=74,height=30)

b_button_svae_1=Button(gui,background="#948b82",text="ยืนยัน")
b_button_svae_1.place(x=640,y=20,width=74,height=30)
b_button_svae_1.bind("<Button-1>",def_svae)

xyz_1=[1,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2,2.1,2.2,2.3,2.4,2.5,2.6,2.7,2.9,2.9,3]
_svae_2=StringVar()
b_button_svae_2=OptionMenu(gui,_svae_2,*xyz_1)
b_button_svae_2.place(x=470,y=20,width=80,height=30)
_svae_2.set(size_1)


b_gui=Label(gui,background="#DEB887",font=20)
delete_La = Label(gui,text="ลบ")
try:
    photo4 = PhotoImage(file="D:\project\งานออกแบบที่ไม่มีชื่อ (9).png")
    delete_La["image"]=photo4
except:
    pass

def code_python_1():
    a_data= data.execute(f""" SELECT * FROM {def_svae_1()} WHERE box = "Button" or id = 1 """)
    for i in a_data:
        if i[0]==1:
            txtarea.insert(END,f"""roon.geometry("{i[9]}x{i[10]}+0+0")\n\n""")
        if i[0]!=1 and i[11] != "ไม่มี" :
                txtarea.insert(END,f"""def {i[11]}():\n""")
                txtarea.insert(END,f"""    print("{i[1]}")\n""")
    a_data= data.execute(f"""SELECT * FROM {def_svae_1()}   """)
    for i in a_data:
        if i[0] != 1 and i[2]=="Button":
            if i[11] =="ไม่มี":
                txtarea.insert(END,f"""{i[1]}={i[2]}(roon,text="{i[3]}",font=Font(family='Times',size={i[4]}),bg="{i[5]}",fg="{i[6]}")\n""")
                txtarea.insert(END,f"""{i[1]}.place(x={i[7]},y={i[8]},width={i[9]},height={i[10]})\n\n""")    
            else:
                txtarea.insert(END,f"""{i[1]}={i[2]}(roon,text="{i[3]}",font=Font(family='Times',size={i[4]}),bg="{i[5]}",fg="{i[6]}",command={i[11]})\n""")
                txtarea.insert(END,f"""{i[1]}.place(x={i[7]},y={i[8]},width={i[9]},height={i[10]})\n\n""")    
        elif i[0] != 1 and i[2] =="Label":
            txtarea.insert(END,f"""{i[1]}={i[2]}(roon,text="{i[3]}",font=Font(family='Times',size={i[4]}),bg="{i[5]}",fg="{i[6]}")\n""")
            txtarea.insert(END,f"""{i[1]}.place(x={i[7]},y={i[8]},width={i[9]},height={i[10]})\n\n""")
        elif i[0] != 1 and i[2]=="Entry":
            txtarea.insert(END,f"""{i[1]}={i[2]}(roon,bg="{i[5]}",fg="{i[6]}",font=Font(family='Times',size={i[4]}))\n""")
            txtarea.insert(END,f"""{i[1]}.place(x={i[7]},y={i[8]},width={i[9]},height={i[10]})\n\n""")
lon_2=0
def code_python(e):
    if 30<=e.x<=75:
        global lon_2
        try:
            if  lon_2 == 1:   
                
                txtarea.delete(0.0,END)
            txtarea.insert(END,f"from tkinter import *\n")
            txtarea.insert(END,f"from tkinter.font import * \n")
            txtarea.insert(END,f"roon = Tk()\n")
            code_python_1()
            txtarea.insert(END,"roon.mainloop()")
            
            lon_2=1
        except:
            pass

billarea=Frame(python,bd=10,relief=GROOVE,bg="#000000")
billarea.place(x=0,y=0,width=1280,height=650)
bill_title=Label(billarea,text="PYTHON",font=("Times",19),fg="#000000",bd=7,bg="#6495ed",relief=GROOVE).pack(fill=X)
scrol_y=Scrollbar(billarea,orient=VERTICAL)
txtarea=Text(billarea,font=("Times",11),yscrollcommand=scrol_y.set)
scrol_y.pack(side=RIGHT,fill=Y)
scrol_y.config(command=txtarea.yview)
txtarea.pack(fill=BOTH,expand=2)
t.bind("<Button-1>",code_python)

tk.geometry("1290x650+-10+0")
tk.resizable(width=False, height=False)
tk.mainloop()
