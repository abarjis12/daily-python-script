import datetime
import requests
from bs4 import BeautifulSoup

# Current date and time
current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M %Z")
print(f"Generated on: {current_date} (CDT)")

# Simulated news data (replace with API calls for real-time data)
news_data = [
    {
        "title": "Cisco Unveils AI-Driven Networking Platform at Cisco Live 2025",
        "summary": "Cisco introduced its AI Canvas and Deep Network Model at Cisco Live 2025, enhancing network troubleshooting and automation with a domain-specific LLM, 20% more precise than previous tools. The platform integrates with Hypershield for AI-driven security across distributed networks. New Nexus switches support AI workloads with post-quantum cryptography.",
        "source": "https://www.networkworld.com/article/123456/cisco-ai-networking-2025",
        "date": "2025-06-10",
        "vendors": ["Cisco"],
        "topics": ["AI-driven networking", "network automation", "cybersecurity"]
    },
    {
        "title": "HPE Aruba Expands AI Capabilities with Networking Central",
        "summary": "HPE Aruba Networking Central now uses AI to diagnose connectivity issues quickly, showcased at HPEDiscover 2025. New distributed services switches offload security tasks, supporting AI-driven cloud networking. Liquid cooling solutions address AI workload heat challenges.",
        "source": "https://www.computerweekly.com/news/123456/hpe-aruba-ai-2025",
        "date": "2025-06-18",
        "vendors": ["HPE", "Aruba"],
        "topics": ["AI-driven networking", "cloud networking", "cybersecurity"]
    },
    {
        "title": "Palo Alto Networks Advances Precision AI for Cybersecurity",
        "summary": "Palo Alto Networks leverages Precision AI, combining machine learning and GenAI, to achieve 100% accuracy in threat detection. The company’s SASE services with Kyndryl enhance zero-trust security, impacting network engineering skills with AI-augmented threat hunting.",
        "source": "https://www.paloaltonetworks.com/blog/2025/06/precision-ai-update",
        "date": "2025-06-13",
        "vendors": ["Palo Alto Networks"],
        "topics": ["cybersecurity", "AI-driven networking", "job skills"]
    },
    {
        "title": "DriveNets Introduces Schedule Fabric for AI and HPC Networks",
        "summary": "Startup DriveNets launched Schedule Fabric, a deterministic Ethernet solution for multi-tenant AI and HPC infrastructures, addressing InfiniBand limitations. This breakthrough supports scalable cloud networking at ISC 2025.",
        "source": "https://www.drivenets.com/insights/isc-2025-ai-networking",
        "date": "2025-06-18",
        "vendors": ["DriveNets"],
        "topics": ["cloud networking", "network automation"]
    },
    {
        "title": "Cisco and xAI Join AI Infrastructure Partnership",
        "summary": "Cisco collaborates with xAI and others to raise $30 billion for AI data centers, focusing on secure AI portfolios with G42. This trend signals increased demand for network engineers skilled in AI infrastructure.",
        "source": "https://www.networkworld.com/article/123457/cisco-xai-partnership",
        "date": "2025-05-13",
        "vendors": ["Cisco", "xAI"],
        "topics": ["AI-driven networking", "job skills"]
    },
    {
        "title": "AI in Cybersecurity Market Growth to $120.8 Billion by 2032",
        "summary": "The AI cybersecurity market is projected to grow due to ML-driven threat prediction and NLP for phishing detection. Major players like IBM and Microsoft are investing heavily, reshaping network security skills.",
        "source": "https://www.newstrail.com/ai-cybersecurity-market-2025",
        "date": "2025-06-19",
        "vendors": ["IBM", "Microsoft"],
        "topics": ["cybersecurity", "job skills"]
    }
]

# Filter news for today (June 20, 2025) - currently static, adjust with real-time API
today_news = [news for news in news_data if news["date"] <= "2025-06-20"]

# Function to print news summary
def print_news_summary():
    if not today_news:
        print("No news available for today.")
        return

    print("\n=== Top Network Engineering News for June 20, 2025 ===")
    for news in today_news:
        print(f"\n{news['title']}")
        print(f"- Summary: {news['summary']}")
        print(f"- Source: {news['source']}")
        print(f"- Date: {news['date']}")
        print(f"- Vendors: {', '.join(news['vendors'])}")
        print(f"- Topics: {', '.join(news['topics'])}")

    # Job Skills and Certifications Section
    print("\n=== Changes in Network Engineering Job Skills and Certifications ===")
    print("AI and automation are reshaping network engineering roles. Key updates include:")
    print("- Cisco's DevNet certifications will transition to CCNA, CCNP, and CCIE Automation by February 2026, emphasizing AI and automation skills (https://blogs.cisco.com/2025/05/devnet-certifications-update).")
    print("- Demand for Zero Trust Architecture (ZTA) knowledge, with platforms like Palo Alto Prisma and Cisco Duo, is rising, requiring new cybersecurity expertise.")
    print("- Emerging skills include AI-augmented threat hunting and network automation, driven by tools like Cisco's AI Canvas and Palo Alto's Precision AI.")

# Execute the summary
print_news_summary()
