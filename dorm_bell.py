import requests
import time
import playsound


def groupme_post(body):
    return requests.post("https://push.groupme.com/faye", json=body)


def handshake(call_id):
    return {"channel": "/meta/handshake", "version": "1.0",
            "supportedConnectionTypes": ["websocket"], "id": str(call_id)}


def subscribe(call_id, client_id, sub_id, groupme_token):
    return {"channel": "/meta/subscribe", "clientId": client_id,
            "subscription": sub_id, "id": str(call_id),
            "ext": {"access_token": groupme_token}}


def poll(call_id, client_id):
    return {"channel": "/meta/connect", "clientId": client_id,
            "connectionType": "websocket", "id": call_id}


def main():
    call_id = 1
    handshake_response = groupme_post(handshake(call_id)).json()
    if not handshake_response[0]["successful"]:
        return
    client_id = handshake_response[0]["clientId"]

    call_id += 1
    sub_id = "/user/YOUR USER ID HERE"
    groupme_token = "YOUR GROUPME API TOKEN HERE"
    sub_response = groupme_post(subscribe(call_id, client_id, sub_id, groupme_token)).json()
    if not sub_response[0]["successful"]:
        return

    end_time = time.time() + 3550  # Run for a hour because of signature refresh
    while time.time() < end_time:
        call_id += 1
        poll_response = groupme_post(poll(call_id, client_id)).json()
        if not poll_response[0]["successful"]:
            return
        else:
            if "subject" in poll_response[1]["data"]:
                new_text = poll_response[1]["data"]["subject"]["text"].lower()
                if "door" in new_text:
                    playsound.playsound("YOUR MUSIC FILE")
                elif "YOUR KEYWORD" in new_text:
                    playsound.playsound("YOUR MUSIC FILE")


if __name__ == '__main__':
    main()
