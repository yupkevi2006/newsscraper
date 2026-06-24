import streamlit as st
from newspaper import Article
import feedparser

st.set_page_config(page_title="NewsScraper", page_icon="📰")

st.title("📰 NewsScraper App")
st.write("Fetch latest news from any RSS feed")

# Input field
feed_url = st.text_input("Enter RSS Feed URL:", "http://feeds.bbci.co.uk/news/rss.xml")

# Button
if st.button("Fetch News"):
    feed = feedparser.parse(feed_url)

    if not feed.entries:
        st.error("No news found!")
    else:
        for i, entry in enumerate(feed.entries[:5], 1):
            st.subheader(f"📰 Article {i}")

            url = entry.link
            article = Article(url)

            try:
                article.download()
                article.parse()

                st.write("**Title:**", article.title)
                st.write("**Summary:**", article.text[:300] + "...")
                st.markdown(f"[Read more]({url})")

            except Exception as e:
                st.error(f"Error: {e}")