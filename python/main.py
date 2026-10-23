nome_app = "estoque facil"
nome_tela = "login"

print(nome_app)
print("========================")
print(nome_tela)
print("========================")

usuario = input("usuario:")
senha = input("senha:")
print("========================")


if(usuario == "bia" and senha == "senha"):
  print("usuario liberado")

else:
  print("usuario ou senha errada")