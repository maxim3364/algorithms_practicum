def huffman_decode(encoded_text, huffman_tree):
    decoded_text = []
    current_code = ""

    for bit in encoded_text:
        current_code += bit
        for symbol_code in huffman_tree:
            if current_code == symbol_code[1]:
                decoded_text.append(symbol_code[0])
                current_code = ""
                break

    return ''.join(decoded_text)


encoded_text = "100011110001001101000111111011001010011000010110011010111110"
huffman_tree = [
    (' ', '1011'),
    ('.', '1110'),
    ('D', '1000'),
    ('c', '000'),
    ('d', '001'),
    ('e', '1001'),
    ('i', '010'),
    ('m', '1100'),
    ('n', '1010'),
    ('o', '1111'),
    ('s', '011'),
    ('u', '1101')
]

decoded_text = huffman_decode(encoded_text, huffman_tree)

print(f"Результат: {decoded_text}")