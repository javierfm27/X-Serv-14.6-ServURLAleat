#!/usr/bin/python3
from webapp import webApp
import socket
import random


class aleat(webApp):
    def parse(self, request):
        return None

    def process(self, parsedRequest):
        numero = random.randint(0, 1000000000000000)
        html = "<!DOCTYPE html><html><body> Dame <a href=" + str(numero) +
        " > otra </a> </body></html>"
        return ("200 Ok", html)

    def __init__(self, hostname, port):
        webApp.__init__(self, hostname, port)

if __name__ == "__main__":
    servidorAleat = aleat(socket.gethostname(), 1231)
