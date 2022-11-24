import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class Application(tk.Tk):
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
        return list(self.units.units_mapper.keys()) if self.units is not None else []

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

        self.entry_1 = ttk.Entry(self, width=30, name='entry_1', font=f"{self.DEFAULT_FONT} 12")
        self.entry_1.config(validate='key', validatecommand=entries_validation_cmd)
        self.entry_1.grid(row=1, column=1)
        self.select_1_value = tk.StringVar()
        self.select_1 = ttk.Combobox(self, textvariable=self.select_1_value, width=5, font=f"{self.DEFAULT_FONT} 12")
        self.select_1['values'] = self._conversible_units_list
        self.select_1.grid(row=1, column=2)
        self.select_1.current(newindex=0 if self._conversible_units_list else None)
        self.select_1.config(state="readonly")
        self.label_1 = ttk.Label(self, text='', font=f"{self.DEFAULT_FONT} 8", foreground='red')
        self.label_1.grid(row=2, column=1, sticky=tk.E + tk.W, padx=4)

        self.entry_2 = ttk.Entry(self, width=30, name='entry_2', font=f"{self.DEFAULT_FONT} 12")
        self.entry_2.config(validate='key', validatecommand=entries_validation_cmd, state=tk.DISABLED)
        self.entry_2.grid(row=3, column=1)
        self.select_2_value = tk.StringVar()
        self.select_2 = ttk.Combobox(self, textvariable=self.select_2_value, width=5, font=f"{self.DEFAULT_FONT} 12")
        self.select_2['values'] = self._conversible_units_list
        self.select_2.grid(row=3, column=2)
        self.select_2.current(newindex=0 if self._conversible_units_list else None)
        self.select_2.config(state="readonly")
        self.label_2 = ttk.Label(self, text='', font=f"{self.DEFAULT_FONT} 8", foreground='red')
        self.label_2.grid(row=4, column=1, sticky=tk.E + tk.W, padx=4)

    def _alert_user(self, message: str) -> str:
        return messagebox.showwarning(title='Atenção', message=message)

    def _convert(self, value: str, widget_name: str) -> bool:
        #TODO: implement convertion
        return True

    def _validate_and_convert_callback(self, value: str) -> bool:
        INVALID_MESSAGE = 'Só é permitido introduzir valores numéricos'
        code, entry, widget = value.split()

        widget = widget.strip()
        widget = widget[1:] if widget.startswith('.') else widget

        valid = True
        if code == '1' or code == '0':
            if '.' in entry and len((_vals := entry.split('.'))) == 2:
                valid = _vals[0].isnumeric() and (_vals[1].isnumeric() or _vals[1] == '')
            else:
                valid = entry.isnumeric() or (code == '0' and entry == '{}')

        if widget == 'entry_1':
            self.label_1.config(text=INVALID_MESSAGE if not valid else '')
        elif widget == 'entry_2':
            self.label_2.config(text=INVALID_MESSAGE if not valid else '')

        return self._convert(entry[:-1] if entry.endswith('.') else entry, widget) if valid else valid

    def _objectify(self, value: int | float | str, unit_ref: str) -> any or None:
        """Converts the `value` param into a unit value object if it is possible, else return None."""
        if unit_ref in self._conversible_units_list and isinstance(value, (int, float, str)):
            return self.units.units_mapper[unit_ref](float(value))
        return None

