import argparse
from Regulator import BuildYoutubeURL
from Downloader import DownloadVideo


def command():
    '''
    使用CLI執行時，取得參數
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--url', nargs='+', help='YouTube網址或影片代碼')
    parser.add_argument('-f', '--file', nargs='+', help='影片網址列表檔案')
    args = parser.parse_args()
    U2mp3(args.url, args.file)


def U2mp3(URL=None, File=None):
    # 有Youtube網址或影片代碼參數
    if URL is not None:
        # 正規化為標準網址
        list_video = BuildYoutubeURL(URL)
        # 下載影片
        DownloadVideo(list_video)

    # 有網址清單檔案
    if File is not None:
        # 將所有檔案清單內容轉為list
        URL = []
        for f in File:
            fs = open(f, "r")
            # 存到list
            URL.extend(fs.readlines())
            fs.close()
        # 解析網址
        list_video = BuildYoutubeURL(URL)
        # 下載影片
        DownloadVideo(list_video)


if __name__ == "__main__":
    command()
