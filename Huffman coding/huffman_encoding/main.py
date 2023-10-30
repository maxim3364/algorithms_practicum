def huffman_encode(text):
    frequency = {}
    for char in text:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    nodes = [[weight, [char, ""]] for char, weight in frequency.items()]

    while len(nodes) > 1:
        nodes = sorted(nodes)

        lo = nodes[0]
        hi = nodes[1]

        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]

        nodes.append([lo[0] + hi[0]] + lo[1:] + hi[1:])

        nodes = nodes[2:]

    return nodes[0][1:]

def encode_huffman(text, huffman_tree):
    codes = dict(huffman_tree)

    encoded_text = ""
    for char in text:
        encoded_text += codes[char]

    return encoded_text

text = "Errare humanum est."
huffman_tree = huffman_encode(text)
encoded_text = encode_huffman(text, huffman_tree)

print(f"Количество уникальных букв: {len(huffman_tree)}")
print(f"Размер закодированной строки: {len(encoded_text)} бит")

print("Коды символов:")
for char, code in huffman_tree:
    print(f"'{char}': {code}")

print(f"Закодированная строка: {encoded_text}")