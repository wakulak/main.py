import tkinter as tk
from ctypes import windll
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter.scrolledtext import ScrolledText
from tkinter import filedialog as fd
import configparser
import os


windll.shcore.SetProcessDpiAwareness(1)

# root window
root = tk.Tk()
root.title('Rachunki ZUS')
#root.geometry('350x200+50+50')
#root.resizable(0, 0)
root.iconbitmap('./assets/pythontutorial-1-150x150.ico')

# widgets
button = ttk.Button
label = ttk.Label
entry = ttk.Entry
frame = ttk.Frame
checkbutton = ttk.Checkbutton
menubutton = ttk.Menubutton
separator = ttk.Separator
Menu=tk.Menu


# icones
download_icon = tk.PhotoImage(file='./assets/download.png')

# odczytanie pliku config
config = configparser.ConfigParser()
config.read('./config/config.ini')

# zmienne
cena=float(config.get('Zmienne', 'cena'))




def main():
    przygotuj_okno()
    root.mainloop()


def przygotuj_okno():
    global var0, zmiana, entry0


# frames


    buttonFrame=frame(root)
    buttonFrame.pack(
        anchor=tk.W,
        )
    textFrame=frame(root)
    textFrame.pack(
        anchor=tk.W,
        fill=tk.BOTH,
        expand=True,
        )
    # Menu

    menubar = Menu(root)
    root.config(menu=menubar)

    # create the file_menu
    file_menu = Menu(
        menubar,
        tearoff=0
    )

    # add menu items to the File menu
    file_menu.add_command(label='Otwórz plik .xml', command=select_file)
    file_menu.add_command(label='Zapisz sygnatury do .xlsx', command=save_file)
    file_menu.add_command(label='Zapisz do pliku .txt', command=lambda: showinfo('Uwaga', "Przycisk jeszcze nie działa"))
    file_menu.add_separator()
    file_menu.add_command(label='Konfiguracja')
    file_menu.add_separator()
    file_menu.add_command(label='Zakończ',command=root.destroy)

    # add the File menu to the menubar
    menubar.add_cascade(
        label="Plik",
        menu=file_menu
    )
    # create the Help menu
    help_menu = Menu(
        menubar,
        tearoff=0
    )

    help_menu.add_command(label='Pomoc')
    help_menu.add_command(label='O autorze')

    # add the Help menu to the menubar
    menubar.add_cascade(
        label="Pomoc",
        menu=help_menu
    )


# przyciski w buttonFrame
    przycisk0 = button(
        buttonFrame,
        image=download_icon,
        text='Otwórz plik .xml',
        underline=0,
        compound=tk.TOP,
        command=select_file,
    )
    przycisk0.pack(
        ipadx=5,
        ipady=5,
        padx=5,
        pady=5,
        anchor=tk.W,
        fill=tk.BOTH,
        expand=False,
        side=tk.LEFT,
        )

    przycisk1 = button(
        buttonFrame,
        image=download_icon,
        text='Zapisz sygn. do .xlsx',
        underline=0,
        compound=tk.TOP,
        command=save_file,
    )
    przycisk1.state(
        ['!disabled']
    )
    przycisk1.pack(
        ipadx=5,
        ipady=5,
        padx=5,
        pady=5,
        anchor=tk.W,
        fill=tk.BOTH,
        expand=False,
        side=tk.LEFT,
        )


    przycisk2 = button(
        buttonFrame,
        image=download_icon,
        text='Zapisz do pliku.txt',
        underline=0,
        compound=tk.TOP,
        #command=select_file,
    )
    przycisk2.pack(
        ipadx=5,
        ipady=5,
        padx=5,
        pady=5,
        anchor=tk.W,
        fill=tk.BOTH,
        expand=False,
        side=tk.LEFT,
    )


    label0=label(
        buttonFrame,
        text="Cena zapytania:"
    )
    label0.pack(
        ipadx=5,
        ipady=5,
        padx=5,
        pady=5,
        anchor=tk.S,
        fill=tk.X,
        expand=False,
        side=tk.TOP,
    )

    var0=tk.DoubleVar()
    var0.set(cena)

    entry0=entry(
        buttonFrame,
        textvariable=var0,
        state='disabled'
    )
    entry0.pack(
        ipadx=5,
        ipady=5,
        padx=5,
        pady=5,
        anchor=tk.CENTER,
        fill=tk.X,
        expand=False,
        side=tk.LEFT,
    )

    zmiana=tk.IntVar()

    check0=checkbutton(
        buttonFrame,
        text='zmienić cenę?',
        variable=zmiana,
        onvalue=1,
        offvalue=0,
        command=zmiana_ceny,

    )
    check0.pack(
        ipadx=5,
        ipady=5,
        padx=5,
        pady=5,
        anchor=tk.CENTER,
        fill=tk.X,
        expand=False,
        side=tk.LEFT,
    )

    separator0 = separator(textFrame, orient='horizontal')
    separator0.pack(
        fill=tk.X,
        )

    text0=ScrolledText(
        textFrame,
        # height=10,
        # width=50,
        #state='disabled',
        state='normal',
    )
    text0.pack(
        ipadx=5,
        ipady=5,
        padx=5,
        pady=5,
        anchor=tk.S,
        fill=tk.BOTH,
        expand=True,
        side=tk.BOTTOM,
    )
    for line in range(100):
        text0.insert(tk.END, "This is line number %s\n" % str(line))

    sg = ttk.Sizegrip(root)
    sg.pack(
        anchor=tk.SE,
        side=tk.BOTTOM,
    )




    root.bind('<Alt-KeyPress-o>', lambda a: select_file())
    root.bind('<Alt-KeyPress-z>', lambda a: save_file())




def select_file():

    filetypes = (
        ('Dokumenty .xml', '*.xml'),
        ('Wszystkie pliki', '*.*')
    )

    filename = fd.askopenfilename(
    title='Otwórz plik',
    initialdir=os.getcwd(),
    filetypes=filetypes)

    return filename

    # showinfo(
    #     title='Selected File',
    #     message=filename
    #     )

def save_file():

    filetypes = (
        ('Dokumenty Excel', '*.xlsx'),
        ('Wszystkie pliki', '*.*')
    )

    filename = fd.asksaveasfile(
    title='Zapisz plik',
    initialdir=os.getcwd(),
    filetypes=filetypes)

    return filename

    # showinfo(
    #     title='Selected File',
    #     message=filename
    #     )

def zmiana_ceny():
    if zmiana.get()==1:
        entry0.config(state = '!disabled')
    else:
        entry0.config(state='disabled')


main()
