import random

numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['*','+','-','/','_','#','@','!','?','$','%','&',')','(','=']

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G',
'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U','V', 'W', 'X', 'Y', 'Z']


def generate_password():
    letters_count = random.randint(8, 10)
    symbols_count = random.randint(2, 4)
    numbers_count = random.randint(2, 4)

    pass_letters = [random.choice(letters) for _ in range(letters_count)]
    pass_symbols = [random.choice(symbols) for _ in range(symbols_count)]
    pass_numbers = [random.choice(numbers) for _ in range(numbers_count)]

    password = pass_letters + pass_symbols + pass_numbers
    random.shuffle(password)
    password = ''.join(password)

    return password



