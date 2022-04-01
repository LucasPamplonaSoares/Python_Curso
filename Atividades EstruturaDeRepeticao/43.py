# O cardápio de uma lanchonete é o seguinte:
# Especificação   Código  Preço
# Cachorro Quente 100     R$ 1,20
# Bauru Simples   101     R$ 1,30
# Bauru com ovo   102     R$ 1,50
# Hambúrguer      103     R$ 1,20
# Cheeseburguer   104     R$ 1,30
# Refrigerante    105     R$ 1,00
# Faça um programa que leia o código dos itens pedidos e as quantidades desejadas.
# Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido.
# Considere que o cliente deve informar quando o pedido deve ser encerrado.

codigos = [100, 101, 102, 104, 105]
comidas = ['Cachorro Quente', 'Bauru Simples', 'Bauru com ovo', 'Hambúrguer', 'Cheeseburguer', 'Refrigerante']
preco = [1.20, 1.30, 1.50, 1.20, 1.30, 1.0]
codigo = True
numeros_pedidos = 1
pedido = []

while codigo != 0:
    print('Pedido n° ', numeros_pedidos)
    codigo = int(input('Digite o código do alimento: '))
    if codigo == 0:
        break
    else:
        while codigo not in codigos:
            print('Este código está errado ou não está cadastrado')
            codigo = int(input('Digite o código de alimento: '))

        indice = codigos.index(codigo)
        quantidade = int(input('Digite a quantidade: '))
        valor_pedido = preco[indice] * quantidade
        pedido.append(valor_pedido)
    numeros_pedidos += 1

pedido_nota = 0
for i in range(numeros_pedidos - 1):
    print('Pedido n°', pedido_nota + 1, '= R$', round(pedido[pedido_nota], 2))
    pedido_nota += 1
print('Total: R$', round(sum(pedido), 2))