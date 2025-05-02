class Tarefa:
    def __init__(self, chegada, duracao):
        self.chegada = chegada    # Tempo de chegada da tarefa no sistema
        self.duracao = duracao    # Tempo necessário para concluir a tarefa
        self.inicio = None        # Tempo em que a tarefa começa a ser executada
        self.fim = 0              # Tempo em que a tarefa termina
        self.espera = 0           # Tempo total de espera antes da execução
        self.retorno = 0          # Tempo total no sistema (fim - chegada)
        self.resposta = 0         # Tempo de resposta (início - chegada)
        self.restante = duracao   # Tempo restante de execução da tarefa

# Função para carregar as tarefas a partir de um arquivo de entrada
def carregar_arquivo(caminho):
    tarefas = []
    with open(caminho, 'r') as arquivo:
        for linha in arquivo:
            chegada, duracao = map(int, linha.split())
            tarefas.append(Tarefa(chegada, duracao))
    return tarefas

# Algoritmo First-Come, First-Served (FCFS) - Executa tarefas na ordem de chegada
def algoritmo_fcfs(tarefas):
    tarefas.sort(key=lambda t: t.chegada)  # Ordena tarefas por tempo de chegada
    tempo_corrente = 0
    for tarefa in tarefas:
        tempo_corrente = max(tempo_corrente, tarefa.chegada)  # Garante que o tempo atual seja pelo menos o tempo de chegada
        tarefa.inicio = tempo_corrente
        tarefa.fim = tarefa.inicio + tarefa.duracao
        tarefa.retorno = tarefa.fim - tarefa.chegada
        tarefa.resposta = tarefa.inicio - tarefa.chegada
        tarefa.espera = tarefa.retorno - tarefa.duracao
        tempo_corrente += tarefa.duracao  # Atualiza o tempo corrente
    return tarefas

# Algoritmo Shortest Job First (SJF) - Executa a tarefa com menor duração disponível
def algoritmo_sjf(tarefas):
    tarefas.sort(key=lambda t: (t.chegada, t.duracao))  # Ordena por chegada e menor duração
    tempo_corrente = 0
    tarefas_concluidas = []
    while tarefas:
        prontas = [t for t in tarefas if t.chegada <= tempo_corrente]  # Tarefas disponíveis para execução
        if prontas:
            tarefa_selecionada = min(prontas, key=lambda t: t.duracao)  # Escolhe a mais curta
            tarefas.remove(tarefa_selecionada)
            tarefa_selecionada.inicio = tempo_corrente
            tarefa_selecionada.fim = tarefa_selecionada.inicio + tarefa_selecionada.duracao
            tarefa_selecionada.retorno = tarefa_selecionada.fim - tarefa_selecionada.chegada
            tarefa_selecionada.espera = tarefa_selecionada.retorno - tarefa_selecionada.duracao
            tarefa_selecionada.resposta = tarefa_selecionada.inicio - tarefa_selecionada.chegada
            tempo_corrente += tarefa_selecionada.duracao
            tarefas_concluidas.append(tarefa_selecionada)
        else:
            tempo_corrente = min(tarefas, key=lambda t: t.chegada).chegada  # Avança o tempo até a próxima tarefa
    return tarefas_concluidas

# Algoritmo Round Robin (RR) - Distribui o tempo de CPU igualmente entre as tarefas
def algoritmo_rr(tarefas, quantum=2):
    fila_execucao = []
    fila_finalizada = []
    tempo_corrente = 0
    indice = 0
    tarefas_ordenadas = sorted(tarefas, key=lambda t: t.chegada)  # Ordena por chegada
    
    while True:
        while indice < len(tarefas_ordenadas) and tarefas_ordenadas[indice].chegada <= tempo_corrente:
            fila_execucao.append(tarefas_ordenadas[indice])
            indice += 1
        
        if fila_execucao:
            tarefa_atual = fila_execucao.pop(0)
            if tarefa_atual.inicio is None:
                tarefa_atual.inicio = tempo_corrente
            
            execucao = min(quantum, tarefa_atual.restante)  # Executa por no máximo "quantum" unidades de tempo
            tarefa_atual.restante -= execucao
            tempo_corrente += execucao
            
            if tarefa_atual.restante > 0:
                while indice < len(tarefas_ordenadas) and tarefas_ordenadas[indice].chegada <= tempo_corrente:
                    fila_execucao.append(tarefas_ordenadas[indice])
                    indice += 1
                fila_execucao.append(tarefa_atual)  # Reinsere a tarefa na fila se ainda não terminou
            else:
                tarefa_atual.fim = tempo_corrente
                fila_finalizada.append(tarefa_atual)
        else:
            tempo_corrente += 1  # Avança o tempo até a chegada da próxima tarefa
        
        if not fila_execucao and indice >= len(tarefas_ordenadas):
            break  # Sai do loop quando todas as tarefas forem concluídas
    
    for tarefa in fila_finalizada:
        tarefa.resposta = tarefa.inicio - tarefa.chegada
        tarefa.espera = tarefa.fim - tarefa.chegada - tarefa.duracao
        tarefa.retorno = tarefa.fim - tarefa.chegada
    
    return fila_finalizada

# Calcula médias dos tempos de espera, resposta e retorno
def calcular_medias(tarefas):
    media_espera = sum(t.espera for t in tarefas) / len(tarefas)
    media_retorno = sum(t.retorno for t in tarefas) / len(tarefas)
    media_resposta = sum(t.resposta for t in tarefas) / len(tarefas)
    return media_espera, media_retorno, media_resposta

# Leitura do arquivo com as tarefas
caminho_arquivo = 'entrada.txt'
lista_tarefas = carregar_arquivo(caminho_arquivo)

# Execução dos algoritmos e cálculo de médias
resultado_fcfs = algoritmo_fcfs([Tarefa(t.chegada, t.duracao) for t in lista_tarefas])
resultado_sjf = algoritmo_sjf([Tarefa(t.chegada, t.duracao) for t in lista_tarefas])
resultado_rr = algoritmo_rr([Tarefa(t.chegada, t.duracao) for t in lista_tarefas], quantum=2)

# Cálculo das médias
media_fcfs = calcular_medias(resultado_fcfs)
media_sjf = calcular_medias(resultado_sjf)
media_rr = calcular_medias(resultado_rr)

# Impressão dos resultados formatados
print(f"FCFS: {media_fcfs[1]:.2f} {media_fcfs[2]:.2f} {media_fcfs[0]:.2f}")
print(f"SJF: {media_sjf[1]:.2f} {media_sjf[2]:.2f} {media_sjf[0]:.2f}")
print(f"RR: {media_rr[1]:.2f} {media_rr[2]:.2f} {media_rr[0]:.2f}")