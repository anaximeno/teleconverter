########################################################""
# GUI PARA CONVERTER UNIDADES (dB, dBm, dBU, W, mW, etc)
#:. Ailton Duarte <coyas>
########################################################""

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter import Menu
from tkinter import Label
from tkinter import Button
from tkinter import Entry


def search(list, platform) -> bool:
    print(len(list))
    for i in range(len(list)):
        if list[i] == platform:
            print(list[i])
            return True
    return False

class Application(tk.Tk):
    def __init__(self, title: str = "Kraki", description: str = "Conversor de Unidades", version: str = "0.1.0", width: int = 405, height: int = 600) -> None:
        super(Application, self).__init__()

        self._title = title
        self._description = description
        self._version = version
        self._width = width
        self._height = height

        self.geometry(f'{self._width}x{self._height}')
        self.resizable(False, False)
        self.title(self._title)

        self.__create_menu()
        self.__create_body()

    def run(self) -> None:
        self.mainloop()

    def __create_menu(self) -> None:
        self.menu = Menu(self)

        new_item = Menu(self.menu)
        new_item.add_command(label='Contact us')
        new_item.add_command(label=f'{self._title} {self._version}')

        self.menu.add_cascade(label='File')
        self.menu.add_cascade(label='Config')
        self.menu.add_cascade(label='About', menu=new_item)

        self.config(menu=self.menu)

    def __create_body(self):
        self.body_title_label = ttk.Label(text=self._description, font="Arial 20 bold")
        self.body_title_label.pack(fill=tk.X, padx=20, pady=20)

        self.entry_value_label = ttk.Label(text="Entre com valor:.")
        self.entry_value_label.pack(fill=tk.X, padx=10, pady=10)

        self.entry_value = Entry(self)
        self.entry_value.focus()
        self.entry_value.pack(padx=10, pady=10)

        # cria combobox de selecao
        self.convertion_unit = tk.StringVar()
        self.convertion_unit_list = ttk.Combobox(self, textvariable=self.convertion_unit)

        # get first 3 letters of every month name
        self.convertion_unit_list['values'] = ['dbm','dbu','dbr','wat','mwt'] # TODO: get this from the domain

        # prevent typing a value
        self.convertion_unit_list['state'] = 'readonly'

        # place the widget
        self.convertion_unit_list.pack(padx=5, pady=5)
        # self.convertion_unit_list.bind('<<ComboboxSelected>>', self.uni_changed)

        # apresenta "status" antes de proceguir
        self.converted_value_label = ttk.Label(text="Valor convertido:")
        self.converted_value_label.pack(fill=tk.X, padx=5, pady=5)

        self.convet_button = Button(self, text="Converter", command=self.convert)
        self.convet_button.pack()

    # bind the selected value changes
    # def uni_changed(self, event) -> None:
    #     """ handle the uni changed event """
    #     showinfo(
    #         title='Resultado',
    #         message=f'Selecionou: {self.convertion_unit.get()}!'
    #     )

    def convert(self) -> None:
        # get o valor do combobox
        valor = self.convertion_unit.get()

        if not valor :
            # print("valor")
            # print(valor)
            showinfo(
                title='Importante!',
                message=f'Selecione a unidade de conversão!'
            )
        else:
            # Status
            label_Final = Label(self, text="Converter %s para %s" % (self.entry_value.get(), valor))
            label_Final.pack()

            # se os ultimos 3 digitos do valor de entrada for um valor da lista combobox estao converte
            # uniConversaoList["values"]
            # o valor deve ser separado por "."
            x = self.entry_value.get().split(".")

            # self.convertion_unit_list = lita das unidades, valor = valor selecionado do combobox
            # valorEntrada = valor entrado pelo utilizador
            # print(search(existeF, valor))
            # if search(self.convertion_unit_list["values"], valor):
            if x[1].lower() == valor.lower() and search(self.convertion_unit_list['values'], x[1].lower()):
                # se alguem escolher a mesma unidade entrada é igual a saida
                # Apresentar o valor
                label_Final2 = Label(self, text="::= %s %s" % (x[0], valor))
                label_Final2.pack()
            elif search(self.convertion_unit_list['values'], x[1].lower()) and x[1].lower() != valor.lower():
                # calculo final
                # aqui ira ficar a funcao de conversao
                # valorFinal = mainConvertor(valorEntrada, UnidadeValorEntrada, converterPara)
                valorFinal = 12321322
                # Apresentar o valor
                label_Final2 = Label(self, text="::= %f %s" % (float(valorFinal), valor))
                label_Final2.pack()
