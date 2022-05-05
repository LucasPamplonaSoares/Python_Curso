# Valida e corrige número de telefone. Faça um programa que leia um número de telefone, e corrija o número no caso deste conter somente 7 dígitos, acrescentando o '3' na frente. O usuário pode informar o número com ou sem o traço separador.

# Valida e corrige número de telefone
# Telefone: 461-0133
# Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.
# Telefone corrigido sem formatação: 34610133
# Telefone corrigido com formatação: 3461-0133

def corrigir_telefone(telefone, formatar=True):
    telefone_sem_hifen = telefone.replace('-', '')
    qtd_caracteres = len(telefone_sem_hifen)
    telefone_corrigido = telefone_sem_hifen

    if qtd_caracteres < 8:
        print(f'Telefone possui {qtd_caracteres} dígitos. Vou acrescentar o digito três na frente.')
        caracteres_faltantes = 8 - qtd_caracteres
        telefone_corrigido = caracteres_faltantes * '3' + telefone_sem_hifen

    if formatar:
        telefone_corrigido = telefone_corrigido[0:4] + '-' + telefone_corrigido[4:8]

    return telefone_corrigido


if __name__ == '__main__':
    print('Valida e corrige número de telefone:')
    print('Telefone:')
    telefone = str(input())

    print('Telefone corrigido sem formatação:', corrigir_telefone(telefone, formatar=False))
    print('Telefone corrigido com formatação:', corrigir_telefone(telefone))