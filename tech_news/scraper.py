from bs4 import BeautifulSoup
import requests
from time import sleep
from tech_news.database import create_news

create_news([{"url": "https://www.google.com"}])


# Requisito 1
def fetch(url):
    headers = {
        "User-Agent": "Fake user-agent",
        # "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)
        # AppleWebKit/537.36 (KHTML, like Gecko)
        # Chrome/58.0.3029.110 Safari/537.36"
    }
    try:
        sleep(1)
        response = requests.get(url, headers=headers, timeout=5)
        response.raise_for_status()
    except requests.RequestException as e:
        print("Erro ao fazer requisição: ", e)
        return None
    return response.text


# Requisito 2
def scrape_updates(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    a = soup.find_all("a", {"class": "cs-overlay-link"})
    if a == []:
        return []
    links = [anchor.get("href") for anchor in a]
    return links


# Requisito 3
def scrape_next_page_link(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    next_page = soup.find("a", {"class": "next"})
    if next_page is None:
        return None
    next_page = next_page.get("href")
    return next_page


# Requisito 4


def extract_news_url(url):
    if "facebook.com/sharer.php?u=" in url:
        url_split = url.split("u=")

        if len(url_split) > 1:

            url = url_split[1]
            return url
    return url


def extract_number_from_string(string):
    number = "".join(filter(str.isdigit, string))
    return int(number)


def scrape_news(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    news = dict()
    sharer_link = soup.find("a", {"class": "pk-share-buttons-link"}).get(
        "href"
    )
    news["url"] = extract_news_url(sharer_link)
    news["title"] = soup.find("h1", {"class": "entry-title"}).string.strip()
    news["timestamp"] = soup.find("li", {"class": "meta-date"}).string
    news["writer"] = soup.find("span", {"class": "fn"}).text.strip()

    reading_time = soup.find("li", {"class": "meta-reading-time"}).text
    news["reading_time"] = extract_number_from_string(reading_time)

    news["summary"] = (
        soup.find("div", {"class": "entry-content"})
        .find("p")
        .get_text()
        .strip()
    )
    news["category"] = soup.find("span", {"class": "label"}).string

    return news


# print(
#     scrape_news(
#         fetch(
#             "https://blog.betrybe.com/tecnologia/jogos-iniciantes-aprender-programar/"
#         )
#     )
# )


# Requisito 5
def get_tech_news(amount):
    last_news = []

    url = "https://blog.betrybe.com/"

    while len(last_news) < amount:
        html_content = fetch(url)

        links = scrape_updates(html_content)

        for link in links:
            news_html_content = fetch(link)

            news = scrape_news(news_html_content)

            last_news.append(news)

            if len(last_news) >= amount:
                break

        next_page = scrape_next_page_link(html_content)
        if next_page is None:
            break

        url = next_page

    create_news(last_news)

    return last_news
