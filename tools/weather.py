"""날씨 조회 도구 - wttr.in API 사용"""
import requests
from langchain_core.tools import tool


@tool
def get_current_weather(location: str) -> str:
    """
    주어진 위치의 현재 날씨를 조회합니다.

    Args:
        location: 도시 이름 (예: 서울, Seoul, Tokyo, New York)
    """
    try:
        # wttr.in API 호출 (JSON 형식)
        url = f"https://wttr.in/{location}?format=j1"
        headers = {"Accept-Language": "ko"}

        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        data = response.json()

        # 현재 날씨 정보 추출
        current = data["current_condition"][0]

        # 날씨 상태 (한국어 설명 사용 가능하면 사용)
        weather_desc = current.get("lang_ko", [{}])
        if weather_desc and len(weather_desc) > 0:
            condition = weather_desc[0].get("value", current["weatherDesc"][0]["value"])
        else:
            condition = current["weatherDesc"][0]["value"]

        temp_c = current["temp_C"]
        feels_like = current["FeelsLikeC"]
        humidity = current["humidity"]
        wind_kmph = current["windspeedKmph"]

        # 지역 정보
        area = data["nearest_area"][0]
        area_name = area["areaName"][0]["value"]
        country = area["country"][0]["value"]

        return (
            f"{area_name}, {country}\n"
            f"날씨: {condition}\n"
            f"기온: {temp_c}°C (체감 {feels_like}°C)\n"
            f"습도: {humidity}%\n"
            f"바람: {wind_kmph}km/h"
        )

    except requests.exceptions.Timeout:
        return f"날씨 서버 응답 시간이 초과되었어요. 잠시 후 다시 시도해 주세요."
    except requests.exceptions.RequestException as e:
        return f"날씨 정보를 가져오는 중 오류가 발생했어요: {str(e)}"
    except (KeyError, IndexError):
        return f"'{location}'의 날씨 정보를 찾을 수 없어요. 도시 이름을 확인해 주세요."
