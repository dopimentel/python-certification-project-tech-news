from tech_news.database import db


# Requisito 7
def search_by_title(title):
    query = db.news.find(
        {"title": {"$regex": title, "$options": "i"}},
    )
    return [(news["title"], news["url"]) for news in query]


# Requisito 8
def search_by_date(date):
    query = db.news.find({"timestamp": date})
    search_results = [(news["title"], news["url"]) for news in query]
    return search_results


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    raise NotImplementedError
