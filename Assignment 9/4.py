def caesar_cipher(filename, shift, direction):
    if direction.lower() == "left":
        shift = -shift
    with open(filename, "r", encoding="utf-8") as f:
        text = f.read()

    result = ""

    for ch in text:
        if ch.isalpha():
            x = ord(ch)
            if ch.isupper():
                y = (x - 65 + shift) % 26 + 65
                result += chr(y)
            else:
                y = (x - 97 + shift) % 26 + 97
                result += chr(y)
        else:
            result += ch
    out_file = "ciphertext.txt"
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(result)

    print(f"Ciphertext saved to {out_file}")
