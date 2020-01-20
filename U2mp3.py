import argparse
from Prepare import AutoPackage
from pytube import YouTube


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
    # 前置處理，檢查是否已安裝需要的套件，沒有的話自動安裝
    AutoPackage('pytube')
    AutoPackage('pytube3')

    # 有Youtube網址或影片代碼參數
    if URL is not None:
        print('URL')
        print(URL)

    # 有網址清單檔案
    if File is not None:
        print('File')
        print(File)


if __name__ == "__main__":
    command()
