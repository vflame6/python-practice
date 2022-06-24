from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
from random import randint
import time


class GameMenu():
    def __init__(self, name):
        self.name = name
        self.initial_gamemode = self.current_gamemode = 0
        self.initial_light_mode = self.current_light_mode = False


    def OpenMenu(self):
        self.Game_window = Tk()
        self.Game_window.title('Speedtest')
        self.Game_window.geometry('1280x760+320+160')
        self.Game_window.configure(bg='#55c5ff')
        self.Game_window.iconphoto(True, PhotoImage(file='images/icon.png'))
        self.Game_window.resizable(width=0, height=0)

        # Header
        self.menu_frame = Frame(self.Game_window,
                                bg='#32a9f9',
                                height=75)
        self.menu_frame.pack(fill=BOTH, padx=150, pady=20)

        self.home_button_image0 = PhotoImage(file="images/homeicon0.png")
        self.home_button_image1 = PhotoImage(file="images/homeicon1.png")
        self.home_button = Button(self.menu_frame,
                                  image=self.home_button_image0,
                                  height=60,
                                  width=130,
                                  relief='flat',
                                  command=self.home_button_click)
        self.home_button.pack(side=LEFT, padx=10, pady=10)

        self.home_button_leave = Button(self.menu_frame,
                                        text='Выйти',
                                        command=self.leave_save,
                                        bg='#32a9f9',
                                        fg='#fff',
                                        relief='flat',
                                        font='Arial 17 underline')
        self.home_button_leave.pack(side=RIGHT, padx=10)

        self.textname = 'Здравствуй, ' + str(self.name) + '!'
        self.nickname = Label(self.menu_frame,
                              text=self.textname,
                              font='Arial 17 underline',
                              bg='#32a9f9',
                              fg='#fff',
                              justify=CENTER)
        self.nickname.pack(side=RIGHT, padx=10)

        self.light_button_image0 = PhotoImage(file='images/light0.png')
        self.light_button_image1 = PhotoImage(file='images/light1.png')
        self.light_button = Button(self.menu_frame,
                                   image=self.light_button_image0,
                                   relief='flat',
                                   command=self.change_light)
        self.light_button.pack(side=RIGHT)

        # 0 - Menu
        self.start_menu_frame = Frame(self.Game_window,
                                      bg='#fff'
                                      )
        self.start_menu_frame.pack(fill=BOTH, pady=40, padx=148)

        self.start_menu_frame_label = Label(self.start_menu_frame,
                                            fg='#000',
                                            font='Arial 18',
                                            text='Добро пожаловать в тренажер!\nВыбери уровень и начинай!')
        self.start_menu_frame_label.pack(pady=15, padx=80)

        self.start_menu_frame_combobox = Combobox(self.start_menu_frame,
                                                  width=22,
                                                  font='Arial 16',
                                                  state='readonly',
                                                  values=('1 - Easy', '2 - Medium', '3 - Hard', '4 - Very hard'))
        self.start_menu_frame_combobox.current(0)
        self.start_menu_frame_combobox.pack()

        self.start_menu_frame_button0 = Button(self.start_menu_frame,
                                               command=self.play_game,
                                               text='Начать игру!',
                                               justify=CENTER,
                                               bg='#ffe319',
                                               fg='#0e50a1',
                                               font='Arial 14')
        self.start_menu_frame_button0.pack(ipadx=80, pady=20)

        self.start_menu_frame_button1 = Button(self.start_menu_frame,
                                               command=self.get_help,
                                               text='Справка',
                                               justify=CENTER,
                                               bg='#ffe319',
                                               fg='#0e50a1',
                                               font='Arial 14')
        self.start_menu_frame_button1.pack(ipadx=100)

        self.start_menu_frame_button2 = Button(self.start_menu_frame,
                                               command=self.leave,
                                               text='Выход',
                                               justify=CENTER,
                                               bg='#ffe319',
                                               fg='#0e50a1',
                                               font='Arial 14')
        self.start_menu_frame_button2.pack(pady=20, ipadx=108)


        self.keyboardphoto = PhotoImage(file='images/keyboard1.png')
        self.keyboardphoto_label = Label(self.start_menu_frame,
                                         image=self.keyboardphoto)

        # main
        self.Game_window.mainloop()

    # leave_button
    def leave(self):
        self.Game_window.destroy()


    # leave_save_button
    def leave_save(self):
        with open('save\\saves.txt', 'w') as f:
            f.write('')
            f.close()
        self.Game_window.destroy()


    # button_light_change
    def change_light(self):
        if self.current_light_mode == self.initial_light_mode:
            self.Game_window.configure(bg='#433394')
            self.menu_frame.configure(bg='#22117b')
            self.nickname.configure(bg='#22117b')
            self.home_button_leave.configure(bg='#22117b')
            self.light_button.configure(image=self.light_button_image1)
            self.home_button.configure(image=self.home_button_image1)
            self.current_light_mode = True
        else:
            self.Game_window.configure(bg='#55c5ff')
            self.menu_frame.configure(bg='#32a9f9')
            self.nickname.configure(bg='#32a9f9')
            self.home_button_leave.configure(bg='#32a9f9')
            self.light_button.configure(image=self.light_button_image0)
            self.home_button.configure(image=self.home_button_image0)
            self.current_light_mode = False


    # Homebutton
    def home_button_click(self):
        # From Game
        if self.current_gamemode == 1:
            self.close_game_menu()
        # From Help
        elif self.current_gamemode == 2:
            self.close_help()


    # 2 - Help
    def get_help(self):
        self.get_help_text = Label(self.start_menu_frame,
                                   text='Сиди ровно и держи спину прямой.\nЛокти держи согнутыми под прямым углом.\nГолова должна быть немного наклонена вперед.\nРасстояние от глаз до экрана должно быть 45-70 см.\nРасслабь мышцы плеч, рук и кистей.\nКисти могут немного касаться стола в нижней части клавиатуры,\nно не переноси вес тела на руки, чтобы не перенапрягать кисти.',
                                   font='Arial 16',
                                   justify=LEFT)


        self.start_menu_frame_label.pack_forget()
        self.start_menu_frame_combobox.pack_forget()
        self.start_menu_frame_button0.pack_forget()
        self.start_menu_frame_button1.pack_forget()
        self.start_menu_frame_button2.pack_forget()
        self.get_help_text.pack(fill=BOTH, pady=10)
        self.keyboardphoto_label.pack(pady=10)
        self.current_gamemode = 2


    def close_help(self):
        self.get_help_text.pack_forget()
        self.keyboardphoto_label.pack_forget()
        self.start_menu_frame_label.pack(pady=15, padx=80)
        self.start_menu_frame_combobox.pack()
        self.start_menu_frame_button0.pack(ipadx=80, pady=20)
        self.start_menu_frame_button1.pack(ipadx=100)
        self.start_menu_frame_button2.pack(pady=20, ipadx=108)
        self.current_gamemode = 0


    # 1 - Game
    def play_game(self):
        self.current_gamemode = 1
        self.start_game_time = time.time()
        self.open_game_menu()
        self.current_level = self.get_level_text(self.start_menu_frame_combobox.get())
        self.Game_window.bind("<Key>", self.hit)


    def hit(self, event):
        pressed_key = event.char.upper()
        if self.game_window_label_text['text'][0] == pressed_key:
            self.game_window_label_text['text'] = self.game_window_label_text['text'][1:]
            self.Game_window.update()
        else:
            current_errs = int(self.game_window_label['text'].split()[0]) + 1
            self.game_window_label['text'] = str(current_errs) + ' Ошибок'
            self.Game_window.update()

        if self.game_window_label_text['text'] == '':
            self.win()
            self.close_game_menu()


    def win(self):
        gameT = time.time() - self.start_game_time
        typespeeD = str(int(self.current_level / gameT * 60))
        gameT = str(gameT)[:4]
        wrongS = self.game_window_label['text'].split()[0]
        result = messagebox.showinfo(title='Результат:',
                                     message='Умничка!\nВаши показатели:\n Скорость: ' + typespeeD + ' символов в минуту!\nОшибок: ' + wrongS + '!\nОбщее время: ' + gameT + ' секунд.')


    def get_level_text(self, level):
        alphabet = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        LEVELS = {'1 - Easy': 10, '2 - Medium': 15, '3 - Hard': 20, '4 - Very hard': 25}
        current_level = LEVELS.get(level)
        current_text = list()

        for i in range(0, current_level):
            current_text.append(alphabet[randint(0, 35)])

        self.game_window_label_text['text'] = ''.join(current_text)

        return current_level


    def open_game_menu(self):
        self.game_window_label = Label(self.start_menu_frame,
                                       font='Arial 30',
                                       text=str(0) + ' Ошибок',
                                       bg='#ffe319',
                                       fg='#32a9f9',
                                       justify=CENTER)


        self.game_window_label_text = Label(self.start_menu_frame,
                                            font='Arial 30',
                                            text='',
                                            bg='#ffe319',
                                            fg='#32a9f9',
                                            justify=LEFT)

        self.start_menu_frame_label.pack_forget()
        self.start_menu_frame_combobox.pack_forget()
        self.start_menu_frame_button0.pack_forget()
        self.start_menu_frame_button1.pack_forget()
        self.start_menu_frame_button2.pack_forget()

        self.game_window_label.pack(fill=BOTH, padx=100, pady=20, ipady=2)
        self.game_window_label_text.pack(fill=BOTH, padx=100)
        self.keyboardphoto_label.pack(pady=10)


    def close_game_menu(self):
        self.start_menu_frame.update()
        self.game_window_label.pack_forget()
        self.game_window_label_text.pack_forget()
        self.keyboardphoto_label.pack_forget()
        self.game_window_label_text['text'] = ''
        self.game_window_label['text'] = str(0) + ' Ошибок'

        self.start_menu_frame_label.pack(pady=15, padx=80)
        self.start_menu_frame_combobox.pack()
        self.start_menu_frame_button0.pack(ipadx=80, pady=20)
        self.start_menu_frame_button1.pack(ipadx=100)
        self.start_menu_frame_button2.pack(pady=20, ipadx=108)
        self.current_gamemode = 0

        self.Game_window.unbind("<Key>")
