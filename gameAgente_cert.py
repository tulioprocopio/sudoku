cima = ''
meio = ''
risco = ''
bConflito = False
valor = ""
cordenadaLinha = ""
cordenadaColuna = ""
fimJogo = False
bateNum = False
matriz = []
quadrante = []
listaNaoPodeMudar = []
listaVlrCorreto = [1,2,3,4,5,6,7,8,9]
conflitoQuad = False
posicaoConflito = []
bNaoPodeAlterar = False

def regras():
    global bateNum
    global fimJogo
    global valor
    global matriz
    global cordenadaLinha
    global cordenadaColuna
    global listaVlrCorreto
    global conflitoQuad
    global posicaoConflito
    bAux = False
    cordenadas = False
    verificacaoMelhorEstado = -1
    melhorEstado = []
    
    matrizResultado = tuple(matriz)
    acoesRetornadas = []
    auxAcoesRetornadas = 0
    acoesRetornadas = acoes(tuple(matriz))
    auxFuncaoAvaliacao = 0
    
    for linha in range(len(matrizResultado)):
        for coluna in range(len(matrizResultado[linha])):
            if matrizResultado[linha][coluna] == ' ':
                matrizResultado[linha][coluna] = acoesRetornadas[auxAcoesRetornadas]
                auxAcoesRetornadas = auxAcoesRetornadas+1

    auxFuncaoAvaliacao = funcaoAvaliacao(tuple(matriz), tuple(matrizResultado))
    if ((verificacaoMelhorEstado == -1) or (auxFuncaoAvaliacao < verificacaoMelhorEstado)):
        verificacaoMelhorEstado = auxFuncaoAvaliacao
        melhorEstado = matrizResultado
        if verificacaoMelhorEstado == 0:
            return melhorEstado



def verificaConflito():
    global bConflito
    global fimJogo
    global bateNum
    global matriz
    global posicaoConflito
    global bNaoPodeAlterar
    for i in range(len(listaNaoPodeMudar)):                    
        if listaNaoPodeMudar[i] == str(int(cordenadaLinha)-1) + str(int(cordenadaColuna)-1):
            fimJogo = False
            bateNum = True
            bNaoPodeAlterar = True
            print("Esta posição não pode ser Alterada!")
            break
        else: 
            bateNum = False
            bNaoPodeAlterar = False     
    if not bNaoPodeAlterar:
        for i in range(len(matriz[int(cordenadaLinha)-1])):            
            if matriz[int(cordenadaLinha)-1][i] == valor:
                #TEM CONFLITO NA LINHA
                if not verificaArray(str(int(cordenadaLinha)-1)+str(i)):
                    posicaoConflito.append(str(int(cordenadaLinha)-1)+str(i))
                    posicaoConflito.append(str(int(cordenadaLinha)-1)+str(int(cordenadaColuna)-1))
                    
                return True    
                
                fimJogo = False
                bateNum = True
                bConflito = True
                #print("Valor em conflito!")
                break
            else: 
                bateNum = False
                bConflito = False        
    #if ((not bateNum) and (not bConflito)):        
    for i in range(len(matriz)):            
        if matriz[i][int(cordenadaColuna)-1] == valor:
            #TEM CONFLITO NA COLUNA
            if not verificaArray(str(i)+str(int(cordenadaColuna)-1)):                    
                posicaoConflito.append(str(i)+str(int(cordenadaColuna)-1))
                posicaoConflito.append(str(int(cordenadaLinha)-1)+str(int(cordenadaColuna)-1))
            
            return True
            fimJogo = False
            bateNum = True
            bConflito = True
            print("Valor em conflito!")
            break
        else: 
            bateNum = False
            bConflito = False 

def verificaQuadrante():
    global quadrante
    global matriz
    global conflitoQuad    
    global posicaoConflito
    colunaAux=0
    linhaAux=0
    posicaoColorirQuadAux = []
    quadrante = []
    i=0
    j=0
    if int(cordenadaColuna) in [1,2,3]:
        colunaAux = 0
    elif int(cordenadaColuna) in [4,5,6]:
        colunaAux = 3
    elif int(cordenadaColuna) in [7,8,9]:
        colunaAux = 6

    if int(cordenadaLinha) in [1,2,3]:
        linhaAux = 0
    elif int(cordenadaLinha) in [4,5,6]:
        linhaAux = 3
    elif int(cordenadaLinha) in [7,8,9]:
        linhaAux = 6

    i=linhaAux
    j=colunaAux
    while i < (linhaAux+3):
        j=colunaAux
        while j < (colunaAux+3):            
            if ((matriz[i][j] != ' ') and (matriz[i][j] != '\n')):
                quadrante.append(int(matriz[i][j]))                
            else:
                quadrante.append(matriz[i][j])
            posicaoColorirQuadAux.append(str(i)+str(j))
            j = j + 1        
        i = i + 1
    
    for i in range(0, len(quadrante)):
        if int(valor) == quadrante[i]:
            conflitoQuad = True
            auxiliar = i
            break

    
    
    if conflitoQuad:
        if not verificaArray(posicaoColorirQuadAux[auxiliar]):
            posicaoConflito.append(posicaoColorirQuadAux[auxiliar])
            posicaoConflito.append(str(int(cordenadaLinha)-1)+str(int(cordenadaColuna)-1))
        
        #print("Existe conflitos no quadrante!")                        
        return True
        
    else:
        return False










#PARTE DA BUSCA
def acoes(estadoInicial):
    estadoGerado = []
    #while True:
    for linha in range(len(estadoInicial)):
        for coluna in range(len(estadoInicial[i])):
            if estadoInicial[linha][coluna] == ' ':
                estadoGerado.append(str(random.randint(1,9)))

    return estadoGerado


def funcaoAvalicao(estadoInicial, estadoVerificacao):
    somaVazioInicial = 0
    linha = 0
    coluna = 0
    for linha in range(len(estadoInicial)):
        for coluna in range(len(estadoInicial[i])):
            if estadoInicial[linha][coluna] == 0:
                somaVazioInicial = somaVazioInicial+1

    linha = 0
    coluna = 0
    for linha in range(len(estadoVerificacao)):
        for coluna in range(len(estadoVerificacao[i]))


    
    return retorno