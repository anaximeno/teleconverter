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
    def __init__(self, title: str = "Kraki", description: str = "Conversor de Unidades", version: str = "0.1.0", width: int = 600, height: int = 600) -> None:
        super(Application, self).__init__()

        self._title = title
        self._description = description
        self._version = version
        self._width = width
        self._height = height

        self.geometry(f'{self._width}x{self._height}')
        self.resizable(False, False)
        self.title(self._title)

        # self.__create_menu()
        self.__create_body()

    @classmethod
    def inject(cls, units: any, teleconverter: any, telecalculator: any) -> None:
        """Inject dependencies from domain or other submodules of this project."""
        cls.teleconverter = teleconverter
        cls.telecalculator = telecalculator
        cls.units = units

    @property
    def _conversible_units_list(self) -> list[str]:
        return list(self.units.units_mapper.keys()) if self.units is not None else []

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
        self.body_title_label = ttk.Label(
            text=self._description, font="Arial 20 bold")
        self.body_title_label.grid(sticky='we', padx=5, pady=5)

        self.entry_value_label = ttk.Label(text="Entre com valor:.")
        self.entry_value_label.grid(row=2, column=0)

        self.entry_value = Entry(self)
        self.entry_value.focus()
        self.entry_value.grid(padx=10, pady=10,row=3, column=0)

        self.convertion_unit = tk.StringVar()

        self.convertion_unit_list_entry = ttk.Combobox(self, textvariable=self.convertion_unit)
        self.convertion_unit_list_entry['values'] = self._conversible_units_list
        # prevent typing a value
        self.convertion_unit_list_entry['state'] = 'readonly'
        self.convertion_unit_list_entry.grid(row=4, column=0, sticky="")

        # self.convertion_unit_list = ttk.Combobox(self, textvariable=self.convertion_unit)

        # get first 3 letters of every month name
        # self.convertion_unit_list['values'] = ['dbm','dbu','dbr','wat','mwt'] # TODO: get this from the domain

        self.converted_value_label = ttk.Label(text="para ==> ")
        self.converted_value_label.grid(row=4, column=1)

        self.convertion_unit_list = ttk.Combobox(self, textvariable=self.convertion_unit)
        self.convertion_unit_list['values'] = self._conversible_units_list
        # prevent typing a value
        self.convertion_unit_list['state'] = 'readonly'
        self.convertion_unit_list.grid(row=4, column=2, sticky="")
        # self.convertion_unit_list.bind('<<ComboboxSelected>>', self.uni_changed)

        self.converted_value_label = ttk.Label(text="Valor convertido:")
        self.converted_value_label.grid(row=6, column=0, sticky="")

        self.convert_button = Button(
            self, text="Converter", command=self.convert)
        self.convert_button.grid()

    # bind the selected value changes
    # def uni_changed(self, event) -> None:
    #     """ handle the uni changed event """
    #     showinfo(
    #         title='Resultado',
    #         message=f'Selecionou: {self.convertion_unit.get()}!'
    #     )

    def _alert_user(self, message: str) -> str:
        return showinfo(title='Alerta!', message=message)

    def convert(self) -> None:
        typeFrom = self.convertion_unit.get()
        valueFrom = self.entry_value.get()

        print("Dados:.")
        print(typeFrom)
        print(valueFrom)

        # se os ultimos 3 digitos do valor de entrada for um valor da lista combobox estao converte
        # uniConversaoList["values"]
        # o valor deve ser separado por "."
        x = self.entry_value.get().split(".") # ou valueFrom.split(".") ou ...

        print(valueFrom, typeFrom)
        # if not valueFrom.isnumeric():
        if not valueFrom:
            self._alert_user('Precisa introduzir um valor válido para a conversão!')
            return
        elif typeFrom == '':
            self._alert_user('Precisa escolher uma unidade para a conversão!')
            return
        else:
            # Status
            label_Final = Label(self, text="Converter %s para %s" % (valueFrom, typeFrom))
            label_Final.grid()

            # self.convertion_unit_list = lita das unidades, valor = valor selecionado do combobox
            # valorEntrada = valor entrado pelo utilizador
            # if search(self.convertion_unit_list["values"], valor):
            # para isso todo valor tem k estar a minuscula
            if x[1].lower() == typeFrom.lower() and search(self.convertion_unit_list['values'], x[1].lower()):
                # se alguem escolher a mesma unidade entrada é igual a saida
                # Apresentar o valor
                label_Final2 = Label(self, text="::= %s %s" % (x[0], typeFrom))
                label_Final2.grid()
            elif search(self.convertion_unit_list['values'], x[1].lower()) and x[1].lower() != typeFrom.lower():
                # calculo final
                # aqui ira ficar a funcao de conversao
                # valorFinal = mainConvertor(valorEntrada, UnidadeValorEntrada, converterPara)
                valorFinal = 12321322
                # Apresentar o valor
                label_Final2 = Label(self, text="::= %f %s" % (float(valorFinal), typeFrom))
                label_Final2.grid()

        value = self._objectify(x[0], typeFrom)
        print(value)

    def _objectify(self, value: float | str, unit_ref: str) -> any or None:
        """Converts the `value` param into a unit value object if it is possible, else return None."""
        if len(self._conversible_units_list) > 0 and unit_ref in self._conversible_units_list:
            return self.units.units_mapper[unit_ref](float(value))
        return None

