import subprocess
import sys

'''
前置處理模組
'''


def AutoPackage(pkg):
    '''
    檢查套件是否已安裝，如未安裝則使用pip安裝
    '''
    # TODO 是否可以修改讓他不顯示執行敘述
    rtn = subprocess.call([sys.executable, '-m', 'pip', 'show', pkg])
    if (rtn == 0):
        print('%s 已安裝' % pkg)
    else:
        print('進行安裝 %s' % pkg)
        result = subprocess.call(
            [sys.executable, '-m', 'pip', 'install', pkg])
        if (result == 0):
            print('%s 安裝完成' % pkg)
        else:
            print('%s 安裝失敗' % pkg)
