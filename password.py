import random
class Password:
    def __init__(self, length):
        self.length = length
        self.characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123-_123456789!@#$%^&*()'
    def generate(self):
        password = ''.join(random.choice(self.characters) for _ in range(self.length))
        return password
print('Welcome to the Password Generator!')
length = int(input('Enter the desired password length: '))
pwd = Password(length)
password = pwd.generate()
print('Generated password:', password)