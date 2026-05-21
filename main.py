# IMPORTA ARQUIVO DE VEÍCULOS
import veiculos


# FUNÇÃO DE INTRODUÇÃO
def menu_usuario():
    print()
    print("=" * 10 + " SISTEMA DE FROTAS " + "=" * 10)

    print("[1] Cadastrar veículo")
    print("[2] Listar Veículos")
    print("[3] Excluir veículos")
    print("[4] Sair do sistema")
    user_menu = input("Opção: ").strip()

    return user_menu

    
# LOOP DO MENU DO USUÁRIO
while True:
    user_menu = menu_usuario()

    # Verificar se a entrada foi preenchida
    if not user_menu:
        print("Preencha o campo obrigatório!")
        continue

    try:
        # Converte entrada para inteiro
        opcao = int(user_menu)

        if opcao not in range(1, 5):
            print("Opção inválida, tente novamente!")
            continue

        elif opcao == 1:
            veiculos.cadastrar_veiculos()

        elif opcao == 2:
            veiculos.listar_veiculos()

        elif opcao == 3:
            veiculos.excluir_veiculo()
            
        elif opcao == 4:
            print("Saindo do sistema...")
            break
            
    except ValueError:
        print("Apenas números podem ser preenchidos!")
