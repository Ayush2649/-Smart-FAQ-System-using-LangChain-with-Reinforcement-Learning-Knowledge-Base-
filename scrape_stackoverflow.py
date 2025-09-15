import pandas as pd
from stackapi import StackAPI
from bs4 import BeautifulSoup

# Topics to scrape
topics = ["reinforcement learning", "supervised learning", "unsupervised learning", "semi-supervised learning"]

SITE = StackAPI('stackoverflow')
SITE.max_pages = 3   # scrape 3 pages per topic
SITE.page_size = 50

all_data = []

for topic in topics:
    print(f"🔍 Scraping for topic: {topic}")
    questions = SITE.fetch('search/advanced', q=topic, site='stackoverflow', filter='withbody')
    
    for item in questions['items']:
        q_title = item.get('title', '')
        q_body = BeautifulSoup(item.get('body', ''), "html.parser").get_text()
        accepted_answer_id = item.get('accepted_answer_id', None)

        if accepted_answer_id:
            ans = SITE.fetch(f'answers/{accepted_answer_id}', filter='withbody')
            if ans['items']:
                answer_body = BeautifulSoup(ans['items'][0]['body'], "html.parser").get_text()
                all_data.append({
                    "topic": topic,
                    "question": q_title,
                    "answer": answer_body
                })

# Save to CSV
df = pd.DataFrame(all_data)
df.to_csv("stackoverflow_faq.csv", index=False, encoding="utf-8")
print(f"✅ Saved {len(df)} Q&A pairs to stackoverflow_faq.csv")
