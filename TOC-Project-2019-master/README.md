# 2018 TOC Project
 ## Environment
 *   Python 3
 *   transitions
 *   pygraphviz
 *   ngrok
 ## Finite State Machine
 ![](https://i.imgur.com/nDqATqp.png)
 ## fb粉專
 https://www.facebook.com/%E6%9C%8D%E9%A3%BE%E6%99%82%E5%B0%9A%E5%93%81%E7%89%8C-214520036142602/?modal=admin_todo_tour
 ## Usage
>1. The initial state is set to start.
>2. The starting state is triggered to user state by typing start.
>3 .The user's state is triggered to advance to another state,and another state is triggered to advance to other states,too.
>4. Some states will back to user state after the bot replies corresponding message.
>5. In some states, you can either choose end to go back to user or back to go back to the upper layer.
>6. If you want to leave user , you should type seeya.
 ## My bot
>我的聊天室功能主要是要尋找台南服飾專賣店商品價格的相關資訊。
>一開始，使用者有三個選擇，分別為南紡購物中心、nike專賣店、gucci專賣店這三家店，接著，讓使用者輸入南紡購物中心、NIKE專賣店、GUCCI專賣店這三間其中一間，會進到下一層，選擇服飾或鞋款的種類，選定後，會回傳出價格!
舉例來說如：
南紡,NIKE專賣店,GUCCI專賣店->

<-NIKE專賣店

板鞋/跑鞋/足鞋/籃球鞋/健身鞋->

<-跑鞋

nike_zoom/nike_fly_flyknit/nike_vapormax_flyknit->

<-NIKE_VAPORMAX_FLYKNIT

->價格資訊

## 問題
 * BOT一直收不到我傳的訊息，上週三下課後找助教解決，試過各種方法(砍掉所有應用程式重新創)，依然無法解決!
