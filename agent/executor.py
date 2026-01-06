"""에이전트 생성 및 실행"""
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

def create_agent(
    llm: ChatOpenAI,
    tools: list,
    prompt: ChatPromptTemplate,
    verbose: bool = True
) -> AgentExecutor:
    """에이전트 실행기 생성"""
    agent = create_tool_calling_agent(llm, tools, prompt)
    return AgentExecutor(
        agent=agent,
        tools=tools,
        verbose=verbose,
    )