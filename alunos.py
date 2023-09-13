print("Olá! Digite o nome de cada aluno e suas respectivas notas")

alunos = []

for numero_do_aluno in range(1, 6):
    while True:
        nome = input(f'\nAluno {numero_do_aluno}: ')

        if(not nome.isdigit()):
            break
        
        print('Digite um nome válido (Sem números)')  

    while True:
        nota1 = float(input('Nota 1: '))
        nota2 = float(input('Nota 2: '))

        if(0 <= nota1 <= 10 and 0 <= nota2 <= 10):
            break
        else:
            print('Digite apenas valores entre 0 e 10:')

    aluno = {
        "nome": nome,
        "nota1": nota1,
        "nota2": nota2,
        "media aluno": (nota1 + nota2) / 2
        }
    
    alunos.append(aluno)

print('\n********************************')
print('Todos os dados foram cadastrados')
print('********************************\n')

soma_notas = 0

for aluno in alunos:
    soma_notas += aluno['nota1'] + aluno['nota2']

numero_de_alunos = len(aluno['nome'])

media_turma = soma_notas / numero_de_alunos

print("Lista de alunos e notas:\n")
for aluno in alunos:
    print(f"{aluno['nome']}: Nota 1 - {aluno['nota1']} / Nota 2 - {aluno['nota2']}\nMédia: {aluno['media aluno']}\n")

print('************************')
print(f"Média da turma: {media_turma:.2f}")
print('************************\n')