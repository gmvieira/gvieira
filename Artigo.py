# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 12:17:38 2019

@author: Gabriel Mauricio Oswald Vieira
         Redes Complexas 2019/3 PESC/COPPE/UFRJ
              
@title:  A singular relação de cardinalidade entre as cliques 
         de 3 e 4 vértices do conectoma do C. elegans 

"""

# Função para calcular o número de triangulos, quadrados, pentágonos e 
# respectivos diamantes em grafos direcionados. Além disso, a função também
# identifica, para cada vértice, a participação destes
# nas 5 figuras estudadas e suas respectivas distribuições.
# 
# 
def contaFigura(g):
    
    """
    import networkx as nx    
    # Conectoma do C. elegans
    g = nx.read_gml("D:/celegansneural.gml")
    # Matriz Adjacente do Grafo Direcionado do C. Elegans
    g = nx.adj_matrix(g).toarray()
    """     
    
    nodes = len(g)
     
    qInter  = []   # resultado participação de vértices em quadrados
    dqInter = []   # idem diamantes-quadrados
    tInter  = []   # idem triangulos
    pInter  = []   # idem pentágonos
    dpInter = []   # idem diamantes-pentagonos
    
    # inicializa arrays interseção
    for i in range(nodes):
        qInter.append(1)
        dqInter.append(1)
        tInter.append(1)
        pInter.append(1)
        dpInter.append(1)
        
        qInter[i]  = 0
        dqInter[i] = 0
        tInter[i]  = 0
        pInter[i]  = 0
        dpInter[i] = 0
    
    #Inicializa resultados
    conta_Qua   = 0 
    conta_dQua  = 0
    conta_tri   = 0 
    conta_Pen   = 0
    conta_dPen  = 0
    
    
    # Complexidade n^5
    for i in range(nodes):
        for j in range(nodes):
            
            # Teste triangulo
            for k in range(nodes):
                if(i!=j and i !=k and g[i][j] and g[j][k] and g[k][i]):
                  conta_tri += 1
                  tInter[i] += 1
                  tInter[j] += 1
                  tInter[k] += 1
                   
                # Teste Quadrado                  
                for l in range(nodes):
                     if(i!=j and i !=k and i!= l and j!= k and j!= l and k != l and
                        g[i][j] and g[j][k] and g[k][l] and g[l][i]):
                        conta_Qua += 1
                        qInter[i] += 1
                        qInter[j] += 1
                        qInter[k] += 1
                        qInter[l] += 1    
                         
                        # Se quadrado, testa Diamante
                        if (g[j][l] or g[l][j]) and (g[i][k] or g[k][i]):
                             conta_dQua += 1                                             
                             dqInter[i] += 1
                             dqInter[j] += 1
                             dqInter[k] += 1
                             dqInter[l] += 1
                              
                     # Teste pentagono                  
                     for m in range(nodes):
                                 if(i!=j and i!=k and i!=l and i!=m and j!=k and j!=l and j!=m and
                                    k !=l and k!= m and l!=m and
                                    g[i][j] and g[j][k] and g[k][l] and g[l][m] and g[m][i]):
                                    conta_Pen += 1
                                    pInter[i] += 1
                                    pInter[j] += 1
                                    pInter[k] += 1
                                    pInter[l] += 1
                                    pInter[m] += 1
                                     
                                    # Se pentagono, testa Diamante
                                    if (g[i][l] or g[l][i]) and (g[i][k] or g[k][i]) and (g[m][j] or g[j][m]) and (g[m][k] or g[k][m]) and (g[l][j] or g[j][l]):
                                          conta_dPen += 1  
                                          dpInter[i] += 1
                                          dpInter[j] += 1
                                          dpInter[k] += 1
                                          dpInter[l] += 1
                                          dpInter[m] += 1
    
    #import sys
    #temp = sys.stdout                        # store original stdout object for later
    #sys.stdout = open('conectoma.txt', 'w') # redirect all prints to this log file
    #Imprime ∑∩
    for i in range(nodes):
         print("------- vértice", i+1,"--Triangulo--Quadrado-dQuadrado--Pentagono--dPentagono--|")
         print("                        ",int(tInter[i]/3), "        ", int(qInter[i]/4), 
               "      ", int(dqInter[i]/4),"       ", int(pInter[i]/5), "        " ,int(dpInter[i]/5))
   
    
    
    # Imprime deselegância ...
    print("\n---------Totais ==> Triangulo--Quadrado-dQuadrado--Pentagono--dPentagono--|")
    print("                        ",int(conta_tri/3), "        ", int(conta_Qua/4), 
               "      ", int(conta_dQua/4),"       ", int(conta_Pen/5), "        " ,int(conta_dPen/5))
    

    
    # normaliza arrays interseção para distribuição
    for i in range(nodes):
   
        tInter[i]  /= 3
        qInter[i]  /= 4
        dqInter[i] /= 4
        pInter[i]  /= 5
        dpInter[i] /= 5
    
    a=sorted(tInter)
    b=sorted(qInter)
    c=sorted(dqInter)
    d=sorted(pInter)
    e=sorted(dpInter)
    
    print ("\n--Distribuições ----------------------------")
    print ("Tri  ==>", a)
    print ("Qua  ==>", b)
    print ("dQua ==>", c)
    print ("Pen  ==>", d)
    print ("dPen ==>", e)
    
    
    #sys.stdout.close()                # ordinary file object
    #sys.stdout = temp                 # restore print commands to interactive prompt
    #print("back to normal") 

        
    return 

# MA final do artigo do curso de RC 
digraph  =  [[0,1,1,1,1,1,0],
             [1,0,1,1,0,1,0],
             [1,1,0,1,1,1,1],
             [1,1,1,0,1,0,0],
             [1,0,1,1,0,0,0],
             [1,1,1,0,0,0,1],
             [0,0,1,0,0,1,0]]
   
contaFigura(digraph)
