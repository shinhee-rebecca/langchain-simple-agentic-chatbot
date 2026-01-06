"""도구 모음"""
from tools.weather import get_current_weather
from tools.calculator import calculate
from tools.search import search_web

# 사용 가능한 모든 도구 목록
ALL_TOOLS = [
    get_current_weather,
    calculate,
    search_web,
]