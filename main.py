import os
import requests
import feedparser

# 깃허브 Secrets에서 값 가져오기
TOKEN = os.environ['TELEGRAM_TOKEN']
CHAT_ID = os.environ['TELEGRAM_CHAT_ID']

def send_news():
    # 구글 뉴스 RSS
    rss_url = "https://news.google.com/rss?hl=ko&gl=KR&ceid=KR:ko"
    feed = feedparser.parse(rss_url)
    
    # 메시지 시작 (HTML 사용 알림)
    message = "<b>📢 오늘의 주요 뉴스 (10개)</b>\n\n"
    
    # 상위 10개 뉴스 가져오기
    for i, entry in enumerate(feed.entries[:10], 1):
        # HTML 태그를 사용해 제목에 링크를 숨김: <a href='주소'>제목</a>
        message += f"{i}. <a href='{entry.link}'>{entry.title}</a>\n\n"
    
    # 텔레그램 전송
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "HTML",      # 이 부분이 핵심입니다!
        "disable_web_page_preview": True # 링크 미리보기(썸네일)를 꺼서 더 간결하게
    }
    
    response = requests.post(url, data=payload)
    print(response.json())

if __name__ == "__main__":
    send_news()
