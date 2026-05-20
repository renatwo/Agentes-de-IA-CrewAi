# Agentes de IA com CrewAI

Projeto desenvolvido em Python utilizando o framework CrewAI para criação de agentes inteligentes capazes de trabalhar em conjunto na geração, planejamento e revisão de conteúdo.

Este projeto faz parte dos meus estudos em Inteligência Artificial Aplicada, automação de processos, agentes autônomos e integração com APIs.

---

## Objetivo do projeto

O objetivo deste projeto é demonstrar uma estrutura inicial de agentes de IA usando CrewAI.

O fluxo criado possui três agentes principais:

1. Planejador de Conteúdo
2. Escritor de Conteúdo
3. Editor de Conteúdo

Cada agente possui uma função específica dentro do processo, simulando uma equipe colaborativa de criação de conteúdo com Inteligência Artificial.

---

## Como funciona

O projeto executa um fluxo automatizado com três etapas:

### 1. Planejamento

O primeiro agente cria um plano de conteúdo estratégico sobre o tema informado.

Ele define:

- Público-alvo
- Objetivo do conteúdo
- Tópicos principais
- Palavras-chave
- Estrutura sugerida para o artigo

### 2. Escrita

O segundo agente usa o planejamento criado para escrever um artigo em Markdown.

Ele organiza o conteúdo com:

- Título
- Introdução
- Subtítulos
- Desenvolvimento
- Conclusão

### 3. Edição

O terceiro agente revisa o artigo final.

Ele melhora:

- Clareza
- Gramática
- Organização das ideias
- Qualidade do texto
- Preparação para publicação

---

## Tecnologias utilizadas

- Python
- CrewAI
- CrewAI Tools
- OpenAI API
- Serper API
- python-dotenv
- Git
- GitHub

---

## Estrutura do projeto

```text
.
├── main.py
├── .env.example
├── .gitignore
├── README.md
└── LICENSE
