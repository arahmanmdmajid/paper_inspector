import json
from serpapi.google_scholar_search_results import GoogleScholarSearchResults
client = GoogleScholarSearchResults({"q": "Coffee"})
data =client.get_json()

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)