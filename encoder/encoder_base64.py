import base64

text = input("masukan inputan: ")
encoded = base64.b64encode(text.encode('utf-8'))
le = encoded.decode('utf-8')
print("output: ", le)