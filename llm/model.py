"""LLM 모델 초기화"""
from langchain_openai import ChatOpenAI
from config.settings import OPENAI_API_KEY, OPENAI_MODEL

def get_llm(temperature: float = 0.7) -> ChatOpenAI:
    """ChatOpenAI 모델 인스턴스 반환"""
    return ChatOpenAI(
        api_key=OPENAI_API_KEY,
        model=OPENAI_MODEL,
        temperature=temperature,
    )