"""검색 도구"""
from langchain_core.tools import tool

@tool
def search_web(query: str) -> str:
    """
    웹에서 정보를 검색합니다.
    
    Args:
        query: 검색할 키워드
    """
    # 실제 구현 시 DuckDuckGo, Tavily 등 API 사용
    return f"'{query}'에 대한 검색 결과입니다."