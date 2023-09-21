#Menu Principal - Caixa com menu dentro.

# Atributos: ID, Desc, Status, Solicitante, Custo, Equipamento, Executor.

def menu (lista_OS, numeroOS):
    
    while True:
    
        print ("\n\n======VRESTON -Ordens de Serviço==========")
        print ("#                                            #")
        print ("#        1 - Cadastrar Ordem se serviço      #")
        print ("#        2 - Buscar Ordem de Serviço         #")
        print ("#        3 - Listar Ordens de Serviço        #")
        print ("#        4 - Atualizar Ordem de Serviço      #")
        print ("#        5 - Excluir Ordem de Serviço        #")
        print ("#        6 - Exibir média de custo           #")                  
        print ("#        7 - Exibir OS com mair custo        #")
        print ("#        8 - Exibir OS com menor custo       #")
        print ("#        9 - Exibir quantidade de OSs        #")
        print ("#        10 - Exibir LOG de uso              #")                      
        print ("#                                            #")
        print ("#                                            #")
        print ("#                                            #")
        print ("#                                            #")
        print ("##############################################")
        
        opc = int (input("\n\nSelecione uma Opção>>>"))
        
        match opc:
            case 1:
                cadastrar_OS(lista_OS,numeroOS)
            case 2:
                
                print ("\n\n==========VRESTON -Ordens de Serviço==========")
                print ("#           Por qual dado deseja buscar?     #")
                print ("#                                            #")
                print ("#        1 - Buscar por Numero de OS         #")
                print ("#        2 - Buscar por Descrição da OS      #")
                print ("#                                            #")
                print ("##############################################")
                
                opc = int(input("Digite uma opção>>>"))
                
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                pass
            case 7:
                pass
            case 8:
                pass
            case 9:
                pass
            case 10:
                pass
            case 0:
                pass
            case _:
                pass



def cadastrar_OS(lista, numero_OS):
    
    pass
    
    print ("\n\n======VRESTON -Ordens de Serviço==========\n\n")
    
    id = int(numero_OS)
    desc = str(input("Digite a Descriçào da Ordem de Serviço>>>"))
    status = bool(1)
    solicitante = str (input ("Digite po nome do solicitante>>>"))
    custo = str (input("Digite o custo total da OS>>>"))
    equipamento = str(input("Digite o nome do Equipamento>>>"))
    executor = str(input("Digite o nome do executor da OS>>>"))
    
    OS = dict(numero = id, desc = desc, status = status, solicitante = solicitante, custo = custo, equipamento = equipamento, executor = executor )
    
    lista_OS.append(OS)
    
    


lista_OS = []
Numero_OS = int(0)

      
menu (lista_OS, Numero_OS)

