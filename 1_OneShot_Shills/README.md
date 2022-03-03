# 項目1. 一鍵Shills工具: 
此工具提供大家自訂好宣傳內容後，一鍵分享至多個頻道當中，不僅可以幫忙宣傳保羅社區，也可以快速達成多個項目的白單條件。

## 使用介紹:
### Step1. 下載檔案
若是熟悉git的朋友可自行下載，初次使用的朋友可以跳回[首頁](https://github.com/Cihsaing/CryptoPaul)，點選右上角的"Code"(綠色按鈕) -> Download Zip.
下載完成後，至下載資料夾為至解壓縮應該會看見所有項目。  
<img src="https://user-images.githubusercontent.com/91179422/156627722-3a7414d3-4642-4e62-b43c-0d1986cc4884.png" width="100" alt="下載"/>

### Step2. DC Authorization 設定
此時為了讓程式可以幫你進行操作，需要獲得您的帳號權限，其中需要注意!
!!! 每個DC授權碼代表著你的帳號，可進行任何操作，請妥善保管 !!!
!!! 每個DC授權碼代表著你的帳號，可進行任何操作，請妥善保管 !!!
!!! 每個DC授權碼代表著你的帳號，可進行任何操作，請妥善保管 !!!
* 步驟:
  

1. 瀏覽器登入預使用Discord，並進入任何一個Channels
2. 瀏覽器(Chrome, Edge..) 點選右上角 (三點處) -> 更多工具 -> 開發人員工具
3. 選擇 **網路(Network)** -> **Fetch/XHR**
4. 接著重新整理網頁，可以看到有許多條例跑出來
5. 找到 **Messages** -> **標頭(Header)** -> 找到**authorization**
6. 選取自己的authorization code，貼至 **0_authorizations.txt** 檔案內即可。
**注意每一行只能貼一個帳號的authorization code，且結尾不可以有空格與換行!** 
<img src="https://user-images.githubusercontent.com/91179422/156632572-fb96375e-0f88-413d-a5e1-7093817abc4a.png" alt="auth教學"/>

<img src="https://user-images.githubusercontent.com/91179422/156629857-a3914484-2798-4cef-8b2f-e19fce30efc7.png" width="200" alt="開發人員工具"/>
<img src="https://user-images.githubusercontent.com/91179422/156630448-3eaaff41-6442-4453-83d7-1a601a24ddd3.png" width="200" alt="FetchXHR"/>
<img src="https://user-images.githubusercontent.com/91179422/156631419-3de0ca1a-9431-4d05-bc0d-5e715f9d47b1.png" width="200" alt="Message"/>
<img src="https://user-images.githubusercontent.com/91179422/156632095-3bbf960e-61a0-44e5-bb8b-c7b7aeb0918c.png" width="200" alt="auth"/>

![image](https://user-images.githubusercontent.com/91179422/156632572-fb96375e-0f88-413d-a5e1-7093817abc4a.png)
