import requests


class Usuario:
    nombre = ""
    id_coment = ""

    def __init__(self):
        self.url = "https://graph.facebook.com/v2.8/me"
        self.token = "EAACEdEose0cBAO2U1xtIEZBZAf2SqMAfZAzEHulf3EZBinlTeM8iZB7mPET2tLyFVufIO6Kg3YxysGHh3SEHsXPahyNei5PoJQaD7JPW6RmJF7cZCLTAOGwAbrhwiZAT8rZCoBuS5ZBPZCgZBzRqxwKhXef5xm4BeU9VUuxUydZC2xd9RgZDZD"

    def obtenInformacion(self):
        parametros = {"access_token": self.token}
        resultado = requests.get(self.url, params=parametros)
        return resultado

    def publicarComentario(self, message):
        self.url = "https://graph.facebook.com/v2.8/feed"
        parametros = {"message": message, "access_token": self.token}
        resultado = requests.post(self.url, params=parametros).json()
        print(resultado)
        return resultado
