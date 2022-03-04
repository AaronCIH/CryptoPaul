# 項目1. 一鍵Shills工具: 
此工具提供大家自訂好宣傳內容後，一鍵分享至多個頻道當中，不僅可以幫忙宣傳保羅社區，也可以快速達成多個項目的白單條件。  
主要是透過python讀取文字檔與預設的帳號權限&頻道資訊，自動選定分享，除此之外每個頻道的Pid都是動態的正常兩週會更新一次。  
因此功能設計上多加上了分享有效性檢驗，可以透過shill_chs.csv Vaild欄位檢查是否還有效，若為'False'就需要更新頻道連結!  
**注意: 每個頻道分享限制不同，有些有符號限制、時間限制，為了大量分享統一規格化1~2小時自動分享一次，因此有些時候可能頻道內尚未冷卻就不會顯示分享資訊呦!**  
**注意: 有些字符在網頁和程式上不支援就會自動被屏蔽而一直失敗喔!** 

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
這邊需要手動整理要分享至哪些頻道，此步驟需要耗費較長時間，但一勞永逸。
而由於每個頻道都會有自己的動態PID，因此複製網址即可，我已透過程式讀取。
* 步驟:
```
1. 瀏覽器登入預使用Discord，並進入任何一個shill頻道，請認真挑選看每個頻道的規定!
2. 複製網址連結，每個網址最後面一串就是牠們的動態PID。
3. 貼至 2_shill_chs.csv檔案中的**Url**位置，注意此時貼上要從function貼上才不會被轉換格式，可以看到貼上後格子內顯示應該沒有縮寫!
4. 可以記錄一下 DC名稱，Channel名稱，方便未來動態Pid連結失效時可以方便檢查，注意不能使用中文!
```
<img src="https://user-images.githubusercontent.com/91179422/156635672-d484528f-58f2-44b4-94cb-de5e7baf2655.png" alt="挑選dc"/>
<img src="https://user-images.githubusercontent.com/91179422/156635346-920f4f61-5b63-44bd-a4d9-232c4fe91ba0.png" alt="貼上文件"/>

## Step4. 更新分享文案
可以自訂義宣傳文案，更改1_shill_content.txt 檔案，一次共享於所有頻道當中。
**後續需要分享不同內容只需更改此檔案即可!**
範例如下:
<img src="https://user-images.githubusercontent.com/91179422/156637104-251b6ea6-7737-42a6-afa3-6d27dd5c1b78.png" alt="貼上文件"/>

## Step5. 使用Python 環境開始執行
詳細執行流程與環境安裝請看以下教學步驟:
[Python環境安裝與執行教學](https://github.com/Cihsaing/CryptoPaul/blob/main/0_Python%E7%92%B0%E5%A2%83%E5%AE%89%E8%A3%9D%E6%95%99%E5%AD%B8/)  
**!!! 注意此版本目前設定為間格1~2小時自動發放所有頻道，有些較不活絡的頻道可能被占滿或者有MOD在監測將被禁言，因此也推薦大家可以執行後直接中斷，手動控制分享時間 !!!**  
*BTW. 現在觀察晚上7.到晚上11.宣傳效果最佳。
