from tkinter import *
import tkinter as tk


janela = tk.Tk()
janela.geometry("322x440")


display = StringVar()

txt = ""


def clickbutton(val):
    global txt
    txt = txt + str(val)
    display.set(txt)


def clickigual():
    global txt
    res = str(eval(txt))
    display.set(res)
    txt = res


def clickclear():
    global txt
    txt = ""
    display.set(txt)


frmdisplay = tk.Frame(janela, width=322, height=100, highlightbackground="black",
                      highlightcolor="black", highlightthickness=2)
frmdisplay.pack(side=tk.TOP)

frmbutton = tk.Frame(janela, width=322, height=190)
frmbutton.pack()

tela = tk.Entry(frmdisplay, textvariable=display, width=60,
                background="cyan", font=["arial", 20, "bold"], justify=tk.RIGHT)
tela.grid(column=0, row=0)
tela.pack(ipady=22)

botao1 = tk.Button(frmbutton, text="1", command=lambda: clickbutton(1), width=10,
                   height=4).grid(column=0, row=2, sticky=W)
botao2 = tk.Button(frmbutton, text="2", command=lambda: clickbutton(2), width=10, height=4).grid(
    column=1, row=2, sticky=W)
botao3 = tk.Button(frmbutton, text="3", command=lambda: clickbutton(3), width=10, height=4).grid(
    column=2, row=2, sticky=W)
botao4 = tk.Button(frmbutton, text="4", command=lambda: clickbutton(4), width=10, height=4).grid(
    column=0, row=3, sticky=W)
botao5 = tk.Button(frmbutton, text="5", command=lambda: clickbutton(5), width=10, height=4).grid(
    column=1, row=3, sticky=W)
botao6 = tk.Button(frmbutton, text="6", command=lambda: clickbutton(6), width=10, height=4).grid(
    column=2, row=3, sticky=W)
botao7 = tk.Button(frmbutton, text="7", command=lambda: clickbutton(7), width=10, height=4).grid(
    column=0, row=4, sticky=W)
botao8 = tk.Button(frmbutton, text="8", command=lambda: clickbutton(8), width=10, height=4).grid(
    column=1, row=4, sticky=W)
botao9 = tk.Button(frmbutton, text="9", command=lambda: clickbutton(9), width=10, height=4).grid(
    column=2, row=4, sticky=W)
botaomais = tk.Button(frmbutton, text="+", command=lambda: clickbutton("+"), width=10,
                      height=4).grid(column=3, row=3, sticky=W)
botaomenos = tk.Button(frmbutton, text="-", command=lambda: clickbutton("-"), width=10,
                       height=4).grid(column=3, row=2, sticky=W)
botaovezes = tk.Button(frmbutton, text="x", command=lambda: clickbutton("*"), width=10, height=4).grid(
    column=3, row=1, sticky=W)
botaodividir = tk.Button(frmbutton, text="/", command=lambda: clickbutton("/"), width=10,
                         height=4).grid(column=3, row=4, sticky=W)
botaoponto = tk.Button(frmbutton, text=".", command=lambda: clickbutton("."), width=10,
                       height=4).grid(column=2, row=5, sticky=W)
botaoigual = tk.Button(frmbutton, text="=", command=lambda: clickigual(), width=10, height=4, background="purple").grid(
    column=3, row=5, sticky=W)
botaolimpar = tk.Button(frmbutton, text="CE", command=lambda: clickclear(), width=33,
                        height=4).grid(columnspan=4, row=1, sticky=W)
botao0 = tk.Button(frmbutton, text="0", command=lambda: clickbutton(0), width=22, height=4).grid(
    columnspan=3, row=5, sticky=W)


janela.mainloop()
