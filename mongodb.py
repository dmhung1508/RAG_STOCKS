from pymongo import MongoClient
from datetime import datetime, timedelta
import config
# MongoDB connection details
client = MongoClient(config.MONGO_URI)
db = client['vn-newsflow']
collection = db['stockarticles']
def get_articles():
    today = datetime.now().date()

    # Query to find articles from the last 2 days based on 'postedAt' field
    query = {
        'postedAt': {
            '$gte': datetime.combine(today - timedelta(days=3), datetime.min.time()),
            '$lt': datetime.combine(today + timedelta(days=1), datetime.min.time())
        },
        'process': False  # Only fetch articles that haven't been processed
    }

    # Fetch articles
    articles = collection.find(query)
    count = collection.count_documents(query)
    print("Số lượng bài viết lấy được:", count)
    return articles, count
def update_article(article_id):
    collection.update_one({'_id': article_id}, {'$set': {'process': True}})
    # Process articles
    # for article in articles:
    #     # Process the article (placeholder for actual processing logic)
    #     print(f"Processing article: {article['_id']}")

    #     # Mark the article as processed
    #     collection.update_one({'_id': article['_id']}, {'$set': {'process': True}})
