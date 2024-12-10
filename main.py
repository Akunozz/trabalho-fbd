import mysql.connector

# Função para estabelecer a conexão com o banco de dados
def conectar_banco():
    try:
        conexao = mysql.connector.connect(
            host='localhost',   
            user='root',        
            password='admin',
            database='trabalho_academico',
             charset='utf8mb4',
            collation='utf8mb4_general_ci'
        )
        print("Conexão estabelecida com sucesso!")
        return conexao
    except mysql.connector.Error as err:
        print(f"Erro ao conectar ao banco: {err}")
        return None

# incluir processo
def incluir(conexao):
    cursor = conexao.cursor()
    
    try:
        numero = input("Digite o número do processo: ")
        deliberacao = input("Digite a deliberação: ")
        transito = input("Digite a data de trânsito: ")
        datafinal = input("Digite a data final: ")
        dataacordao = input("Digite a data do acórdão: ")
        responsavel_id = int(input("Digite o ID do responsável: "))
        query = """
        INSERT INTO processo (numero, deliberacao, transito, datafinal, dataacordao, responsavel_id)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (numero, deliberacao, transito, datafinal, dataacordao, responsavel_id))
        conexao.commit()
        print("Registro incluído com sucesso!")
    except ValueError:
        print("Erro: Certifique-se de que os IDs e datas estão nos formatos corretos.")
    except mysql.connector.Error as err:
        print(f"Erro ao incluir registro no banco de dados: {err}")

# alterar processo
def alterar(conexao):
    cursor = conexao.cursor()
    registro_id = input("Digite o ID do registro que deseja alterar: ")
    print("Campos disponíveis para alteração:")
    print("1 - Número do Processo")
    print("2 - Deliberação")
    print("3 - Data de Trânsito")
    print("4 - Data Final")
    print("5 - Data do Acórdão")
    print("6 - ID do Responsável")
    campo_opcao = input("Digite o número do campo que deseja alterar: ")
    if campo_opcao == "1":
        novo_valor = input("Digite o novo número do processo: ")
        query = "UPDATE processo SET numero = %s WHERE id = %s"
    elif campo_opcao == "2":
        novo_valor = input("Digite a nova deliberação: ")
        query = "UPDATE processo SET deliberacao = %s WHERE id = %s"
    elif campo_opcao == "3":
        novo_valor = input("Digite a nova data de trânsito: ")
        query = "UPDATE processo SET transito = %s WHERE id = %s"
    elif campo_opcao == "4":
        novo_valor = input("Digite a nova data final: ")
        query = "UPDATE processo SET datafinal = %s WHERE id = %s"
    elif campo_opcao == "5":
        novo_valor = input("Digite a nova data do acórdão: ")
        query = "UPDATE processo SET dataacordao = %s WHERE id = %s"
    elif campo_opcao == "6":
        novo_valor = int(input("Digite o novo ID do responsável: "))
        query = "UPDATE processo SET responsavel_id = %s WHERE id = %s"
    else:
        print("Opção inválida!")
        return
    try:
        cursor.execute(query, (novo_valor, registro_id))
        conexao.commit()
        print("Registro alterado com sucesso!")
    except mysql.connector.Error as err:
        print(f"Erro ao alterar registro: {err}")

# excluir processo
def excluir(conexao):
    cursor = conexao.cursor()
    registro_id = input("Digite o ID do registro que deseja excluir: ")
    try:
        query = "DELETE FROM processo WHERE id = %s"
        cursor.execute(query, (registro_id,))
        conexao.commit()
        print("Registro excluído com sucesso!")
    except mysql.connector.Error as err:
        print(f"Erro ao excluir registro: {err}")

# consultar processos
def consultar(conexao):
    cursor = conexao.cursor()
    try:
        query = "SELECT * FROM processo"
        cursor.execute(query)
        resultados = cursor.fetchall()
        print("\n=== Resultados da Consulta ===")
        for linha in resultados:
            print(linha)
    except mysql.connector.Error as err:
        print(f"Erro ao consultar registros: {err}")

###################################################################################################

def incluir_responsavel(conexao):
    cursor = conexao.cursor()

    try:
        nome = input("Digite o nome do responsável: ")
        cpf = input("Digite o CNPJ do responsável: ")
        uf = input("Digite o estado (UF) do responsável: ")
        query = """
        INSERT INTO responsavel (nome, cpf, uf)
        VALUES (%s, %s, %s)
        """
        cursor.execute(query, (nome, cpf, uf))
        conexao.commit()
        print("Responsável incluído com sucesso!")
    except mysql.connector.Error as err:
        print(f"Erro ao incluir responsável no banco de dados: {err}")

def alterar_responsavel(conexao):
    cursor = conexao.cursor()
    id_responsavel = input("Digite o ID do responsável que deseja alterar: ")
    print("Campos disponíveis para alteração:")
    print("1 - Nome do Responsável")
    print("2 - CNPJ")
    print("3 - UF")
    campo_opcao = input("Digite o número do campo que deseja alterar: ")
    if campo_opcao == "1":
        novo_valor = input("Digite o novo nome do responsável: ")
        query = "UPDATE responsavel SET nome = %s WHERE id = %s"
    elif campo_opcao == "2":
        novo_valor = input("Digite o novo CNPJ do responsável: ")
        query = "UPDATE responsavel SET cpf = %s WHERE id = %s"
    elif campo_opcao == "3":
        novo_valor = input("Digite o novo estado (UF) do responsável: ")
        query = "UPDATE responsavel SET uf = %s WHERE id = %s"
    else:
        print("Opção inválida!")
        return
    try:
        cursor.execute(query, (novo_valor, id_responsavel))
        conexao.commit()
        print("Responsável alterado com sucesso!")
    except mysql.connector.Error as err:
        print(f"Erro ao alterar responsável: {err}")


def excluir_responsavel(conexao):
    cursor = conexao.cursor()
    id = input("Digite o ID do responsável que deseja excluir: ")
    try:
        query = "DELETE FROM responsavel WHERE id = %s"
        cursor.execute(query, (id,))
        conexao.commit()
        if cursor.rowcount > 0:
            print(f"Responsável com ID {id} excluído com sucesso!")
        else:
            print(f"Responsável com ID {id} não encontrado.")
    except mysql.connector.Error as err:
        print(f"Erro ao excluir responsável: {err}")

def consultar_responsavel(conexao):
    cursor = conexao.cursor()
    try:
        query = "SELECT * FROM responsavel"
        cursor.execute(query)
        resultados = cursor.fetchall()
        if not resultados:
            print("Nenhum responsável encontrado.")
        else:
            print("\n=== Responsáveis Cadastrados ===")
            for linha in resultados:
                print(f"ID: {linha[0]}, Responsável: {linha[1]}, CPF: {linha[2]}, UF: {linha[3]}")
    except mysql.connector.Error as err:
        print(f"Erro ao consultar responsáveis: {err}")

# Menu
def menu():
    print("\n=== MENU ===")
    print("1. Incluir Processo")
    print("2. Alterar Processo")
    print("3. Excluir Processo")
    print("4. Consultar Processo")
    print("5. Incluir Responsável")
    print("6. Alterar Responsável")
    print("7. Excluir Responsável")
    print("8. Consultar Responsável")
    print("9. Sair")

def main():
    conexao = conectar_banco()
    if not conexao:
        return

    while True:
        menu()
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            incluir(conexao)
        elif opcao == '2':
            alterar(conexao)
        elif opcao == '3':
            excluir(conexao)
        elif opcao == '4':
            consultar(conexao)
        elif opcao == '5':
            incluir_responsavel(conexao)
        elif opcao == '6':
            alterar_responsavel(conexao)
        elif opcao == '7':
            excluir_responsavel(conexao)
        elif opcao == '8':
            consultar_responsavel(conexao)
        elif opcao == '9':
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")
    if conexao.is_connected():
        conexao.close()
        print("Conexão encerrada.")

if __name__ == "__main__":
    main()