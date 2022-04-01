# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
# mostrando uma mensagem de erro e voltando a pedir as informações.

nome = str(input('Digite seu usuário: '))
senha = str(input('Digite a sua senha: '))
while senha == nome:
    senha = int(input('Sua senha não pode ser igual ao seu nome de login. Digite a sua senha: '))
print(f'Seu usuário é: {nome}')
print(f'Sua senha é: {senha}')