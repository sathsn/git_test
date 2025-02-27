from transformers import pipeline

summarizer = pipeline("summarization")
text = "Hugging Face is an AI research company that develops open-source AI tools."
summary = summarizer(text, max_length=50, min_length=10, do_sample=False)

print(summary[0]["summary_text"])

