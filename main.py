import feedparser
import requests
import os

# 깃허브 Secrets에서 정보 가져오기
TOKEN = os.environ['8792132626:AAE9kDbx2I39qbSjy6e4lVsFS4nTKsqTEuM']
CHAT_ID = os.environ['TELEGRAM_CHAT_ID']

def send_news():
    # 네이버 뉴스 RSS (주요 뉴스)
    url = "https://news.naver.com/rss/rss_feed.naver?template=all"
    feed = feedparser.parse(url)
    
    message = "📢 오늘의 주요 뉴스\n\n"
    for entry in feed.entries[:5]: # 상위 5개 뉴스만
        message += f"🔹 {entry.title}\n🔗 {entry.link}\n\n"
    
    # 텔레그램으로 전송
    telegram_url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    params = {'chat_id': CHAT_ID, 'text': message}
    requests.get(telegram_url, params=params)

if __name__ == "__main__":
    send_news()
