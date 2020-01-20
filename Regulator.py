import re


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
