"""에이전트 생성 및 실행"""
from langchain.agents import create_agent as langchain_create_agent
from langchain_openai import ChatOpenAI


def create_agent(
    llm: ChatOpenAI,
    tools: list,
    system_prompt: str,
    verbose: bool = True
):
    """에이전트 실행기 생성"""
    return langchain_create_agent(
        model=llm,
        tools=tools,
        system_prompt=system_prompt,
        debug=verbose,
    )