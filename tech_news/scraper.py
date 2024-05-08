import requests
from time import sleep


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
        response = requests.get(url, headers=headers, timeout=3)
        response.raise_for_status()
    except requests.RequestException as e:
        print("Erro ao fazer requisição: ", e)
        return None
    return response.text


# Requisito 2
def scrape_updates(html_content):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    raise NotImplementedError
