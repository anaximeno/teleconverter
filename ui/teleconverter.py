import tkinter as tk


class Application(tk.Frame):
    def __init__(self, title: str = "Teleconverter") -> None:
        tk.Frame.__init__(self, None)
        self.grid()
        self.createWidgets()

        self._title = title
        self.master.title(self._title)

    def createWidgets(self) -> None:
        self.quitButton = tk.Button(self, text='Quit', command=self.quit())
        self.quitButton.grid()

    def run(self) -> None:
        self.mainloop()
