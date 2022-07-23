from tkinter import*
from tkinter import font
import qrcode
class Qr_Generator:
    def __init__(self, root):
        
        self.root=root
        self.root.geometry("900x600+200+50")
        self.root.title("Qr Generator | Developed by Group11")
        self.root.resizable(False,False) # Window cannot be maximised
        #--------------------------------------------------------------------
        title=Label(self.root, text="Qr Code Generator", font=("times new roman", 40), bg='#053246', fg='white').place(x=0,y=0,relwidth=1) #-----> Title of the project

        #--------------------------------------------------------------------


        self.var_emp_code=StringVar()
        self.var_name=StringVar()
        self.var_branch=StringVar()
        self.var_year=StringVar()
        self.var_type=StringVar()
        self.var_period=StringVar()
        self.var_company=StringVar()
        emp_Frame=Frame(self.root, bd=2, relief=RIDGE)
        emp_Frame.place(x=25,y=100,width=500,height=400) #-----> Detail Box design
     
        emp_title=Label(emp_Frame, text="Student Details", font=("goudy old style",30),bg='#053246', fg='white').place(x=0,y=0,relwidth=1)
        #--------------------------------------------------------------------
        # Student Info Section
       
        lbl_emp_code=Label(emp_Frame, text="Roll No.", font=("times new roman", 15, 'bold')).place(x=0,y=80)
        lbl_name=Label(emp_Frame, text="Name", font=("times new roman", 15, 'bold')).place(x=0,y=110)
        lbl_branch=Label(emp_Frame, text="Branch", font=("times new roman", 15, 'bold')).place(x=0,y=140)
        lbl_year=Label(emp_Frame, text="Year and Semester", font=("times new roman", 15, 'bold')).place(x=0,y=170)
        lbl_type=Label(emp_Frame, text="Type of Internship", font=("times new roman", 15, 'bold')).place(x=0,y=200)
        lbl_period=Label(emp_Frame, text="Intership Period", font=("times new roman", 15, 'bold')).place(x=0,y=230)
        lbl_company=Label(emp_Frame, text="Company Name", font=("times new roman", 15, 'bold')).place(x=0,y=260)

        txt_emp_code=Entry(emp_Frame, font=("times new roman", 15, 'bold'),textvariable=self.var_emp_code).place(x=250,y=80)
        txt_name=Entry(emp_Frame, font=("times new roman", 15, 'bold'),textvariable=self.var_name).place(x=250,y=110)
        txt_branch=Entry(emp_Frame, font=("times new roman", 15, 'bold'),textvariable=self.var_branch).place(x=250,y=140)
        txt_year=Entry(emp_Frame, font=("times new roman", 15, 'bold'),textvariable=self.var_year).place(x=250,y=170)
        txt_type=Entry(emp_Frame, font=("times new roman", 15, 'bold'),textvariable=self.var_type).place(x=250,y=200)
        txt_period=Entry(emp_Frame, font=("times new roman", 15, 'bold'),textvariable=self.var_period).place(x=250,y=230)
        txt_company=Entry(emp_Frame, font=("times new roman", 15, 'bold'),textvariable=self.var_company).place(x=250,y=260)
        
        btn_generate=Button(emp_Frame,text='QR Generator',command=self.generate,font=("times new roman",18,'bold'),bg='#2196f3',fg='white').place(x=90,y=320,width=200,height=30)
        btn_clear=Button(emp_Frame,text='Clear',command=self.clear,font=("times new roman",18,'bold'),bg='#607d8b',fg='white').place(x=325,y=320,width=130,height=30)
        self.msg=''

        self.lbl_msg=Label(emp_Frame,text=self.msg,font=("times new roman", 14, 'bold'),bg='white',fg='green')
        self.lbl_msg.place(x=0,y=360,relwidth=1)
         #Employee QR Code Window
         #variable
        qr_Frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        qr_Frame.place(x=600,y=100,width=250,height=380)

        emp_title=Label(qr_Frame,text="Student QR Code",font=("goudy old style",20),bg='#043256',fg='white').place(x=0, y=0, relwidth=1)

        self.qr_code=Label(qr_Frame,text='No Qr\nAvailable',font=('times new roman',15),bg='#3f51bf',fg='white',bd=1,relief=RIDGE)
        self.qr_code.place(x=35,y=100,width=180,height=180)

    def clear(self):
        
        self.var_emp_code.set('')
        self.var_name.set('')
        self.var_branch.set('')
        self.var_year.set('')
        self.var_type.set('')
        self.var_period.set('')
        self.var_company.set('')
        self.msg=''
        self.lbl_msg.config(text=self.msg)

    def generate(self):
        if self.var_company.get()=='' or self.var_branch.get()=='' or self.var_emp_code.get()=='' or self.var_name.get()=='' or self.var_period.get()=='' or self.var_type.get()=='' or self.var_year.get()=='':
            self.msg='All fields are required'
            self.lbl_msg.config(text=self.msg,fg='red')
        else:
             self.msg='QR code Generated succesfully'
             self.lbl_msg.config(text=self.msg,fg='green')    
        




root=Tk()
obj = Qr_Generator(root)
root.mainloop()

       


