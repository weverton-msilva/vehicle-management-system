# IMPORTA ARQUIVO DO PROJETO
import vehicles

# FUNÇÃO DE INTERFACE DO USUÁRIO
def interface_user():
    print()
    print("=" * 10 + " SISTEMA DE VEÍCULOS " + "=" * 10)

    # Dicionário de opções disponíveis
    options_menu = {
        1: "Cadastrar veículo",
        2: "Listar Veículos",
        3: "Excluir veículos",
        4: "Sair do sistema"
    }

    # Imprimir o dicionário de opções
    for key, value in options_menu.items():
        print(f"{key} - {value}")

    # Receber e retorna a entrada de dados
    user_menu = input("Opção: ").strip()
    return user_menu


# INTERFACE E REDIRECIONAMENTO DO USUÁRIO
while True:
    user_menu = interface_user()

    # Verificar campo vazio
    if not user_menu:
        print("Preencha os campos!")
        continue

    # Verificar a entrada apenas com números
    try:
        option = int(user_menu)

        # Verificar número informado
        if option not in range(1, 5):
            print("Escolha apenas opções entre 1 e 4")
            continue

        # Sair do sistema se entrada for igual a '4'
        if option == 4:
            print("Saindo do sistema...")
            break

        # Dicionário para as funções
        options_menu = {
            1: vehicles.register_vehicles,
            2: vehicles.list_vehicles,
            3: vehicles.delete_vehicle
        }

        # Redirecionar usuário conforme opção
        options_menu[option]()
        
    except ValueError:
        print("Preencha apenas com números informados em tela")
