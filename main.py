"""
🫧 버블이 챗봇 - 메인 실행 파일
"""
from llm.model import get_llm
from prompts.persona import get_system_prompt
from tools import ALL_TOOLS
from agent.executor import create_agent


def chat():
    """대화 루프 실행"""
    # 초기화
    llm = get_llm(temperature=0.7)
    system_prompt = get_system_prompt()
    agent = create_agent(llm, ALL_TOOLS, system_prompt, verbose=False)

    messages = []

    print("=" * 50)
    print("🫧 버블이 챗봇에 오신 것을 환영합니다!")
    print("   (종료: 'quit' 또는 'exit')")
    print("=" * 50)

    while True:
        user_input = input("\n👤 You: ").strip()

        if user_input.lower() in ['quit', 'exit', '종료']:
            print("\n🫧 버블이: 안녕~ 다음에 또 봐! 👋")
            break

        if not user_input:
            continue

        messages.append({"role": "user", "content": user_input})

        response = agent.invoke({"messages": messages})

        ai_message = response["messages"][-1]
        output = ai_message.content

        print(f"\n🫧 버블이: {output}")

        messages.append({"role": "assistant", "content": output})


if __name__ == "__main__":
    chat()