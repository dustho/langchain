from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_ollama.chat_models import ChatOllama
from third_parties.linkedin import scrape_linkedin_profile
from agents.linkedin_lookup_agent import lookup

def ice_break_with(name: str):
    username = lookup(name=name)
    linkedin_profile_data = scrape_linkedin_profile(username, mock=True)

    summary_template = """
        given the LinkedIn information about a person: 
        {information} 

        from I want you to create:
        1. a short summary
        2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOllama(model="llama3.1:8b")
    chain = summary_prompt_template | llm | StrOutputParser()
    res = chain.invoke(input={"information": linkedin_profile_data})

    return res


if __name__ == "__main__":
    load_dotenv()
    ice_break_data = ice_break_with(name="eden marco")
    print(ice_break_data)
