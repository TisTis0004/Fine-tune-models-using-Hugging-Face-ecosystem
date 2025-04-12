import requests
from bs4 import BeautifulSoup

cnn_url = "https://edition.cnn.com"

if __name__ == "__main__":
    response = requests.get(cnn_url)
    soup = BeautifulSoup(response.text, 'html.parser')


    container_tag = soup.find('div', class_="container__title")
    article_link_tag = container_tag.find('a', href=True)


    article_url = cnn_url + article_link_tag["href"]
    article_response = requests.get(article_url)
    article_soup = BeautifulSoup(article_response.text, 'html.parser')


    news_content_div = article_soup.find_all("div", class_="live-story-post__wrapper")
    news_paragraphs = news_content_div[1].find_all("p")

    with open("news_article.txt", 'w') as file:
        file.write("Latest CNN News")
        for paragraph in news_paragraphs:
            file.write(paragraph.get_text())