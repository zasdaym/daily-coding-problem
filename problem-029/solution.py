def run_length_encode(text: str) -> str:
    count = 0
    prev_char = ""
    result = ""

    for char in text:
        if not count:
            prev_char = char
            count = 1
            continue

        if char == prev_char:
            count += 1
            continue

        result += str(count)
        result += prev_char
        prev_char = char
        count = 1

    result += str(count)
    result += prev_char
    return result


def run_length_decode(text: str) -> str:
    result = ""
    for i in range(0, len(text), 2):
        count = int(text[i])
        char = text[i+1]
        result += char * count
    return result


original_text = "AAAABBBCCDAA"
encoded = run_length_encode(original_text)
decoded = run_length_decode(encoded)
assert original_text == decoded
