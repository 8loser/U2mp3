import re
import os


def BuildYoutubeURL(List_URL):
    '''
    代碼、網址正規化為
    https://youtube.com/watch?v=****
    '''
    # 回傳資料的列表
    rtn = []
    # 完整網址樣板
    URL_sample = 'https://www.youtube.com/watch?v=%s'
    # 正則式樣板，取出 v=*** 資料
    pattern = 'v=([^&]+).*$'
    for item in List_URL:
        m = re.search(pattern, item)
        if m is not None:
            # 有找到參數 v=***，取出代碼
            rtn.append(URL_sample % m.group(1))
        else:
            # 沒找到對應參數，直接判定字串為代碼
            rtn.append(URL_sample % item)
    return rtn


def CheckFolder(folderName, folderDescription):
    '''
    檢查程式目錄下資料夾是否存在，不存在則建立
    '''
    # 完整資料夾路徑
    fullPath = os.path.join(os.getcwd(), folderName)
    # 資料夾是否存在，不存在則建立
    if not os.path.isdir(fullPath):
        # 顯示建立資料夾敘述
        print('建立 %s 資料夾 %s' % (folderDescription, fullPath))
        os.mkdir(fullPath)
    return fullPath

def BuildSavePath(tempFolder='temp'):
    '''
    使用參數建立完整儲存資料夾路徑回傳
    預設完整儲存路徑 {程式所在位置}\\temp
    如路徑不存在則自動建立
    '''
    return CheckFolder(tempFolder, '暫存資料夾')

def BuildMp3Path(mp3Folder='mp3'):
    '''
    建立轉換mp3後儲存資料夾 {程式所在位置}\\mp3
    資料夾不存在則自動建立
    '''
    return CheckFolder(mp3Folder, 'mp3儲存位置')