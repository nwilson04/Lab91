def encode(password):
  encoded_pass = ''
  for num in password:
    encoded_pass += str((int(num)+3))
  return encoded_pass
def decode(password):
  decoded_pass = ''
  for num in password:
    decoded_pass += str((int(num)-3))
  return decoded_pass