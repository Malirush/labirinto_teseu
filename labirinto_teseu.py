
################################             BUSCA EM PROFUNDIDADE             #####################################

#        MAXIMO POSSIVEL PARA UMA DIRECAO 

#        VOLTA O MINIMO 

#        PEGA CAMINHO AINDA NAO VISITADO





#funcao usada para ler o labirinto

def divide_caracteres(nome_arquivo):
    with open(nome_arquivo) as arquivo:
        linhas = arquivo.readlines()
    format = [list(lista.strip()) for lista in linhas]
    return format



def percorre(labirinto):
    inicio='E'
    fim='S' 

    #cria lista de tuplas para salvar posicoes visitadas (coordenadas)

    visitados=[]

    #itero os elementos do labirinto e uso enumerate para salvar as cordenadas quando o inicio for encontrado

    for linha, lista in enumerate(labirinto):
        for coluna, elemento in enumerate(lista):
            if elemento == inicio:                
                while True:
                    atual = labirinto[linha][coluna]

                    #verifica caminho a esquerda

                    if (labirinto[linha][coluna-1]==' ' or labirinto[linha][coluna-1]==fim) and (linha,coluna-1) not in visitados :
                        if  (linha,coluna) not in visitados:
                            iteracoes=2
                        else:
                            iteracoes+=1
                        if labirinto[linha][coluna]!= inicio:
                            labirinto[linha][coluna]='O'
                        visitados.append((linha,coluna))
                        coluna-=1
                        if labirinto[linha][coluna]==fim:
                            labirinto[linha][coluna]='O'
                            return print('caminho encontrado')
                        
                    #verifica caminho abaixo 

                    elif (labirinto[linha+1][coluna]==' ' or labirinto[linha+1][coluna]==fim) and (linha+1,coluna) not in visitados:
                        if  (linha,coluna) not in visitados:
                            iteracoes=2
                        else:
                            iteracoes+=1
                        if labirinto[linha][coluna]!= inicio:
                            labirinto[linha][coluna]='O'  
                        visitados.append((linha,coluna))
                        linha+=1 
                        if labirinto[linha][coluna]==fim:
                            labirinto[linha][coluna]='O'
                            return print('caminho encontrado')
                          






                    #verifica ha caminho a direita ou se e o fim alem de verificar se o caminho ja nao foi visitado
                       
                    elif (labirinto[linha][coluna+1]==' ' or labirinto[linha][coluna+1]==fim) and (linha,coluna+1) not in visitados:

                        #verifica se o atual esta no visitados, caso nao, reinicia o valor iteracao com a lista visitados
                        #no primeiro valor adicionado a visitados, o valor iteracoes e criado para caso a proxima posicao nao tenha caminho ele puxa para a penultima posicao

                        if  (linha,coluna) not in visitados:
                            iteracoes=2

                        #caso o valor nao esteja em visitados adiciona um ao iterador pois ira ser adicionado um valor em seguida
                            
                        else:
                            iteracoes+=1

                        #marca a casa que esta sendo visitada

                        if labirinto[linha][coluna]!= inicio:
                            labirinto[linha][coluna]='O'

                        #adiciona a casa na lista de tuplas

                        visitados.append((linha,coluna))

                        #anda para o proximo valor

                        coluna+=1

                        # verifica se o proximo valor e o fim do labirinto e se for marca o atual

                        if labirinto[linha][coluna+1]==fim:
                            labirinto[linha][coluna]='O'
                            return print('caminho encontrado')
                        








                    #verifica caminho em cima
                         
                    elif (labirinto[linha-1][coluna]==' ' or labirinto[linha-1][coluna]==fim) and (linha-1,coluna) not in visitados:
                        if  (linha,coluna) not in visitados:
                            iteracoes=2
                        else:
                            iteracoes+=1
                        if labirinto[linha][coluna]!= inicio:
                            labirinto[linha][coluna]='O'
                        visitados.append((linha,coluna))
                        linha-=1
                        if labirinto[linha-1][coluna]==fim:
                            labirinto[linha][coluna]='O'
                            return print('caminho encontrado')
                        



                    #caso nao encontre valor, desmarca as posicoes ate a posicao que ira retornar, altera a posicao para a qual retornou e soma 1 ao numero de iteracoes
                       
                    else:
                        if len(visitados) == 0:
                            return False
                        apaga=1
                        while apaga<iteracoes:
                            valor1, valor2 = visitados[-apaga]
                            labirinto[valor1][valor2] = ' ' 
                            apaga+=1                   
                        linha, coluna = visitados[-iteracoes]
                        iteracoes+=1                        
 
                        
    return print('erro')


                    
    
    



nome_arquivo = r"C:\Users\Lfcgl\Desktop\labirinto.txt"
labirinto=divide_caracteres(nome_arquivo)
percorre(labirinto)


with open('labirinto_feito.txt', 'w') as arquivo:
    # Percorrer cada lista na lista de listas
    for linha in labirinto:
        # Escrever cada elemento da linha separado por vírgula
        arquivo.write(','.join(linha) + '\n')
