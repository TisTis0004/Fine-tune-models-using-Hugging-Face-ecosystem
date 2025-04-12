Assignment 1 -- Exploring Generative AI with Hugging Face
\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Course : Special Topics in Artificial Intelligence Instructor: Dr.
Yousef Sanjalawe Student : Fares Hatahet Semester : Spring 2024/2025

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--
Project Structure:

\- report.pdf : 1-page reflection on challenges and ethics -
text_generation.py : Task 1 - Text generation using GPT-2 -
summarization.py : Task 2 - Summarization and Q&A using BART -
scrap_CNN_news.py : Task 2 - Scraps news to be used for summarization -
train.ipynb : Task 3 - Fine-tuning distilgpt2 on dad jokes -
generated_jokes.txt : Output samples from fine-tuned model -
generated_stories.txt : Output stories from text generation model -
joke-model \| \| \|- checkpoint-65000 : Fine-tuned model - README.txt :
This file

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--
Task 1: Text Generation (text_generation.py) - Generates creative story
continuations using GPT-2. - Prompts the user 3 times for a story
beginning. - Uses text-generation pipeline with sampling (temperature =
0.7). - Saves each prompt and generated story to generated_stories.txt.
To run: python text_generation.py

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--
Task 2: Summarization & Q&A (summarization.py + scrap_CNN_news.py) -
Scrapes a CNN article, summarizes it, and answers a question about it. -
scrap_CNN_news.py: Scrapes the latest article and saves it to
news_article.txt. - summarization.py: Summarizes the article using
facebook/bart-large-cnn. - Answers a question using
google/electra-base-discriminator. - Saves the result to
news_article_summarization.txt. First run: python scrap_CNN_news.py then
run: python summarization.py

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--
Task 3: Fine-Tuning (train_llm.ipynb) - Fine-tunes distilgpt2 on the
\'shuttie/dadjokes\' dataset. - Shows before/after outputs and evaluates
on the test set. To open: Use Jupyter Notebook or VS Code to run
train.ipynb

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--
Requirements: Install the dependencies provided in the requirements file
(reqs.txt) if you have a GPU capable of training the model. Or it can be
run in Google Colab.
