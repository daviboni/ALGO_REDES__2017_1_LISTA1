contador = 0

msg1 = ' Esse programa é voltado a Meninas entre 9 e 13 anos, para a vacinação da doença HPV. \n'
msg2 = 'Você irá digitar o  sexo F para Feminino e M para Masculino e logo após a idade. \n'
msg3 = 'Se o sexo for femino e a menina estiver entre 9 e 13 anos, irá ser contabilizado entre os abrangidos,\n'
msg4 = 'se for do sexo masculino ou a idade da menina náo estiver entre 9 e 13 anos sera ignorado.\n '
print(msg1,msg2,msg3,msg4)
print('Vamos Começar...\n')

for i in range(10):
    sexo = input("Digite o seu sexo(F/M):  ")
    if sexo == "F" or sexo == "f":
         idade = int(input("Digite sua idade: "))
         if (idade >= 9 and idade <=13):
            contador = contador +1
            print("DEVE SER VACINADA")
            print('Todal de Meninas vacinadas contra o HPV: ', contador)
         else:
              print("Não deve se vacinar")
              print('Total de meninas vacinadas contra o HPV: ',contador)
    else:
         print("Não deve se vacinar")
         print('Total de meninas vacinadas contra o HPV: ',contador)
