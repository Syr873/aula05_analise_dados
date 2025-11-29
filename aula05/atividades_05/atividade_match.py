  #Verificando numero
# numero = float(input('Digite um numero: '))
# match numero:
#     case i if i<0:
#         print('NEGATIVO')
#     case i if i>0:
#         print('POSITIVO')
#     case _:
#         print('NULO')

  #Classificação de vendas
# venda = float(input('Informe o valor de venda: '))
# match venda:
#     case i if i<100:
#         print('Venda pequena')
#     case i if 100<=i<500:
#         print('Venda média')
#     case _:
#         print('Venda alta')

  #Sistema de usuarios
# print('Bem-vindo \nSelecione a opçao: \n[1]Criar um usuario \n[2]Editar usuario \n[3]Visualizar usuario \n[4]Deletar usuario')
# opcao = int(input('Digite sua opçao: '))
# match opcao:
#     case 1:
#         print('Você escolheu criar um novo usuario')
#         usuario = input('Digite o nome do novo usuario: ')
#         print(f'Novo usuário adicionado: {usuario}')
#     case 2:
#         print('Você escolheu editar um usuario')
#         usuario01 = input('Informe o usuario a ser editado: ')
#         usuario02 = input('Digite o novo usuario: ')
#         print(f'Você editou {usuario01} para {usuario02}')
#     case 3:
#         print("Você escolheu visualizar um usuario: ")
#         usuario = input('Informe o usuario: ')
#         print(f'Exibindo informaçoes de {usuario}')
#     case 4:
#         print('Você escolheu deletar um usuario!!')
#         usuario = input('Informe o usuario a ser deletado: ')
#         print(f'{usuario} deletado!')
#     case _:
#         print('Opção inválida!')

  #Formas de pagamento
# print("Formas de Pagamento: \n[1]Pix \n[2]Débito \n[3]Crédito \n[4]Dinheiro")
# opcao = int(input('Informe sua escolha: '))
# match opcao:
#     case 1:
#         print('Opção 1: Pix! Desconto de 12%')
#         valor = float(input('Informe o valor da compra: '))
#         desconto = valor*(12/100)
#         total = valor - desconto
#         print(f'Valor original: {valor:.2f} \nDesconto de 12%: {desconto:.2f} \nTotal a pagar: R${total:.2f}')
#     case 2:
#         print('Opção 2: Débito! Desconto de 8%')
#         valor = float(input('Informe o valor da compra: '))
#         desconto = valor*(8/100)
#         total = valor - desconto
#         print(f'Valor original: {valor:.2f} \nDesconto de 8%: {desconto:.2f} \nTotal a pagar: R${total:.2f}')
#     case 3:
#         print('Opçâo 3: Crédito! Acréscimo de 7%')
#         valor = float(input('Informe o valor da compra: '))
#         acrescimo = valor*(7/100)
#         total = valor + acrescimo
#         print(f'Valor original: {valor:.2f} \nAcréscimo de 7%%: {acrescimo:.2f} \nTotal a pagar: R${total:.2f}')
#     case 4:
#         print('Opção 4: Dinheiro! Desconto de 15%')
#         valor = float(input('Informe o valor da compra: '))
#         desconto = valor*(15/100)
#         total = valor - desconto
#         print(f'Valor original: {valor:.2f} \nDesconto de 15%: {desconto:.2f} \nTotal a pagar: R${total:.2f}')
#     case _:
#         print('Opção inválida!')



        