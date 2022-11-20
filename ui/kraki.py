import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter import Menu
from tkinter import Label
from tkinter import Button
from tkinter import Entry


class Application(tk.Tk):
    teleconverter: any = None
    telecalculator: any = None
    units: any = None

    def __init__(self, title: str = "Kraki", description: str = "Conversor de Unidades", version: str = "0.1.0", width: int = 480, height: int = 320) -> None:
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

        self.menu.add_cascade(label='About', menu=new_item)
        self.menu.add_cascade(label='File')
        self.menu.add_cascade(label='Config')

        self.config(menu=self.menu)

    def __create_body(self):
        self.body_title_label = ttk.Label(
            text=self._description, font="Arial 20 bold")
        self.body_title_label.pack(fill=tk.X, padx=20, pady=20)

        self.entry_value_label = ttk.Label(text="Entre com valor:.")
        self.entry_value_label.pack(fill=tk.X, padx=10, pady=10)

        self.entry_value = Entry(self)
        self.entry_value.pack(padx=10, pady=10)

        # cria combobox de selecao
        self.convertion_unit = tk.StringVar()
        self.convertion_unit_list = ttk.Combobox(
            self, textvariable=self.convertion_unit)
        self.convertion_unit_list['values'] = self._conversible_units_list
        self.convertion_unit_list['state'] = 'readonly'
        self.convertion_unit_list.pack(padx=5, pady=5)
        self.convertion_unit_list.bind(
            '<<ComboboxSelected>>', self.uni_changed)

        self.converted_value_label = ttk.Label(text="Valor convertido:")
        self.converted_value_label.pack(fill=tk.X, padx=5, pady=5)

        self.convert_button = Button(
            self, text="Converter", command=self.convert)
        self.convert_button.pack()

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
        label_Final = Label(self, text="Converter %s para %s" %
                            (self.entry_value.get(), valor))
        label_Final.pack()

        # calculo final
        valorFinal = 12321322
        # Apresentar o valor
        label_Final2 = Label(self, text=":. %f %s" %
                             (float(valorFinal), valor))
        label_Final2.pack()
