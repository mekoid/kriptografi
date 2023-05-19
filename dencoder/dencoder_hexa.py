def hex_to_text(hex_string):
    hex_bytes = bytes.fromhex(hex_string)
    text = hex_bytes.decode('utf-8')
    return text
text = hex_to_text(input("Masukan text: "))
print("output:", text)