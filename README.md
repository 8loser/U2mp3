# U2mp3
Youtube轉mp3

* 安裝需求套件
    * pip install -r requirements.txt

* 需求套件
    * pytube
    * pytube3

* 參數
    ```
    python U2mp3.py -h
    ```
    * -u (--url), YouTube網址或影片代碼(v=***)
    * -f (--file), YouTube網址清單或影片代碼清單的檔案

* 使用方法
    * 使用直接傳入網址
    ```
    python U2mp3.py -u https://www.youtube.com/watch?v=jDV5q37rGlg
    ```
    * 傳入多個網址
    ```
    python U2mp3.py -u https://www.youtube.com/watch?v=jDV5q37rGlg https://www.youtube.com/watch?v=nBnaYNWmTWo
    ```
    * 簡化，只傳參數 v
        * https://www.youtube.com/watch?v=<font color="red">jDV5q37rGlg</font>
        * https://www.youtube.com/watch?v=<font color="red">nBnaYNWmTWo</font>
    ```
    python U2mp3.py -u jDV5q37rGlg nBnaYNWmTWo
    ```
    * 傳入檔案清單
    ```
    python U2mp3.py -f youtubelist.txt youtubelist2.txt
    ```

* 備註
    * 取消pip自動安裝套件功能，因為未安裝套件import也會失敗，程式也不能跑，就無法自動安裝