from duckduckgo_search import DDGS
import json

# results = DDGS().text("keir starmer", max_results=10)
results = DDGS().news("keir starmer", max_results=10)
# results = DDGS().answers("keir starmer news")
# results = DDGS().suggestions("keir starmer")
# results = DDGS().chat("write a haiku about how much you love custard")
print(json.dumps(results, indent=4))