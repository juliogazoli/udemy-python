"""
Exercício - sistema de perguntas e respostas
"""

# # Minha solução
# perguntas = [
#     {
#         'Pergunta': 'Quanto é 2+2?',
#         'Opções': ['1', '3', '4', '5'],
#         'Resposta': '4',
#     },
#     {
#         'Pergunta': 'Quanto é 5*5?',
#         'Opções': ['25', '55', '10', '51'],
#         'Resposta': '25',
#     },
#     {
#         'Pergunta': 'Quanto é 10/2?',
#         'Opções': ['4', '5', '2', '1'],
#         'Resposta': '5',
#     },
# ]

# acertos = 0
# contador = 0
# for pergunta in perguntas:
#     print(f'Pergunta: {pergunta["Pergunta"]}\n')
#     print('Opções:')
#     for indice, opcao in enumerate(pergunta['Opções']):
#         print(f'{indice}) {opcao}')
#     resposta_usuario = int(input('Escolha uma opção: '))
#     resposta_correta = pergunta['Opções'].index(pergunta['Resposta'])
#     if resposta_correta == resposta_usuario:
#         print('Acertou\n')
#         acertos += 1
#     else:
#         print('Errou\n')
#     contador += 1
# print(f'Você acertou {acertos} de {contador} perguntas.')


# Solução
perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

qtd_acertos = 0
for pergunta in perguntas:
    print('Pergunta:', pergunta['Pergunta'])
    print()
    
    opcoes = pergunta['Opções']
    for i, opcao in enumerate(opcoes):
        print(f'{i})', opcao)
    print()
    
    escolha = input('Escolha uma opção: ')
    
    acertou = False
    escolha_int = None
    qtd_opcoes = len(opcoes)
    
    if escolha.isdigit():
        escolha_int = int(escolha)
        
    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opcoes:
            if opcoes[escolha_int] == pergunta['Resposta']:
                acertou = True
    
    print()
    if acertou:
        qtd_acertos += 1
        print('Acertou 👍')
    else:
        print('Errou ❌ ')
        
    print()

print('Você acertou', qtd_acertos)
print('de', len(perguntas), 'perguntas.')
