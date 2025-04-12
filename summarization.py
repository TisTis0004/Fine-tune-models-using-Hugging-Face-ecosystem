from transformers import pipeline
from scrap_CNN_news import cnn_url


summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
text = open("news_article.txt", 'r').read()

summary = summarizer(text)[0]["summary_text"]


question = "What is the main issue discussed in the article?"
qa = pipeline("question-answering", model="google/electra-base-discriminator")
answer = qa(question=question, context=summary[:])['answer']

print(f"Article URL: {cnn_url}")
print(f"--- SUMMARY ---\n{summary}")
print(f"\n--- Q&A ---\nQ: {question}\nA: {answer}")


with open("news_article_summarization.txt", "w") as file:
    file.write(f"--- SUMMARY ---\n{summary}\n")
    file.write(f"\n--- Q&A ---\nQ: {question}\nA: {answer}")