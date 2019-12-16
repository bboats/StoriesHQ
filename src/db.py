import os
import psycopg2

# con = psycopg2.connect(
#     host = "localhost",
#     database = "testDB",
#     user = "postgres",
#     password = '777123',
# )

# cursor = con.cursor()
# cursor.execute("select * from empregados")
# print(cursor.fetchall())

# con.commit()

lista_de_consultas_pre_fabricadas = [ ('select * from pipipi'), ('outra consulta muito legal') ]

def consultas_pre_fabricadas():
  print('executando as 10 consultas premade')
  for consulta in lista_de_consultas_pre_fabricadas:
    print('executando ' + consulta)

def executar_consulta(consulta):
  print('executando: ' + consulta)


escolha_do_usuario = ""
while escolha_do_usuario != '0' :
  os.system('cls')
  print('1: Rodar demonstracao do SGBD ( 10 consultas pre-fabricadas ).\n'
        '2: Rodar uma consulta de sua escolha.\n'
        '\n0: Encerrar o programa.')
  escolha_do_usuario = input('Escolha?  ')

  if escolha_do_usuario == '1':
    consultas_pre_fabricadas()
    input('\n\nPressione enter para retornar ao menu!')
  elif escolha_do_usuario == '2':
    consulta_customizada = input('Qual sua consulta?\n')
    executar_consulta(consulta_customizada)
    input('\n\nPressione enter para retornar ao menu!')
  elif escolha_do_usuario == '0':
    # con.close()
    break
