import math
import matplotlib.pyplot as plt

file_path = open("otpfile1.txt", "r")

encrypted_Text = file_path.read()

to_compare = {
    'e': 11.1607,
    'a': 8.4966,
    'r': 7.5809,
    'i': 7.5448,
    'o': 7.1635,
    't': 6.9509,
    'n': 6.6544,
    's': 5.7351,
    'l': 5.4893,
    'c': 4.5388,
    'u': 3.6308,
    'd': 3.3844,
    'p': 3.3844,
    'm': 3.0129,
    'h': 3.0034,
    'g': 2.4705,
    'b': 2.0720,
    'f': 1.8121,
    'y': 1.7779,
    'w': 1.2899,
    'k': 1.1016,
    'v': 1.0074,
    'x': 0.2902,
    'z': 0.2722,
    'j': 0.1965,
    'q': 0.1962
}


def frequency_dictionary(text, to_compare_dict):
    freq_dict = {}
    n = 0
    for element in text:
        if element.isalpha():
            if element.lower() not in freq_dict:
                freq_dict[element.lower()] = 1
                n += 1
            else:
                freq_dict[element.lower()] += 1
                n += 1
    relative_dict = expected_frequency(to_compare_dict, n)
    return freq_dict, relative_dict


def expected_frequency(dictionary, total):
    for element in dictionary:
        dictionary[element] = math.floor(dictionary[element] * total / 100)
    return dictionary


def draw_graph(dictionary):
    plt.plot(dictionary.keys(), dictionary.values())
    plt.xlabel("letter")
    plt.ylabel("rate")
    plt.title("Frequency dict")
    plt.show()


def decrypt_char(char, key):
    albet = "abcdefghijklmnopqrstuvwxyz"
    i = 0
    while char != albet[i]:
        i += 1
    i = i - key;
    while i < 0:
        i += 25
    while i > 25:
        i -= 25
    return albet[i]


def decrypt_with_key(key, frequency_dict):
    local_shifted_dict = {}
    for element in frequency_dict:
        new_char = decrypt_char(element, key)
        local_shifted_dict[new_char] = frequency_dict[element]
    return local_shifted_dict


def calc_diff(frequency_dict, relative_freq):
    diff = 0
    for element in frequency_dict:
        diff += abs(relative_freq[element] - frequency_dict[element])

    return diff


def decrypt(relative_freq, frequency_dict):
    key_diff_dict = {}
    try_key = 0
    while try_key <= 25:
        shifted_dict = decrypt_with_key(try_key, frequency_dict)
        key_diff_dict[try_key] = calc_diff(shifted_dict, relative_freq)
        try_key += 1
    return key_diff_dict


call = frequency_dictionary(encrypted_Text, to_compare)
(first, second) = call
relative_freq = first
frequency_dict = second
print("real: ")
print(frequency_dict)
print("expected: ")
print(relative_freq)
draw_graph(relative_freq)

answer_list = decrypt(relative_freq, frequency_dict)

print("ll key was:")
print(min(answer_list))
