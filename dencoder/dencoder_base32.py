import base64
def base32_to_text(encoded_str):
    decoded_bytes = base64.b32decode(encoded_str)
    decoded_text = decoded_bytes.decode('utf-8')
    return decoded_text
decoded_text = base32_to_text(input("masukan text: "))
print("output: ", decoded_text)