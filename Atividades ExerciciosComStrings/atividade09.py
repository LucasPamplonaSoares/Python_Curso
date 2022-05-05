# Verificação de CPF. 
# Desenvolva um programa que solicite a digitação de um número de CPF no formato xxx.xxx.xxx-xx e indique se é um número válido ou inválido através da validação dos dígitos verificadores edos caracteres de formatação.

def verificarNumeros(cpf): 
    for posicao,caractere in enumerate(cpf): 
        if posicao!=3 and posicao!=7 and posicao!=11 and not caractere.isdigit(): 
            return True 
    return False 

cpf = input("CPF(xxx.xxx.xxx-xx) :") #3 7 11

while verificarNumeros(cpf) or cpf[3] !="." or cpf[7] !="." or cpf[11] !="-":
    cpf = input("O 'CPF' pricisa estar no formato (xxx.xxx.xxx-xx) :")

print("O 'CPF' está no formato correto")