import os
from Regulator import BuildMp3Path

def ConvertMp3(sourcePath):
    # 檔案名稱
    fileName = os.path.basename(sourcePath)
    # 目的路徑
    targetPath = os.path.join(BuildMp3Path(), fileName[:-3]+'mp3')
    # 路徑使用雙引號包住，不然檔名或者路徑空白會有錯誤
    sourcePath = '"%s"' % sourcePath
    targetPath = '"%s"' % targetPath
    # 系統呼叫 ffmpeg 執行轉檔
    # TODO 如果目的mp3有相同檔案，則忽略
    os.system('ffmpeg -i {0} {1}'.format(sourcePath, targetPath))