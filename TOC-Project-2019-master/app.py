from bottle import route, run, request, abort, static_file

from fsm import TocMachine

VERIFY_TOKEN = "123"

machine = TocMachine(
    states=[
        'start',
        'user',
        'state1',
        'state2',
        'state3',
        'state11',
        'state12',
        'state21',
        'state22',
        'state23',
        'state24',
        'state25',
        'state211',
        'state221',
        'state222',
        'state223',
        'state231',
        'state241',
        'state242',
        'state251',
        'state252'
    ],
    transitions=[
        {
            'trigger': 'advance',
            'source': 'start',
            'dest': 'user',
            'conditions': 'is_going_to_user'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state1',
            'conditions': 'is_going_to_state1'
        },
        {
            'trigger': 'advance',
            'source': 'state1',
            'dest': 'state11',
            'conditions': 'is_going_to_state11'
        },
        {
            'trigger': 'advance',
            'source': 'state1',
            'dest': 'state12',
            'conditions': 'is_going_to_state12'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state2',
            'conditions': 'is_going_to_state2'
        },
        {
            'trigger': 'advance',
            'source': 'state2',
            'dest': 'state21',
            'conditions': 'is_going_to_state21'
        },
        {
            'trigger': 'advance',
            'source': 'state21',
            'dest': 'state211',
            'conditions': 'is_going_to_state211'
        },
        {
            'trigger': 'advance',
            'source': 'state2',
            'dest': 'state22',
            'conditions': 'is_going_to_state22'
        },
        {
            'trigger': 'advance',
            'source': 'state22',
            'dest': 'state221',
            'conditions': 'is_going_to_state221'
        },
        {
            'trigger': 'advance',
            'source': 'state22',
            'dest': 'state222',
            'conditions': 'is_going_to_state222'
        },
        {
            'trigger': 'advance',
            'source': 'state22',
            'dest': 'state223',
            'conditions': 'is_going_to_state223'
        },
        {
            'trigger': 'advance',
            'source': 'state2',
            'dest': 'state23',
            'conditions': 'is_going_to_state23'
        },
        {
            'trigger': 'advance',
            'source': 'state23',
            'dest': 'state231',
            'conditions': 'is_going_to_state231'
        },
        {
            'trigger': 'advance',
            'source': 'state2',
            'dest': 'state24',
            'conditions': 'is_going_to_state24'
        },
        {
            'trigger': 'advance',
            'source': 'state24',
            'dest': 'state241',
            'conditions': 'is_going_to_state241'
        },
        {
            'trigger': 'advance',
            'source': 'state24',
            'dest': 'state242',
            'conditions': 'is_going_to_state242'
        },
        {
            'trigger': 'advance',
            'source': 'state2',
            'dest': 'state25',
            'conditions': 'is_going_to_state25'
        },
        {
            'trigger': 'advance',
            'source': 'state25',
            'dest': 'state251',
            'conditions': 'is_going_to_state251'
        },

        {
            'trigger': 'advance',
            'source': 'state25',
            'dest': 'state252',
            'conditions': 'is_going_to_state252'
        },

        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state3',
            'conditions': 'is_going_to_state3'
        },
                
        {
            'trigger': 'go_back',
            'source': [
                'state211',
                'state231',
                'state3'
            ],
            'dest': 'user'
        },
        {
            'trigger': 'advance',
            'source': [
                'state11',
                'state12'
               ],
            'dest': 'state1',
            'conditions': 'back_to_state1'
        },
         {
            'trigger': 'advance',
            'source': [
                'user',             
               ],
            'dest': 'start',
            'conditions': 'back_to_start'
        },
        {
            'trigger': 'advance',
            'source': [
                'state221',
                'state222',
                'state223'
               ],
            'dest': 'state22',
            'conditions': 'back_to_state22'
        },
       
        {
            'trigger': 'advance',
            'source': [
                'state241',
                'state242'
               ],
            'dest': 'state24',
            'conditions': 'back_to_state24'
        },
        {
            'trigger': 'advance',
            'source': [
                'state251',
                'state252'
               ],
            'dest': 'state25',
            'conditions': 'back_to_state25'
        },
        {
            'trigger': 'advance',
            'source': [
                'state11',
                'state12',
                'state221',
                'state222',
                'state223',   
                'state241',
                'state242', 
                'state251',
                'state252'    
            ],
            'dest': 'user',
            'conditions': 'end'
        }
       
        
    ],
    initial='start',
    auto_transitions=False,
    show_conditions=True,
)

@route("/webhook", method="GET")
def setup_webhook():
    mode = request.GET.get("hub.mode")
    token = request.GET.get("hub.verify_token")
    challenge = request.GET.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        print("WEBHOOK_VERIFIED")
        return challenge

    else:
        abort(403)


@route("/webhook", method="POST")
def webhook_handler():
    body = request.json
    print('\nFSM STATE: ' + machine.state)
    print('REQUEST BODY: ')
    print(body)

    if body['object'] == "page":
        event = body['entry'][0]['messaging'][0]
        machine.advance(event)
        return 'OK'


@route('/show-fsm', methods=['GET'])
def show_fsm():
    machine.get_graph().draw('fsm.png', prog='dot', format='png')
    return static_file('fsm.png', root='./', mimetype='image/png')


if __name__ == "__main__":
    run(host="localhost", port=8085, debug=True)
