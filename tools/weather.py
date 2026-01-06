"""날씨 조회 도구"""
from langchain_core.tools import tool

@tool
def get_current_weather(location: str) -> str:
    """
    주어진 위치의 현재 날씨를 조회합니다.
    
    Args:
        location: 도시 이름 (예: 서울, 부산)
    """
    weather_data = {
        "서울": "맑음 ☀️, 15°C",
        "부산": "흐림 ☁️, 18°C",
        "제주": "비 🌧️, 20°C"
    }
    return weather_data.get(location, f"{location}의 날씨 정보를 찾을 수 없어요")