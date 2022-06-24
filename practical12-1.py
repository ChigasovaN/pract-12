'''
    Практическое занятие №12.
    Вариант №32.

    Задание 1. В соответствии с номером варианта перейти
    по ссылке на прототип. Реализовать его в IDE PyCharm Community с применением пакета tk.
    Получить интерфейс максимально приближенный к оригиналу (см. таблицу 1)
    Ссылка на прототип:
    https://i2.wp.com/ps.w.org/ultimate-form-builder-lite/assets/screenshot-1.png
'''

from tkinter import *
from tkinter import ttk


class Forms(Tk):
    def __init__(self):
        super().__init__()

        self.title('Практическая 12.1')
        self.geometry('800x500')
        self.resizable(0, 0)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # переменные с стилями
        font_and_bg = {'font': ('Times', 13), 'background': 'white'}
        frame_indents = {'padx': 30, 'pady': 40}
        pady_top = {'pady': (30, 0)}
        field_indents = {'padx': (10, 20)}
        header_style = {'font': ('Times', 20), 'foreground': '#7F93AD', 'background': 'white'}
        password_style = {'font': 'Times', 'background': '#F7F6BD'}
        button_style = {'background': '#74BAF5', 'foreground': 'white'}

        '''
            Поддерживать стандартные параметры для полосы прокрутки (скроллбара) могут лишь
            такие виджеты, как Text, Listbox, Entry(частично) и Canvas. Поскольку наши компоненты
            будут располагаться в фрейме, то добавим скроллбар следующим образом:
                1. Создаем фрейм (main_frame), указываем корень self и растягиваем фрейм на всё окно;
                2. Создаем канву (main_canvas), указываем корень main_frame и растягиваем на всё окно;
                3. Создаем скроллбар (scrollbar), указываем корень главный фрейм (main_frame) и управление канвой (main_canvas);
                4. Через канву с помощью метода create_window создаем второй фрейм (second_frame) и растягиваем на всё окно;
                5. Показываем канве, насколько большой фрейм, чтобы канва знала, сколько ей прокручивать.
        '''
        # 1-й этап
        main_frame = Frame(self, bg='lightblue')
        main_frame.grid(row=0, column=0, sticky='nsew')
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(0, weight=1)

        # 2-й этап
        main_canvas = Canvas(main_frame, bg='lightblue')
        main_canvas.grid(row=0, column=0, sticky='nsew')
        main_canvas.columnconfigure(0, weight=1)
        main_canvas.rowconfigure(0, weight=1)

        # 3-й этап
        scrollbar = Scrollbar(main_frame, orient='vertical', command=main_canvas.yview)
        scrollbar.grid(row=0, column=1, sticky='nsew')
        main_canvas['yscrollcommand'] = scrollbar.set

        # 4-й этап
        second_frame = Frame(main_canvas, bg='white')
        second_frame.configure(**frame_indents)
        main_canvas.create_window((0, 0), window=second_frame, anchor='nw')

        # 5-й этап (последний)
        main_canvas.bind('<Configure>', lambda e: main_canvas.configure(scrollregion=main_canvas.bbox('all')))

        # конфигурации для колонок
        second_frame.columnconfigure(0, weight=1)
        second_frame.columnconfigure(1, weight=2)

        # заголовок и поля формы
        header = Label(second_frame, text='ALL FIELDS FORM', **header_style)
        header.grid(row=0, column=0, columnspan=2, sticky=W)

        textfield_label = ttk.Label(second_frame, text='Textfield')
        textfield_label.grid(row=1, column=0, sticky=W, **pady_top)
        textfield = Entry(second_frame, **font_and_bg)
        textfield.grid(row=1, column=1, sticky=W+E, **pady_top, **field_indents)

        textarea_label = ttk.Label(second_frame, text='Textarea')
        textarea_label.grid(row=2, column=0, sticky=W+N, **pady_top)
        textarea = Text(second_frame, height=7, width=66, **font_and_bg)
        textarea.grid(row=2, column=1, sticky=W, **pady_top, **field_indents)

        email_label = ttk.Label(second_frame, text='Email Address')
        email_label.grid(row=3, column=0, sticky=W, **pady_top)
        email_string = StringVar()
        email = Entry(second_frame, textvariable=email_string, **font_and_bg)
        email.grid(row=3, column=1, sticky=W+E, **pady_top, **field_indents)

        dropdown_label = ttk.Label(second_frame, text='Dropdown')
        dropdown_label.grid(row=4, column=0, sticky=W, **pady_top)
        optionList = [
            'Option 1',
            'Option 2',
            'Option 3',
        ]
        option_var = StringVar(second_frame)
        dropdown = ttk.OptionMenu(second_frame, option_var, optionList[0], *optionList)
        # для стилизации выпадающего списка
        dropdown['menu'].config(**font_and_bg)
        dropdown.grid(row=4, column=1, sticky=W, **pady_top, **field_indents)

        rb_label = ttk.Label(second_frame, text='Radio Button')
        rb_label.grid(row=5, column=0, sticky=W, **pady_top)
        rb_value = BooleanVar()
        rb1 = Radiobutton(second_frame, text='Option 1', variable=rb_value, value=0, **font_and_bg)
        rb1.grid(row=5, column=1, sticky=W, **pady_top, **field_indents)
        rb2 = Radiobutton(second_frame, text='Option 2', variable=rb_value, value=1, **font_and_bg)
        rb2.grid(row=6, column=1, sticky=W, **field_indents)

        cb_label = ttk.Label(second_frame, text='Checkbox')
        cb_label.grid(row=7, column=0, sticky=W, **pady_top)
        cb1_value = IntVar()
        cb1 = Checkbutton(second_frame, text='Option 1', variable=cb1_value, onvalue=1, offvalue=0, **font_and_bg)
        cb1.grid(row=7, column=1, sticky=W, **pady_top, **field_indents)
        cb2_value = IntVar()
        cb2 = Checkbutton(second_frame, text='Option 2', variable=cb2_value, onvalue=1, offvalue=0, **font_and_bg)
        cb2.grid(row=8, column=1, sticky=W, **field_indents)
        cb3_value = IntVar()
        cb3 = Checkbutton(second_frame, text='Option 3', variable=cb3_value, onvalue=1, offvalue=0, **font_and_bg)
        cb3.grid(row=9, column=1, sticky=W, **field_indents)

        password_label = ttk.Label(second_frame, text='Password')
        password_label.grid(row=10, column=0, sticky=W, **pady_top)
        password_field = Entry(second_frame, show='*', **password_style)
        password_field.grid(row=10, column=1, sticky=W+E, **pady_top, **field_indents)

        number_label = ttk.Label(second_frame, text='Number Field')
        number_label.grid(row=11, column=0, sticky=W, **pady_top)
        number_field = Entry(second_frame, **font_and_bg)
        number_field.grid(row=11, column=1, sticky=W, **pady_top, **field_indents)

        mathcaptcha_label = ttk.Label(second_frame, text='Mathematical\nCaptcha')
        mathcaptcha_label.grid(row=12, column=0, sticky=W, **pady_top)

        mathcaptcha_frame = Frame(second_frame, background='white')
        mathcaptcha_frame.grid(row=12, column=1, sticky=W, **pady_top, **field_indents)

        mathcaptcha = ttk.Label(mathcaptcha_frame, text='6 + 8 = ')
        mathcaptcha.grid(row=0, column=0, sticky=W)
        mathcaptcha2 = Entry(mathcaptcha_frame, **font_and_bg)
        mathcaptcha2.grid(row=0, column=1, sticky=W)

        googlecaptcha = ttk.Label(second_frame, text='Google Captcha')
        googlecaptcha.grid(row=13, column=0, sticky=W, **pady_top)
        # пока не знаю, как реализовать капчу в форме, поэтому пока оставлю под нее место
        googlecaptcha = Frame(second_frame, background='lightblue')
        Label(googlecaptcha, text='Тут могла быть капча').pack()
        googlecaptcha.grid(row=13, column=1, sticky=W, **pady_top, **field_indents)

        submit_button = Button(second_frame, text='Submit', **button_style)
        submit_button.grid(row=14, column=1, sticky=W, **pady_top, **field_indents)


        # изменение стилей виджетов
        self.style = ttk.Style(self)
        self.style.configure('TLabel', **font_and_bg)
        self.style.configure('TMenubutton', **font_and_bg)


def runForms():
    window = Forms()
    window.mainloop()


if __name__ == '__main__':
    runForms()
