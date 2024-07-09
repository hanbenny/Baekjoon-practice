def decode_caesar_cipher(cipher_text):
    decoded_text = ''
    for char in cipher_text:
        # 'A'의 아스키 코드 값은 65
        original_char = chr(((ord(char) - ord('A') - 3) % 26) + ord('A'))
        decoded_text += original_char
    return decoded_text

def main():
    cipher_text = input().strip()
    print(decode_caesar_cipher(cipher_text))

if __name__ == "__main__":
    main()