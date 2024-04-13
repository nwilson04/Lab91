def encode(password):
    encoded_password = ''
    for num in password:
        encoded_password +=str(int(num)+3)
    return encoded_password
