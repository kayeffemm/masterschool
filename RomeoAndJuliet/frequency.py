from romeo_and_juliet import PLAY
import re

# Uses regex to extract only words from given string and return them as a list.
def get_words(text):
    text = text.lower()
    return re.findall("[a-z]+", text)


# Checks how often a word from given list exists and maps the words to a frequency.
def words_frequency(words):
    words_by_frequency = {}
    for word in words:
        if word not in words_by_frequency.keys():
            words_by_frequency[word] = 0
        words_by_frequency[word] += 1
    return words_by_frequency


# Prints the top n used words from the given dictionary.
def top_n_words(freq, n):
    current_highest_freq = ["word", 0]
    n = n
    while n > 0:
        for word, frequency in freq.items():
            if frequency > current_highest_freq[1]:
                current_highest_freq[0] = word
                current_highest_freq[1] = frequency
        print(f"{current_highest_freq[0]}: {current_highest_freq[1]}")
        del freq[current_highest_freq[0]]
        current_highest_freq = ['word', 0]
        n -= 1


def main():
    text_as_list = get_words(PLAY)
    frequency_dictionary = words_frequency(text_as_list)
    top_n_words(frequency_dictionary, 50)


if __name__ == "__main__":
    main()
