import tkinter as tk
from tkinter import messagebox, RIGHT
from Forms import Application;
import os;
from tkinter.filedialog import asksaveasfile, askopenfile
from tkinter.messagebox import showerror


class Form1(Application):

    # Event Callback Function
    def calculate(self):
        work_string = self.value.get();  #Считую введені данні
        work_string = self.clear_space(work_string);  #Очищую їх від мусору
        self.value.set(work_string);
        if(work_string == ""):
            return ;
        lister = [];
        sumbul_list = ["^", "/", "*", "-", "+"] #Список операторів
        i = 0;
        start = 0;
        while i < len(work_string):  #Розділяю отримані данні на числа та операторию.
            if (work_string[i] in sumbul_list):
                lister.append(work_string[start:i])
                lister.append(work_string[i])
                start = i + 1;
            if (i == len(work_string) - 1):
                lister.append(work_string[start:i + 1])
            i += 1;
        i = 2;
        sumbul = 0;
        while i < len(lister): #Виконую необхідні дії над введеними числами
            if (lister[i - 1] == sumbul_list[sumbul]):
                match lister[i - 1]:
                    case "^":
                        result = (float(lister[i - 2]) ** float(lister[i]));
                        lister[i - 1] = result;
                        lister.pop(i)
                        lister.pop(i - 2)
                    case "/":
                        result = (float(lister[i - 2]) / float(lister[i]));
                        lister[i - 1] = result;
                        lister.pop(i)
                        lister.pop(i - 2)
                    case "*":
                        result = (float(lister[i - 2]) * float(lister[i]));
                        lister[i - 1] = result;
                        lister.pop(i)
                        lister.pop(i - 2)
                    case "-":
                        result = (float(lister[i - 2]) - float(lister[i]));
                        lister[i - 1] = result;
                        lister.pop(i)
                        lister.pop(i - 2)
                    case "+":
                        result = (float(lister[i - 2]) + float(lister[i]));
                        lister[i - 1] = result;
                        lister.pop(i)
                        lister.pop(i - 2)
            if (len(lister) == 1):
                break;
            if (i + 2 > len(lister) - 1): #Поченаю спочатку беручи наступний по порядку знак.
                sumbul += 1;
                i = 0;
            if (sumbul == len(sumbul_list)):
                sumbul = 0;
            i += 2;
        self.label_result.configure(text=lister[0]);

    def clear_space(self,text): #Очищую данні від непотрібних значень.
        sumbul_list = ["^", "/", "*", "-", "+", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9","."] #Список можливих значень.
        i = 0;
        while i < len(text):
            if(text[i] == "," and text[i-1] in sumbul_list and text[i+1] in sumbul_list): #Замінюю коми між числами на точки
                text = text.replace(text[i], ".")
            if (text[i] not in sumbul_list):
                text = text.replace(text[i], ""); #Прибираю непотрібні числа.
                i -= 1;
            i += 1
        return text;

    def loadimage(self): #Завантаження данних для фото.
        formuls = ["/photo/kin.png","/photo/dino.png","/photo/save.png","/photo/vater.png",
                   "/photo/va.png","/photo/MKT.png","/photo/term.png","/photo/optik.png",
                   "/photo/statik.png","/photo/tok.png","/photo/omg.png","/photo/ind.png",
                   "/photo/kva.png","/photo/yad.png","/photo/STO.png"]

        self.photo_formuls = tk.PhotoImage(file=os.getcwd() + formuls[self.formul_listbox.curselection()[0]])
        self.LoadImage();

    def convert(self): #Конвертує певні велечини.
        from_ = self.v.get();  #Збираю данні із програми
        to_ = self.v2.get();
        count = self.value_convert.get();
        count = self.clear_space(count);
        result = (float(count)*float(from_[0]))
        result = result/float(to_)  #Виконую дії для конвертування
        text_ = f"{result}"
        if(self.CheckVar1.get() == 1): #Записую значення в блокнот при нажатому чек боксі.
            data = f"{count}=>{result}\n"
            self.entry_value_save.insert(1.0,data)
        self.label_converter_result.delete(0, 'end')
        self.label_converter_result.insert(0,text_)

    def exiting(self): #Виходить з програми
        exit();

    def LoadImage(self): #Завантажую зображення.
        self.canvaser.configure(image=self.photo_formuls,width=560, height=650)
        self.canvaser.pack(side=RIGHT);

    def about(self): # Вивід про програму.
        s = 'Навчальна практика\n' \
            'Виконав:\nCтудент гр. КН-20Б\n' \
            'Оврамець І. В.'
        messagebox.showinfo(title="About", message=s)

    def help(self): # Вивід при питаннях до програми.
        s = 'Звяжіться із розробником\n' \
            'Gmail ovramets.i@donnu.edu.ua\n' \
            'Telegram @Ovramets2003'

        messagebox.showinfo(title="About", message=s)

    def save_text(self): # Зберігаю данні із віджита блокнот.
        out = asksaveasfile(mode='w', defaultextension='.txt')
        data = self.entry_value_save.get('1.0', tk.END)
        try:
            out.write(data.rstrip())
        except Exception:
            showerror(title="Error", message="Saving file error....")


def main():
    root = tk.Tk()
    app = Form1(master=root)  # Створення екземпляра класу Form1!
    app.mainloop()  #Запускаємо саму програму


if __name__ == "__main__": #Запускаєм програму
    main()
