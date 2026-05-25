# LISTA DE VEÍCULOS CADASTRADOS
registered_vehicles = []


# FUNÇÃO PARA CADASTRAR VEÍCULOS
def register_vehicles():
    while True:
        print()
        print("=" * 10 + " CADASTRO DE VEÍCULO " + "=" * 10)

        # Variáveis de dados dos veículos
        vehicle_name = input("Nome: ").strip()
        vehicle_types = {
            1: "Carro", 
            2: "Moto", 
            3: "Caminhão", 
            4: "Ônibus", 
            5: "Van"
        }

        # Imprimir o dicionário de veículos
        for key, value in vehicle_types.items():
            print(f"{key} - {value}")

        # Receber entrada do tipo de veículo
        option_type = input("Opção selecionada: ").strip()

        # Verificação das opções e entardas
        if not vehicle_name:
            print("Preencha o nome do veículo antes de continuar!")
            continue

        if not option_type not in range(1, 6):
            print("Escolha apenas as opções entre 1 e 5, tente novamente!")
            continue

        # Criar um código único para os veículos
        vehicle_code = len(registered_vehicles) + 1

        # Adicionar informação a lista de veículos
        registered_vehicles.append({
            "Código": vehicle_code, 
            "Nome": vehicle_name,
            "Tipo": option_type
        })

        # Informações de cadastro
        print()
        print("Veículo cadastrado com sucesso!")
        break  # Finalizar loop e voltar ao menu inici
        al


# FUNÇÃO PARA LISTAR VEÍCULOS
def list_vehicles():
    print()
    print("=" * 10 + " LISTA DE VEÍCULOS " + "=" * 10)

    if not registered_vehicles:
        print("Nenhum veículo cadastrado ainda!")
    else:
        for vehicle in registered_vehicles:
            print(f"Código: {vehicle['Código']:<5} Nome: {vehicle['Nome']:<10} Tipo: {vehicle['Tipo']}")


# FUNÇÃO PARA EXCLUIR VEÍCULO
def delete_vehicle():
    while True:
        print()
        print("=" * 10 + " EXCLUIR DE VEÍCULO " + "=" * 10)

        delete_text = input("Nome: ").strip()

        if not delete_text:
            print("Preencha o nome do veículo!")
            return

        for vehicle in registered_vehicles:
            if delete_text.lower() == vehicle["Nome"].lower():
                registered_vehicles.remove(vehicle)
                print(f"Veículo removido: {vehicle['Nome']}")
                return

        print("Veículo não encontrado!")
        break
