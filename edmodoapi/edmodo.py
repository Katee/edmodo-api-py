import requests
import json

class EdmodoApi:
    VERSION = "v1.1" # version of the edmodo API we are using

    def __init__(self, api_key, is_sandbox=False):
        """
        Init an EdmodoApi object.
        """
        self.api_key = api_key # the api key is needed to make any request

        if is_sandbox:
            self.base_url = "https://appsapi.edmodobox.com/%s/" % self.VERSION
        else:
            self.base_url = "https://appsapi.edmodo.com/%s/" % self.VERSION
        pass

    def launch_request(self, launch_key):
        """
        Get information about the user launching the app.
        """
        payload = {
            "api_key": self.api_key,
            "launch_key": launch_key
        }
        r = requests.get(self.base_url + "launchRequests", params=payload)
        return r.json()

    def user_post(self, access_token, user_token, content, recipients):
        """
        Post on the user's behalf. This should be used sparingly.
        """
        payload = {
            "api_key": self.api_key,
            "access_token": access_token,
            "user_token": user_token,
            "content": content,
            "recipients": json.dumps(recipients)
        }
        r = requests.post(self.base_url + "userPost", params=payload)
        return r.json()

    def set_notification(self, access_token, user_token, notification_count):
        """
        Set the notification count of your app.
        """
        payload = {
            "api_key": self.api_key,
            "access_token": access_token,
            "user_token": user_token,
            "notification_count": notification_count
        }
        r = requests.post(self.base_url + "setNotification", params=payload)
        return r.json()
