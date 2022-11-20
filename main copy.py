from teleconverter import *

# pacotes adicionais
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter import Menu
from tkinter import Label
from tkinter import Button
from tkinter import Entry 

# if __name__ == '__main__':
#     a = DB(90)
#     b = Teleconverter(a).to_dbm()
#     print(f'{a} = {b}')


########################################################""
# GUI PARA CONVERTER UNIDADES (dB, dBm, dBU, W, mW, etc)
#:. Ailton Duarte <coyas>
########################################################""

# Funcoes
def search(list, unidade) -> bool:
    for i in range(len(list)):
        if list[i] == unidade:
            print("Existe::")
            print(list[i])
            return True
    return False


def converterValor() -> None:
    # get o valor do combobox (valorCombobox)
    valorCb = unidadeConversao.get()    
    # se valor selecionado no combobox estiver vazio, i.e, se nao for selecionado um valor
    if not valorCb :
        print("valorCb")
        print(valorCb)
        showinfo(
            title='Importante',
            message=f'Selecione a unidade de conversão!'
        )
        
    else:
        # Status
        label_Final = Label(app, text="Converter %s para %s" % (valorEntrada.get(), valorCb))
        label_Final.pack()

        # se os ultimos 3 digitos do valor de entrada for um valor da lista combobox estao converte
        # uniConversaoList["values"]
        # o valor deve ser separado por "."
        x = valorEntrada.get().split(".")
        # if 

        # uniConversaoList = lita das unidades, valor = valor selecionado do combobox
        # valorEntrada = valor entrado pelo utilizador
        # x[1] = unidade do valor
        print(search(x[1].lower(), valorCb))
        if x[1].lower() == valorCb.lower() and search(uniConversaoList["values"], x[1].lower()):
            # se alguem escolher a mesma unidade entrada é igual a saida
            # Apresentar o valor
            label_Final2 = Label(app, text=":= %s %s" % (x[0], valorCb))
            label_Final2.pack()
        # se as unidades de conversao sao diferentes faz o calculo de conversao
        elif search(uniConversaoList["values"], x[1].lower()) and x[1].lower() != valorCb.lower():
            print("x[1] == unidadeConversao.get()")
            print(x[1])
            print(valorCb.lower())
            # calculo final
            # aqui ira ficar a funcao de conversao
            # valorFinal = mainConvertor(valorEntrada, UnidadeValorEntrada, converterPara)
            valorFinal = 12321322
            # Apresentar o valor
            label_Final2 = Label(app, text=":. %f %s" % (float(valorFinal), valorCb))
            label_Final2.pack()
    # pass


# GUI
app = tk.Tk()


# Meno do app
menu = Menu(app)

new_item = Menu(menu)

new_item.add_command(label='Contact us')
new_item.add_command(label='About kraki v0.01')

menu.add_cascade(label='File')
menu.add_cascade(label='Config')
menu.add_cascade(label='About', menu=new_item)

app.config(menu=menu)
## fim do meno do app

# config da janela app
app.geometry('405x600')
app.resizable(False, False)
app.title('Kraki - Conversor de Unidades')

# label
label = ttk.Label(text="CONVERSOR DE UNIDADES", font="Arial 20 bold")
label.pack(fill=tk.X, padx=20, pady=20)

label = ttk.Label(text="Entre com valor:.")
label.pack(fill=tk.X, padx=10, pady=10)

valorEntrada = Entry(app)
valorEntrada.focus()
valorEntrada.pack(padx=10, pady=10)

# cria combobox de selecao
unidadeConversao = tk.StringVar()
uniConversaoList = ttk.Combobox(app, textvariable=unidadeConversao)
# get first 3 letters of every month name
uniConversaoList['values'] = ['dbm','dbu','dbr','wat','mwt']

# prevent typing a value
uniConversaoList['state'] = 'readonly'

# place the widget
uniConversaoList.pack(padx=5, pady=5)

# apresenta "status" antes de prosseguir
label = ttk.Label(text="Valor convertido:")
label.pack(fill=tk.X, padx=5, pady=5)

btn = Button(app, text="Converter", command=converterValor)
btn.pack()


# bind the selected value changes
# def uni_changed(event):
#     """ handle the uni changed event """
#     showinfo(
#         title='Resultado',
#         message=f'Selecionou: {unidadeConversao.get()}!'
#     )

# uniConversaoList.bind('<<ComboboxSelected>>', uni_changed)


app.mainloop()
