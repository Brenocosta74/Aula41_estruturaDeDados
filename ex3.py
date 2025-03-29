contatos = {}

def adicionar_contato():
  nome = input("Digite o nome do contato: ")
  telefone = input("Digite o número de telefone: ")
  contatos[nome] = telefone
  print(f"Contato {nome} adicionado com sucesso!")

def buscar_contato():
  nome = input("Digite o nome do contato: ")
  if nome in contatos:
    print(f"O número de telefone de {nome} é: {contatos[nome]}")
  else:
    print(f"Contato {nome} não encontrado.")

def listar_contatos():
  if contatos:
    print("Lista de contatos:")
    for nome, telefone in contatos.items():
      print(f"{nome}: {telefone}")
  else:
    print("Sua lista de contatos está vazia.")

while True:
  print("\nMenu:")
  print("1. Adicionar contato")
  print("2. Buscar contato")
  print("3. Listar contatos")
  print("4. Sair")

  opcao = input("Digite a opção desejada: ")

  if opcao == '1':
    adicionar_contato()
  elif opcao == '2':
    buscar_contato()
  elif opcao == '3':
    listar_contatos()
  elif opcao == '4':
    print("Até logo!")
    break
  else:
    print("Opção inválida.")
