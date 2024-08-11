lista_alunos = []

while True:
    nome = str(input('Nome do aluno(a): '))
    # Irá armazenar as notas em uma lista
    notas = []
    
    # Coleta as 4 notas
    avaliacoes = 1
    while avaliacoes < 5:
        nota = float(input(f'Avaliação {avaliacoes}: '))
        
        # Enquanto a nota não estiver entre 0 a 10, o loop permanecerá no mesmo índice
        if 0 <= nota <= 10:
            notas.append(nota)
            avaliacoes += 1
        else:
            print('As notas devem ser de 0 a 10!')

    # Calcula a média
    media = sum(notas) / len(notas)

    # Adiciona os alunos à lista de alunos
    lista_alunos.append({'Aluno': nome,'Notas': notas,'Media': media})

    # Verifica se há mais alunos para cadastrar
    resposta = input('Deseja continuar cadastrando mais alunos? (s/n): ').lower()
    if resposta != 's':
        break
# Retorno das informações cadastradas
print(f'\nForam cadastrados {len(lista_alunos)} alunos')
print('Boletim escolar dos alunos cadastrados:')
for aluno in lista_alunos:
    print("-=" * 20)
    print(f' Aluno: {aluno['Aluno']}')
    # Acessa a lista e usa join para formatar a saída, necessário utilizar o map str
    print(f' Notas: {', '.join(map(str, aluno['Notas']))}')
    print(f' Media: {aluno['Media']}')
    print("-=" * 20)