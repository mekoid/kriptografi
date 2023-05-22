
def text_to_hex(text):
    text_bytes = text.encode('utf-8')
    hex_string = text_bytes.hex()
    return hex_string
hex_string = text_to_hex(input("masukan text: "))
print(hex_string)