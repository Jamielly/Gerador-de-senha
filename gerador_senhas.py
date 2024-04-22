import random
import string

def gerar_senha(tamanho=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

def verificar_repeticao(senha, senhas_geradas):
    return senha not in senhas_geradas

def gerar_senhas_unicas(numero_senhas=5):
    senhas_geradas = set()
    senhas = []
    while len(senhas) < numero_senhas:
        senha = gerar_senha()
        if verificar_repeticao(senha, senhas_geradas):
            senhas.append(senha)
            senhas_geradas.add(senha)
    return senhas

# Gerar e imprimir até 5 senhas únicas
senhas = gerar_senhas_unicas()
for senha in senhas:
    print(senha)
