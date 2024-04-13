from coder import decode
def encode(password):
    encoded_password = ''
    for num in password:
        encoded_password +=str(int(num)+3)
    return encoded_password
if __name__ == '__main__':
    while True:
        print('Menu')
        print('-----------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit')
        choice = input('Please enter an option: ')
        if choice == '1':
            password = input('Please enter your password to encode: ')
            encoded_password = encode(password)
            print('Your password has been encoded and stored!')
        elif choice == '2':
            decoded_password = decode(password)
            print(f"The encoded password is {password}, and the original password is {decoded_password}.")
        else:
            break
