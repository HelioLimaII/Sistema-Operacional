# Função para ler os dados de entrada do arquivo
def carregar_dados_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()
    valores = [int(linha.strip()) for linha in linhas]  # Remove espaços em branco
    return valores

# Algoritmo FIFO (First-In, First-Out)
def substituicao_fifo(qtd_quadros, sequencia_paginas):
    
    memoria = []  # Lista para representar os quadros de memória
    contador_falhas = 0  # Contador de falhas de página
    
    for pagina in sequencia_paginas:
        # Verifica se a página não está na memória (falha de página)
        if pagina not in memoria:
            contador_falhas += 1  # Incrementa o contador de falhas
            
            # Se ainda há espaço na memória, apenas adiciona a página
            if len(memoria) < qtd_quadros:
                memoria.append(pagina)
            else:
                # Remove a página mais antiga (primeira da lista)
                memoria.pop(0)
                # Adiciona a nova página no final
                memoria.append(pagina)
    return contador_falhas

# Algoritmo Ótimo (OTM)
def substituicao_otima(qtd_quadros, sequencia_paginas):
    
    memoria = []  # Lista para representar os quadros de memória
    contador_falhas = 0  # Contador de falhas de página
    
    # Percorre cada página na sequência com seu índice
    for indice, pagina in enumerate(sequencia_paginas):
        # Verifica se a página não está na memória (falha de página)
        if pagina not in memoria:
            contador_falhas += 1  # Incrementa o contador de falhas
            
            # Se ainda há espaço na memória, apenas adiciona a página
            if len(memoria) < qtd_quadros:
                memoria.append(pagina)
            else:
                maior_distancia = -1  # Armazena a maior distância encontrada
                indice_substituir = -1  # Índice da página a ser substituída
                
                # Para cada página na memória, verifica quando será usada novamente
                for j, pagina_mem in enumerate(memoria):
                    try:
                        # Procura o próximo uso da página após o índice atual
                        prox_uso = sequencia_paginas[indice+1:].index(pagina_mem)
                    except ValueError:
                        # Se a página não for mais usada, define distância infinita
                        prox_uso = float('inf')
                        
                    # Atualiza a página a ser substituída se encontrar uma mais distante
                    if prox_uso > maior_distancia:
                        maior_distancia = prox_uso
                        indice_substituir = j
                
                # Substitui a página selecionada
                memoria[indice_substituir] = pagina
    return contador_falhas

# Algoritmo LRU (Least Recently Used)
def substituicao_lru(qtd_quadros, sequencia_paginas):

    memoria = []  # Lista para representar os quadros de memória
    historico_uso = {}  # Dicionário para armazenar o último acesso de cada página
    contador_falhas = 0  # Contador de falhas de página
    
    # Percorre cada página na sequência com seu índice
    for indice, pagina in enumerate(sequencia_paginas):
        # Verifica se a página não está na memória (falha de página)
        if pagina not in memoria:
            contador_falhas += 1  # Incrementa o contador de falhas
            
            # Se ainda há espaço na memória, apenas adiciona a página
            if len(memoria) < qtd_quadros:
                memoria.append(pagina)
            else:
                # Encontra a página com o último acesso mais antigo
                pagina_lru = min(memoria, key=lambda p: historico_uso.get(p, -1))
                # Substitui a página LRU pela nova página
                memoria[memoria.index(pagina_lru)] = pagina
        
        # Atualiza o histórico de uso com o índice atual (último acesso)
        historico_uso[pagina] = indice
    
    return contador_falhas

# Execução principal
arquivo_entrada = "entrada2.txt"
dados = carregar_dados_arquivo(arquivo_entrada)

# Separa o número de quadros da sequência de páginas
num_quadros = dados[0]
referencia_paginas = dados[1:]

# Calcula as falhas para cada algoritmo
falhas_fifo = substituicao_fifo(num_quadros, referencia_paginas)
falhas_otm = substituicao_otima(num_quadros, referencia_paginas)
falhas_lru = substituicao_lru(num_quadros, referencia_paginas)

# Exibe os resultados
print(f"FIFO {falhas_fifo}")
print(f"OTM {falhas_otm}")
print(f"LRU {falhas_lru}")


# ----- FEITO POR HÉLIO E THOMAS -----