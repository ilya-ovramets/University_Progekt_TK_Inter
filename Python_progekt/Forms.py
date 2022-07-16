import tkinter as tk
from tkinter import ttk
from tkinter import *
import os
from PIL import ImageTk, Image;

class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()
        self.master.geometry("1170x650")
        self.master.title("Помічник фізика")
        self.master.maxsize(width=1170, height=650)
        self.master.minsize(width=1170, height=650)


        self.create_widgets()

    # Create Widgets function
    def create_widgets(self):
        #Meny
        mainmenu = Menu(self.master)
        self.master.config(menu=mainmenu)

        #Додаю колір в фортаті HEX
        blue = "#219aeb";

        # Створюємо вспливаюче меню із функціями програми
        filemenu = Menu(mainmenu, tearoff=0)
        filemenu.add_command(label="Зберегти записи", command=self.save_text)
        filemenu.add_command(label="Вихід" ,command=self.exiting)

        helpmenu = Menu(mainmenu, tearoff=0)
        helpmenu.add_command(label="Допомога",command=self.help)
        helpmenu.add_command(label="Про програму",command=self.about)

        mainmenu.add_cascade(label="Файл",
                             menu=filemenu)
        mainmenu.add_cascade(label="Справка",
                             menu=helpmenu)


        #TabControl
        self.tab1 = self.master


        #Calculater
        # Frame
        self.formul_frame_calculate = LabelFrame(self.tab1,bg="yellow") #Створюємо окремий фрейм для модуля калькулятора.
        self.formul_frame_calculate.place(x=165)


        # Label1
        self.label_1 = Label(self.formul_frame_calculate,bg="yellow")
        self.label_1.configure(text='В цьому полі можете вести необхідні вам розрахунки',font=("Times New Roman", 10, "bold"))
        self.label_1.pack()

        # Entry
        self.value = tk.StringVar()
        self.entry_value = ttk.Entry(self.formul_frame_calculate)
        self.entry_value.configure(textvariable=self.value, width=40, font=("Times New Roman", 12, "bold"),justify=CENTER)
        self.entry_value.pack()



        # Button для обрахунків.
        self.button_hello = Button(self.formul_frame_calculate,font=("Times New Roman", 12, "bold"))
        self.button_hello.configure(text="Обрахувати",bg = "lime")
        self.button_hello.configure(command=self.calculate)  # Біндимо на кнопку функцію калькулятора.
        self.button_hello.pack()

        # Label  Результати
        self.label_result = Label(self.formul_frame_calculate,bg="yellow")
        self.label_result.config(font=("Times New Roman", 12, "bold"))
        self.label_result.pack()

        # Label
        self.label_6 = Label(self.formul_frame_calculate,bg="yellow")
        self.label_6.config(text="Нижче ви можете робити необхідні вам записи",font=("Times New Roman", 12, "bold"))
        self.label_6.pack()

        # Додаємо текстове поле для записів користувача.
        self.entry_value_save = Text(self.formul_frame_calculate,width=56, height=7, wrap="word")
        self.entry_value_save.pack()

        self.entry_value_save.config(font=("Times New Roman", 11,"bold"))


        # Helper image.
        # Frame
        self.formul_frame = LabelFrame(self.tab1) #Створюю фрейм із розділами фізика
        self.formul_frame.place(x=0, y=0)

        self.formul_frame_image = LabelFrame(self.tab1) #Створюю фрейм для виводу фото.
        self.formul_frame_image.place(x=615)

        # Lable
        self.label_4 = Label(self.formul_frame)
        self.label_4.configure(text="Оберіть розділ фізики", font=("Times New Roman", 12, "bold"),bg = "yellow")
        self.label_4.pack()

        # Список назв розділів.
        formuls = ["Кінематика", "Динаміка", "Закони збереження", "Механіка рідин", "Коливання та хвилі", "Основи МКТ",
                   "Термодинаміка", "Оптика", "Електростатика", "Постійний ток", "Електромагнітні коливання",
                   "Індукція", "Квантова фізика", "Ядерні реакції", "Основи СТО."]

        #ListBox Створюю список із розділами та виводжу на екран.
        self.formul_listbox = Listbox(self.formul_frame,font=("Times New Roman", 11, "bold"))
        for formul in formuls:  #Записую значення в список.
            self.formul_listbox.insert(END, formul)
        self.formul_listbox.pack()

        #Button Кнопка для завантаження фото залежно від обраного розділу.
        self.button_help= Button(self.formul_frame)
        #Бінжу функцію для завантаження.
        self.button_help.configure(text="Отримати підказки",font=("Times New Roman", 12, "bold"),bg = "lime",command=self.loadimage,pady=5)
        self.button_help.pack(fill=BOTH);

        self.photo_formuls = PhotoImage(file=os.getcwd()+'\photo\kin.png')  #Підвантажую стартовий файл.
        self.canvaser= Label(self.formul_frame_image,image=self.photo_formuls,bg = "lime") #Створюю поле для виводу.

        self.LoadImage(); #Виводжу зображення.



        ## Calculater



        #Convert
        #Frame
        self.converter = LabelFrame(self.tab1,bg = blue); #Вставляємо фрейм для обєднання функції конвертатора.
        self.converter.place(x=0,y=250)
        self.radio_buttom_frame_left = Frame(self.converter,bg = blue) #Вставляю фрейм із кнопками ліворуч
        self.radio_buttom_frame_left.pack(side=LEFT)
        self.radio_buttom_frame_right = Frame(self.converter,bg = blue) #Вставляю фрейм із кнопками праворуч
        self.radio_buttom_frame_right.pack(side=RIGHT)

        # Frame
        self.result_convert = Frame(self.converter,bg = blue)   #Вставляю фрейм із результатами
        self.place(x=0, y=675,width=900,height=125)
        self.result_convert.pack()

        #Lable
        self.label_2 = Label(self.radio_buttom_frame_left,bg = blue)
        self.label_2.configure(text="З чого",font=("Times New Roman", 12, "bold"),foreground="purple")
        self.label_2.pack()

        # Entry поле для введення значинь які потрібно конвертувати.
        self.value_convert_str = tk.StringVar()
        self.value_convert = ttk.Entry(self.radio_buttom_frame_left)
        self.value_convert.configure(textvariable=self.value_convert_str, width=30,
                                     font=("Times New Roman", 12, "bold"))
        self.value_convert.pack()

        #Lable
        self.label_3 = Label(self.radio_buttom_frame_right,bg = blue)
        self.label_3.configure(text="В що",font=("Times New Roman", 12, "bold"),foreground="orange")
        self.label_3.pack()

        # Entry поле яке виводить обраховані результати
        self.label_converter_result = ttk.Entry(self.radio_buttom_frame_right, width=30)
        self.label_converter_result.configure(font=("Times New Roman", 12, "bold"))
        self.label_converter_result.pack();


        self.v = StringVar(self.tab1, "1") #Обєкти для збереження значинь Радіобатонів
        self.v2 = StringVar(self.tab1, "1")
        self.diktionary_values = {"Джоуль": (1,"1"), # Словрик велечин
                  "Кілоджоуль": (1000,"1000"),
                  "Грам-калорій": (4.184,"4.184"),
                  "Кілокалорії": (4184,"4184"),
                  "Ват-час": (3600,"3600.0"),
                  "Кіловат-час": (3.6e+6,"3.6e+6"),
                  "Електровольт": (6.242e+18,"6.242e+18"),
                  "Британська теплова одиниця": (1055,"1055"),
                  "Фут-фунт": (1.356,"1.356")}


        # Виводжу 2 вертикальні списки велечин.
        for (text, value) in self.diktionary_values.items():
            Radiobutton(self.radio_buttom_frame_left, text=text, variable=self.v,
                        value=value[0],font=("Times New Roman", 12, "bold"),bg = blue).pack( ipady=5)
        for (text, value) in self.diktionary_values.items():
            Radiobutton(self.radio_buttom_frame_right, text=text, variable=self.v2,
                        value=value[1],font=("Times New Roman", 12, "bold"),bg = blue).pack( ipady=5)

        # Button для конвертації значинь.
        self.button_convert = Button(self.result_convert,bg = "lime",font=("Times New Roman", 12, "bold"),padx=2)
        self.button_convert.configure(text="Конвертувати",command=self.convert) #Бінджу кнопку для конвертації значинь.
        self.button_convert.pack();

        self.CheckVar1 = IntVar(self.tab1)
        self.C1 = Checkbutton(self.result_convert, text="Зберігати\n результати", variable=self.CheckVar1,onvalue=1, offvalue=0,bg = blue)
        self.C1.pack();

        ##Convert
