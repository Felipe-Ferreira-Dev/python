def trataString(str):

    if(str.find('-')):
        str = str.replace('-', ' ')
        str = str.title()
        strTratada = str.replace(' ', '')
        return strTratada
    else:
        str = str.title()
        strTratada = str
        return strTratada


def main():
    print('get'+trataString('modo-entrada'))
    print('get'+trataString('tipo-processamento'))
    print('get'+trataString('bandeira'))

      
main()

