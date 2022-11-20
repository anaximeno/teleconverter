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
def search(list, platform):
    print(len(list))
    for i in range(len(list)):
        if list[i] == platform:
            print(list[i])
            return True
    return False


# def getUni(*arg) -> None:
#     Label(app, text= "The value at index " + str(self.convertion_unit_list.current()) + " is " + " "+ str(unidadeConversao.get()), font= ('Helvetica 12')).pack()


    # pass


class Application(tk.Tk):
    def __init__(self, title: str = "Kraki - Conversor de Unidades") -> None:
        super(Application, self).__init__()
        self._title = title

        # Meno do app
        self.menu = Menu(self)

        new_item = Menu(self.menu)
        new_item.add_command(label='Contact us')
        new_item.add_command(label='About kraki v0.01')

        self.menu.add_cascade(label='File')
        self.menu.add_cascade(label='Config')
        self.menu.add_cascade(label='About', menu=new_item)

        self.config(menu=self.menu)
        ## fim do meno do app

        # config da janela app
        self.geometry('405x600')
        self.resizable(False, False)
        self.title(self._title)

        # label
        self.body_title_label = ttk.Label(text="CONVERSOR DE UNIDADES", font="Arial 20 bold")
        self.body_title_label.pack(fill=tk.X, padx=20, pady=20)

        self.entry_value_label = ttk.Label(text="Entre com valor:.")
        self.entry_value_label.pack(fill=tk.X, padx=10, pady=10)

        self.entry_value = Entry(self)
        self.entry_value.pack(padx=10, pady=10)

        # cria combobox de selecao
        self.convertion_unit = tk.StringVar()
        self.convertion_unit_list = ttk.Combobox(self, textvariable=self.convertion_unit)
        # get first 3 letters of every month name
        self.convertion_unit_list['values'] = ['dBm','dBu','dBr','Wat','mWt'] # TODO: get this from the domain

        # prevent typing a value
        self.convertion_unit_list['state'] = 'readonly'

        # place the widget
        self.convertion_unit_list.pack(padx=5, pady=5)
        self.convertion_unit_list.bind('<<ComboboxSelected>>', self.uni_changed)

        # apresenta "status" antes de proceguir
        self.converted_value_label = ttk.Label(text="Valor convertido:")
        self.converted_value_label.pack(fill=tk.X, padx=5, pady=5)

        self.convet_button = Button(self, text="Converter", command=self.convert)
        self.convet_button.pack()

    def run(self) -> None:
        self.mainloop()

    # bind the selected value changes
    def uni_changed(self, event) -> None:
        """ handle the uni changed event """
        showinfo(
            title='Resultado',
            message=f'Selecionou: {self.convertion_unit.get()}!'
        )

    def convert(self) -> None:
        # get o valor do combobox
        valor = self.convertion_unit.get()
        # Status
        label_Final = Label(self, text="Converter %s para %s" % (self.entry_value.get(), valor))
        label_Final.pack()

        # se os ultimos 3 digitos do valor de entrada for um valor da lista combobox estao converte
        # self.convertion_unit_list["values"]
        # if

        # self.convertion_unit_list = lita das unidades, valor = valor selecionado do combobox
        # valorEntrada = valor entrado pelo utilizador
        # print(search(existeF, valor))
        if search(self.convertion_unit_list["values"], valor):
            # se alguem escolher a mesma unidade entrada é igual a saida
            # Apresentar o valor
            label_Final2 = Label(self, text=":tera. %s %s" % (self.entry_value.get(), valor))
            label_Final2.pack()
        else:
            # calculo final
            valorFinal = 12321322
            # Apresentar o valor
            label_Final2 = Label(self, text=":. %f %s" % (float(valorFinal), valor))
            label_Final2.pack()
