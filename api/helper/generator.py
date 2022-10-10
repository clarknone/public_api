import secrets
import random


class Generator:

    @staticmethod
    def generate_hash():
        return secrets.token_hex(16)

    @staticmethod
    def generate_pk():
        return secrets.randbits(31)
