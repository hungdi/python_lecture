import threading
import requests
import os

# 저장할 폴더 생성
os.makedirs("images", exist_ok=True)

# 다운로드할 이미지 URL 목록
urls = [
    "https://via.placeholder.com/300x200.png?text=Image1",
    "https://via.placeholder.com/300x200.png?text=Image2",
    "https://via.placeholder.com/300x200.png?text=Image3",
    "https://via.placeholder.com/300x200.png?text=Image4",
    
]

def download_image(url, filename):
    print(f"다운로드 시작: {filename}")
    response = requests.get(url)
    with open(filename, "wb") as f:
        f.write(response.content)
    print(f"다운로드 완료: {filename}")

threads = []
for i, url in enumerate(urls, start=1):
    filename = os.path.join("images", f"image_{i}.png")
    t = threading.Thread(target=download_image, args=(url, filename))
    threads.append(t)
    t.start()

# 모든 스레드 종료 대기
for t in threads:
    t.join()

print("모든 이미지 다운로드 완료")
