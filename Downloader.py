from pytube import YouTube
from Prepare import AutoPackage


def Download(list_video):
    # 前置處理，檢查是否已安裝需要的套件，沒有的話自動安裝
    # AutoPackage('pytube')
    # AutoPackage('pytube3')
    for URL in list_video:
        yt = YouTube(URL)
        print(yt.title)


if __name__ == "__main__":
    # 測試
    urlList = ['https://www.youtube.com/watch?v=AQWYfvgh_ws',
            'https://www.youtube.com/watch?v=djACkCHl3JA', 'https://www.youtube.com/watch?v=o5muvc-LOlA']
    Download(urlList)
