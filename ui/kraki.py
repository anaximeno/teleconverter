import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class Application(tk.Tk):
    FIRST_ENTRY_ID_NAME = "entry_1"
    SECOND_ENTRY_ID_NAME = "entry_2"
    DEFAULT_FONT = "Arial"

    def __init__(self, title: str = "Kraki", description: str = "Conversor de Unidades", version: str = "0.1.0") -> None:
        super(Application, self).__init__()

        self._title = title
        self._description = description
        self._version = version

        self.resizable(False, False)
        self.title(self._title)

        #self.__create_menu()
        self.__create_body()

    @classmethod
    def inject(cls, units: any, teleconverter: any, telecalculator: any) -> None:
        """Inject dependencies from domain or other submodules of this project."""
        cls.teleconverter = teleconverter
        cls.telecalculator = telecalculator
        cls.units = units

    @property
    def _conversible_units_list(self) -> list[str]:
        return [] if self.teleconverter is None else list(self.teleconverter.CONVERTION_MAPPER.keys())

    def _unit_available_convertions(self, unit: str) -> list[str]:
        return [] if self.teleconverter is None or unit not in self.teleconverter.CONVERTION_MAPPER \
                  else list(self.teleconverter.CONVERTION_MAPPER[unit].keys())

    def _get_convertion_method(self, convert_from: str, convert_to: str) -> any or None:
        if convert_from in self.teleconverter.CONVERTION_MAPPER and convert_to in self.teleconverter.CONVERTION_MAPPER[convert_from]:
                return self.teleconverter.CONVERTION_MAPPER[convert_from][convert_to]
        return None

    def run(self) -> None:
        self.mainloop()

    def __create_menu(self) -> None:
        self.menu = tk.Menu(self, font=f"{self.DEFAULT_FONT} 10")

        item = tk.Menu(self.menu, font=f"{self.DEFAULT_FONT} 10")
        item.add_command(label='Contato')
        item.add_command(label=f'{self._title} {self._version}')

        self.menu.add_cascade(label='Arquivo')
        self.menu.add_cascade(label='Configurações')
        self.menu.add_cascade(label='Sobre', menu=item)

        self.config(menu=self.menu)

    def __create_body(self):
        self.body_title = ttk.Label(self, text=self._description, font=f"{self.DEFAULT_FONT} 20 bold")
        self.body_title.grid(row=0, column=1, columnspan=2, pady=10, padx=30)

        entries_validation_cmd = (self.register(self._validate_and_convert_callback), '%d %P %W')

        self.entry_1 = ttk.Entry(self, width=30, name=self.FIRST_ENTRY_ID_NAME, font=f"{self.DEFAULT_FONT} 12")
        self.entry_1.config(validate='key', validatecommand=entries_validation_cmd)
        self.entry_1.grid(row=1, column=1)
        self.select_1_value = tk.StringVar()
        self.select_1 = ttk.Combobox(self, textvariable=self.select_1_value, width=5, font=f"{self.DEFAULT_FONT} 12")
        self.select_1['values'] = self._conversible_units_list
        self.select_1.grid(row=1, column=2)
        self.select_1.config(state="readonly")
        self.select_1.bind('<<ComboboxSelected>>', self._handle_entry_unit_selected)
        self.select_1.current(0 if self._conversible_units_list else None)
        self.label_1 = ttk.Label(self, text='', font=f"{self.DEFAULT_FONT} 8", foreground='red')
        self.label_1.grid(row=2, column=1, sticky=tk.E + tk.W, padx=4)

        self.entry_2_value = tk.StringVar()
        self.entry_2 = ttk.Entry(self, textvariable=self.entry_2_value, width=30, name=self.SECOND_ENTRY_ID_NAME, font=f"{self.DEFAULT_FONT} 12")
        self.entry_2.config(validate='key', validatecommand=entries_validation_cmd)
        self.entry_2.bind("<Key>", self._handle_entry_2_key_event)
        self.entry_2.grid(row=3, column=1)
        self.select_2_value = tk.StringVar()
        self.select_2 = ttk.Combobox(self, textvariable=self.select_2_value, width=5, font=f"{self.DEFAULT_FONT} 12")
        self.select_2['values'] = self._unit_available_convertions(self._conversible_units_list[0]) if self._conversible_units_list else []
        self.select_2.grid(row=3, column=2)
        self.select_2.config(state="readonly")
        self.select_2.bind('<<ComboboxSelected>>', self._handle_entry_unit_selected)
        self.select_2.current(0 if self._conversible_units_list else None)
        self.label_2 = ttk.Label(self, text='', font=f"{self.DEFAULT_FONT} 8", foreground='red')
        self.label_2.grid(row=4, column=1, sticky=tk.E + tk.W, padx=4)

    def _alert_user(self, message: str) -> str:
        return messagebox.showwarning(title='Atenção', message=message)

    def _convert(self, value: str, widget_name: str) -> bool:
        if value != '' and not self._is_valid_number(value):
            self._alert_user('Valor Inválido Fornecido Para Converção')
            return False

        if widget_name == self.FIRST_ENTRY_ID_NAME:
            result = ''
            value = value[:-1] if value.endswith('.') else value

            if value != '':
                convert_from_unit = self.select_1.get()
                convert_to_unit = self.select_2.get()

                value_from = self._objectify(value, convert_from_unit)

                if value_from and (convert := self._get_convertion_method(convert_from_unit, convert_to_unit)):
                    result = convert(value_from).value
                    # result = round(result, self._number_of_decimal_places(value))
                    result = int(result) if int(result) == result else result
                else:
                    self._alert_user(f'Erro durante a converção de {convert_from_unit!r} para {convert_to_unit!r}')
                    return False

            self.entry_2_value.set(result)
        elif widget_name == self.SECOND_ENTRY_ID_NAME:
            pass # NOTE: this would be implemented for a bidirectional convertion

        return True

    def _validate_and_convert_callback(self, value: str) -> bool:
        INVALID_MESSAGE = 'Só é permitido introduzir valores numéricos'
        code, entry, widget = value.split()

        widget = widget.strip()
        widget = widget[1:] if widget.startswith('.') else widget

        valid = self._is_valid_number(entry) or code == '0' and entry == '{}'

        if widget == self.FIRST_ENTRY_ID_NAME:
            self.label_1.config(text=INVALID_MESSAGE if not valid else '')
        elif widget == self.SECOND_ENTRY_ID_NAME:
            self.label_2.config(text=INVALID_MESSAGE if not valid else '')

        return self._convert(entry if entry != '{}' else '', widget) if valid else valid

    def _handle_entry_unit_selected(self, _):
        convert_to_unit = self.select_2.get()
        values = self._unit_available_convertions(self.select_1.get())
        self.select_2.config(values=values)
        self.select_2.current((values.index(convert_to_unit) if convert_to_unit in values else 0) if values else None)
        self._convert(self.entry_1.get(), self.FIRST_ENTRY_ID_NAME)

    def _objectify(self, value: int | float | str, unit_ref: str) -> any or None:
        """Converts the `value` param into a unit value object if it is possible, else return None."""
        if unit_ref in self._conversible_units_list and isinstance(value, (int, float, str)):
            return self.units.UNITS_MAPPER[unit_ref](float(value))
        return None

    def _is_valid_number(self, value: str) -> bool:
        if '.' in value and len((_vals := value.split('.'))) == 2:
            return _vals[0].isnumeric() and (_vals[1].isnumeric() or _vals[1] == '')
        return value.isnumeric()

    def _handle_entry_2_key_event(self, e) -> str:
        return "break"

    def _number_of_decimal_places(self, value) -> int:
        if not self._is_valid_number(value) or not '.' in value:
            return 0
        return len(value.split('.')[1])