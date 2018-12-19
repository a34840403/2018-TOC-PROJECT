import requests

GRAPH_URL = "https://graph.facebook.com/v2.6"
ACCESS_TOKEN = "EAAP67ZCeXFt0BAL2O3CIZBspfFyxfTZAPqhlKWRdtdKIpkNARiluZBTMC18U23bvIowvHmZCZAt67yZAEMatDRq8SXlF6gnv65V9klutOtWqye3ir6P8qSIuIL0rgPZAZAjZCRnjhWDc5wB8FxZA1tlxqUVZCIdjCjg4I3ZBa3kj1E4dZCcwZDZD"
def send_text_message(id, text):
    url = "{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)
    payload = {
        "recipient": {"id": id},
        "message": {"text": text}
    }
    response = requests.post(url, json=payload)

    if response.status_code != 200:
        print("Unable to send message: " + response.text)
    return response


"""
def send_image_url(id, img_url):
    pass

def send_button_message(id, text, buttons):
    pass
"""
