# Projetos de Sistemas Operacionais

Este repositório contém dois projetos desenvolvidos para a disciplina de Sistemas Operacionais.

## Projeto 1: Escalonador de Processos (`escalonador.py`)

Este projeto implementa e compara três algoritmos de escalonamento de CPU:

* **First-Come, First-Served (FCFS)**: As tarefas são executadas na ordem em que chegam.
* **Shortest Job First (SJF)**: A tarefa com o menor tempo de duração restante é executada primeiro.
* **Round Robin (RR)**: Cada tarefa recebe uma fatia de tempo (quantum = 2) para executar, alternando entre as tarefas prontas.

### Como executar

1.  Certifique-se de ter um arquivo chamado `entrada.txt` no mesmo diretório do script `escalonador.py`.
2.  O arquivo `entrada.txt` deve conter pares de números inteiros por linha, representando o tempo de chegada e a duração de cada tarefa, separados por espaço.
3.  Execute o script Python: `python escalonador.py`
4.  O script calculará e imprimirá os tempos médios de retorno, resposta e espera para cada algoritmo (FCFS, SJF, RR).

### Saída

A saída será no formato:
FCFS: [Média Retorno] [Média Resposta] [Média Espera]
SJF: [Média Retorno] [Média Resposta] [Média Espera]
RR: [Média Retorno] [Média Resposta] [Média Espera]

## Projeto 2: Substituição de Páginas (`paginas.py`)

Este projeto implementa e compara três algoritmos de substituição de páginas na memória virtual:

* **First-In, First-Out (FIFO)**: A página que está na memória há mais tempo é substituída.
* **Optimal (OTM)**: Substitui a página que será referenciada mais tarde no futuro (ou nunca mais).
* **Least Recently Used (LRU)**: Substitui a página que não foi utilizada por mais tempo.

### Como executar

1.  Certifique-se de ter um arquivo chamado `entrada2.txt` no mesmo diretório do script `paginas.py`.
2.  O arquivo `entrada2.txt` deve conter uma sequência de números inteiros. O primeiro número representa a quantidade de quadros de memória disponíveis, e os números seguintes representam a sequência de referências de páginas.
3.  Execute o script Python: `python paginas.py`
4.  O script calculará e imprimirá o número total de faltas de página para cada algoritmo (FIFO, OTM, LRU).

### Saída

A saída será no formato:
FIFO [Número de Faltas]
OTM [Número de Faltas]
LRU [Número de Faltas]

