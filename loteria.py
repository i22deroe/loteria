import requests as r
import time
import sys

from datetime import datetime as dt

WAIT_TIME=30

url= 'https://api.elpais.com/ws/LoteriaNavidadPremiados'

def loteria(numeros):
    res = dict(eval(r.get(url+'?n={}'.format(numeros[0])).text[9:]))
    n_orig = len(numeros)
    while res['status'] < 3:
        print("[{}]: Comprobando números. {} han resultado premiados.".format(dt.now(), n_orig-len(numeros)))
        for n in numeros:
            res = dict(eval(r.get(url+'?n={}'.format(n)).text[9:]))
            if res['premio']:
                print("\007[{}]: ¡PREMIO AL NÚMERO {}: {}!".format(dt.now(), n, res['premio']))
                numeros.remove(n)
            time.sleep(WAIT_TIME)
    else:
        print("El sorteo ha terminado.")
        return(0)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Por favor indica al menos un número.")
        exit()
    if len(sys.argv) > 1:
        print("Vas a jugar con los números {}.".format(sys.argv[1:]))
        loteria(sys.argv[1:])
        exit()
    else:
        print("Por favor, indica al menos un número.")
        exit()
