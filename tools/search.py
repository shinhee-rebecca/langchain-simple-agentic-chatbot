"""검색 도구 - DuckDuckGo 사용"""
from langchain_core.tools import tool
from duckduckgo_search import DDGS


@tool
def search_web(query: str) -> str:
    """
    웹에서 정보를 검색합니다.

    Args:
        query: 검색할 키워드
    """
    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=5))

        if not results:
            return f"'{query}'에 대한 검색 결과를 찾을 수 없어요."

        # 검색 결과 포맷팅
        formatted_results = []
        for i, result in enumerate(results, 1):
            title = result.get("title", "제목 없음")
            body = result.get("body", "내용 없음")
            href = result.get("href", "")

            formatted_results.append(
                f"{i}. {title}\n"
                f"   {body[:150]}{'...' if len(body) > 150 else ''}\n"
                f"   링크: {href}"
            )

        return f"'{query}' 검색 결과:\n\n" + "\n\n".join(formatted_results)

    except Exception as e:
        return f"검색 중 오류가 발생했어요: {str(e)}"
