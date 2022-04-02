def trataString(str):

    strTratada = str.title()
    if('-' in strTratada):
        strTratada = strTratada.replace('-', '')
    
    return strTratada


def main():
    print('get'+trataString('modo-entrada'))
    print('get'+trataString('tipo-processamento'))
    print('get'+trataString('bandeira'))

      
main()

