class Tarefa:
    def __init__(self, nome, prioridade, horas_estimadas):
        self.nome = nome
        self.prioridade = prioridade
        self.horas_estimadas = horas_estimadas

def criar_lista_tarefas():
    tarefas = [
        Tarefa("Implementar autenticação", "alta", 10),
        Tarefa("Desenvolver interface do usuário", "média", 20),
        Tarefa("Configurar banco de dados", "baixa", 8),
        Tarefa("Testes de unidade", "média", 15),
        Tarefa("Preparar documentação", "baixa", 12),
    ]
    return tarefas

def calcular_estimativa_total(tarefas):
    estimativa_total = 0
    for tarefa in tarefas:
        if tarefa.prioridade == "alta":
            fator_complexidade = 1.5
        elif tarefa.prioridade == "média":
            fator_complexidade = 1.2
        else:
            fator_complexidade = 1.0

        estimativa_total += tarefa.horas_estimadas * fator_complexidade

    return estimativa_total

# Criar lista de tarefas
lista_tarefas = criar_lista_tarefas()

# Calcular estimativa total de esforço
estimativa_total_esforco = calcular_estimativa_total(lista_tarefas)

print(f"A estimativa total de esforço para as tarefas é de {estimativa_total_esforco} horas.")
