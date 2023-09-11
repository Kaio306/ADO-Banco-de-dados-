import os
import sqlite3

caminho = 'C:\\Users\\Administrador\\Desktop\\BD\\contatos.db'

try:
    con = sqlite3.connect(caminho)
except sqlite3.Error as ex:
    print("Erro na conexão com o banco de dados")
else:
    print("A conexão com o banco de dados efetuada com sucesso")
    
vsql="""CREATE TABLE IF NOT EXISTS tb_contatos(ID_CONTATO INTEGER PRIMARY KEY AUTOINCREMENT, NOME_CONTATO CHAR, TELEFONE_CONTATO CHAR, E_MAIL_CONTATO CHAR)"""

try: 
    c = con.cursor()
    c.execute(vsql)
except sqlite3.OperationalError as ex:
    print(ex)
else:
    print("Tabela criada com sucesso")
    
def menuinserir():
    os.system("cls")
    vnome = input("Digite o Nome: ")
    vtelefone = input("Digite o Telefone: ")
    vemail = input("Digite o email: ")
    caminho = 'C:\\Users\\Administrador\\Desktop\\BD\\contatos.db'
    try:
        con = sqlite3.connect(caminho)
        c = con.cursor()
        c.execute("INSERT INTO tb_contatos(NOME_CONTATO, TELEFONE_CONTATO, E_MAIL_CONTATO) VALUES(?,?,?)",(vnome,vtelefone,vemail))
        con.commit()
    except sqlite3.Error as ex:
        print(ex)
        os.system("pause")
    finally:
        print("Registro adicionado com sucesso")
        con.close()
        os.system("pause")
        
def menuconsultar():
    os.system("cls")    
    caminho = 'C:\\Users\\Administrador\\Desktop\\BD\\contatos.db'
    try:
        con = sqlite3.connect(caminho)
        c = con.cursor()
        c.execute("SELECT * from tb_contatos")
        res = c.fetchall()
        vlimite = 10
        vcont = 0
        for r in res:
            print( "ID:{0:_^3} Nome: {1:_^30} Telefone {2:_^17} E-mail: {3:_^30}".format(r[0],r[1],r[2],r[3]))
            vcont +=1
            if(vcont >= vlimite):
                vcont = 0
                os.system("pause")
                os.system("cls")
            print("Fim da Lista")
            print("Registros consultados com sucesso")
            os.system("pause")
    except sqlite3.Error as ex:
        print(ex)        
        os.system("pause")
    finally:
        con.close()
        
def menuconsultarNome():
    os.system("cls")
    caminho = 'C:\\Users\\Administrador\\Desktop\\BD\\contatos.db'
    v_nome = input("Digite o nome do contato: ")
    v_sql = "Select * from tb_contatos WHERE nome_contato LIKE '%"+v_nome+"%'"
    try:
        con = sqlite3.connect(caminho)
        c = con.cursor()
        c.execute(v_sql)
        res = c.fetchall()
        vlimite = 10
        vcont = 0
        for r in res:
            print( "ID:{0:_<3} Nome: {1:_<30} Telefone {2:_<17} E-mail: {3:_<30}".format(r[0],r[1],r[2],r[3]))
            vcont +=1
            if(vcont >= vlimite):
                vcont = 0
                os.system("pause")
                os.system("cls")
            print("Fim da Lista")
            print("Registros consultados com sucesso")
            os.system("pause")
    except sqlite3.Error as ex:
        print(ex)
        os.system("pause")
    finally: 
        con.close()
    
def menudeletar():
    os.system("cls")
    caminho = 'C:\\Users\\Administrador\\Desktop\\BD\\contatos.db'
    try:
        v_id_contato = input("Digite o ID do contato: ")
        con = sqlite3.connect(caminho)
        c = con.cursor()
        c.execute("SELECT * from tb_contatos WHERE ID_CONTATO  =?", (v_id_contato))
        r = c.fetchall()
        if len(r) > 0:
            print( "ID:{0:_<3} Nome: {1:_<30} Telefone {2:_<17} E-mail: {3:_<30}".format(r[0][0],r[0][1],r[0][2],r[0][3]))
            print("Registro consultado com sucesso")
            decide = input("Confirme a exclusao do registro acima (S/N): ")
            if decide.upper() == "S":
                try:
                    v_sql_deleta = "DELETE FROM tb_contatos WHERE ID_CONTATO = " + v_id_contato
                    c.execute(v_sql_deleta)
                    con.commit()
                except sqlite3.Error as ex:
                    print(ex)
                finally:
                    print("Resgistro excluido com sucesso")
                    os.system("pause")
        else:
            print("Registro não localizado")
            os.system("pause")
    except sqlite3.Error as ex:
        print(ex)
        os.system("pause")
    finally:
        con.close()
        
def menuatualizar():
    os.system("cls")
    caminho = 'C:\\Users\\Administrador\\Desktop\\BD\\contatos.db'
    try:
        v_id_contato = input("Digite o ID do Contato: ")
        con = sqlite3.connect(caminho)
        c = con.cursor()
        c.execute("SELECT * from tb_contatos WHERE ID_CONTATO = ? ", (v_id_contato))
        r = c.fetchall()
        if len(r) > 0:
            print( "ID:{0:_<3} Nome: {1:_<30} Telefone {2:_<17} E-mail: {3:_<30}".format(r[0][0],r[0][1],r[0][2],r[0][3]))
            print("Registro consultado com sucesso")
            v_nome = input("Digite o novo nome: ")
            if len(v_nome) == 0:
                v_nome = r[0][1]
                
            v_telefone = input("Digite o novo telefone: ")
            if len(v_telefone) == 0:
                v_telefone [0][2]
                
            v_email = input("Digite o novo e-mail: ")
            if len(v_email) == 0:
                v_email [0][3]
            
            print("================================================== Novos Dados ==================================================")
            print("ID: {0:_<3} Nome: {1:_<30} Telefone: {2:_<17} E-mail: {3:_<30}".format(r[0][0],v_nome,v_telefone,v_email))
            decide = input("Confirme a alateracao (S/N): ")
            if decide.upper() == "S":
                try:
                    v_sql_atualiza = "UPDATE tb_contatos SET NOME_CONTATO = ?, TELEFONE_CONTATO = ?, E_MAIL_CONTATO = ? WHERE ID_CONTATO =" + v_id_contato
                    c.execute(v_sql_atualiza,(v_nome, v_telefone, v_email))
                    con.commit()
                except sqlite3.Error as ex:
                    print(ex)
                finally:
                    print("Registro atualizado com sucesso")
                    os.system("pause")
            else:
                print("Registro nao localizado")
                os.system("pause")
    except sqlite3.Error as ex:
        print(ex)
        os.system("pause")
    finally:
        con.close()            
                             
        
def menuprincipal():
    os.system("cls")
    print("1 - Inserir Novo Registro")
    print("2 - Deletar Registro")
    print("3 - Atualizar Registro")
    print("4 - Consultar Registros")
    print("5 - Consultar Registros por Nome")
    print("6 - Sair")
    
opc = 0
while opc !=6:
    menuprincipal()
    opc = int(input("Digite uma opcao: "))
    if opc == 1:
        menuinserir()
    elif opc == 2:
        menudeletar()
    elif opc == 3:
        menuatualizar()
    elif opc == 4:
        menuconsultar()
    elif opc == 5:
        menuconsultarNome()
    elif opc == 6:
        os.system("cls")
        print("Programa Finalizado")
else:
    os.system("cls")
    print("Programa Finalizado")
    os.system("pause")