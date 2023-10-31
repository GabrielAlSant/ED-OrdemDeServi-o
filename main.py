#Menu Principal - Caixa com menu dentro.

# Atributos: ID, nomeDaOrdem = (solicitante+data), Desc, Status, Solicitante, Custo, Equipamento, Executor.

import datetime as dt
from operator import itemgetter

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
        print ("#       10 - Exibir LOG de uso               #")                      
        print ("#       11 - Exibir a lista ordenada         #")
        print ("#        0 - Sair do sistema                 #")
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
                        
                        registrarLog("Buscar Elemento por Descrição", lista_log)
                        
                        valor = str(input("Digite a String a ser buscada>>>"))
                        
                        buscarPorDescricao(valor, lista_OS)
                        
                    case 2:
                        
                        registrarLog("Buscar Elemento por Campo único", lista_log)
                        
                        buscarElementoCampoUnico (lista_OS)
                        
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
                        registrarLog("Listar todas as OSs", lista_log)
                        listarTodosElementos(lista_OS)
                    case 2:
                        registrarLog("Listar todas as OSs Abertas", lista_log)
                        listarOSabertas(lista_OS)
                    case 3:
                        registrarLog("Listar todas as Fechadas", lista_log)
                        listarOSfechadas(lista_OS)
                    case 0:
                        pass
                
            case 4:
                registrarLog("Alterar OS", lista_log)
                alterarOS(lista_OS)
                
            case 5:
                registrarLog("Excluir OS", lista_log)
                excluirOS(lista_OS)
                
            case 6:
                registrarLog("Exibir média de custo das OSs", lista_log)
                exibirMediaCusto(lista_OS)
                
            case 7:
                registrarLog("Exibir OS com maior custo", lista_log)
                maior(lista_OS)
                
            case 8:
                registrarLog("Exibir OS com menor custo", lista_log)
                menor(lista_OS)
                
            case 9:
                registrarLog("Exibir contagem de OSs", lista_log)
                contagem(lista_OS)
                
            case 10:
                registrarLog("Exibir Log do sistema", lista_log)
                listarlog(lista_log)
                
            case 11:
                registrarLog("Exibir Ordenado", lista_log)
                exibirOrdenado(lista_OS)
            
            case 0:
               break
            case _:
                pass



def cadastrar_OS(lista, numero_OS, lista_log):
    
    
    arq = open("matheus.txt", "a")
    
    
    print ("\n\n======VRESTON -Ordens de Serviço==========\n\n")
    
    id = int(numero_OS)
    
    
    print ("Cadastro ===== OS N."+ str (numero_OS))
    solicitante = str (input ("Digite o nome do solicitante>>>"))
    
    dataatual = dt.date.today()
    nomeOS = str(solicitante + dataatual.strftime("%d-%m-%y"))
    
    val = verificarUnicidade(nomeOS, lista)
    
    if val == 1:
        while val == 1:
            print ("OS ja existe no sistema.")
            
            solicitante = str (input ("Digite o nome do solicitante>>>"))
            nomeOS = str(solicitante + dataatual.strftime("%d-%m-%y"))
            
            val = verificarUnicidade (nomeOS,lista)
    else:    
        print ("Unicidade validada.")    
        print ("Nome da OS:" + str(nomeOS))
        
    desc = str(input("Digite a Descrição da Ordem de Serviço>>>"))
    status = bool(1) #O indicador 1 significa que a OS esta aberta
    custo = float(input("Digite o custo total da OS>>>"))
    equipamento = str(input("Digite o local que sera realizado o serviço:>>>"))
    executor = str(input("Digite o nome do executor da OS>>>"))
    
     ## - Durante o cadastro a função cadastro chama a função registrar, e passa como parametro uma string
     # com o tipo de dado acessado e a lista log.
     
    registrarLog ("Cadastro - ", lista_log)
    
    OS = dict(id = id, desc = desc, nomeOS = nomeOS, status = status, solicitante = solicitante, custo = custo, equipamento = equipamento, executor = executor )
    
    lista_OS.append(OS)
    
    #grava o dicionário no arquivo de texto
    arq.write(str(OS))
    
    arq.close()
    
    print ("OS cadastrada com sucesso!\n")
        
def registrarLog (tipo, lista_log):
    
    tipo = tipo
    
    horario = str (dt.datetime.now().replace(microsecond=0))
    
    registro = dict (tipo = tipo, horario = horario)
    
    lista_log.append(registro)
    
def listarlog (lista_log):
    
    for i in lista_log:
        print ("função acessada:" , i["tipo"])
        print ("Horario do acesso", i["horario"])


def buscarElementoCampoUnico (lista_OS):
    
    valor = input("Digite uma opção>>>")
    
    for i in lista_OS:
        
        if i["nomeOS"] == valor:
            
            print ("\n\nValor Encontrado>>>\n")
            
            print ("Numero da OS:" + str(i["id"]))
            print ("Nome da OS:" + i["nomeOS"])
            print ("Descrição:" + i["desc"])
            if i["status"] == True:
                    print("Status: Em andamento.")
            else: 
                    print("Status: Finalizada!")
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
        if i["status"] == True:
                    print("Status: Em andamento.")
        else: 
                    print("Status: Finalizada!")
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
            if i["status"] == True:
                    print("Status: Em andamento.")
            else: 
                    print("Status: Finalizada!")
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
            if i["status"] == True:
                    print("Status: Em andamento.")
            else: 
                    print("Status: Finalizada!")
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
    
def alterarOS(lista_OS):
    
    valor = str(input("Digite o nome da OS que deseja alterar>>>"))

    for i in lista_OS:
        
        if valor == i["nomeOS"]:
            
            print("Numero da OS:" + str(i["id"]))
            print("Nome da OS:" + i["nomeOS"])
            print("Descrição:" + i["desc"])
            if i["status"] == True:
                    print("Status: Em andamento.")
            else: 
                    print("Status: Finalizada!")
            print("Solicitante:" + i["solicitante"])
            print("Custo da OS: R$:" + str(i["custo"]))
            print("Equipamento:" + i["equipamento"])
            print("Executor da OS:" + i["executor"])

            print("=======Qual campo deseja alterar========\n\n")
            print("1 - Descrição:")
            print("2 - Status:")
            print("3 - Solicitante:")
            print("4 - Custo:")
            print("5 - Equipamento:")
            print("6 - Executor:")

            opc4 = input("Digite uma opção>>>")

            if opc4 == "1":
                val = str(input("Digite a nova descrição>>>"))
                i["desc"] = val
                
            elif opc4 == "2":
                print("\nQual o novo status da OS\n")
                print("1 - Aberta")
                print("2 - Fechada")
                
                opc5 = input(">>>>")
                
                if opc5 == "1":
                    
                    i["status"] = True
                    
                elif opc5 == "2":
                    
                    i["status"] = False
                    
            elif opc4 == "3":
                
                val = str(input("Digite o novo solicitante>>>"))
                i["solicitante"] = val
                
            elif opc4 == "4":
                val = float(input("Digite o novo custo>>>"))
                i["custo"] = val
                
            elif opc4 == "5":
                val = str(input("Digite o novo equipamento>>>"))
                i["equipamento"] = val
                
            elif opc4 == "6":
                val = str(input("Digite o novo executor>>>"))
                i["executor"] = val
                
            else:
                print("Opção inválida")
                
            break
    else:
        print("OS não encontrada!")

def excluirOS (lista_OS):

    val = str(input(" Digite o nome da OS para excluir>>>"))
  
    for ind , i in enumerate( lista_OS):
        if val == i["nomeOS"]:
            lista_OS.pop(ind)
            print ("Ordem excluida!")
            break
    else:
        print ("Valor não encontrado!")

def exibirMediaCusto (lista_OS):

    valor = 0

    for i in lista_OS:

      valor = valor + float(i["custo"])
    
    quant = len (lista_OS)

    media = float(valor/quant)

    print (" A media do custos da OSs:", round(media, 2), " reais.")


def contagem(lista_OS):
    print("Há um total de " , len(lista_OS), " OSs cadastradas no sistema")

def imprimir(i):
  print("Nome da OS:" + i["nomeOS"])
  print("Descrição:" + i["desc"])
  if i["status"] == True:
   print("Status: Em andamento.")
  else: 
   ("Status: Finalizada!")
  print("Solicitante:" + i["solicitante"])
  print("Custo da OS: R$:" + str(i["custo"]))
  print("Equipamento:" + i["equipamento"])
  print("Executor da OS:" + i["executor"])


def maior(lista_OS):
    maior  = 0
    indice = False

    for ind, i in enumerate(lista_OS):
      valor = int(i["custo"])
      
      if valor >= maior:
          indice = True
          maior = valor
          os = lista_OS[ind]
    
    if indice == True:
         print("A ultima ordem com maior valor no cadastrado é " , maior)
         imprimir(os)
    else: 
        print('Não tem nenhuma ordem cadastrada')
      

def menor(lista_OS):
    menor = lista_OS[0] ['custo']
    indice = False

    for ind, i in enumerate(lista_OS):
      valor = int(i["custo"])
      
      if menor >= valor:
          indice = True
          menor = valor
          os = lista_OS[ind]    
    
    if indice == True:
        print("A ultima ordem com menor valor no cadastrado é" , menor, " cadastrados no sistema")
        imprimir(os)
    else: 
        print('Não tem nenhuma ordem cadastrada')
              

def exibirOrdenado (lista_OS):
    
    print ("Exibir OSs ordenadas\n")
    print ("1 - Crescente")
    print ("2 - Decrescente")
    print ("\n\n")
    
    opc = int(input("Digite a opção desejada>>>"))
    
    match opc:
        case 1:
            lista_crescente = sorted (lista_OS, key=itemgetter("nomeOS"))
            
            for i in lista_crescente:
                
                print ("\n")
                print("Numero da OS:" + str(i["id"]))
                print("Nome da OS:" + i["nomeOS"])
                print("Descrição:" + i["desc"])
                if i["status"] == True:
                    print("Status: Em andamento.")
                else: 
                    print("Status: Finalizada!")
                print("Solicitante:" + i["solicitante"])
                print("Custo da OS: R$:" + str(i["custo"]))
                print("Equipamento:" + i["equipamento"])
                print("Executor da OS:" + i["executor"])
                print (">>>>>>>>\n")
                
        case 2:
            lista_desc = sorted (lista_OS, key=itemgetter("nomeOS"), reverse=True)
            
            for i in lista_desc:
                
                print ("\n")
                print("Numero da OS:" + str(i["id"]))
                print("Nome da OS:" + i["nomeOS"])
                print("Descrição:" + i["desc"])
                if i["status"] == True:
                    print("Status: Em andamento.")
                else: 
                    print("Status: Finalizada!")
                print("Solicitante:" + i["solicitante"])
                print("Custo da OS: R$:" + str(i["custo"]))
                print("Equipamento:" + i["equipamento"])
                print("Executor da OS:" + i["executor"])
                print (">>>>>>>>\n")
                
    
            
lista_OS = []
lista_log = []
Numero_OS = 0
      
menu (lista_OS, lista_log, Numero_OS)

