from dotenv import load_dotenv
from langchain.agents.output_parsers import ReActSingleInputOutputParser
from langchain.output_parsers import OutputFixingParser
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import Tool
from langchain.agents import (
  create_react_agent,
  AgentExecutor
)
from langchain import hub
from langchain_ollama import ChatOllama
from tools.tools import get_linkedin_profile_url

load_dotenv()

def lookup(name: str) -> str:
  llm = ChatOllama(temperature=0, model="llama3.1:8b")
  template = """
  given the full name {name_of_person} I want to get it me a link to their LinkedIn profile page.
  your answer should contain only a url. 
  """
  prompt_template = PromptTemplate(template=template, input_variables=["name_of_person"])
  tools_for_agent = [
    Tool(
      name="Crawl Google 4 linkedin profile page", # 간결하지만 LLM 추론 엔진이 명확하게 이해하고, 적절한 상황에 사용할 수 있도록 작성
      func=get_linkedin_profile_url,
      description="useful for when you need get the LinkedIn page URL",
    )
  ]
  react_prompt = hub.pull("hwchase17/react") + "\n >>> Output should be started with `Final Answer: [link]`"
  agent = create_react_agent(llm=llm, tools=tools_for_agent, prompt=react_prompt)
  agent_executor = AgentExecutor(agent=agent, tools=tools_for_agent, verbose=True)
  result = agent_executor.invoke(
      input={"input": prompt_template.format_prompt(name_of_person=name)},
  )

  linked_profile_url = result["output"]
  return linked_profile_url

if __name__ == '__main__':
  linkedin_url = lookup(name="jaeho lim")
  print(linkedin_url)
