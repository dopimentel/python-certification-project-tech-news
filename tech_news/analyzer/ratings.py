from tech_news.database import db


# Requisito 10
def top_5_categories():
    pipelines = [
        {"$unwind": "$category"},
        {"$group": {"_id": "$category", "count": {"$sum": 1}}},
        {"$sort": {"count": -1, "_id": 1}},
        {"$limit": 5},
    ]

    query = db.news.aggregate(
        pipelines,
    )

    categories = [category["_id"] for category in query]

    return categories if categories else []
