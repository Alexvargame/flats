import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
from Enter_info import *
from Search_info_class import *
from boolean import *
from Type_object import *
import xlsxwriter
from tkinter.filedialog import askopenfilename, asksaveasfilename
import pickle
from Autorization import *
from Registration import *
from tkinter import messagebox as mb





class main:
   def __init__(self, master):
      self.user = Users("","","","","")
      self.master = master
      self.master.title('DATA')
      self.master.geometry('250x250+300+225')
      self.main_frame = Frame(self.master)
      self.main_frame.pack(expand=1)
      self.admin_frame = Frame(self.master)
      self.admin_frame.pack(expand=1)
      global user_
      self.main_panel()
      self.master.mainloop()
      panel = ""

   def main_panel(self): 
      
      for widget in self.admin_frame.winfo_children():
               widget.destroy()
      
  
      self.button1 = Button(master=self.main_frame,
                            text="Жилые объекты",width=15, height=3,
                            command = self.openDialog)
      self.button1.pack()

      self.button2 = Button(master=self.main_frame, text="Поиск",width=15, height=3,
                            command = self.openSearch)
      self.button2.pack(pady=2)
      
      self.button3 = Button(master=self.main_frame, text="Войти",width=15, height=2, command=self.openAutoriz)
      #self.button3.bind("<Button-1>", self.openAutoriz)                    
      self.button3.pack(pady=2)
      self.button4 = Button(master=self.main_frame, text="Регистрация",width=15, height=2,

                            command = self.openRegistr)
      self.button4.pack()
      """
      try:
         if autorization.user_value(self)=="admin" :
            self.button5 = Button(master=self.main_frame, text="Админ-панель",width=15, height=2,
                           command = self.admin_panel)
            self.button5.pack()
      except:
         pass
      """
      self.master.protocol('WM_DELETE_WINDOW', 
                         self.exitMethod)
      
   
   def admin_button(self):
      if autorization.user_value(self)=="admin" :
         self.button5 = Button(master=self.main_frame, text="Админ-панель",width=15, height=2)
                           #command = self.admin_panel)
         self.button5.pack()

      """
      try:
         if autorization.user_value(self)=="admin" :
            self.master.geometry('250x350+300+225')
            for widget in self.main_frame.winfo_children():
               widget.destroy()
            self.button6 = Button(master=self.admin_frame,
                         text="Admin",width=15, height=3, command=self.main_panel)
            self.button6.pack()
      except:
         pass
      """
   def openDialog(self):
      try:
         if autorization.user_value(self)=="user" or autorization.user_value(self)=="admin" :
            child(self.master)
      except:
         mb.showwarning("","Войдите пол своим аккаунтом или зарегистрируйтесь")

   def openReport(self):
      self.report = child_report(self.master)
      with open('1.txt', 'r') as output_file:
           self.t = output_file.read() 
           self.returnText = self.report.go(self.t)
   def openAutoriz(self):
      autorization(self.master, self.user)
      
      print('1',autorization.autoriz(self))
      
            
      

   def openRegistr(self):
      registration(self.master)
      
              
   def openSearch(self):
      try:
         if autorization.return_user(self).accept=="user":# or autorization.user_value(self)=="admin" :
            child_search(self.master)   
      except:
         mb.showwarning("","Войдите пол своим аккаунтом или зарегистрируйтесь")
    

   def exitMethod(self):
    self.dialog = yesno(self.master)
    self.returnValue = self.dialog.go('question',
                                      'Вы хотите выйти?')
    if self.returnValue:
      self.master.destroy()
      

        



root = Tk()
main(root)
      
    
