

class ConfigFile():

    COOKIE = None

    TOKEN = None

    @staticmethod
    def set_token():
        token = {
            "authorization":ConfigFile.TOKEN
        }
        return token