import tkinter as tk
import cv2
import numpy


def vazio():
    print()


def teste():
    global janela
    janela = tk.Tk()
    janela.geometry('940x625+40+40')
    janela.title('Apresentando a Imagem')

    menu_bt_teste1 = tk.Button(janela, text='Processar', command=vazio, width=10, height=5)
    menu_bt_teste1.place(x=0, y=5)