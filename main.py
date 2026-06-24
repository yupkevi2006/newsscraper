from newspaper import Article
import feedparser

def fetch_news(feed_url, limit=5):
    print("\n🔍 Fetching latest news...\n")
    
    feed = feedparser.parse(feed_url)

    if not feed.entries:
        print("No news found!")
        return

    for i, entry in enumerate(feed.entries[:limit], 1):
        print(f"\n📰 Article {i}")
        print("=" * 60)

        url = entry.link
        article = Article(url)

        try:
            article.download()
            article.parse()

            print("Title:", article.title)
            print("\nSummary:", article.text[:300], "...")
            print("\nRead more:", url)

        except Exception as e:
            print("❌ Failed to fetch article:", e)


if __name__ == "__main__":
    # You can change RSS feed here
    feed_url = "http://feeds.bbci.co.uk/news/rss.xml"
    
    fetch_news(feed_url)