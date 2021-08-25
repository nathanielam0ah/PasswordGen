
import random, string

theLetters = string.ascii_letters
capitalLts = theLetters.upper()
spcCharacters = string.punctuation
dgts = string.digits
def GetLength(): # Gets the desired password length
    length = input("Type Desired Length: ")
    if length.isdigit(): return int(length) 
    else: return 0
def Generator(length=8): # Funtion to generate password based on random
    printable = f'{theLetters}{capitalLts}{dgts}{spcCharacters}'
    printable = list(printable)
    random.shuffle(printable)
    random_password = random.choices(printable, k=length)
    random_password = ''.join(random_password)
    return random_password

while 1:
    passwd_length = GetLength()
    if passwd_length == 0:
        passwd = Generator()
        print(f'password (default=8):\t\t{passwd}')
    else:
        passwd = Generator(passwd_length)
        print(f'password ({str(len(passwd))}):\t\t{passwd}')

