"""계산기 도구"""
from langchain_core.tools import tool

@tool
def calculate(expression: str) -> str:
    """
    수학 계산을 수행합니다.
    
    Args:
        expression: 계산할 수식 (예: 2+2, 100*5)
    """
    try:
        allowed = set('0123456789+-*/.() ')
        if not all(c in allowed for c in expression):
            return "허용되지 않은 문자가 포함되어 있어요"
        result = eval(expression)
        return f"{result}"
    except Exception as e:
        return f"계산 오류: {str(e)}"