from pytube import YouTube
from Prepare import AutoPackage


def DownloadVideo(list_video):
    # 前置處理，檢查是否已安裝需要的套件，沒有的話自動安裝
    # AutoPackage('pytube')
    # AutoPackage('pytube3')
    for URL in list_video:
        try:
            yt = YouTube(URL)
            print('下載 %s' % yt.title)
            yt.register_on_progress_callback(onProgress)
            yt.register_on_complete_callback(onComplete)
            # 加上 only_audio=True 雖然下載檔案比較小，但是下載很慢
            # stream = yt.streams.filter(only_audio=True).first()
            stream = yt.streams.first()
            # TODO 改為下載至相同資料夾內
            stream.download('B:\\tmp')
        except:
            print('下載失敗 %s' % URL)


def onProgress(stream, chunk, file_handler, bytes_remaining):
    # 顯示下載進度
    mb = 2**20
    total = stream.filesize
    progress = total-bytes_remaining
    percent = progress/total*100
    print('進度...{:05.2f}% ({:.2f}/{:.2f} MB)'
          .format(percent, progress/mb, total/mb), end='\r')

def onComplete(stream, file_handler):
    print('\n下載完成')
    # 下載完成執行動作
    return  # do work


if __name__ == "__main__":
    # 測試
    urlList = ['https://www.youtube.com/watch?v=AQWYfvgh_ws']
    DownloadVideo(urlList)
