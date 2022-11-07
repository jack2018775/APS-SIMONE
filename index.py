from Telas import *
from funcao import *

'''
1) Campo para escolher a imagem
2) Telas para processar as imagens
'''

janela = tk.Tk()
janela.geometry('1366x768')
janela.state("zoomed")
janela.title("Processamento de Imagem")

menu_bt_teste1 = tk.Button(janela, text='1', command=teste, width=10, height=5)
btn_sair = tk.Button(janela, text='Sair', command=janela.destroy, width=10, height=5)

menu_bt_teste1.place(x=0, y=5)
btn_sair.place(x=1280, y=5)


janela.mainloop()
