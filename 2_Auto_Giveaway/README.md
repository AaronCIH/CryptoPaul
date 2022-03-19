# 項目2. 自動抽獎機器人: 
此工具提供大家自動參與多種模式的抽獎，只需要設定好想參加的抽獎頻道清單，剩下的就交給他吧!
主要是透過python讀取預設的帳號權限&頻道資訊，爬蟲偵測是否有抽獎機器人或者相關關鍵字，除此之外每個頻道的Pid都是動態的正常兩週會更新一次。  
功能設計上有加上了分享有效性檢驗，可以透過"1_giveaway_chs.csv":Vaild欄位檢查是否還有效，若為'False'就需要更新頻道連結，或者是此頻道未有任何訊息!
另外尚未找到較佳的中獎通知方法，因此將成功參與的抽獎紀錄都寫在"2_Participate_log.csv"內，方便大家檢查所有抽獎項目。
**注意: 由於每個頻道使用的抽獎機器人並不相同，我已預設大多數頻道的機器人，若日後有遇到新型的抽獎機器人也歡迎大家回報!** 

# 使用介紹:
## Step1. 下載檔案
若是熟悉git的朋友可自行下載，初次使用的朋友可以跳回[首頁](https://github.com/Cihsaing/CryptoPaul)，點選右上角的"Code"(綠色按鈕) -> Download Zip.
下載完成後，至下載資料夾為至解壓縮應該會看見所有項目。  
<img src="https://user-images.githubusercontent.com/91179422/156627722-3a7414d3-4642-4e62-b43c-0d1986cc4884.png" width="100" alt="下載"/>

## Step2. DC Authorization 設定
此時為了讓程式可以幫你進行操作，需要獲得您的帳號權限，其中需要注意!
!!! 每個DC授權碼代表著你的帳號，可進行任何操作，請妥善保管 !!!
!!! 每個DC授權碼代表著你的帳號，可進行任何操作，請妥善保管 !!!
!!! 每個DC授權碼代表著你的帳號，可進行任何操作，請妥善保管 !!!
* 步驟:
```
1. 瀏覽器登入預使用Discord，並進入任何一個Channels
2. 瀏覽器(Chrome, Edge..) 點選右上角 (三點處) -> 更多工具 -> 開發人員工具
3. 選擇 **網路(Network)** -> **Fetch/XHR**
4. 接著重新整理網頁，可以看到有許多條例跑出來
5. 找到 **Messages** -> **標頭(Header)** -> 找到**authorization**
6. 選取自己的authorization code，貼至 **0_authorizations.txt** 檔案內即可。
```
**注意每一行只能貼一個帳號的authorization code，且結尾不可以有空格與換行!** 
<img src="https://user-images.githubusercontent.com/91179422/156632572-fb96375e-0f88-413d-a5e1-7093817abc4a.png" alt="auth教學"/>

## Step3. 分享channels 設定
這邊需要手動整理抽獎頻道和記錄他們的觀察機器人，此步驟需要耗費較長時間，但一勞永逸。
而由於每個頻道都會有自己的動態PID，因此複製網址即可，我已透過程式讀取。
* 步驟:
```
1. 瀏覽器登入預使用Discord，並進入任何一個giveaway頻道!
2. 複製網址連結，每個網址最後面一串就是牠們的動態PID。
3. 貼至"2_giveaway_chs.csv"檔案中的**Url**位置，注意此時貼上要從function貼上才不會被轉換格式，可以看到貼上後格子內顯示應該沒有縮寫!，可看
4. 建議記錄一下 DC名稱，Channel名稱，方便記錄抽獎紀錄，未來動態Pid連結失效時也方便檢查，注意不能使用中文!
5. 接著開始記錄抽獎關鍵字，此步驟每個頻道都不同稍顯複雜，整體流程跟紀錄帳號權限很像，後面熟悉時也可以不用每個都點開
6. 瀏覽器(Chrome, Edge..) 點選右上角 (三點處) -> 更多工具 -> 開發人員工具
7. 選擇 **網路(Network)** -> **Fetch/XHR** ，接著重新整理網頁，可以看到有許多條例跑出來，可看[圖1]
8. 接著可以對應頻道內容找到他們機器人的類型，對應的訊息指標是指倒數第幾筆，可將其展開，可看[圖2]
9. 優先尋找content作為條件，若無的話也可以觀察username適合種機器人，我已新增機器人包含["Giveaway Boat", "GiveawayBoat", "TylerTakesATrip", "Lawliet"]，遇到這些機器人content可以填none.
10. 將其內容記錄至"2_giveaway_chs.csv":Keyword位置，此時要注意輸入須為MarkDown語法，詳細可以看[圖3]
```
* 挑選頻道!!
<img src="https://user-images.githubusercontent.com/91179422/159115708-c4bd23e3-edfd-4061-a214-8cc7d16ba5cc.png" alt="挑選頻道"/>

* 紀錄抽獎關鍵字!!
<img src="https://user-images.githubusercontent.com/91179422/159115795-11bc72f6-3a64-46d8-8fee-9c00ba03d070.png" alt="開啟開發者"/>
<img src="https://user-images.githubusercontent.com/91179422/159115745-ca7885bd-de53-4d21-ab43-955f089e7006.png" alt="尋找關鍵字"/>
<img src="https://user-images.githubusercontent.com/91179422/159115384-d45049d1-ac01-4bdc-80af-c2dae94e8e8a.png" alt="記錄關鍵字"/>

## Step5. 使用Python 環境開始執行
詳細執行流程與環境安裝請看以下教學步驟:
[Python環境安裝與執行教學](https://github.com/Cihsaing/CryptoPaul/blob/main/0_Python%E7%92%B0%E5%A2%83%E5%AE%89%E8%A3%9D%E6%95%99%E5%AD%B8/)  

**!!! 此版本尚未加入中獎通知，遇到一些技術障礙中，但提供了Participate_log方便大家觀察抽獎紀錄，可以每天上去手動檢查是否中獎即可 !!!**  
*BTW. 現在觀察晚上7.到晚上11.宣傳效果最佳。
執行後應該會顯示出資訊! 就代表成功囉 可以去頻道檢查是否有成功!
![image](https://user-images.githubusercontent.com/91179422/156918023-8adf71a4-c2f0-45b9-bea5-a1cade9c615e.png)


