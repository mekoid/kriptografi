def rot(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            code = ord(char)
            if char.isupper():
                base = ord("A")
            else:
                base = ord("a")
            code = ((code - base + shift) % 26) + base
            result += chr(code)
        else:
            result += char
    return result
text = input("masukan text: ")
for i in range(1, 26):
    print(f"ROT{i}: {rot(text, i)}")
