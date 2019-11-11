import random

def generate_random():
    spec_char = ["!", "#", "$", "%", "&", "(", ")", "*", "+", "/", "<", ">", "=", "?", "@"]
    generated = ''
    for i in range(8):
        if i == 0 or i == 5:
            generated += chr(random.randrange(97, 122)) # a-z
        elif i == 1 or i == 4:
            generated += chr(random.randrange(65, 90)) # A-Z
        elif i == 2 or i == 3:
            generated += str(random.randrange(0, 9)) # 0-9
        elif i == 6 or i == 7:
            generated += random.choice(spec_char) # Special characters
    return generated