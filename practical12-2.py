'''
    Практическое занятие №12.
    Вариант №32.

    Задание 2. Разработать программу с применением пакета tk,
    взяв в качестве условия одну любую задачу из ПЗ №№3-8.

    1. Дано вещественное число А и целое число N (>0). Используя цикл,
        вывести все целые степени числа А от 1 до N.
    2. Дано целое число N (>0). Используя операции деления нацело и взятия остатка от деления,
        найти количество и сумму его цифр.
'''

from tkinter import *


class mainWindow(Tk):
    def __init__(self):
        super().__init__()

        self.geometry('500x400')
        self.minsize(500, 400)
        self.title('Практическая работа 12.2')
        self.config(background='white', padx=30, pady=30)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        style_conf = {'background': 'white',  'font': 'Courier'}
        button_style = {'relief': 'solid'}
        pad_conf = {'padx': 10, 'pady': 10, 'ipadx': 10, 'ipady': 10}

        task1 = '1. Дано вещественное число А и целое число N (>0). Используя цикл, вывести все целые степени числа А от 1 до N.'
        task2 = '2. Дано целое число N (>0). Используя операции деления нацело и взятия остатка от деления, найти количество и сумму его цифр.'

        def task1window():
            root = Toplevel(self)
            root.geometry('500x400')
            root.minsize(500, 400)
            root.title('Условие задания 1')
            root.config(background='white', padx=30, pady=30)
            root.columnconfigure(0, weight=1)
            root.columnconfigure(1, weight=1)

            Label(root, text='Условие задания 1:', **style_conf).grid(row=0, column=0, columnspan=2)
            task_label = Label(root, text=task1, **style_conf, justify='left')
            task_label.grid(row=1, column=0, columnspan=2)
            task_label.bind('<Configure>', lambda e: task_label.config(wraplength=task_label.winfo_width()))
            root.update_idletasks()

            Label(root, text='Введите число А: ').grid(row=2, column=0)
            input1 = Entry(root)
            input1.grid(row=2, column=1, sticky=W + E)


            Label(root, text='Введите число N: ').grid(row=3, column=0)
            input2 = Entry(root)
            input2.grid(row=3, column=1, sticky=W + E)

            def calculate():
                valueA = int(input1.get())
                valueN = int(input2.get())

                i = 1
                while i<=valueN:
                    result = valueA**i
                    result_output.insert(INSERT, result)
                    if i!=valueN:
                        result_output.insert(END, ', ')
                    i += 1

            Button(root, text='рассчитать', command=calculate).grid(row=4, column=1)

            result_output = Text(root, height=10)
            result_output.grid(row=5, column=0, columnspan=2, sticky=W+E)


        def task2window():
            root = Toplevel(self)
            root.geometry('500x400')
            root.minsize(500, 400)
            root.title('Условие задания 2')
            root.config(background='white', padx=30, pady=30)
            root.columnconfigure(0, weight=1)
            root.columnconfigure(1, weight=1)

            Label(root, text='Условие задания 2:', **style_conf).grid(row=0, column=0, columnspan=2)
            task_label = Label(root, text=task2, **style_conf, justify='left')
            task_label.grid(row=1, column=0, columnspan=2)
            task_label.bind('<Configure>', lambda e: task_label.config(wraplength=task_label.winfo_width()))
            root.update_idletasks()

            Label(root, text='Введите число: ').grid(row=2, column=0, sticky=W)
            input_value = Entry(root)
            input_value.grid(row=2, column=1, sticky=W)

            def calculate():
                value = int(input_value.get())
                sum = 0
                count = 0
                while value != 0:
                    num = value % 10
                    sum += num
                    value //= 10
                    count += 1
                print('sum : ', end=' ')
                print(sum)
                print('count : ', end=' ')
                print(count)

            Button(root, text='Посчитать', command=calculate).grid(row=3, column=1, sticky=W)







        Label(text='Выберите условие задания:', **style_conf).grid(row=0, column=0, columnspan=2, **pad_conf)
        button1 = Button(text=task1, justify='left', **style_conf, **button_style, command=task1window)
        button1.grid(row=1, column=0, sticky=N, **pad_conf)
        button1.bind('<Configure>', lambda e: button1.config(wraplength=buttonWidth()))
        button2 = Button(text=task2, justify='left', **style_conf, **button_style, command=task2window)
        button2.grid(row=1, column=1, sticky=N, **pad_conf)
        button2.bind('<Configure>', lambda e: button2.config(wraplength=buttonWidth()))

        def buttonWidth():
            return (button1.winfo_width() + button2.winfo_width() - 40)/2



def runMainWindow():
    window = mainWindow()
    window.mainloop()


if __name__ == '__main__':
    runMainWindow()
