from pytube import YouTube
from Regulator import BuildSavePath
from Converter import ConvertMp3


def DownloadVideo(list_video):
    # 下載位置
    savePath = BuildSavePath()
    for URL in list_video:
        try:
            yt = YouTube(URL)
            print('下載 %s' % yt.title)
            yt.register_on_progress_callback(onProgress)
            yt.register_on_complete_callback(onComplete)
            # 選取下載串流類型
            # 加上 only_audio=True 雖然下載檔案比較小，但是下載很慢
            # stream = yt.streams.filter(only_audio=True).first()
            stream = yt.streams.first()
            # 執行下載動作
            # TODO 下載前先確認檔案是否已存在，已存在的不重複下載
            stream.download(savePath)
        except Exception as e:
            print('下載失敗 %s' % URL)
            print(e)


def onProgress(stream, chunk, file_handler, bytes_remaining):
    # 顯示下載進度
    mb = 2**20
    total = stream.filesize
    progress = total-bytes_remaining
    percent = progress/total*100
    print('進度...{:05.2f}% ({:.2f}/{:.2f} MB)'
          .format(percent, progress/mb, total/mb), end='\r')


def onComplete(stream, file_handler):
    # 下載完成執行動作
    ConvertMp3(file_handler.name)
    return


if __name__ == "__main__":
    # 測試
    urlList = ['https://www.youtube.com/watch?v=AQWYfvgh_ws']
    DownloadVideo(urlList)
