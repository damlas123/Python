import transformers
print(transformers.__version__)
from transformers import pipeline

pipe = pipeline("fill-mask", model="bert-base-uncased")

# Farklı cümlelerde maske kelimeleri dene
results = pipe("I didn't feel good . Am I [MASK] ?", top_k=10)  # En iyi 5 sonucu al
for result in results:
    print(f"Word: {result['token_str']}, Score: {result['score']}")
