# TODO: Criar um programa de cadastro de usuário
# TODO: Nome,CPF, ID
# TODO: o uuid sera usado pra cada user tem sua chave unica
# TODO: o cpf é um dado sensivel,logo sera salvo no banco criptografado pelo SHA256

#libs
import sqlite3
from uuid import uuid4
from hashlib import sha256

def db_commands(command):
    con = sqlite3.connect('cadastro-user.db')
    cur = con.cursor()
    try:
        cur.execute('CREATE TABLE users(NOME text,ID text,CPF text)')
    except: pass

    # outros comandos
    cur.execute(command)
    con.commit()
    con.close()

# MENU

# inicializando as variaveis
menu = ['NOME', 'CPF']
user = []
validationCPF = 0
shaCPF = ''
id = ''


print('BEM VINDO AO CADASTRO DE USUÁRIO')
for index, item in enumerate(menu):

    userInput = input(f'{item}: ')
    if item == 'CPF':
        if len(userInput) == 11 and userInput.isnumeric():
            for itemCPF in userInput:
                validationCPF += int(itemCPF)
                # print(f'Item do CPF: {itemCPF} e por enquanto a soma é: {validationCPF}')
            if validationCPF == 44 or validationCPF == 55 or validationCPF == 66:
                shaCPF = str(sha256(userInput.encode('utf-8')).hexdigest())
                user.append(shaCPF)
        else: raise Exception(f'Error: {item} inválido')
    elif item == 'NOME':
        id = str(uuid4())
        user.append(userInput)
        user.append(id)

#print(f'Nome: {user[0]}\nCPF: {user[1]}\nID: {user[2]}')
db_commands(f'INSERT INTO users(NOME, CPF, ID) VALUES("{user[0]}", "{user[1]}", "{user[2]}");')











