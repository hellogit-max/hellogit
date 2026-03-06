import os
import requests
import feedparser

# 깃허브 Secrets에서 값 가져오기
TOKEN = os.environ['TELEGRAM_TOKEN']
CHAT_ID = os.environ['TELEGRAM_CHAT_ID']

def send_news():
    # 네이버 뉴스 RSS (작동 확인된 주소)
    rss_url = "https://news.google.com/rss?hl=ko&gl=KR&ceid=KR:ko"
    feed = feedparser.parse(rss_url)
    
    message = "📢 오늘의 주요 뉴스\n\n"
    
    # 상위 5개 뉴스만 가져오기
    for entry in feed.entries[:5]:
        message += f"🔹 {entry.title}\n🔗 {entry.link}\n\n"
    
    # 텔레그램 전송
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }
    
    response = requests.post(url, data=payload)
    print(response.json())  # 실행 로그에 결과 출력

if __name__ == "__main__":
    send_news()
