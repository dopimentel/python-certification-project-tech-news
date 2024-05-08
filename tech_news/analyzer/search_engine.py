from datetime import datetime
from tech_news.database import db


# Requisito 7
def search_by_title(title):
    query = db.news.find(
        {"title": {"$regex": title, "$options": "i"}},
    )
    return [(news["title"], news["url"]) for news in query]


# Requisito 8
def search_by_date(date):
    try:
        date_obj = datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")

    formatted_date = date_obj.strftime("%d/%m/%Y")

    query = db.news.find(
        {"timestamp": {"$regex": formatted_date, "$options": "i"}},
    )

    return [(news["title"], news["url"]) for news in query]


# Requisito 9
def search_by_category(category):
    query = db.news.find(
        {"category": {"$regex": category, "$options": "i"}},
    )
    return [(news["title"], news["url"]) for news in query]
