# print('\n[1]Sacar \n[2]Extrato \n[0]Sair: \n')
# opcao = int(input('Resposta:'))
# match opcao:
#     case 1:
#         print('Sacando')
#     case 2:
#         print('Exibindo o extrato...')
#     case _:
#         print('Opção inválida!')

#Exemplo pratico:
# idade = int(input('Digite sua idade: '))
# match idade:
#     case i if i<12:
#         print('Você é uma criança!')
#     case i if 12<=i<18:
#         print('Você é um adolescente!')
#     case i if i>18:
#         print('Você é um adulto!')
#     case _:
#         print('Idade inválida!')

#Verifica numero par:
# numero = int(input('Digite um numero: '))

# match numero:
#     case n if 10<=n<=20 and n%2==0:
#         print('O numero esta entre 10 e 20, e é par.')
#     case n if 10<=n<=20 and n%2!=0:
#         print('O numero esta entre 10 e 20, mas não é par.')
#     case n if n<10 or n>20:
#         print('O numero esta fora do intervalo 10 a 20!')

#Valor e pipe(|):
numero = int(input("Digite um valor entre 1 e 5: "))
match numero:
    case 1|2:
        print('Numero baixo')
    case 3|4:
        print('Numero medio')
    case 5:
        print("Numero alto")
    case _:
        print('Numero fora do intervalo!')