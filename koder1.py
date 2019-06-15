from hashlib import blake2b

# from: https://docs.python.org/3/library/hashlib.html#hashlib.hash.digest_size
# BLAKE2 is a cryptographic hash function defined in RFC 7693 that comes in two flavors:#
# BLAKE2b, optimized for 64-bit platforms and produces digests of any size between 1 and 64 bytes
# BLAKE2 supports keyed mode (a faster and simpler replacement for HMAC),
# salted hashing, personalization, and tree hashing.

def koder(haslo,ilosc_znakow):
    try:
        blake = blake2b(digest_size=ilosc_znakow)
        #blake = blake2b()
        blake.update(haslo.encode())
        kod = blake.hexdigest()
        print(kod)
    except: print('Błąd. Wprowadź liczbę znaków')
    
koder2 = blake2b(digest_size=20)
podane = 'admin'
koder2.update(podane.encode())
kod = koder2.hexdigest()
print('Hashowanie hasła algorytmem Blake2.')
print('Przykładowe hasło: "{}", ilość znaków 20:'.format(podane))
print(kod)
print()

def run():
    zapyt = input('Podaj haslo: ')
    zapyt_ilosc_cyfr = input('Ilość znaków ?(max 64)')
    try:
        print('--' * int(zapyt_ilosc_cyfr))
        koder(zapyt, int(zapyt_ilosc_cyfr))
        print('--' * int(zapyt_ilosc_cyfr))
    except: print('Błąd. Wprowadź liczbę znaków'), run()

run()