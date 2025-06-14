# scrape_discourse.py
import requests, json
from datetime import datetime

BASE="https://discourse.onlinedegree.iitm.ac.in/c/courses/tds-kb/34"
START = datetime(2025,1,1)
END = datetime(2025,4,14)
posts = []
page = 0

while True:
    r = requests.get(f"{BASE}/c/tds.json?page={page}")
    if r.status_code!=200: break
    topics = r.json().get("topic_list", {}).get("topics", [])
    if not topics: break
    for t in topics:
        dt = datetime.fromisoformat(t["created_at"].replace("Z",""))
        if START<=dt<=END:
            posts.append({
                "title": t["title"],
                "url": f"{BASE}/t/{t['slug']}/{t['id']}",
                "created_at": t["created_at"]
            })
    page += 1

with open("discourse_posts.json", "w") as f:
    json.dump(posts, f, indent=2)

print(f"✅ Saved {len(posts)} posts to discourse_posts.json")