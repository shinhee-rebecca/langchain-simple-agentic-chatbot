"""
🫧 버블이 챗봇 - 메인 실행 파일
"""
from langchain_core.messages import HumanMessage, AIMessage

from llm.model import get_llm
from prompts.persona import get_prompt_template
from tools import ALL_TOOLS
from agent.executor import create_agent


def chat():
    """대화 루프 실행"""
    # 초기화
    llm = get_llm(temperature=0.7)
    prompt = get_prompt_template()
    agent_executor = create_agent(llm, ALL_TOOLS, prompt)
    
    chat_history = []
    
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
        
        response = agent_executor.invoke({
            "input": user_input,
            "chat_history": chat_history,
        })
        
        print(f"\n🫧 버블이: {response['output']}")
        
        chat_history.append(HumanMessage(content=user_input))
        chat_history.append(AIMessage(content=response['output']))


if __name__ == "__main__":
    chat()