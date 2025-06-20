import datetime
import os
import requests
from bs4 import BeautifulSoup

# API configuration (using GitHub Secret)
API_KEY = os.getenv("NEWSAPI_KEY")
if not API_KEY:
    raise ValueError("NEWSAPI_KEY environment variable not set. Add it as a GitHub Secret.")
BASE_URL = "https://newsapi.org/v2/everything"

# Current date and time
current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M %Z")
print(f"Generated on: {current_date} (CDT)")

# Parameters for NewsAPI query
params = {
    "q": "network engineering OR AI OR Cisco OR Aruba OR Palo Alto Networks OR cybersecurity OR automation",  # Simplified query
    "from": (datetime.datetime.now() - datetime.timedelta(days=30)).strftime("%Y-%m-%d"),  # 30 days back
    "to": datetime.datetime.now().strftime("%Y-%m-%d"),  # Up to today
    "sortBy": "publishedAt",
    "language": "en",
    "apiKey": API_KEY
}

# Fetch news from NewsAPI
try:
    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()
    news_data = response.json()
    print(f"API Response Status: {news_data.get('status')}")
    print(f"Total Articles: {news_data.get('totalResults', 0)}")
    news_data = news_data.get("articles", [])
except requests.exceptions.RequestException as e:
    print(f"Error fetching news: {e}")
    news_data = []

# Filter and process news
today_news = [
    {
        "title": article["title"],
        "summary": article.get("description", "No summary available"),
        "source": article["url"],
        "date": article["publishedAt"][:10],
        "vendors": [vendor for vendor in ["Cisco", "Aruba", "Palo Alto Networks", "HPE", "DriveNets", "IBM", "Microsoft", "Adtran"] if vendor.lower() in article["title"].lower() or vendor.lower() in article.get("description", "").lower()],
        "topics": ["AI-driven networking", "network automation", "cybersecurity", "cloud networking", "job skills"] if any(topic.lower() in article["title"].lower() or topic.lower() in article.get("description", "").lower() for topic in ["AI", "automation", "security", "cloud", "skills"]) else []
    }
    for article in news_data if article.get("publishedAt", "").startswith(datetime.datetime.now().strftime("%Y-%m-%d"))
]

# Fallback to last 7 days if no today news
if not today_news and news_data:
    recent_news = [
        {
            "title": article["title"],
            "summary": article.get("description", "No summary available"),
            "source": article["url"],
            "date": article["publishedAt"][:10],
            "vendors": [vendor for vendor in ["Cisco", "Aruba", "Palo Alto Networks", "HPE", "DriveNets", "IBM", "Microsoft", "Adtran"] if vendor.lower() in article["title"].lower() or vendor.lower() in article.get("description", "").lower()],
            "topics": ["AI-driven networking", "network automation", "cybersecurity", "cloud networking", "job skills"] if any(topic.lower() in article["title"].lower() or topic.lower() in article.get("description", "").lower() for topic in ["AI", "automation", "security", "cloud", "skills"]) else []
        }
        for article in news_data if (datetime.datetime.now() - datetime.datetime.strptime(article.get("publishedAt", ""), "%Y-%m-%dT%H:%M:%SZ")).days <= 7
    ]
    today_news = recent_news if recent_news else today_news

# Function to print news summary
def print_news_summary():
    if not today_news:
        print("No news available for today or the last 7 days.")
        return

    print("\n=== Top Network Engineering News ===")
    for news in today_news:
        print(f"\n{news['title']}")
        print(f"- Summary: {news['summary']}")
        print(f"- Source: {news['source']}")
        print(f"- Date: {news['date']}")
        print(f"- Vendors: {', '.join(news['vendors']) if news['vendors'] else 'None'}")
        print(f"- Topics: {', '.join(news['topics']) if news['topics'] else 'None'}")

    # Job Skills and Certifications Section
    print("\n=== Changes in Network Engineering Job Skills and Certifications ===")
    print("AI and automation are reshaping network engineering roles. Key updates include:")
    print("- Demand for skills in AI-augmented tools like Cisco AI Canvas and Palo Alto Precision AI is growing.")
    print("- Certifications such as Cisco DevNet (evolving to CCNA/CCNP Automation) are critical for 2026.")
    print("- Zero Trust Architecture (ZTA) expertise, supported by tools like Prisma and Duo, is increasingly required.")

# Function to save history to file
def save_history():
    with open("news_history.txt", "a") as f:
        f.write(f"\n--- News Summary for {current_date} ---\n")
        if not today_news:
            f.write("No news available for today or the last 7 days.\n")
        else:
            for news in today_news:
                f.write(f"\n{news['title']}\n- Summary: {news['summary']}\n- Source: {news['source']}\n- Date: {news['date']}\n- Vendors: {', '.join(news['vendors']) if news['vendors'] else 'None'}\n- Topics: {', '.join(news['topics']) if news['topics'] else 'None'}\n")
            f.write("\n=== Changes in Network Engineering Job Skills and Certifications ===\n")
            f.write("- Demand for skills in AI-augmented tools like Cisco AI Canvas and Palo Alto Precision AI is growing.\n")
            f.write("- Certifications such as Cisco DevNet (evolving to CCNA/CCNP Automation) are critical for 2026.\n")
            f.write("- Zero Trust Architecture (ZTA) expertise, supported by tools like Prisma and Duo, is increasingly required.\n")

# Execute the summary and save history
if __name__ == "__main__":
    print_news_summary()
    save_history()
