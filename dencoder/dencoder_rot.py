def rot_to_text(encoded_str, rot_num):
    decoded_text = ""
    for char in encoded_str:
        if char.isalpha():
            char_code = ord(char)
            if char.islower():
                base_code = ord('a')
            else:
                base_code = ord('A')
            decoded_code = ((char_code - base_code - rot_num) % 26) + base_code
            decoded_char = chr(decoded_code)
            decoded_text += decoded_char
        else:
            decoded_text += char
    return decoded_text
encoded_str = input("masukan text: ")
for rot_num in range(1, 26):
    decoded_text = rot_to_text(encoded_str, rot_num)
    print(f"ROT{rot_num}: {decoded_text}")
