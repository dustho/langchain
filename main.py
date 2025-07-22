from langchain_core.prompts import PromptTemplate
from langchain_openai.chat_models import ChatOpenAI

information = """
- Name: 침착맨
- Link: https://namu.wiki/w/%EC%B9%A8%EC%B0%A9%EB%A7%A8
"""

if __name__ == "__main__":
    print("Hello World")

    summary_template = """
        given the information link about a person: 
        {information} 
        
        from I want you to create:
        1. a short summary
        2. two interesting facts about them
        
        output language is korean.
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")

    chain = summary_prompt_template | llm

    res = chain.invoke(input={"information": "I want you to create"})

    print(res)
