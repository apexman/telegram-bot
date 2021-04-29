class Configs:
    token = ""

    def __init__(self):
        with open("token.txt", "r") as token:
            self.token = token

    def get_token(self):
        return self.properties[self.TOKEN_NAME]
