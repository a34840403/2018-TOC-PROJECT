from transitions.extensions import GraphMachine

from utils import send_text_message

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )

    def is_going_to_user(self, event):
        
        if event.get("message") and event['message'].get("text"):
            text = event['message']['text']
            return text.lower() == 'start'
        return False
      

    def is_going_to_state1(self, event):
        
       if event.get("message") and event['message'].get("text"):
            text = event['message']['text']
            return text.lower() == '南紡購物中心'
     #  return False

    def is_going_to_state11(self, event):
        
        if event.get("message") and event['message'].get("text"):
            text = event['message']['text']
            return text.lower() == 'bubbery'
      # return False

    def is_going_to_state12(self, event):
        
        if event.get("message") and event['message'].get("text"):
            text = event['message']['text']
            return text.lower() == 'g2000'
      #  return False

    def is_going_to_state2(self, event):
        
       if event.get("message") and event['message'].get("text"):
            text = event['message']['text']
            return text.lower() == 'nike專賣店'
      #  return False
        
    def is_going_to_state21(self, event):
        
        if event.get("message") and event['message'].get("text"):
            text = event['message']['text']
            return text.lower() == '板鞋'
       # return False

    def is_going_to_state211(self, event):
        
       if event.get("message") and event['message'].get("text"):
            text = event['message']['text']
            return text.lower() == 'nike_class_cortez'
       # return False

    def is_going_to_state22(self, event):
        
       if event.get("message") and event['message'].get("text"):
            text = event['message']['text']
            return text.lower() == '跑鞋'
      #  return False

    def is_going_to_state221(self, event):
        
       if event.get("message") and event['message'].get("text"):
            text = event['message']['text']
            return text.lower() == 'nike_zoom'
       # return False  

    def is_going_to_state222(self, event):
        
        if event.get("message") and event['message'].get("text"):
            text = event['message']['text']
            return text.lower() == 'nike_fly_flyknit'
      #  return False


    def is_going_to_state223(self, event):
        
        if event.get("message") and event['message'].get("text"):
            text = event['message']['text']
            return text.lower() == 'nike_vapormax_flyknit'
     #   return False

    def is_going_to_state23(self, event):
        
       if event.get("message") and event['message'].get("text"):
            text = event['message']['text']
            return text.lower() == '足鞋'
     #   return False


    def is_going_to_state231(self, event):
        
        if event.get("message") and event['message'].get("text"):
            text = event['message']['text']
            return text.lower() == 'nike_timepox'
      #  return False
        
    def is_going_to_state24(self, event):
        
       if event.get("message") and event['message'].get("text"):
            text = event['message']['text']
            return text.lower() == '籃球鞋'
     #   return False

    def is_going_to_state241(self,event):
         if event.get("message") and event['message'].get("text"):
            text = event['message']['text']
            return text.lower() == 'lebron_16'
      #  return False
        
    def is_going_to_state242(self,event):
         if event.get("message") and event['message'].get("text"):
            text = event['message']['text']
            return text.lower() == 'kyrie_5'
      #  return False
      
       
    def is_going_to_state25(self,event):
         if event.get("message") and event['message'].get("text"):
            text = event['message']['text']
            return text.lower() == '健身鞋'
      #  return False
      
    def is_going_to_state251(self,event):
         if event.get("message") and event['message'].get("text"):
            text = event['message']['text']
            return text.lower() == 'nike_metcon'
      # return False
      
    def is_going_to_state252(self,event):
        if event.get("message") and event['message'].get("text"):
            text = event['message']['text']
            return text.lower() == 'nike_flex'
      #  return False

    def is_going_to_state3(self,event):
         if event.get("message") and event['message'].get("text"):
            text = event['message']['text']
            print(text.lower() == 'gucci專賣店')
            return text.lower() == 'gucci專賣店'
      # return False
            
    def back_to_state1(self,event):
        
        text = send_text_message
        return text.lower() == 'back'

    def back_to_state22(self,event):
        
        text = send_text_message
        return text.lower() == 'back'

    def back_to_start(self,event):
        
        text = send_text_message
        return text.lower() == 'seeya'

    def back_to_state24(self,event):
        
        text = send_text_message
        return text.lower() == 'back'

    def back_to_state25(self,event):
        
        text = send_text_message
        return text.lower() == 'back'

    def end(self,event):
        
        text = send_text_message
        return text.lower() == 'end'

    def on_enter_user(self, event):
        
         sender_id = event['sender']['id']
         send_text_message(sender_id, "南紡購物中心\nnike專賣店\ngucci專賣店")

    def on_exit_user(self,event):
        
        print('Leaving user')

    def on_enter_state1(self,event):
        
        sender_id = event['sender']['id']
        send_text_message(sender_id, "bubbery\nG2000")

    def on_exit_state1(self,event):
        print('Leaving state1')

    def on_enter_state11(self, event):
        
        sender_id = event['sender']['id']
        send_text_message(sender_id, '上 衣：2000NT\n'
                                     '褲 子：1500NT\n'
                                     '襯 衫：3000NT\n')
        self.go_back()

    def on_exit_state11(self,event):
        print('Leaving state11')

    def on_enter_state12(self, event):
        sender_id = event['sender']['id']

        send_text_message(sender_id, '上 衣：2000NT\n'
                                  '褲 子：1500NT\n'
                                  '襯 衫：3000NT\n')
        self.go_back()

    def on_exit_state12(self,event):
        print('Leaving state12')

    def on_enter_state2(self,event):
        sender_id = event['sender']['id']
        send_text_message(sender_id, "板鞋\n跑鞋\n足鞋\n籃球鞋\n健身鞋")

    def on_exit_state2(self,event):
        print('Leaving state2')

    def on_enter_state21(self, event):
        sender_id = event['sender']['id']
        send_text_message(sender_id, "nike_class_cortez")

    def on_exit_state21(self,event):
        print('Leaving state2')

    def on_enter_state211(self, event):
        sender_id = event['sender']['id']
        send_text_message(sender_id, '原 價：3000\n'
                                     '特 價：2000')        
        self.go_back()

    def on_exit_state211(self,event):
        print('Leaving state211')

    def on_enter_state22(self,event):
        sender_id = event['sender']['id']
        send_text_message(sender_id,'nike_zoom\nnike_fly_flyknit\nnike_vapormax_flyknit')
  
    def on_exit_state22(self,event):
        print('Leaving state22')

    def on_enter_state221(self, event):
        sender_id = event['sender']['id']
        send_text_message(sender_id,'原 價：3000\n'
                                    '特 價：2000')


    def on_exit_state221(self,event):
        print('Leaving state221')

    def on_enter_state222(self, event):
        sender_id = event['sender']['id']
        send_text_message(sender_id,'原 價：3000\n'
                                    '特 價：2000')

    def on_exit_state222(self,event):
        print('Leaving state222')

    def on_enter_state223(self, event):
        sender_id = event['sender']['id']
        send_text_message(sender_id,'原 價：3000\n'
                                    '特 價：2000')

    def on_exit_state223(self,event):
        print('Leaving state223')

    def on_enter_state23(self, event):
        sender_id = event['sender']['id']
        send_text_message(sender_id,'拖鞋')
    

    def on_exit_state23(self,event):
        print('Leaving state23')

    def on_enter_state231(self, event):
        sender_id = event['sender']['id']
        send_text_message(sender_id,'原 價：3000\n'
                                    '特 價：2000')
        self.go_back()

    def on_exit_state231(self,event):
        print('Leaving state231')

    def on_enter_state24(self, event):
        sender_id = event['sender']['id']
        send_text_message(sender_id,'lebron_16\nkyrie_5')
       

    def on_exit_state24(self,event):
        print('Leaving state24')

    def on_enter_state241(self, event):
        sender_id = event['sender']['id']
        send_text_message(sender_id,'原 價：3000\n'
                                    '特 價：2000')
        
    def on_exit_state241(self,event):
        print('Leaving state241')

    def on_enter_state242(self, event):
        sender_id = event['sender']['id']
        send_text_message(sender_id,'原 價：3000\n'
                                    '特 價：2000')

    def on_exit_state242(self,event):
        print('Leaving state242')

    def on_enter_state25(self,event):
        sender_id = event['sender']['id']
        send_text_message(sender_id,'nike_metcon\nnike_flex')

    def on_exit_state25(self, event):
        print('Leaving state25')

    def on_enter_state251(self,event):
        sender_id = event['sender']['id']
        send_text_message(sender_id,'原 價：3000\n'
                                    '特 價：2000')
        self.go_back()

    def on_exit_state251(self,event):
        print('Leaving state251')

    def on_enter_state252(self,event):
        sender_id = event['sender']['id']
        send_text_message(sender_id,'原 價：3000\n'
                                    '特 價：2000')
        self.go_back()

    def on_exit_state252(self,event):
        print('Leaving state252')

    def on_enter_state3(self, event):
        sender_id = event['sender']['id']
        send_text_message(sender_id,'查無此分店\n'
                                    '查無此分店')
        self.go_back()

    def on_exit_state3(self,event):
        print('Leaving state3')
