def melhorAluno(alunos):
    maior_nota = 0
    melhorAluno = None  # Initialize to None

    for aluno in alunos:
        nota = float(aluno['nota'])
        if nota > maior_nota:
            maior_nota = nota
            melhorAluno = aluno  

    return melhorAluno

alunos = [
    {"nome": "Joao", "nota": 8.5},
    {"nome": "Bruno", "nota": 9},
    {"nome": "Pedro", "nota": 5},
    {"nome": "Lucas", "nota": 7}
]

melhorAluno = melhorAluno(alunos)
print("O melhor aluno é", melhorAluno['nome'], "com nota", melhorAluno['nota'])
