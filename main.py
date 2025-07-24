from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_ollama.chat_models import ChatOllama
from langchain_openai.chat_models import ChatOpenAI
from langchain_anthropic.chat_models import ChatAnthropic

information = """
- Link: https://en.wikipedia.org/wiki/Elon_Musk
"""

if __name__ == "__main__":
    print("Hello World")

    summary_template = """
        given the information linked page about a person: 
        {information}
        
        If you can't access internet and read content in linked page, Reply that "I can't read it".
        Do not pretend to have read or accessed any URLs or external web pages.
        Honesty and accuracy are more important than trying to be helpful. 
        
        If you can access internet and read content in link, from I want you to create:
        1. a short summary
        2. two interesting facts about them
        3. Please complete the sentence that begins with "Born to a wealthy family in Pretoria," as it appears in the linked page.
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    # llm = ChatAnthropic(temperature=0, model_name="claude-sonnet-4-20250514", max_tokens_to_sample=200, timeout=120, max_retries=2)
    # llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
    llm = ChatOllama(model="llama3.1:8b")
    chain = summary_prompt_template | llm | StrOutputParser()

    res = chain.invoke(input={"information": information})

    print(res)
