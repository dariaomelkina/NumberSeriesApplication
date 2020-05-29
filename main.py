"""
Application for calculation of series partial sum and
determination if a series is convergent or not.
Main module with gui implementation and app launching.

Author: Daria Omelkina, 2020.
"""
from tkinter import *
from calculate_series import series_partial_sum, convergence
from tkinter import scrolledtext

root = Tk()
root.title('Числові Ряди')
root.geometry('590x500')

lbl = Label(root, text="Вітаю в додатку для роботи з числовими рядами!", font=("Arial", 25), fg='dark slate blue')
lbl.grid(columnspan=2, row=0)

instruction = Label(root, text="Додаток передбачає роботу з числовими рядами,"
                               "в загальному вигляді яких змінною є n.\n"
                               "Перевіряються необхідна умова збіжності ряду,"
                               "критерій для узагальненого гармонійного\nряду,"
                               "ознаки Коші і Даламбера.", font=("Arial", 13), fg='dark slate blue')
instruction.grid(columnspan=2, row=5)

author = Label(root, text="Daria Omelkina, 2020.", font=("Arial", 13), fg='seashell3')
author.grid(columnspan=2, row=6)

lbl1 = scrolledtext.ScrolledText(root, width=19, height=10, font=("Arial", 20), fg='PaleVioletRed4', bg='lavender')
lbl1.grid(column=0, row=3)

lbl2 = scrolledtext.ScrolledText(root, width=19, height=10, font=("Arial", 20), fg='PaleVioletRed4', bg='lavender')
lbl2.grid(column=1, row=3)

txt1 = Entry(root, width=10)
txt1.grid(column=0, row=1)
txt1.focus()

txt2 = Entry(root, width=10)
txt2.grid(column=1, row=1)


def convergence_button():
    """ Event for convergence calculation. """
    lbl1.delete(1.0, END)
    res = convergence(txt1.get())
    if res == 'error1':
        res = 'На жаль, використовуваних додатком перевірок не вистачило.\nНеобхідна перевірка ряду вручну.'
    elif res == 'error2':
        res = 'Заданий n-тий член ряду не відповідає вимогам для роботи додатку.'
    elif res:
        res = 'Ряд збіжний.'
    else:
        res = 'Ряд розбіжний.'
    lbl1.insert(INSERT, str(res))


def series_partial_sum_button():
    """ Event for series partial sum calculation. """
    lbl2.delete(1.0, END)
    res = series_partial_sum(txt1.get(), txt2.get())
    if res == 'error2':
        res = 'На жаль, порахувати суму цього ряду в додатку не можливо.'
    else:
        pass
    lbl2.insert(INSERT, res)


but1 = Button(root, command=convergence_button)
but1["text"] = "Перевірити збіжність ряду."
but1.grid(column=0, row=2)

but2 = Button(root, command=series_partial_sum_button)
but2["text"] = "Порахувати часткову суму для заданого n."
but2.grid(column=1, row=2)

root.mainloop()
