import json
import logging


class Peloton:
    def __init__(self, username: str, password: str):
        self.log = logging.getLogger("main.peloton")
        self.log.info("setting username & password")
        try:
            self.username = username
            self.password = password
        except KeyError:
            exit(1)

