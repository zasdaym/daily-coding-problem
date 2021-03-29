from typing import List


def justify_words(words: List[str], line_length: int) -> List[str]:
    """
    The main idea is to build line by line.
    Iterate and add every word into a temporary list while checking if it fits into the current line.
    If the current word will overflow the temporary, distribute spaces evenly to words on the temporary list.
    """
    result: List[List[str]] = []
    curr_line_words: List[str] = []
    curr_line_letter_count = 0

    for word in words:
        if curr_line_letter_count + len(word) + len(curr_line_words) > line_length:
            # Distribute space evenly between words (round robin)!
            for i in range(line_length - curr_line_letter_count):
                curr_line_words[i % (len(curr_line_words)-1 or 1)] += ' '

            # Add new line to the final result
            result.append(''.join(curr_line_words))

            # Reset line word and letter counter 
            curr_line_words, curr_line_letter_count = [], 0

        # 
        curr_line_words.append(word)
        curr_line_letter_count += len(word)

    return result + [' '.join(curr_line_words).ljust(line_length)]


justified_text = justify_words(
    ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"], 16)
assert justified_text == ['the  quick brown', 'fox  jumps  over', 'the lazy dog    ']
