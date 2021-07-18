#!/usr/bin/env python3

# ------------------------------------------------------------------
# DESCRIPTION
#    Cesar encrypter/decrypter
#
# OPTIONS
#    -e, --encrypt                 Ingrese la string a encriptar.
#    -d, --decrypt                 Ingrese la string a desencriptar.
#    -h, --help                    Print this help
#
# EXAMPLES
#    $cesar.py -e foobar 2 => hqqdct
#    $cesar.py -d hqqdct 2 => foobar

# ------------------------------------------------------------------

# Encrypt: C = (M + b) % n
# Decrypt: M = (C - n) % n

# ------------------------------------------------------------------

import argparse

def encrypt(string, b, n, alfabeto, result):
    for letra_string in string:
        if letra_string in alfabeto:
            for index, letra_alfabeto in enumerate(alfabeto):
                if letra_string.lower()==letra_alfabeto.lower():
                        M = index
                        C = (M+b) % n
                        C = str(alfabeto[C])
                        result = result + C
        else:
            result = result + letra_string
    print(result)

def decrypt(enc_string, b, n, alfabeto, result):
    for letra_string in enc_string:
        for index, letra_alfabeto in enumerate(alfabeto):
            if letra_string.lower()==letra_alfabeto.lower():
                    C = index
                    M = (C-b) % n
                    M = str(alfabeto[M])
                    result = result + M
        else:
            result = result + letra_string
    print(result)

def parser():
    parser = argparse.ArgumentParser(conflict_handler='resolve', description='Cesar encrypt/decrypt. Enter --help for more information.\nExample: cesar.py -e foobar 3')
    parser.add_argument("-e", "--encrypt", help="Ingrese la string a encriptar.", action="store_true")
    parser.add_argument("-d", "--decrypt", help="Ingrese la string a desencriptar.", action="store_true")
    parser.add_argument("string", nargs='?', default="empty")
    parser.add_argument("desplazamientos", nargs='?',type=int, default=0)
    args = parser.parse_args()

    if args.string!='empty':
        if args.desplazamientos!=0:
            if args.encrypt:
                return ['encrypt', args.string, args.desplazamientos]
            else:
                return ['decrypt', args.string, args.desplazamientos]
        else:
            print('Ingrese la cantidad de desplazamientos a utilizar: -r [number]')
    else:
        parser.print_help()

banner = '''
=========================================================
    Cesar Encrypter and Decrypter por Gonzalo Benito

    Email: gu4n4rt@gmail.com
    Github: https://github.com/Guanart
=========================================================
'''
alfabeto = 'abcdefghijklmnñopqrstuvwxyz'
result = ''
n = len(alfabeto)

def main():
    print(banner)
    funcion = parser()
    if funcion==None:
        pass
    elif funcion[0]=='encrypt':
        encrypt(funcion[1], funcion[2], n, alfabeto, result)
    elif funcion[0]=='decrypt':
        decrypt(funcion[1], funcion[2], n, alfabeto, result)

if __name__ == '__main__':
    main()