import random


def private_key(p):
    """Picks a private key, a, greater than 1 and less than p"""
    return random.randrange(2, p)


def public_key(p, g, private):
    return g**private % p


def secret(p, public, private):
    return public**private % p
