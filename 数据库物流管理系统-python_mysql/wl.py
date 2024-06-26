import pymysql
from tkinter import *
from tkinter.messagebox import *
from tkinter import ttk
import tkinter as tk
import tkinter.font as tkFont
from PIL import Image,ImageTk
 
def delButton(tree):
    x = tree.get_children()
    for item in x:
        tree.delete(item)
 
def back(root):
    root.destroy()
    StartPage()
 
image1=None
img1=None
#(1)物流信息管理系统
def StartPage():
    global image1
    global img1
    root=tk.Tk()
    root.title('物流信息管理系统')
    root.geometry('490x650+500+100')
    root['background']='white'
    image1 = Image.open('./image/1.jpg')
    img1 = ImageTk.PhotoImage(image1)
    Label(root,image=img1).pack()#place(relx=0,rely=0)
    Button(root, text="管理员登录", font=tkFont.Font(size=16), command=lambda: Login(root), width=25,
               height=2, fg='black', bg='gainsboro', activebackground='black', activeforeground='white').place(relx=0.21,rely=0.45)
    Button(root, text="游客登录", font=tkFont.Font(size=16), command=lambda:GuestPage(root), width=25,
               height=2, fg='black', bg='gainsboro', activebackground='black', activeforeground='white').place(relx=0.21,rely=0.6)
    Button(root, text='退出系统', height=2, font=tkFont.Font(size=16), width=25, command=root.destroy,
               fg='black', bg='gainsboro', activebackground='black', activeforeground='white').place(relx=0.21,rely=0.75)
    root.mainloop()
 
image2=None
img2=None
#(2)管理员登录页面
def Login(root):
    global image2
    global img2
    root.destroy()
    root= tk.Tk()
    root.title('管理员登录页面')
    root.geometry('1200x700+200+50')
    root['background']='white'
    image2 = Image.open('./image/6.jpg')
    img2 = ImageTk.PhotoImage(image2)
    Label(root,image=img2).pack()
    Label(root, text='账号：',font=("楷体", 15),bg='white').place(relx=0.4,rely=0.35)
    Label(root, text='密码：',font=("楷体", 15),bg='white').place(relx=0.4,rely=0.45)
    username=StringVar()
    pwd=StringVar()
    entry_username=Entry(root,textvariable=username, show=None)
    entry_username.place(relx=0.45, rely=0.35, relwidth=0.2,relheight=0.039)
    entry_pwd = Entry(root, textvariable=pwd, show='*')
    entry_pwd.place(relx=0.45, rely=0.45, relwidth=0.2,relheight=0.039)
    Button(root, text="登录", width=15, font=tkFont.Font(size=15), command=lambda:sign_in(root, entry_username, entry_pwd),fg='black', activebackground='black', activeforeground='white').place(relx=0.47,rely=0.57)
    Button(root, text="注册", width=15, font=tkFont.Font(size=15),command=lambda:register_Page(root),fg='black',activebackground='black', activeforeground='white').place(relx=0.47,rely=0.65)
    root.protocol('WM_DELETE_WINDOW', lambda:back(root))
    root.mainloop()
#(2.1)
def sign_in(root, entry_username, entry_pwd):
    db = pymysql.connect(host="ip", user="root",\
            password="username", db="db", port=3306)
    cur = db.cursor()
    sql="select * from manger where username='%s'"%(entry_username.get())
    try:
        cur.execute(sql)
        result = cur.fetchone()
        mima=result[1]
    except:
        showinfo(title='提示', message='账号/密码错误！')
        cur.close()
        db.close()
 
    if mima==entry_pwd.get():
        MangerChoosePage(root)
    else:
        showinfo(title='提示', message='账号/密码错误！')
 
image8=None
img8=None
#（3）管理员注册页面
def register_Page(root):
    global image8
    global img8
    root.destroy()
    root=Tk()
    root.title('管理员注册页面')
    root.geometry('1200x700+200+50')
    root['background']='white'
    image8 = Image.open('./image/7.jpg')
    img8 = ImageTk.PhotoImage(image8)
    Label(root,image=img8).pack()
    Label(root, text='输入账号：',font=("楷体", 15),bg='white').place(relx=0.4,rely=0.35)
    Label(root, text='输入密码：',font=("楷体", 15),bg='white').place(relx=0.4,rely=0.45)
    Label(root, text='确认密码：',font=("楷体", 15),bg='white').place(relx=0.4,rely=0.55)
    username=StringVar()
    pwd=StringVar()
    sure_pwd=StringVar()
    entry_username=Entry(root,textvariable=username, show=None)
    entry_username.place(relx=0.495, rely=0.35, relwidth=0.2,relheight=0.039)
    entry_pwd = Entry(root, textvariable=pwd, show='*')
    entry_pwd.place(relx=0.495, rely=0.45, relwidth=0.2,relheight=0.039)
    entry_sure_pwd = Entry(root, textvariable=sure_pwd, show='*')
    entry_sure_pwd.place(relx=0.495, rely=0.55, relwidth=0.2,relheight=0.039)
    Button(root, text="注册", width=15, font=tkFont.Font(size=15),command=lambda:register(root,entry_username,entry_pwd,entry_sure_pwd),fg='black',activebackground='black', activeforeground='white').place(relx=0.47,rely=0.65)
    Button(root, text="退出", width=15, font=tkFont.Font(size=15),command=lambda:Login(root),fg='black',activebackground='black', activeforeground='white').place(relx=0.47,rely=0.75)
    root.protocol('WM_DELETE_WINDOW', lambda:Login(root))
    root.mainloop()
#(3.1)
def register(root,entry_username,entry_pwd,entry_sure_pwd):
    db = pymysql.connect(host="ip", user="root",password="pwd", db="db", port=3306)
    cur = db.cursor()
    sql="insert into manger values('%s','%s')"% (entry_username.get(),entry_pwd.get())
    cur.execute("select * from manger where username='%s'"%(entry_username.get()))
    result = cur.fetchall()
    if result:
        showinfo('提示','该账号已存在，请重新输入！')
    else:
        if len(entry_pwd.get())==6:
            if entry_sure_pwd.get()==entry_pwd.get():
                cur.execute(sql)
                db.commit()
                showinfo('提示','注册成功！')
                Login(root)
            else:
                showinfo('提示','两次输入密码不相同，请重新输入！')
        else:
            showinfo("提示","请输入六位数密码！")
    cur.close()
    db.close()
 
image3 = None
img3 = None
# (4)管理员信息选择操作页面
def MangerChoosePage(root):
    global image3
    global img3
    root.destroy()
    root = Tk()
    root.title('管理员信息选择操作页面')
    root.geometry('600x750+500+40')  # ('950x700')
    root['background'] = 'white'
    image3 = Image.open('./image/8.jpg')
    img3 = ImageTk.PhotoImage(image3)
    Label(root, image=img3).pack()
    Button(root, text="人员信息操作", font=tkFont.Font(size=16), command=lambda: Manger_user_Page(root), width=25,
           height=2, fg='black', bg='gainsboro', activebackground='black', activeforeground='white').place(relx=0.22,
                                                                                                           rely=0.3)
    Button(root, text="订单信息操作", font=tkFont.Font(size=16), command=lambda: MangerPage(root), width=25,
           height=2, fg='black', bg='gainsboro', activebackground='black', activeforeground='white').place(relx=0.22,
                                                                                                           rely=0.5)
    Button(root, text='退出', height=2, font=tkFont.Font(size=16), width=25, command=lambda: back(root),
           fg='black', bg='gainsboro', activebackground='black', activeforeground='white').place(relx=0.22, rely=0.7)
    root.protocol('WM_DELETE_WINDOW', lambda: back(root))
    root.mainloop()
 
image4=None
img4=None
#(5)人员信息操作页面
def Manger_user_Page(root):
    global image4
    global img4
    root.destroy()
    root = Tk()
    root.geometry('565x600+500+80')
    root.title('人员信息操作页面')
    root['background']='white'
    image4 = Image.open('./image/4.jpg')
    img4 = ImageTk.PhotoImage(image4)
    Label(root,image=img4).pack()
    Button(root, text="收件人信息操作",activebackground='gainsboro',font=('楷体',15), command=lambda: Uers_infor_Page(root=root,table='recipient')).place(relx=0.27, rely=0.4, width=250)
    Button(root, text="寄件人信息操作",activebackground='gainsboro',font=('楷体',15), command=lambda: Uers_infor_Page(root=root,table='sender')).place(relx=0.27, rely=0.52, width=250)
    Button(root, text="配送员信息操作", activebackground='gainsboro',font=('楷体',15), command=lambda: Uers_infor_Page(root=root,table='distributor')).place(relx=0.27, rely=0.64, width=250)
    Button(root, text="退出", activebackground='gainsboro',font=('楷体',15), command=lambda:MangerChoosePage(root)).place(relx=0.27, rely=0.76, width=250)
    root.protocol('WM_DELETE_WINDOW', lambda:MangerChoosePage(root))
    root.mainloop()
 
image6=None
img6=None
#(6)收件人、寄件人、配送员信息操作页面
def Uers_infor_Page(root,table):
    global image6
    global img6
    root.destroy()
    root=Tk()
    root.geometry('900x700+300+50')
    if table=='recipient':
        Title='收件人'+'信息操作页面'
        temp1='身份证号'
        temp2='地址'
    elif table=='distributor':
        Title='配送员'+'信息操作页面'
        temp1= '工号'
        temp2='身份证号'
    else:
        Title='寄件人'+'信息操作页面'
        temp1= '身份证号'
        temp2='地址'
    root.title(Title)
    root['background']='floralwhite'
    image6 = Image.open('./image/3.jpg')
    img6 = ImageTk.PhotoImage(image6)
    Label(root,text=Title,compound='bottom',image=img6,font=('楷体',30),fg='blue',bg='floralwhite').pack()
    Label(root, text="姓名：").place(relx=0.02, rely=0.08, relwidth=0.1)
    Label(root, text=temp1+'：').place(relx=0.5, rely=0.08, relwidth=0.1)
    Label(root, text=temp2+'：').place(relx=0.02, rely=0.14, relwidth=0.1)
    Label(root, text="性别：").place(relx=0.5, rely=0.14, relwidth=0.1)
    Label(root, text="电话号码：").place(relx=0.02, rely=0.2, relwidth=0.1)
 
    name = StringVar()
    ID = StringVar()
    address = StringVar()
    sex = StringVar()
    phonenumber = StringVar()
 
    entry_name = Entry(root, textvariable=name )
    entry_name.place(relx=0.12, rely=0.08, relwidth=0.3, height=25)
    entry_ID = Entry(root, textvariable=ID)
    entry_ID.place(relx=0.6, rely=0.08, relwidth=0.3, height=25)
    entry_address = Entry(root, textvariable=address)
    entry_address.place(relx=0.12, rely=0.14, relwidth=0.3, height=25)
    entry_sex = Entry(root, textvariable=sex)
    entry_sex.place(relx=0.6, rely=0.14, relwidth=0.3, height=25)
    entry_phonenumber = Entry(root, textvariable=phonenumber)
    entry_phonenumber.place(relx=0.12, rely=0.2, relwidth=0.3, height=25)
 
    list1=[entry_name,entry_ID,entry_address,entry_sex,entry_phonenumber]
 
    Tree1 = ttk.Treeview(root, show='headings',column=('name','ID','address','sex','phonenumber'))
    Tree1.column('name', width=50, anchor="center")
    Tree1.column('ID', width=70, anchor="center")
    Tree1.column('address', width=40, anchor="center")
    Tree1.column('sex', width=70, anchor="center")
    Tree1.column('phonenumber', width=70, anchor="center")
    # 表格标题设置
    Tree1.heading('name', text='姓名')
    Tree1.heading('ID', text=temp1)
    Tree1.heading('address', text=temp2)
    Tree1.heading('sex', text='性别')
    Tree1.heading('phonenumber', text='电话号码')
 
    Tree1.place(relx=0.01,rely=0.5, relwidth=0.98)
 
    def treeviewClick(event):
        item = Tree1.selection()[0]
        item_text = Tree1.item(item, "values")
 
        entry_name.delete(0, 'end')
        entry_ID.delete(0, 'end')
        entry_address.delete(0, 'end')
        entry_sex.delete(0, 'end')
        entry_phonenumber.delete(0, 'end')
 
        entry_name.insert(0, item_text[0])
        entry_ID.insert(0, item_text[1])
        entry_address.insert(0, item_text[2])
        entry_sex.insert(0, item_text[3])
        entry_phonenumber.insert(0, item_text[4])
 
    Button(root, text="显示所有人员信息", command=lambda: showAll_user_Info(tree=Tree1,table=table)).place(relx=0.12, rely=0.3, width=120)
    Button(root, text="增加人员信息", command=lambda: append_user_Info(tree=Tree1, list=list1,table=table)).place(relx=0.32, rely=0.3,width=120)
    Button(root, text="删除人员信息", command=lambda: delete_user_Info(tree=Tree1,table=table)).place(relx=0.52, rely=0.3, width=120)
    Button(root, text="更改人员信息", command=lambda: update_user_Info(tree=Tree1, list=list1,table=table)).place(relx=0.72, rely=0.3,width=120)
 
    Button(root, text="根据姓名查找", command=lambda: find_use_Info(tree=Tree1,table=table,entry=entry_name,flag='name')).place(relx=0.02, rely=0.38,width=135)
    Button(root, text="根据"+temp1+"查找", command=lambda: find_use_Info(tree=Tree1,table=table,entry=entry_ID,flag='ID')).place(relx=0.22, rely=0.38,width=135)
    Button(root, text="根据"+temp2+"查找", command=lambda: find_use_Info(tree=Tree1,table=table,entry=entry_address,flag='address')).place(relx=0.42, rely=0.38,width=135)
    Button(root, text="根据性别查找", command=lambda: find_use_Info(tree=Tree1,table=table,entry=entry_sex,flag='sex')).place(relx=0.62, rely=0.38,width=135)
    Button(root, text="根据电话号码查找", command=lambda: find_use_Info(tree=Tree1,table=table,entry=entry_phonenumber,flag="phonenumber")).place(relx=0.82, rely=0.38,width=135)
 
    Tree1.bind('<ButtonRelease-1>', treeviewClick)
    root.protocol('WM_DELETE_WINDOW', lambda:Manger_user_Page(root))
    root.mainloop()
#(6.1)
def showAll_user_Info(tree,table):
    delButton(tree)
    db = pymysql.connect(host="ip", user="root",password="pwd", db="db", port=3306)
    cur = db.cursor() #用db操作游标
    if table=='recipient':
        sql="select * from recipient"
    elif table=='sender':
        sql="select * from sender"
    else:
        sql="select * from distributor"
    cur.execute(sql)  # 执行sql语句
    #fetchone()返回一条记录（元组），没有结果则返回none
    #fetchall()返回所有元组，构成一个二维元组
    results = cur.fetchall()
    for item in results:
        tree.insert('', "end", values=item)
    cur.close()
    db.close()  # 关闭连接
#(6.2)
def append_user_Info(tree,list,table):
    delButton(tree)
    list2 = []
    for i in range(len(list)):
        if list[i].get() == '':
            showerror(title='提示', message='输入不能为空!')
            return
        else:
            list2.append(list[i].get())
 
    x = tree.get_children()
    for item in x:
        tree.delete(item)
 
    db = pymysql.connect(host="ip", user="root",password="pwd", db="db", port=3306)
    cur = db.cursor()
    try:
        if table == 'recipient':
            sql1 = "insert into recipient values('%s','%s','%s','%s','%s')"% (list2[0], list2[1], list2[2], list2[3], list2[4])
        elif table == 'sender':
            sql1 = "insert into sender values('%s','%s','%s','%s','%s')"% (list2[0], list2[1], list2[2], list2[3], list2[4])
        else:
            sql1 = "insert into distributor values('%s','%s','%s','%s','%s')"% (list2[0], list2[1], list2[2], list2[3], list2[4])
        cur.execute(sql1)
        db.commit()
        if table == 'recipient':
            sql = "select * from recipient"
        elif table == 'sender':
            sql = "select * from sender"
        else:
            sql = "select * from distributor"
        cur.execute(sql)
        results = cur.fetchall()
        for item in results:
            tree.insert('', "end", values=item)
        showinfo(title='提示', message='添加/更改成功！')
    except:
        showinfo(title='提示', message='该人员/编号已存在！')
        return
    cur.close()
    db.close()
#(6.3)
def delete_user_Info(tree,table):
    if not tree.selection():
        showerror(title='提示', message='请选择一条信息！')
        return
    res=askyesno('提示','是否确认删除？')
    if res==True:
        for item in tree.selection():
            selectedItem = tree.selection()[0]
            no1 = tree.item(selectedItem, 'values')[1]
            tree.delete(item)
            if table == 'recipient':
                sql = "delete from recipient where RID = '%s' " % no1
            elif table == 'sender':
                sql = "delete from sender where SID = '%s' " % no1
            else:
                sql = "delete from distributor where Dnum = '%s' " % no1
            db = pymysql.connect(host="ip", user="root",password="pwd", db="db", port=3306)
            cur = db.cursor()
            cur.execute(sql)
            db.commit()
            cur.close()
            db.close()
            showinfo(title='提示', message='删除成功！')
#(6.4)
def update_user_Info(tree, list,table):
    if not tree.selection():
        showerror(title='提示', message='请选择一条信息！')
        return
    else:
        res=askyesno("提示","是否确认更新数据？")
        if res==True:
            for item in tree.selection():
                selectedItem = tree.selection()[0]
                no1 = tree.item(selectedItem, 'values')[1]
                tree.delete(item)
                if table == 'recipient':
                    sql = "delete from recipient where RID = '%s' " % no1
                elif table == 'sender':
                    sql = "delete from sender where SID = '%s' " % no1
                else:
                    sql = "delete from distributor where Dnum = '%s' " % no1
                db = pymysql.connect(host="ip", user="root",password="pwd", db="db", port=3306)
                cur = db.cursor()
 
                cur.execute(sql)
                db.commit()
 
                cur.close()
                db.close()
            append_user_Info(tree, list,table)
            return
#(6.5)
def find_sql_line(table,flag,entry):
    if table=='recipient':
        if flag=='name':
            sql = "select * from recipient where Rname = '%s'"%(entry.get())
        elif flag=='ID':
            sql = "select * from recipient where RID = '%s'"%(entry.get())
        elif flag=='address':
            sql = "select * from recipient where Raddress = '%s'"%(entry.get())
        elif flag=='sex':
            sql = "select * from recipient where Rsex = '%s'"%(entry.get())
        else:
            sql = "select * from recipient where Rphonenumber = '%s'"%(entry.get())
    elif table=='sender':
        if flag=='name':
            sql = "select * from sender where Sname = '%s'"%(entry.get())
        elif flag=='ID':
            sql = "select * from sender where SID = '%s'"%(entry.get())
        elif flag=='address':
            sql = "select * from sender where Saddress = '%s'"%(entry.get())
        elif flag=='sex':
            sql = "select * from sender where Ssex = '%s'"%(entry.get())
        else:
            sql = "select * from sender where Sphonenumber = '%s'"%(entry.get())
    else:
        if flag=='name':
            sql = "select * from distributor where Dname = '%s'"%(entry.get())
        elif flag=='ID':
            sql = "select * from distributor where Dnum = '%s'"%(entry.get())
        elif flag=='address':
            sql = "select * from distributor where DID = '%s'"%(entry.get())
        elif flag=='sex':
            sql = "select * from distributor where Dsex = '%s'"%(entry.get())
        else:
            sql = "select * from distributor where Dphonenumber = '%s'"%(entry.get())
 
    return sql
#(6.6)
def find_use_Info(tree,table,entry,flag):
    delButton(tree)
    db = pymysql.connect(host="ip", user="root",password="pwd", db="db", port=3306)
    cur = db.cursor()
    sql=find_sql_line(table=table,flag=flag,entry=entry)
    cur.execute(sql)
    results = cur.fetchall()
    if results:
        for item in results:
            tree.insert('', "end", values=item)
    else:
        showinfo(title='提示', message='无该信息！')
    cur.close()
    db.close()
 
image7=None
img7=None
#（7）订单信息操作页面
def MangerPage(root1):
    global image7
    global img7
    root1.destroy()
    root1 = Tk()
    root1.geometry('1000x700+300+50')
    root1.title('订单信息操作页面')
    root1['background']='floralwhite'
    image7 = Image.open('./image/2.jpg')
    img7 = ImageTk.PhotoImage(image7)
    Label(root1, text='订单信息操作页面',bg='floralwhite', fg='blue', font=('楷体', 20),compound='bottom',image=img7).pack()
    Label(root1, text="订单编号：",font=('楷体', 13)).place(relx=0.5, rely=0.07, relwidth=0.1)
    Label(root1, text="运输时间：",font=('楷体', 13)).place(relx=0.5, rely=0.12, relwidth=0.1)
    Label(root1, text="物流站：",font=('楷体', 13)).place(relx=0.5, rely=0.17, relwidth=0.1)
    Label(root1, text="快递员：",font=('楷体', 13)).place(relx=0.5, rely=0.22, relwidth=0.1)
    Label(root1, text="寄件人：",font=('楷体', 13)).place(relx=0.5, rely=0.27, relwidth=0.1)
    Label(root1, text="收件人：",font=('楷体', 13)).place(relx=0.5, rely=0.32, relwidth=0.1)
    Label(root1, text="商品：",font=('楷体', 13)).place(relx=0.5, rely=0.37, relwidth=0.1)
    Label(root1, text="价格：",font=('楷体', 13)).place(relx=0.5, rely=0.42, relwidth=0.1)
 
    Onum = StringVar()
    Odelivery_time = StringVar()
    Olog_station = StringVar()
    Odistributor = StringVar()
    Osender = StringVar()
    Orecipient = StringVar()
    Ogoods = StringVar()
    Oprice = StringVar()
 
    entry_Onum = Entry(root1, textvariable=Onum)
    entry_Onum.place(relx=0.6, rely=0.07, relwidth=0.3, height=25)
    entry_Odelivery_time = Entry(root1, textvariable=Odelivery_time)
    entry_Odelivery_time.place(relx=0.6, rely=0.12, relwidth=0.3, height=25)
    entry_Olog_station = Entry(root1, textvariable=Olog_station)
    entry_Olog_station.place(relx=0.6, rely=0.17, relwidth=0.3, height=25)
    entry_Odistributor = Entry(root1, textvariable=Odistributor)
    entry_Odistributor.place(relx=0.6, rely=0.22, relwidth=0.3, height=25)
    entry_Osender = Entry(root1, textvariable=Osender)
    entry_Osender.place(relx=0.6, rely=0.27, relwidth=0.3, height=25)
    entry_Orecipient = Entry(root1, textvariable=Orecipient)
    entry_Orecipient.place(relx=0.6, rely=0.32, relwidth=0.3, height=25)
    entry_Ogoods = Entry(root1, textvariable=Ogoods)
    entry_Ogoods.place(relx=0.6, rely=0.37, relwidth=0.3, height=25)
    entry_Oprice = Entry(root1, textvariable=Oprice)
    entry_Oprice.place(relx=0.6, rely=0.42, relwidth=0.3, height=25)
 
    list1 = [entry_Onum, entry_Odelivery_time, entry_Olog_station, entry_Odistributor, entry_Osender, entry_Orecipient,entry_Ogoods, entry_Oprice]
 
    Tree1 = ttk.Treeview(root1, show='headings',
                         column=('Onum', 'Odelivery_time', 'Olog_station', 'Odistributor', 'Osender', 'Orecipient', 'Ogoods', 'Oprice'))
    Tree1.column('Onum', width=50, anchor="center")
    Tree1.column('Odelivery_time', width=70, anchor="center")
    Tree1.column('Olog_station', width=40, anchor="center")
    Tree1.column('Odistributor', width=70, anchor="center")
    Tree1.column('Osender', width=70, anchor="center")
    Tree1.column('Orecipient', width=70, anchor="center")
    Tree1.column('Ogoods', width=70, anchor="center")
    Tree1.column('Oprice', width=40, anchor="center")
 
    Tree1.heading('Onum', text='订单编号')
    Tree1.heading('Odelivery_time', text='运输时间')
    Tree1.heading('Olog_station', text='物流站')
    Tree1.heading('Odistributor', text='快递员')
    Tree1.heading('Osender', text='寄件人')
    Tree1.heading('Orecipient', text='收件人')
    Tree1.heading('Ogoods', text='商品')
    Tree1.heading('Oprice', text='价格')
 
    Tree1.place(rely=0.5, relwidth=1)
 
    Button(root1, text="根据编号查找",activebackground='gray',font=('楷体',13), command=lambda:findInfo(check=1, tree=Tree1, list=list1) ).place(relx=0.15, rely=0.17, width=150)
    Button(root1, text="查询所有订单",activebackground='gray',font=('楷体',13), command=lambda: showAllInfo(tree=Tree1)).place(relx=0.15, rely=0.10, width=150)
    Button(root1, text="增加订单", activebackground='gray',font=('楷体',13), command=lambda: appendInfo(tree=Tree1,  list=list1)).place(relx=0.15, rely=0.24, width=150)
    Button(root1, text="删除订单", activebackground='gray',font=('楷体',13), command=lambda: deleteInfo(tree=Tree1)).place(relx=0.15, rely=0.31, width=150)
    Button(root1, text="更改订单信息", activebackground='gray',font=('楷体',13), command=lambda: updateInfo(tree=Tree1, list=list1)).place(relx=0.15, rely=0.38, width=150)
 
    def treeviewClick(event):
        item = Tree1.selection()[0]
        item_text = Tree1.item(item, "values")
 
        entry_Onum.delete(0, 'end')
        entry_Odelivery_time.delete(0, 'end')
        entry_Olog_station.delete(0, 'end')
        entry_Odistributor.delete(0, 'end')
        entry_Osender.delete(0, 'end')
        entry_Orecipient.delete(0, 'end')
        entry_Ogoods.delete(0, 'end')
        entry_Oprice.delete(0, 'end')
 
        entry_Onum.insert(0, item_text[0])
        entry_Odelivery_time.insert(0, item_text[1])
        entry_Olog_station.insert(0, item_text[2])
        entry_Odistributor.insert(0, item_text[3])
        entry_Osender.insert(0, item_text[4])
        entry_Orecipient.insert(0, item_text[5])
        entry_Ogoods.insert(0, item_text[6])
        entry_Oprice.insert(0, item_text[7])
 
    Tree1.bind('<ButtonRelease-1>', treeviewClick)
    root1.protocol('WM_DELETE_WINDOW', lambda:MangerChoosePage(root1))
    root1.mainloop()
#(7.1)
def showAllInfo(tree):
    delButton(tree)
    db = pymysql.connect(host="ip", user="root",password="pwd", db="db", port=3306)
    cur = db.cursor() #用db操作游标
    cur.execute("select * from orders")
 
    results = cur.fetchall()
    for item in results:
        tree.insert('', "end", values=item)
    cur.close()
    db.close()  # 关闭连接
#(7.2)
def appendInfo(tree,list):
    delButton(tree)
    list2 = []
    for i in range(len(list)):
        if list[i].get() == '':
            showerror(title='提示', message='输入不能为空!')
            return
        else:
            list2.append(list[i].get())
 
    x = tree.get_children()
    for item in x:
        tree.delete(item)
 
    db = pymysql.connect(host="ip", user="root",password="pwd", db="db", port=3306)
    cur = db.cursor()
    try:
        cur.execute("insert into orders values('%s','%s','%s','%s','%s','%s','%s','%s')" % (list2[0], list2[1], list2[2], list2[3], list2[4], list2[5], list2[6], list2[7]))
        db.commit()#对数据进行修改、删除、插入时最好都commit一下,跟在execute()后面
        cur.execute("select * from orders")
        results = cur.fetchall()
        for item in results:
            tree.insert('', "end", values=item)
        showinfo(title='提示', message='添加/更新成功！')
    except:
        showinfo(title='提示', message='该编号已存在！')
        return
    cur.close()
    db.close()
#(7.3)
def deleteInfo(tree):
    if not tree.selection():
        showerror(title='提示', message='请选择一条信息！')
        return
    res = askyesno('提示！', '是否确认删除？')
    if res == True:
        for item in tree.selection():
            selectedItem = tree.selection()[0]
            no1 = tree.item(selectedItem, 'values')[0]
            tree.delete(item)
 
            db = pymysql.connect(host="ip", user="root",password="pwd", db="db", port=3306)
            cur = db.cursor()
            cur.execute("delete from orders where Onum = '%s'" % no1)
            db.commit()
 
            cur.close()
            db.close()
            showinfo(title='提示', message='删除成功！')
#(7.4)
def updateInfo(tree, list):
    if not tree.selection():
        showerror(title='提示', message='请选择一条信息！')
        return
    else:
        res=askyesno("提示！","是否确认更新数据？")
        if res==True:
            for item in tree.selection():
                selectedItem = tree.selection()[0]
                no1 = tree.item(selectedItem, 'values')[0]
                tree.delete(item)
 
                db = pymysql.connect(host="ip", user="root",password="pwd", db="db", port=3306)
                cur = db.cursor()
 
                cur.execute("delete from orders where Onum = '%s'" % no1)
                db.commit()
 
                cur.close()
                db.close()
            appendInfo(tree, list)
            return
#(7.5)
def findInfo(check, tree, list):
    if check:
        delButton(tree)
    db = pymysql.connect(host="ip", user="root",password="pwd", db="db", port=3306)
    cur = db.cursor()
    cur.execute("select * from orders where Onum = '%s'" % list[0].get())  # 执行sql语句
    results = cur.fetchall()
    if results:
        for item in results:
            tree.insert('', "end", values=item)
    else:
        showinfo(title='提示', message='无该订单编号！')
    cur.close()
    db.close()
 
image5=None
img5=None
#(8)游客订单信息查询页面
def GuestPage(root):
    global image5
    global img5
    root.destroy()
    root=Tk()
    root.title('游客订单信息查询页面')
    root.geometry('850x730+300+50')
    root['background']='white'
    image5 = Image.open('./image/5.jpg')
    img5 = ImageTk.PhotoImage(image5)
    Label(root,text='游客订单信息查询页面',compound='bottom',image=img5,bg='floralwhite',fg='blue',font=('楷体',20)).pack(side=TOP, fill='x')
    Label(root,text='订单编号：',font=('楷体',13)).place(relx=0.07,rely=0.15,relwidth=0.15)
    Label(root, text='收件人姓名：',font=('楷体',13)).place(relx=0.07, rely=0.25, relwidth=0.15)
    Label(root, text='寄件人姓名：',font=('楷体',13)).place(relx=0.07, rely=0.35, relwidth=0.15)
    Label(root, text='配送时间：',font=('楷体',13)).place(relx=0.07, rely=0.45, relwidth=0.15)
 
    Onum=StringVar()
    Rname=StringVar()
    Sname=StringVar()
    Odeliver_time=StringVar()
 
    entry_Onum = Entry(root, textvariable=Onum)
    entry_Onum.place(relx=0.2, rely=0.15, relwidth=0.3, height=25)
    entry_Rname = Entry(root, textvariable=Rname)
    entry_Rname.place(relx=0.2, rely=0.25, relwidth=0.3, height=25)
    entry_Sname = Entry(root, textvariable=Sname)
    entry_Sname.place(relx=0.2, rely=0.35, relwidth=0.3, height=25)
    entry_Odeliver_time = Entry(root, textvariable=Odeliver_time)
    entry_Odeliver_time.place(relx=0.2, rely=0.45, relwidth=0.3, height=25)
 
 
 
    Tree1 = ttk.Treeview(root, show='headings',column=('Onum', \
        'Odelivery_time', 'Olog_station', 'Odistributor', 'Osender', 'Orecipient', 'Ogoods','Oprice'))
    Tree1.column('Onum', width=50, anchor="center")
    Tree1.column('Odelivery_time', width=80, anchor="center")
    Tree1.column('Olog_station', width=40, anchor="center")
    Tree1.column('Odistributor', width=70, anchor="center")
    Tree1.column('Osender', width=70, anchor="center")
    Tree1.column('Orecipient', width=70, anchor="center")
    Tree1.column('Ogoods', width=70, anchor="center")
    Tree1.column('Oprice', width=40, anchor="center")
    # 表格标题设置
    Tree1.heading('Onum', text='订单编号')
    Tree1.heading('Odelivery_time', text='运输时间')
    Tree1.heading('Olog_station', text='物流站')
    Tree1.heading('Odistributor', text='快递员')
    Tree1.heading('Osender', text='寄件人')
    Tree1.heading('Orecipient', text='收件人')
    Tree1.heading('Ogoods', text='商品')
    Tree1.heading('Oprice', text='价格')
 
    Tree1.place(rely=0.6, relwidth=1)
 
    Button(root, text="按编号查询",bg='gainsboro',fg='black',activebackground='grey',font=('楷体',13), command=lambda:Find_infor_num(Tree1,entry_Onum)).place(relx=0.65, rely=0.15, width=150)
    Button(root, text="按姓名查询",bg='gainsboro',fg='black', activebackground='grey',font=('楷体',13), command=lambda:Find_infor_name(Tree1,entry_Rname,entry_Sname)).place(relx=0.65, rely=0.3, width=150)
    Button(root, text="按时间查询",bg='gainsboro',fg='black', activebackground='grey',font=('楷体',13), command=lambda:Find_infor_time(Tree1,entry_Odeliver_time)).place(relx=0.65, rely=0.45, width=150)
    root.protocol('WM_DELETE_WINDOW', lambda:back(root))
    root.mainloop()
#(8.1)
def Find_infor_num(Tree1,Name):
    delButton(Tree1)
    db = pymysql.connect(host="ip", user="root",password="pwd", db="db", port=3306)
    cur = db.cursor()
 
    cur.execute("select * from orders where Onum = '%s'" % Name.get())
    results = cur.fetchall()  # 获取查询的所有记录
    if results:
        for item in results:
            Tree1.insert('', "end", values=item)
    else:
        showinfo(title='提示', message='无该订单编号！')
 
    cur.close()
    db.close()
#(8.2)
def Find_infor_name(Tree1,Name1,Name2):
    delButton(Tree1)
    db = pymysql.connect(host="ip", user="root",password="pwd", db="db", port=3306)
    cur = db.cursor()
    if Name1.get():
        cur.execute("select * from orders where Orecipient = '%s'" % Name1.get())
        results = cur.fetchall()
        if not results:
            showinfo(title='提示', message='无该收件人！')
        else:
            for item in results:
                Tree1.insert('', "end", values=item)
    if Name2.get():
        cur.execute("select * from orders where Osender = '%s'" % Name2.get())
        results = cur.fetchall()
        if not results:
            showinfo(title='提示', message='无该寄件人！')
        else:
            for item in results:
                Tree1.insert('', "end", values=item)
 
    cur.close()
    db.close()
#(8.3)
def Find_infor_time(Tree1,time):
    delButton(Tree1)
    db = pymysql.connect(host="ip", user="root",password="pwd", db="db", port=3306)
    cur = db.cursor()
    ch='%'+time.get()+'%'
    cur.execute("select * from orders where Odelivery_time like  '%s'" % ch)
    results = cur.fetchall()
    if results:
        for item in results:
            Tree1.insert('', "end", values=item)
    else:
        showinfo(title='提示', message='无该配送日期！')
    cur.close()
    db.close()
 
if __name__=='__main__':
    StartPage()