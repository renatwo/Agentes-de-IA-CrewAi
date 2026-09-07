# Arquitetura do Projeto

Este projeto utiliza o framework CrewAI para criar um fluxo colaborativo entre múltiplos agentes de Inteligência Artificial.

## Fluxo dos agentes

O processo é dividido em três agentes principais:

### 1. Planejador de Conteúdo

Responsável por analisar o tema solicitado e criar um planejamento estratégico.

Principais responsabilidades:

- Definir o público-alvo
- Identificar os principais tópicos
- Criar uma estrutura de conteúdo
- Sugerir palavras-chave
- Organizar o fluxo de produção

### 2. Escritor de Conteúdo

Recebe o planejamento produzido pelo primeiro agente e transforma as informações em um conteúdo estruturado.

Principais responsabilidades:

- Criar título e introdução
- Desenvolver os tópicos
- Organizar o conteúdo em Markdown
- Produzir uma conclusão

### 3. Editor de Conteúdo

Responsável pela revisão final do material produzido.

Principais responsabilidades:

- Revisar gramática
- Melhorar clareza
- Ajustar organização
- Melhorar coerência
- Preparar o conteúdo para publicação

## Fluxo da arquitetura

```text
Usuário
   |
   v
Planejador
   |
   v
Escritor
   |
   v
Editor
   |
   v
Conteúdo Final
