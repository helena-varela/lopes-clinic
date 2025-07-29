import consultas, medicos, pacientes
import os


def limpar_terminal():
    """Limpa o terminal independente do sistema operacional."""
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    print("-" * 40)
    print("\tBem-vindo a Lopes Clinic\n")
    print("1 - Consultas")
    print("2 - Pacientes")
    print("3 - Médicos")
    print("4 - Pagamentos")
    print("5 - Limpar tela")
    print("-" * 40)
    escolha = int(input("No que podemos te ajudar hoje?\n"))
    
    while True:
        print("\n")
        if escolha == 1:
            consultas
        elif escolha == 2:
            pacientes
        elif escolha == 3:
            medicos
        elif escolha == 4:
            print("-" * 30)
            print("\t Pagamentos\n")
            print("1 - Preço da Consulta")
            print("2 - Pagamento médicos")
            print("3 - Gastos Essenciais")
            print("4 - Voltar ao Menu Principal")
            print("5 - Limpar tela")
            print("-" * 30)
            escolha4 = int(input("No que podemos te ajudar hoje?\n"))
            if escolha4 == 1:
                ...
            elif escolha4 ==2:
                ...
            elif escolha4 == 3:
                ...
            elif escolha4 == 4:
                break
            elif escolha4 == 5:
                limpar_terminal()
                
        elif escolha == 5:
            limpar_terminal()
            break