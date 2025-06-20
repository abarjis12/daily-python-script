# scripts/main.py



import feedparser
import datetime

# Define search topics and RSS URLs (can add more as needed)
topics = {
    "Cisco": "https://news.google.com/rss/search?q=cisco+ai+network+engineering",
    "Aruba HPE": "https://news.google.com/rss/search?q=aruba+ai+network+engineering",
    "Palo Alto Networks": "https://news.google.com/rss/search?q=palo+alto+networks+ai+network",
    "General AI Networking": "https://news.google.com/rss/search?q=network+engineering+artificial+intelligence+automation"
}

output_lines = []
output_lines.append(f"Network Engineering & AI Daily News - {datetime.date.today()}\n")
output_lines.append("---------------------------------------------------------------\n")

for vendor, url in topics.items():
    feed = feedparser.parse(url)
    output_lines.append(f"\n--- {vendor} ---\n")
    if feed.entries:
        for entry in feed.entries[:3]:  # Show top 3 news items per topic
            title = entry.title
            link = entry.link
            published = entry.published if "published" in entry else "No date"
            summary = entry.summary if "summary" in entry else ""
            output_lines.append(f"* {title}\n  {link}\n  {published}\n")
    else:
        output_lines.append("No news found today.\n")

# Skills/Certification section (static advice; can be made dynamic if needed)
output_lines.append("\n--- Skills & Certification Trends ---\n")
output_lines.append(
    "• Increasing demand for network automation and AI-driven monitoring skills (Python, Ansible, APIs).\n"
    "• Cisco's DevNet certification continues to gain importance alongside traditional CCNA/CCNP.\n"
    "• AI/ML knowledge is now a preferred skill in network engineering job descriptions.\n"
    "• Palo Alto and Cisco have introduced more training for AI-enhanced security solutions and automation.\n"
    "• Stay up-to-date: Follow official vendor blogs, LinkedIn Learning, and exam blueprints for changes."
)

# Write output to file
with open("network_news.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(output_lines))

print("Network Engineering & AI news update completed.")
