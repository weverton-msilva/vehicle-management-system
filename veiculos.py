# LISTA DE VEÍCULOS CADASTRADOS
veiculos_cadastrados = []


# FUNÇÃO PARA CADASTRAR VEÍCULOS
def cadastrar_veiculos():
    while True:
        print()
        print("=" * 10 + " CADASTRO DE VEÍCULO " + "=" * 10)
        
        nome_veiculo = input("Nome: ").strip()

        if not nome_veiculo:
            print("Preencha o nome do veículo!")
            continue

        # Criar um código único para os veículos
        codigo_veiculo = len(veiculos_cadastrados) + 1

        # Adicionar informação a lista de veículos
        veiculos_cadastrados.append({
            "Código": codigo_veiculo,
            "Nome": nome_veiculo
        })

        # Informações de cadastro
        print()
        print("Veículo cadastrado com sucesso!")
        break # Finalizar loop e voltar ao menu inicial


# FUNÇÃO PARA LISTAR VEÍCULOS
def listar_veiculos():
    print()
    print("=" * 10 + " LISTA DE VEÍCULOS " + "=" * 10)

    if not veiculos_cadastrados:
        print("Nenhum veículo cadastrado ainda!")
    else:
        for veiculo in veiculos_cadastrados:
            print(f"Código: {veiculo['Código']:<5} Nome: {veiculo['Nome']}")


# FUNÇÃO PARA EXCLUIR VEÍCULO
def excluir_veiculo():
    while True:
        print()
        print("=" * 10 + " EXCLUIR DE VEÍCULO " + "=" * 10)

        delete_veiculo = input("Nome: ").strip()

        if not delete_veiculo:
            print("Preencha o nome do veículo!")
            return

        for veiculo in veiculos_cadastrados:
            if delete_veiculo == veiculo['Nome']:
                veiculos_cadastrados.remove(veiculo)
                print("Veículo removido!")
                return

        # Variável para feedback ao usuário
        encontrado = False
        
        if not encontrado:
            print("Veículo não encontrado!")
            break