#Menu Principal - Caixa com menu dentro.

# Atributos: ID, Desc, Status, Solicitante, Custo, Equipamento, Executor.

import datetime as dt

def menu (lista_OS, lista_log, numeroOS):
    
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
                #numeroOS = numeroOS + 1s
                cadastrar_OS(lista_OS,numeroOS, lista_log)
            case 2:
                
                print ("\n\n==========VRESTON -Ordens de Serviço==========")
                print ("#           Por qual dado deseja buscar?     #")
                print ("#                                            #")
                print ("#        1 - Buscar por Numero de OS         #")
                print ("#        2 - Buscar por Equipamento          #")
                print ("#        0 - Sair                            #")
                print ("#                                            #")
                print ("##############################################")
                
                opc = int(input("Digite uma opção>>>"))
                
                match opc:
                    case 1:
                        pass
                    case 2:
                        
                        valor = input("")
                        buscarElementoCampoUnico (lista_OS, valor)
                        
                    case 0:
                        pass

            
                
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
                
                listarlog(lista_log)
            
            case 0:
                pass
            case _:
                pass



def cadastrar_OS(lista, numero_OS, lista_log):
    
    print ("\n\n======VRESTON -Ordens de Serviço==========\n\n")
    
    id = int(numero_OS)
    desc = str(input("Digite a Descriçào da Ordem de Serviço>>>"))
    status = bool(1)
    solicitante = str (input ("Digite po nome do solicitante>>>"))
    custo = str (input("Digite o custo total da OS>>>"))
    
    equipamento = str(input("Digite o nome do Equipamento>>>"))
    
    val = verificarUnicidade(lista, equipamento)
    
    if val == 1:
        while val == 1:
            equipamento = str(input ("Equipamento ja existente, favor digite o nome de outro equipamento>>>"))
            val = verificarUnicidade (lista, equipamento)
        
    
    executor = str(input("Digite o nome do executor da OS>>>"))
    
     ## - Durante o cadastro a função cadastro chama a função registrar, e passa como parametro uma string
     # com o tipo de dado acessado e a lista log.
     
    registrarLog ("Cadastro - ", lista_log)
    
    OS = dict(numero = id, desc = desc, status = status, solicitante = solicitante, custo = custo, equipamento = equipamento, executor = executor )
    
    
    lista_OS.append(OS)
    
def registrarLog (tipo, lista_log):
    
    tipo = tipo
    horario = str (dt.datetime.now())
    
    registro = dict (tipo = tipo, horario = horario)
    
    lista_log.append(registro)
    
def listarlog (lista_log):
    
    for i in lista_log:
        print (i)

def verificarUnicidade (lista_OS, valor):
    
    for i in lista_OS:
        
        if i["equipamento"] == valor:
            
            return 1

            break
    else:
        return 0

def buscarElementoCampoUnico (lista_OS, valor):
    
    for i in lista_OS:
        
        if i["equipamento"] == valor:
            
            print ("Valor Encontrado>>>")
            print ("Numero da OS:" + i["id"])
            print ("Descrição:" + i["desc"])
            print ("Status:" + i["status"])
            print ("Solicitante:" + i["solicitante"])
            print ("Custo da OS: R$:" + i["custo"])
            print ("Equipamento:" + i["equipamento"])
            print ("Executor da OS:" + i["executor"])
            
            print ("\n\n>>>>>>>>>>>>>>>>>>>>")
            break
    else:
        print ("Valor nao encontrado")
            

lista_OS = []
lista_log = []
Numero_OS = 0
      
menu (lista_OS, lista_log, Numero_OS)

