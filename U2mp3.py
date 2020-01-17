import argparse


def command():
    '''
    使用CLI執行時，取得參數
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--url', nargs='+', help='YouTube網址')
    parser.add_argument('-v', '--video', nargs='+', help='YouTube影片代碼')
    parser.add_argument('-f', '--file', nargs='+', help='影片網址列表檔案')
    args = parser.parse_args()
    U2mp3(args.url, args.video, args.file)


def U2mp3(URL=None, VideoCode=None, File=None):
    # 有Youtube網址參數
    if URL is not None:
        print('URL=')
        print(URL)
    # 有Youtube影片代碼
    if VideoCode is not None:
        print('VideoCode')
        print(VideoCode)
    # 有網址清單檔案
    if File is not None:
        print('File')
        print(File)


if __name__ == "__main__":
    command()
