from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox


class Enter_menu():
    def __init__(self):
        self.name = ''
        self.enter_window = Tk()
        self.enter_window.title('Speedtest')
        self.enter_window.geometry('350x210+785+425')
        self.enter_window.configure(bg='#55c5ff')
        self.enter_window.iconphoto(True, PhotoImage(file='images/icon.png'))
        self.enter_window.resizable(width=0, height=0)

        self.enter_label1 = Label(self.enter_window,
                                  text='Как я могу вас называть?',
                                  font='Arial 16',
                                  fg='#fff',
                                  bg='#32a9f9')
        self.enter_label1.pack(pady=15, ipady=10, fill=BOTH)

        self.enter_entry = Entry(self.enter_window,
                                 text='Введите имя',
                                 font='Arial 16',
                                 fg='#000',
                                 justify=CENTER)
        self.enter_entry.pack(padx=30, ipady=3, fill=BOTH)
        self.enter_entry.focus()

        self.enter_label2 = Label(self.enter_window,
                                  text='Имя должно быть от 3 до 12 символов',
                                  font='Arial 14',
                                  fg='red',
                                  bg='#55c5ff')

        self.enter_button = Button(self.enter_window,
                                   command=self.CheckName,
                                   text='Начать!',
                                   justify=CENTER,
                                   bg='#ffe319',
                                   fg='#0e50a1',
                                   font='Arial 14')
        self.enter_button.pack(pady=10)

        self.check_var = IntVar()
        self.check_box = Checkbutton(self.enter_window,
                                     text='Запомнить?',
                                     variable=self.check_var)
        self.check_box.pack()

        self.enter_window.mainloop()


    def CheckName(self):
        self.name = self.enter_entry.get()
        if len(self.name) >= 3 and len(self.name) <= 12:
            if self.check_var.get() == 1:
                with open('save\\saves.txt', 'w') as f:
                    f.write(self.name)
            with open('save\\current_log.txt', 'w') as f:
                f.write(self.name)
            self.enter_window.destroy()
        else:
            self.enter_button.pack_forget()
            self.enter_label2.pack()
            self.enter_button.pack()

