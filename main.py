from database import criar_tabela
import crud

def menu():
    criar_tabela()
    while True:
        print("\n--- Sistema de Controle de Contas ---")
        print("1. Cadastrar conta")
        print("2. Listar contas")
        print("3. Buscar conta por ID")
        print("4. Atualizar conta")
        print("5. Excluir conta")
        print("6. Marcar conta como paga")
        print("7. Consultar contas pendentes")
        print("8. Calcular total pendente")
        print("9. Calcular total pago")
        print("0. Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            descricao = input("Descrição: ")
            valor = float(input("Valor: "))
            crud.cadastrar_conta(descricao, valor)
        elif opcao == "2":
            for conta in crud.listar_contas():
                print(conta)
        elif opcao == "3":
            id = int(input("ID: "))
            print(crud.buscar_conta(id))
        elif opcao == "4":
            id = int(input("ID: "))
            descricao = input("Nova descrição: ")
            valor = float(input("Novo valor: "))
            crud.atualizar_conta(id, descricao, valor)
        elif opcao == "5":
            id = int(input("ID: "))
            crud.excluir_conta(id)
        elif opcao == "6":
            id = int(input("ID: "))
            crud.marcar_como_paga(id)
        elif opcao == "7":
            for conta in crud.contas_pendentes():
                print(conta)
        elif opcao == "8":
            print("Total pendente:", crud.total_pendente())
        elif opcao == "9":
            print("Total pago:", crud.total_pago())
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()

           