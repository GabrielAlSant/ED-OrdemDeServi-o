#Menu Principal - Caixa com menu dentro.

# Atributos: ID, nomeDaOrdem = (solicitante+data), Desc, Status, Solicitante, Custo, Equipamento, Executor.

import datetime as dt

def menu (lista_OS, lista_log, numeroOS):
    
    while True:
    
        print ("\n\n======VRESTON -Ordens de Serviço==========")
        print ("#                                            #")
        print ("#        1 - Cadastrar Ordem se serviço      #")
        print ("#        2 - Buscar Ordem de Serviço         #")
        print ("#        3 - Listar Ordens de Serviço        #")
        print ("#        4 - Alterar Ordem de Serviço        #")
        print ("#        5 - Excluir Ordem de Serviço        #")
        print ("#        6 - Exibir média de custo           #")                  
        print ("#        7 - Exibir OS com mair custo        #")
        print ("#        8 - Exibir OS com menor custo       #")
        print ("#        9 - Exibir quantidade de OSs        #")
        print ("#        10 - Exibir LOG de uso              #")                      
        print ("#                                            #")
        print ("#                                            #")
        print ("##############################################")
        
        opc = int (input("\n\nSelecione uma Opção>>>"))
        
        match opc:
            case 1:
                
                numeroOS = numeroOS + 1
                cadastrar_OS(lista_OS,numeroOS, lista_log)
                
            case 2:
                
                print ("\n\n==========VRESTON -Ordens de Serviço==========")
                print ("#           Por qual dado deseja buscar?     #")
                print ("#                                            #")
                print ("#        1 - Buscar por descrição            #")
                print ("#        2 - Buscar por nome da OS           #")
                print ("#        0 - Sair                            #")
                print ("#                                            #")
                print ("##############################################")
                
                opc2 = int(input("Digite uma opção>>>"))
                
                match opc2:
                    
                    case 1:
                        
                        valor = str(input("Digite a String a ser buscada>>>"))
                        
                        buscarPorDescricao(valor, lista_OS)
                        
                    case 2:
                        
                        valor = input("Digite uma opção>>>")
                        buscarElementoCampoUnico (lista_OS, valor)
                        
                    case 0:
                        pass

            
                
            case 3:
                
                print ("\n\n========VRESTON -Ordens de Servi==========")
                print ("#           \nListagem de OSS                #")
                print ("#                                            #")
                print ("#        1 - Listar todas as OSs             #")
                print ("#        2 - Listar OSs abertas              #")
                print ("#        3 - Listar OSs fechadas              #")
                print ("#        0 - Sair                            #")
                print ("#                                            #")
                print ("##############################################")
                
                opc3 = int(input("Digite uma opção>>>"))
                
                match opc3:
                    case 1:
                        listarTodosElementos(lista_OS)
                    case 2:
                        listarOSabertas(lista_OS)
                    case 3:
                        listarOSfechadas(lista_OS)
                    case 0:
                        pass
                
            case 4:
                alterarOS(lista_OS)
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
    
    print ("Cadastro ===== OS N."+ str (numero_OS))
    solicitante = str (input ("Digite o nome do solicitante>>>"))
    
    dataatual = dt.date.today()
    nomeOS = str(solicitante + dataatual.strftime("%y-%m-%d"))
    
    val = verificarUnicidade(nomeOS, lista)
    
    if val == 1:
        while val == 1:
            print ("OS ja existe no sistema.")
            
            solicitante = str (input ("Digite o nome do solicitante>>>"))
            nomeOS = str(solicitante + dataatual.strftime("%y-%m-%d"))
            
            val = verificarUnicidade (nomeOS,lista)
    else:    
        print ("Unicidade validada.")    
        print ("Nome da OS:" + str(nomeOS))
        
    desc = str(input("Digite a Descrição da Ordem de Serviço>>>"))
    status = bool(1) #O indicador 1 significa que a OS esta aberta
    custo = str (input("Digite o custo total da OS>>>"))
    equipamento = str(input("Digite o local que sera realizado o serviço:>>>"))
    executor = str(input("Digite o nome do executor da OS>>>"))
    
     ## - Durante o cadastro a função cadastro chama a função registrar, e passa como parametro uma string
     # com o tipo de dado acessado e a lista log.
     
    registrarLog ("Cadastro - ", lista_log)
    
    OS = dict(id = id, desc = desc, nomeOS = nomeOS, status = status, solicitante = solicitante, custo = custo, equipamento = equipamento, executor = executor )
    
    lista_OS.append(OS)
        
    print ("OS cadastrada com sucesso!\n")
        
def registrarLog (tipo, lista_log):
    
    tipo = tipo
    horario = str (dt.datetime.now())
    
    registro = dict (tipo = tipo, horario = horario)
    
    lista_log.append(registro)
    
def listarlog (lista_log):
    
    for i in lista_log:
        print (i)


def buscarElementoCampoUnico (lista_OS, valor):
    
    for  x, i in lista_OS:
        
        if i["nomeOS"] == valor:
            
            print ("\n\nValor Encontrado>>>\n")
            
            print ("Numero da OS:" + str(i["id"]))
            print ("Nome da OS:" + i["nomeOS"])
            print ("Descrição:" + i["desc"])
            print ("Status:" + str (i["status"]))
            print ("Solicitante:" + i["solicitante"])
            print ("Custo da OS: R$:" + str( i["custo"]))
            print ("Equipamento:" + i["equipamento"])
            print ("Executor da OS:" + i["executor"])
            
            print ("\n\n>>>>>>>>>>>>>>>>>>>>")
            break
    else:
        print ("\n\nValor nao encontrado")
        
def buscarPorDescricao (valor, lista_OS):
    
    for i in lista_OS:
        
        if valor in i["desc"]:
            
            print ("\n")
            print ("Os numero:" + str(i["id"]))
            print ("Nome da OS:" + str(i["nomeOS"]))
            print ("Descrição:" + i["desc"])
            print (">>>>>>>>>>>>>>\n")
    
    
                    
def listarTodosElementos (lista_OS):
    
    for i in lista_OS:
        
        print ("Numero da OS:" + str(i["id"]))
        print ("\n")
         
        print ("Nome da OS:" + i["nomeOS"])
        print ("Descrição:" + i["desc"])
        print ("Status:" + str (i["status"]))
        print ("Solicitante:" + i["solicitante"])
        print ("Custo da OS: R$:" + str( i["custo"]))
        print ("Equipamento:" + i["equipamento"])
        print ("Executor da OS:" + i["executor"])
        print ("\n")
        print (">>>>>>>>>>>>>>>>>>>>>>>>>>>")
        
def listarOSabertas (lista_OS): #Lista todas as OSs com valor boleano TRUE
    
    for i in lista_OS:
        
        if i["status"] == True:
            
            
            print ("Numero da OS:" + str(i["id"]))
            print ("Nome da OS:" + i["nomeOS"])
            print ("Descrição:" + i["desc"])
            print ("Status:" + str (i["status"]))
            print ("Solicitante:" + i["solicitante"])
            print ("Custo da OS: R$:" + str( i["custo"]))
            print ("Equipamento:" + i["equipamento"])
            print ("Executor da OS:" + i["executor"])
            
            print ("\n\n>>>>>>>>>>>>>>>>>>>>")
            
        

def listarOSfechadas (lista_OS): #Lista todas as OSs com valor boleano FALSE
    
    for i in lista_OS:
        
        if i["status"] == False:
            
            
            print ("Numero da OS:" + str(i["id"]))
            print ("Nome da OS:" + i["nomeOS"])
            print ("Descrição:" + i["desc"])
            print ("Status:" + str (i["status"]))
            print ("Solicitante:" + i["solicitante"])
            print ("Custo da OS: R$:" + str( i["custo"]))
            print ("Equipamento:" + i["equipamento"])
            print ("Executor da OS:" + i["executor"])
            
            print ("\n\n>>>>>>>>>>>>>>>>>>>>")
            

def verificarUnicidade (valor, lista_OS):

    for i in lista_OS:
        if i["nomeOS"] == valor:
            print ("OS já existe.")
            return 1
    else:
        return 0
def alterarOS (lista_OS):
    
    valor =  str(input("Digite o nome da OS que deseja alterar>>>"))
    
    for i in lista_OS:
         if valor == i["nomeOS"]:
             
             buscarElementoCampoUnico(lista_OS, valor)
             
             print ("=======Qual campo deseja alterar========\n\n")
             print ("1 - Descrição:")
             print ("2 - Status:")
             print ("3 - Solicitante:")
             print ("4 - Custo:")
             print ("5 - Equipamento:")
             print ("6 - Executor:")
             
             opc = input("Digite uma opção>>>")
             
             match opc:
                 case 1:
                     val = str(input ("Digite a nova descrição>>>"))
                     i["des"] = val
                 case 2:
                     print ("\nQual o novo status da OS\n")
                     print ("1 - Aberta")
                     print ("2 - Fechada")
                     
                     opc2 = input (">>>>")
                     
                     match opc2:
                        case 1:
                            i["status"] = True
                        case 2:
                            i["status"] = False
                             
                     
                 case 3:
                     val = str(input ("Digite o novo solicitante>>>"))
                     i["solicitante"] = val
                 case 4:
                     val = float(input ("Digite o novo custo>>>"))
                     i["custo"] = val
                 case 5:
                     val = str(input ("Digite o novo equipamento>>>"))
                     i["equipamento"] = val
                 case 6:
                    val = str(input ("Digite o novo executor>>>"))
                    i["executor"] = val
    else:
            print ("OS não encontrada!")
    
    
lista_OS = []
lista_log = []
Numero_OS = 0
      
menu (lista_OS, lista_log, Numero_OS)

