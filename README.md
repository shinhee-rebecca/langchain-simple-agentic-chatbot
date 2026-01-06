# SimpleChat Agent Demo

LangChain 기반의 간단한 AI 챗봇 에이전트 데모 프로젝트입니다.

## 소개

이 프로젝트는 LangChain을 사용하여 도구(Tools)를 활용할 수 있는 대화형 AI 에이전트를 구현한 예제입니다. 기본적으로 "버블이"라는 친근한 페르소나를 가진 챗봇이 포함되어 있습니다.

## 주요 기능

- 대화형 CLI 인터페이스
- 커스터마이징 가능한 AI 페르소나
- 확장 가능한 도구 시스템
  - 날씨 조회
  - 계산기
  - 웹 검색

## 설치

### 요구사항

- Python 3.11 이상
- [uv](https://github.com/astral-sh/uv) (권장) 또는 pip

### 설치 방법

```bash
# 저장소 클론
git clone https://github.com/your-username/simplechat-agent-demo.git
cd simplechat-agent-demo

# uv 사용 시
uv sync

# pip 사용 시
pip install -e .
```

## 환경 설정

### .env 파일 설정

프로젝트 루트에 `.env` 파일을 생성하고 다음 내용을 설정하세요:

```env
OPENAI_API_KEY=your-openai-api-key-here
OPENAI_MODEL=gpt-4o-mini
```

| 변수 | 설명 | 기본값 |
|------|------|--------|
| `OPENAI_API_KEY` | OpenAI API 키 (필수) | - |
| `OPENAI_MODEL` | 사용할 모델 | `gpt-4o-mini` |

> **Note**: `.env` 파일은 `.gitignore`에 포함되어 있어 Git에 커밋되지 않습니다. 각자 환경에 맞게 설정해야 합니다.

## 실행

```bash
# uv 사용 시
uv run python main.py

# 가상환경 활성화 후
python main.py
```

실행하면 대화형 인터페이스가 시작됩니다:

```
==================================================
버블이 챗봇에 오신 것을 환영합니다!
   (종료: 'quit' 또는 'exit')
==================================================

You: 서울 날씨 알려줘
버블이: 서울은 현재 맑음이고, 기온은 15°C야!
```

## 프로젝트 구조

```
simplechat-agent-demo/
├── main.py              # 메인 실행 파일
├── agent/
│   └── executor.py      # 에이전트 생성 로직
├── config/
│   └── settings.py      # 환경 설정 관리
├── llm/
│   └── model.py         # LLM 모델 초기화
├── prompts/
│   └── persona.py       # 페르소나 및 시스템 프롬프트
├── tools/
│   ├── __init__.py      # 도구 모음 (ALL_TOOLS)
│   ├── weather.py       # 날씨 조회 도구
│   ├── calculator.py    # 계산기 도구
│   └── search.py        # 웹 검색 도구
├── pyproject.toml       # 프로젝트 의존성
└── .env                 # 환경 변수 (직접 생성 필요)
```

## 확장 가이드

### 페르소나 커스터마이징

`prompts/persona.py`에서 AI의 성격과 말투를 자유롭게 수정할 수 있습니다:

```python
# prompts/persona.py
MY_PERSONA = """
너는 '나만의 AI'라는 이름의 전문적인 비서야.

## 성격
- 정중하고 전문적이야
- 존댓말을 사용해

## 역할
- 사용자의 업무를 지원해
"""

def get_system_prompt(persona: str = MY_PERSONA) -> str:
    return persona
```

### 새로운 도구 추가

`tools/` 디렉토리에 새로운 도구를 추가할 수 있습니다:

```python
# tools/my_tool.py
from langchain_core.tools import tool

@tool
def my_custom_tool(param: str) -> str:
    """
    도구에 대한 설명을 작성합니다.

    Args:
        param: 파라미터 설명
    """
    # 도구 로직 구현
    return f"결과: {param}"
```

새로운 도구를 `tools/__init__.py`에 등록합니다:

```python
# tools/__init__.py
from tools.my_tool import my_custom_tool

ALL_TOOLS = [
    get_current_weather,
    calculate,
    search_web,
    my_custom_tool,  # 새 도구 추가
]
```

### 활용 예시

- **고객 서비스 봇**: 페르소나를 수정하고 FAQ 검색 도구 추가
- **업무 비서**: 캘린더, 이메일 도구 연동
- **교육용 봇**: 퀴즈, 학습 자료 검색 도구 추가

## 의존성

- [LangChain](https://python.langchain.com/) - LLM 애플리케이션 프레임워크
- [langchain-openai](https://python.langchain.com/docs/integrations/llms/openai/) - OpenAI 통합
- [python-dotenv](https://github.com/theskumar/python-dotenv) - 환경 변수 관리

## 라이선스

MIT License