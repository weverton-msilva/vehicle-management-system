# LISTA DE VEÍCULOS CADASTRADOS
registered_vehicles = []


# FUNÇÃO PARA CADASTRAR VEÍCULOS
def register_vehicles():
    while True:
        print()
        print("=" * 10 + " CADASTRO DE VEÍCULO " + "=" * 10)
        
        vehicle_name = input("Nome: ").strip()

        if not vehicle_name:
            print("Preencha o nome do veículo!")
            continue

        # Criar um código único para os veículos
        vehicle_code = len(registered_vehicles) + 1

        # Adicionar informação a lista de veículos
        registered_vehicles.append({
            "Código": vehicle_code,
            "Nome": vehicle_name
        })

        # Informações de cadastro
        print()
        print("Veículo cadastrado com sucesso!")
        break # Finalizar loop e voltar ao menu inicial


# FUNÇÃO PARA LISTAR VEÍCULOS
def list_vehicles():
    print()
    print("=" * 10 + " LISTA DE VEÍCULOS " + "=" * 10)

    if not registered_vehicles:
        print("Nenhum veículo cadastrado ainda!")
    else:
        for vehicle in registered_vehicles:
            print(f"Código: {vehicle['Código']:<5} Nome: {vehicle['Nome']}")


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
            if delete_text == vehicle['Nome']:
                registered_vehicles.remove(vehicle)
                print("Veículo removido!")
                return

        print("Veículo não encontrado!")
        break
