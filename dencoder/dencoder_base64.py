import base64
def base64_to_text(base64_string):
    base64_bytes = base64_string.encode('ascii')
    text_bytes = base64.b64decode(base64_bytes)
    text = text_bytes.decode('utf-8')
    return text
text = base64_to_text(input("masukan text: "))
print("ouput: ", text)