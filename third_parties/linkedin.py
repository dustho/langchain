import os
import requests
import pprint
from dotenv import load_dotenv

load_dotenv()

# https://gist.githubusercontent.com/psarangi550/74fb57e9da78f8693af99e5cfa88d779/raw/d4f28f8365f63f7b6b5d8a6158211de636b0e51e/eden-macro-tweet.json

def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = False):
  """ scrape information from LinkedIn profiles,
  Manually scrape the information from the LinkedIn profile"""

  if mock:
    linkedin_profile_url = "https://gist.githubusercontent.com/nishantbhurani24/37fd9b6d87628c08b4614d835d5e63b5/raw/4eee5d13ad84db79bd744cde3d9be976220e1565/eden-marco-scrapin.json"
    response = requests.get(linkedin_profile_url, timeout=10)
  else:
    api_endpoint = "...alternative of scrapin api..."
    params = {
      "apikey": os.environ["SCRAPIN_API_KEY"], # environ, getenv 차이
      "linkedInUrl": linkedin_profile_url,
    }
    response = requests.get(api_endpoint, params=params, timeout=10)

  data = response.json()
  data = {
    k: v
    for k, v in data.items()
    if v not in ([], "", None)
    and k not in ["certification"]
  }
  return data

if __name__ == "__main__":
  scrape_linkedin_profile(linkedin_profile_url="", mock=True)