from customtkinter import *
from sql_functions import *
import sqlite3

database = 'database.db'

# CORES:
azul_escuro1 = '#030912'
branco = '#ffffff'

# CRIAÇÃO DA JANELA:
program = CTk()
program.geometry("500x300")
set_appearance_mode("dark")

text = CTkLabel(program, text="SISTEMA DE CADASTROS COM PYHTON E SQL", bg_color="transparent", text_color="#fff")
text.pack(padx=10, pady=5)

# INPUTS / ENTRADA DE DADOS:
inputUsername = CTkEntry(program, placeholder_text="Nome de usuário", fg_color="#fff", text_color="#000", width=220)
inputUsername.pack(padx=10, pady=1)

inputEmail = CTkEntry(program, placeholder_text="E-mail", fg_color="#fff", text_color="#000", width=220)
inputEmail.pack(padx=10, pady=1)

inputTelefone = CTkEntry(program, placeholder_text="Telefone", fg_color="#fff", text_color="#000", width=220)
inputTelefone.pack(padx=10, pady=1)

# VARIÁVEIS DAS COLUNAS:
novo_username = ''
novo_email = ''
novo_telefone = ''


# FUNÇÃO PARA VER CADASTROS:
def ver_cadastros():
    try:
        inputUsername.destroy()
        inputEmail.destroy()
        inputTelefone.destroy()
        botaoCadastrar.destroy()
        botaoVerCadastros.destroy()
    except:
        print('Os botões já foram deletados!')
    finally:
        texto = CTkLabel(program, text='LISTA DE CADASTROS:', text_color='#fff')
        texto.pack(padx=10, pady=1)

    database_connect = sqlite3.connect(database)
    cursor = database_connect.cursor()

    # CRIAR TABELA (CASO NÃO EXISTA):
    criar_tabela(database)

    # BUSCAR REGISTROS DO BANCO DE DADOS:
    cursor.execute("""
    SELECT * FROM cadastros;
    """)

    for linha in cursor.fetchall():
        texto_registro = CTkLabel(program, text=f'Username: {linha[1]} | E-mail: {linha[2]} | Telefone: {linha[3]}', text_color='#fff')
        texto_registro.pack(padx=10, pady=1)

    database_connect.close()


def realizar_cadastro():
    global novo_username
    global novo_email
    global novo_telefone
    database_connect = sqlite3.connect(database)
    cursor = database_connect.cursor()

    # CRIAR TABELA (CASO NÃO EXISTA):
    criar_tabela(database)

    # INSERINDO DADOS NA TABELA:
    # INSERIR DADOS:
    cursor.execute('''
    INSERT INTO cadastros (username, email, telefone)
    VALUES (?, ?, ?)
    ''', (novo_username, novo_email, novo_telefone))

    database_connect.commit()

    database_connect.close()


# VERIFICAR POSSIBILIDADE DE CADASTRAR:
def verificar_cadastro():
    global novo_username
    global novo_email
    global novo_telefone
    try:
        novo_username = inputUsername.get()
        novo_email = inputEmail.get()
        novo_telefone = inputTelefone.get()
    except:
        print('Ocorreu um erro durante o cadastramento!')
    else:
        if novo_username == '':
            inputUsername.configure(placeholder_text='Nome de usuário é um campo obriagtório', placeholder_text_color='#FF0000')

        if novo_email == '':
            inputEmail.configure(placeholder_text='E-mail é um campo obrigatório', placeholder_text_color='#FF0000')

        if novo_telefone == '':
            inputTelefone.configure(placeholder_text='Telefone é um campo obrigatório', placeholder_text_color='#FF0000')
        elif not novo_telefone.isdigit():
            inputTelefone.delete(0, 15)
            inputTelefone.configure(placeholder_text='São permitidos apenas números', placeholder_text_color='#FF0000')

        if novo_username != '' and novo_email != '' and novo_telefone.isdigit():
            inputUsername.destroy()
            inputEmail.destroy()
            inputTelefone.destroy()
            realizar_cadastro()
            botaoCadastrar.destroy()
            textoSucesso.configure(text='Cadastro realizado com sucesso!')


# BOTÃO PARA CADASTRAR:
textoSucesso = CTkLabel(program, text='', text_color='#fff')
textoSucesso.pack(padx=10, pady=1)

botaoCadastrar = CTkButton(program, text="Cadastrar", command=verificar_cadastro)
botaoCadastrar.pack(padx=10, pady=1)

botaoVerCadastros = CTkButton(program, text='Ver cadastros', command=ver_cadastros)
botaoVerCadastros.pack(padx=10, pady=1)

botaoSair = CTkButton(program, text='Sair do programa', command=program.destroy)
botaoSair.pack(padx=10, pady=2)

program.mainloop()
