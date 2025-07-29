from langchain_tavily.tavily_search import TavilySearch

def get_linkedin_profile_url(name: str):
  search = TavilySearch()
  response = search.run(f"{name}")
  return response