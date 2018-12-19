# 2018 TOC Project
 ## Environment
 *   Python 3
 *   transitions
 *   pygraphviz
 *   ngrok
 ## Finite State Machine
 ![](https://i.imgur.com/nDqATqp.png)
 ## Usage
> The initial state is set to start.
> The starting state is triggered to user state by typing start.
> The user's state is triggered to advance to another state,and another state is triggered to advance to other states,too.
> Some states will back to user state after the bot replies corresponding message.
>And in some states, you can either choose end to go back to user or back to go back to the upper layer.
> If you want to leave user , you should type seeya.
 ## My bot
我的聊天室功用是要尋找的服飾鞋子的專賣店家相關資訊。
一開始，使用者有三個選擇，分別為南紡購物中心、NIKE專賣店、GUCCI專賣店，然後，讓使用者輸入南紡購物中心、NIKE專賣店、GUCCI專賣店，會進到下一層，剩下的選項都是打使用者要尋找的選項開頭第一個開頭即可。
舉例來說如：南紡,NIKE專賣店,GUCCI專賣店->  NIKE專賣店->板鞋/跑鞋/足鞋/籃球鞋/健身鞋-> 跑鞋-> NIKE_VAPORMAX_FLYKNIT->價格資訊