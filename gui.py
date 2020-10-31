'''Laguage traslation app'''

from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
from googletrans import Translator, LANGUAGES
import mysql.connector

#create or load database


class MyTranslator:
    
    def run(self,txt='TYPE TEXT HERE',src='english',dest='hindi'):
            self.translator= Translator()
            self.txt=txt
            self.src=src
            self.dest=dest
            try:
                self.translated=self.translator.translate(self.txt,src=self.src,dest=self.dest)
            except:
                self.translated=self.translator.translate(self.txt)
            self.ttext=self.translated.text
            return self.ttext

class home:
    'class that builds the main window for language translator '
    
    def __init__(self):
        #initializing all properties of the main window, colors, logo, size and title
        self.DLstate=0
        self.core = Tk()
        self.bg = '#1d2029' 
        self.mg = '#2a2e3b' #widgets such as frames or text area will use this color
        self.fg = 'white'   #this will be used for font colors
        #self.logo = PhotoImage(file = 'logo.ico') 
        self.core.iconbitmap('logo.ico')
        self.core.title('Langauage Translator')
        self.core.geometry('500x700')
        #DLstate is Dark or Light mode, 0 is Darkmode, 1 is lightmode
        if self.DLstate==0:
            self.core.config(bg=self.bg)
        #function to toggle D/L modes
    def dark_light_mode(self):
        self.DLstate+=1
        if self.DLstate%2==1:
            self.bg='#a9abb0'
            self.mg='lightgray'
            self.fg='#111'
            self.core.config(bg=self.bg)

        else:
            self.bg = '#1d2029'
            self.mg = '#2a2e3b'
            self.fg = 'white'
            self.core.config(bg=self.bg)
            
    def run(self):
        self.core.mainloop()

class button_:
    def __init__(self,master,image,action,h,w,alt=None):
        '''this class will define a button, the tkinter widget "Button" is used
        This class uses a widget object as master, enter image path in and alternative image in alt
        Alternative image will be used when Dark or light modes change'''
        self.master = master
        self.h,self.w=h,w
        self.image = image
        self.alt = alt
        self.action = action
        #call a function to turn our image into a button
        self.imagebtn(self.image,h,w)
        #if no alt image is provided then alt is set to text(image path)
        if alt==None:
            self.alt = self.image
        #function to display the button using GRID, buttons can still be displayed using place and pack, use: objectname.btn.pack()
    def show(self,r,c):
        self.btn['bg']=self.master.bg
        self.btn['activebackground']=self.master.bg
        self.btn.grid(row=r,column=c,padx=5,pady=5)
        #function to change button color or image according to the mode D or L
    def updatecolors(self):
        #image is swapped for alt image and displayed
        self.img = Image.open(self.alt)
        self.alt,self.image=self.image,self.alt
        self.img = self.img.resize((self.w,self.h), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(self.img)
        self.btn['image'] = self.img
        self.btn['bg'] = self.master.bg
        self.btn['activebackground']=self.master.bg
        #function to create an image button
    def imagebtn(self,image,h,w):
        self.img = Image.open(image)
        self.img = self.img.resize((w,h), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(self.img)
        self.btn = Button(self.master.core,image=self.img, bg=self.master.bg, height=h, width=w)
        self.btn['command'] = lambda: self.action()
        self.btn['borderwidth']=0
        self.btn['activebackground']=self.master.bg
        self.btn['padx']=0
        self.btn['pady']=0
        
class frame_:
    '''creates a stylized frame using the tkinter frame widget
    initialize with master, width, height, text(title)'''
    def __init__(self,master, w, h,text=''):
        self.master = master
        self.core = LabelFrame(master.core,height=h,width=w,text=text,font=("Calibri",10))
        #inherits the parent/master's colors
        self.core['background']=self.master.mg
        self.core['foreground']=self.master.fg
        self.core['relief']='flat'
        self.bg = self.master.mg
        self.fg = self.master.fg
        self.mg = self.bg
    def show(self, r, c,):
        self.core.grid(row=r,column=c,sticky='nsew',padx=10,pady=5)
        
    def updatecolors(self):
        self.core['background']=self.master.mg
        self.core['foreground']=self.master.fg
        self.bg = self.master.mg
        self.fg = self.master.fg
        self.mg = self.master.mg
        #function that returns the actual tkinter widget instead of our class instance      
    def asmaster(self):
        return self.core


    #functoin to initiate the color changes for all widgets when dark or light mode toggles
       
class text_:
    '''creates a stylized text input widget using the tkinter Text widget
    initalize with master, width, height and font'''
    def __init__(self,master,width,height,font):
        self.master = master
        self.core = Text(master.core,width=width,height=height,font=font,wrap=WORD)
        self.core['bg'] = self.master.bg
        self.core['fg'] = self.master.fg
        self.core['relief'] = 'flat'
    def show(self,r,c):
        self.core.grid(row=r,column=c)
    def updatecolors(self):
        self.core['bg'] = self.master.bg
        self.core['fg'] = self.master.fg
        
class label_:
    '''creates a stylized Label widget using the tkinter label widget
    initalize with master, text and font'''
    def __init__(self,master,text,font):
        self.master = master
        self.core = Label(master.core,text=text,font=font)
        self.core['bg'] = self.master.mg
        self.core['fg'] = self.master.fg
        self.core['relief'] = 'flat'
    def show(self,r,c):
        self.core.grid(row=r,column=c)
    def updatecolors(self):
        self.core['bg'] = self.master.bg
        self.core['fg'] = self.master.fg    

class dropdown:
    ''''creates a dropdown selection box, using tkinter combobox widget
    initialize with master, values for dropdown options, width, and default values in "sett"'''
    def __init__(self,master,values,width,sett):
        self.style = ttk.Style()
        self.master = master
        self.style.configure('TCombobox',font=('Arial', 22))
        self.style.configure('TCombobox',foreground = '#1d2029')
        self.style.configure('TCombobox',padding=5)
        self.core = ttk.Combobox(master.core,values=values,width=width,style='TCombobox')
        self.core.set(sett)
    def show(self,r,c):
        self.core.grid(row=r,column=c)

def DBconnect():
    try:
        db = mysql.connector.connect(host='localhost', username='root', passwd = 'YOURROOTPASS', database='Transhistory')
    except mysql.connector.ProgrammingError:
        db = mysql.connector.connect(host='localhost', username='root', passwd = 'YOURROOTPASS')
        cur = db.cursor()
        cur.execute('create database TransHistory')
        cur.execute('show databases')
        for i in cur:
            print(i[0])
        db = mysql.connector.connect(host='localhost', username='root', passwd = 'YOURROOTPASS', database='Transhistory')
        cur = db.cursor()
        cur.execute('create table history (ID int auto_increment primary key,source_lang varchar(20),source_input text, destination_lang varchar(20), destination_output text)')
        cur.execute('show tables')
        for i in cur:
            print(i[0])
        cur.close()

def get():
    'this function fetches the users inputs for language options and checks if the languages are available'

    TranslatedText.core['foreground'] = TranslatedText.master.fg
    TranslatedText.core['font'] = ('arial italic',17)
    TranslatedText.core['width']=36
    TranslatedText.core['height']=7

    langs=list(LANGUAGES.values())
    s=srcLanguages.core.get() 
    d=destLanguages.core.get()
    #check if both languages exist
    if s in langs and d in langs:  
        message=SourceIn.core.get(1.0,END)
        translator=MyTranslator()
        text=translator.run(txt=message,src=s,dest=d)
        TranslatedText.core.delete(1.0,END)
        TranslatedText.core.insert(END,text)
        makehistory(s,message,d,text)
    #check if source language exists
    elif s not in langs:
        TranslatedText.core.delete(1.0,END)
        TranslatedText.core['foreground'] = 'tomato'
        TranslatedText.core['font'] = ('arial italic',14)
        TranslatedText.core.insert(END,'Sourse Language not found')
    #check if destination language exist
    elif d not in langs:
        TranslatedText.core.delete(1.0,END)
        TranslatedText.core['foreground'] = 'tomato'
        TranslatedText.core['font'] = ('arial italic',14)
        TranslatedText.core.insert(END,'Destination Language not found')

def colorupdates():
    inputarea.updatecolors()
    outputarea.updatecolors()
    actionsarea.updatecolors()
    DL.updatecolors()
    SourceIn.updatecolors()
    TranslatedText.updatecolors()
    TranslateBtn.updatecolors()
    histbtn.updatecolors()

def makehistory(SourceL,SourceIn,DestL,DestOut):
    s,si,d,do = SourceL,SourceIn,DestL,DestOut
    db = mysql.connector.connect(host='localhost', username='root', passwd = 'YOURROOTPASS', database='Transhistory')
    cur = db.cursor()
    sql = "insert into history (source_lang, source_input, destination_lang, destination_output) values(%s,%s,%s,%s)"
    values = [s,si,d,do]
    cur.execute(sql,values)
    db.commit()
    cur.close()

def gethistory():
    db = mysql.connector.connect(host='localhost', username='root', passwd = 'YOURROOTPASS', database='Transhistory')
    cur = db.cursor()
    sql = "select * from history order by id desc limit 5"
    cur.execute(sql)
    records = cur.fetchall()
    print("Total rows are:  ", len(records))
    print("Printing each row")
    TranslatedText.core.delete(1.0,END)
    TranslatedText.core['font'] = ('arial',10)
    TranslatedText.core['width']=65
    TranslatedText.core['height']=12
    for row in records:
        line1 = str(row[1])+": "+str(row[2])+""
        line2 = str(row[3])+": "+str(row[4])+"\n"
        TranslatedText.core.insert(END,line1)
        TranslatedText.core.insert(END,line2)
    cur.close()
    
################################################__end-of-definitions__#####################################################

#start the main window
DBconnect()
window = home()

#set up all frames 1. for the caption/Title 2. for the text input 3. for the lang options and translate button, 4. for output
captionarea = frame_(window,470,100,'')
captionarea.bg = captionarea.core['background'] = '#3455a9'
captionarea.show(0,0)
inputarea = frame_(window,470,200,'Type your message')
inputarea.show(2,0)
actionsarea = frame_(window,470,70,'Options')
actionsarea.show(3,0)
outputarea = frame_(window,470,200,'Translation')
outputarea.show(4,0)

#display the darkmode/lightmode button
DL = button_(captionarea,'dark.png', lambda: [window.dark_light_mode(),colorupdates()],30,50,'light.png')
DL.btn.place(x=5,y=5)

#diplay the app title
googlelabel = label_(captionarea,'Language Translator',('Arial',30))
googlelabel.core['bg'] = '#3455a9'
googlelabel.core['fg'] = 'white'
googlelabel.core.place(x=50,y=35)

#display the source text area
SourceIn = text_(inputarea, font=('Arial',17),height=7, width=36)
SourceIn.show(0,0)

#get all the languages
langs=list(LANGUAGES.values())

#configure and display the source language dropdown
srcLanguages=dropdown(actionsarea,values=langs,width=15,sett='english')
srcLanguages.core.place(x=20,y=5)

#configure and display the destination language dropdown
destLanguages=dropdown(actionsarea,values=langs,width=15,sett='hindi')
destLanguages.core.place(x=335,y=5)

#configure the text output area for the translated text
TranslatedText = text_(outputarea, font=('Arial bold italic',17),height=7, width=36)
TranslatedText.core.place(x=0,y=0)

#configure the translate button
TranslateBtn = button_(actionsarea,'translate.png',lambda: get(), 35,110)
TranslateBtn.btn.place(x=180,y=0)

#configure a history button
histbtn = button_(outputarea,'eye.png', lambda:gethistory(),35,35)
histbtn.btn.place(x=425,y=0)

#run the window
window.run()
