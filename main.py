## Importa classes principais do SDK 'crewai' e utilitários
from crewai import Agent, Task, Crew
from dotenv import load_dotenv
from crewai_tools import SerperDevTool
import os

## Carrega variáveis de ambiente do arquivo .env para o processo atual
load_dotenv()

## Recupera a chave da OpenAI a partir da variável de ambiente
## - Usada para autenticar chamadas à API de geração de texto
openai_api_key = os.getenv("OPENAI_API_KEY")
serper_api_key = os.getenv("SERPER_API_KEY")

## Verificação simples: garante que a chave exista antes de prosseguir
if not openai_api_key:
    raise ValueError("OPENAI_API_KEY não encontrada. Verifique seu arquivo .env.")

if not serper_api_key:
    raise ValueError("SERPER_API_KEY não encontrada. Verifique seu arquivo .env.")

## Define variáveis de ambiente esperadas pela biblioteca/SDK
os.environ["OPENAI_API_KEY"] = openai_api_key
os.environ["OPENAI_MODEL_NAME"] = "gpt-4o"
os.environ["SERPER_API_KEY"] = serper_api_key

## === Definição dos agentes ===
## Cada `Agent` representa um papel humano/virtual com objetivo e histórico:
## - `planejador`: cria o plano de conteúdo (público, tópicos, palavras-chave)
planejador = Agent(
    role="Planejador de Conteúdo",
    goal="Criar um plano de conteúdo claro e estratégico sobre {topic} para o ano {year}",
    backstory="Você é especialista em planejamento de conteúdo sobre tecnologia e Inteligência Artificial.",
    llm = "gpt-4o",
    tools = [SerperDevTool()],
    cache = True,
    allow_delegation = False,
    memory = True,
    respect_contex_window = True,
    max_retry_limit = 3,
    max_execution_time = 60,
    verbose=True,
)

## - `escritor`: gera o texto do artigo com base no plano
escritor = Agent(
    role="Escritor de Conteúdo",
    goal="Escrever um artigo simples, claro e bem estruturado sobre {topic} para o ano {year}",
    backstory="Você é um redator especializado em transformar temas técnicos em textos fáceis de entender.",
    llm = "gpt-4o",
    tools = [SerperDevTool()],
    cache = True,
    allow_delegation = False,
    memory = True,
    respect_contex_window = True,
    max_retry_limit = 2,
    max_execution_time = 200,
    verbose=True,
)

## - `editor`: revisa e prepara o texto final para publicação
editor = Agent(
    role="Editor de Conteúdo",
    goal="Revisar o conteúdo, melhorar clareza, corrigir erros e deixar o texto pronto para publicação",
    backstory="Você é um editor profissional focado em clareza, gramática e organização do texto.",
    llm = "gpt-4o",
    tools = [SerperDevTool()],
    cache = True,
    allow_delegation = False,
    memory = True,
    respect_contex_window = True,
    max_retry_limit = 3,
    max_execution_time = 300,
    verbose=True,
)


## === Definição das tarefas (Tasks) ===
## Cada `Task` descreve o que deve ser feito e o output esperado, vinculada a um agente:
planejar = Task(
    description="Crie um plano de conteúdo sobre {topic}, com público-alvo, objetivo, tópicos principais e palavras-chave.",
    expected_output="Um plano de conteúdo organizado com público-alvo, objetivo, tópicos principais e palavras-chave.",
    agent=planejador,
)

escrever = Task(
    description="Com base no plano criado, escreva um artigo em Markdown sobre {topic}.",
    expected_output="Um artigo em Markdown com título, introdução, subtítulos, desenvolvimento e conclusão.",
    agent=escritor,
)

editar = Task(
    description="Revise o artigo, corrija erros, melhore a clareza e entregue a versão final pronta para publicação.",
    expected_output="Artigo final revisado em Markdown, claro e pronto para publicação.",
    agent=editor,
)


## === Montagem da equipe (Crew) ===
## `Crew` organiza agentes e tarefas e coordena a execução
equipe = Crew(
    agents=[planejador, escritor, editor],
    tasks=[planejar, escrever, editar],
    verbose=True,
)


## Executa o fluxo de trabalho passando inputs (aqui: tópico e ano do conteúdo)
resultado = equipe.kickoff(inputs={"topic": "Inteligência Artificial", "year": 2026})


## Exibe o resultado final no console
print("\n\n===== RESULTADO FINAL =====\n")
print(resultado)