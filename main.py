import domain
import ui

ui.kraki.Application.inject(
    telecalculator=domain.telecalcultor,
    teleconverter=domain.teleconverter,
    units=domain.units,
)

if __name__ == '__main__':
    app = ui.kraki.Application()
    app.run()
