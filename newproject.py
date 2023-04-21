import sys

while True:
    print("Menu:")
    print("1.Soma")
    print("2.Subtração")
    print("3.Divisão")
    print("4.Multiplicação")
    print("5.Sair")

    choice = input("Escolha a opção desejada: ")
   
    if choice == '1':
        value_1 = input()
        value_2 = input()
        value_1 = float(value_1)
        value_2 = float(value_2)
        sum = value_1 + value_2
        print(sum)

    elif choice == '2':
        value_1 = input() 
        value_2 = input()
        value_1 = float(value_1)
        value_2 = float(value_2)
        subtraction = value_1 - value_2
        print(subtraction)

    elif choice == '3':
        value_1 = input()
        value_2 = input()
        value_1 = float(value_1)
        value_2 = float(value_2)
        division = value_1 / value_2
        print(division)
    
    elif choice == '4':
        value_1 = input()
        value_2 = input()
        value_1 = float(value_1)
        value_2 = float(value_2)
        multiplication = value_1 * value_2
        print(multiplication)
        
    elif choice == '5':
        print("Até a próxima!")
        sys.exit()
    
    else:
        print("Opção inválida")
