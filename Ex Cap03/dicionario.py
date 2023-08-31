alunos = {}  # Dicionário para armazenar os dados dos alunos

while True:
    nome = input("Digite o nome do aluno (ou 'sair' para encerrar): ")
    if nome.lower() == "sair":
        break
    
    media = float(input("Digite a média do aluno: "))
    
    situacao = "AP" if media >= 60 else "RP"
    
    alunos[nome] = {"media": media, "situacao": situacao}

print("\nDados dos alunos:")
for nome, dados in alunos.items():
    print(f"Aluno: {nome}, Média: {dados['media']}, Situação: {dados['situacao']}")
