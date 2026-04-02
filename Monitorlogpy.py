import random
import datetime

def menu():
    nome_arq = 'log.txt'
    while True:
        print('menu\n')
        print('1 - gear logs')
        print('2 - analisar logs')
        print('3 - gerar e analisar logs')
        print('4 - sair')
        opc = int(input('escolha uma opção '))
        if opc == 1:
            try:
                qtd = int(input('quantidade de logs (registros): '))
                gerararquivo(nome_arq, qtd)
            except:
                print('entrada invalida.')
        elif opc == 2:
            analisarlogs(nome_arq)
        elif opc == 3:
            try:
                qtd = int(input('quantidade de logs (registros): '))
                gerararquivo(nome_arq, qtd)
                analisarlogs(nome_arq)
            except:
                print('Entrada invalida.')
        elif opc == 4:
                print('até mais')
                break
        else:
            print('Opção invalida')
            
def gerararquivo(nome_arq, qtd):
    with open(nome_arq, 'w', encoding='UTF-8') as arq:
        for i in range(gtd):
            arq.write(montarlog(i) + '\n')
        print('log gerado')
        
def montarlog(i):
    data = gerardata(i)
    Ip = geraip(i)            
    recurso= gerarrecurso(i)
    metodo = gerarmetodo(i)
    status = gerarstatus(i)
    tempo  = gerartempo(i)
    agente = geraragente(i)
    protocolo =gerarprotocolo(i)
    tamanho = gerartamanho(i)
    return f'[{data}] {i} - {metodo} - {status} - {recurso} - {tempo}ms - {tamanho} - {protocolo} - {agente} - /home'

def gerardata(i):
    base = datetime.datatime.now()
    delta = datatime.timedelta(seconds- i * random.randint(5,20) )
    return (base + delta).strftime('%d/%m/%y %¨h:%m:%s')

def gerarip(i):
    r= random.randint(1,6)
    if i >= 20 and i <= 50:
        return '203.120.45.7'
    
    if r == 1:
        return '192.168.12.1'
    elif r ==2: 
         return '192.168.12.3'
    elif r ==3: 
     return '192.168.12.3'
    elif r ==4: 
     return '192.168.162.3'
    elif r ==5: 
     return '192.168.23.3'
    elif r ==6: 
     return '192.168.0.3'




   
