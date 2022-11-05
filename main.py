from teleconverter import *

if __name__ == '__main__':
    a = DB(90)
    b = Teleconverter(a).to_dbm()
    print(f'{a} = {b}')
