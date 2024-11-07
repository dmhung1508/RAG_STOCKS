from chroma import add_text
from summary import summary_text
import config
import os
from mongodb import get_articles, update_article
from tqdm import tqdm
import time
from hashtag import classify_text
def main():
    while True:
        # Lấy bài viết và số lượng
        articles, count = get_articles()
        print("Processing articles")
        
        # Xử lý từng bài viết
        for article in tqdm(articles, desc="Processing articles", total=count):
            try:
                article_content = article['textContent']
                classification = classify_text(article_content)
                if classification['Symbol'] == None or classification['Symbol'] == "null":
                    symbol = "other"
                else:
                    symbol = classification['Symbol']
                if classification['CategoryName'] == None:
                    category = "other"
                else:
                    category = classification['CategoryName']
                summary = classification['Summary']
                posted_date = article['postedAt'].strftime('%Y-%m-%d')
                add_text(summary, article['_id'], posted_date, article['sourceName'], article['link'], article_content, symbol, category)
                update_article(article['_id'])
            except Exception as e:
                print(f"Error processing article: {article['_id']}")
                print(e)
                continue
        
        print("All articles processed")
        
        # Vòng lặp đếm ngược 15 phút
        print("Waiting for the next run in 15 minutes...")
        for i in tqdm(range(900), desc="Countdown to next run", unit="s"):
            time.sleep(1)  # Chờ 1 giây mỗi vòng lặp
main()