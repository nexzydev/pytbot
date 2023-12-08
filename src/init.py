import requests
import time

class Bot:
    def __init__(self, token):
        self.base_url = f"https://api.telegram.org/bot{token}/"
        self.last_update_id = 0
        self.last_user_id = 0
        self.is_running = True

    def get_updates(self):
        endpoint = f"{self.base_url}getUpdates"
        params = {"offset": self.last_update_id + 1 if self.last_update_id else None}
        response = requests.get(endpoint, params=params)
        return response.json()

    def send_text(self, chat_id, text, parse_mode=None):
        endpoint = f"{self.base_url}sendMessage"
        data = {"chat_id": chat_id, "text": text}
        if parse_mode:
            data["parse_mode"] = parse_mode
        response = requests.post(endpoint, data=data)
        return response.json()

    def command(self, command_name):
        while self.is_running:
            updates = self.get_updates()
            if updates["ok"]:
                for update in updates["result"]:
                    if "message" in update and "text" in update["message"]:
                        chat_id = update["message"]["chat"]["id"]
                        message_id = update["message"]["message_id"]
                        message_text = update["message"]["text"]
                        if message_id == self.last_update_id:
                            return False
                        if message_text.lower() == command_name.lower():
                            if update["update_id"] > self.last_update_id:
                                self.last_update_id = update["update_id"]
                            
                            return {'chat_id': chat_id, 'command': message_text, 'message_id': message_id} 

            time.sleep(1)

        return False  

    def get_last_msg(self):
        endpoint = f"{self.base_url}getChatMember"
        params = {"chat_id": self.last_chat_id, "user_id": self.last_user_id}
        response = requests.get(endpoint, params=params)
        return response.json()

    def exit(self):
        self.is_running = False
