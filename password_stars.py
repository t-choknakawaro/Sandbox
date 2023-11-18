MIN_LENGTH = 3
password = input(f'Enter password at least {MIN_LENGTH} characters: ')
while len(password) < MIN_LENGTH:
    password = input(f'Enter password at least {MIN_LENGTH} characters: ')
print('*' * len(password))
