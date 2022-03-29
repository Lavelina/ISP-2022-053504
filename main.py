import re
import statistics


def read_text():
    file = open("text_1.txt", "r")
    text = file.read()
    print("Text from file: \n\n", text)
    file.close()
    return text


def count_words(sentence):
    words = re.split("; |, |: | ", sentence)
    while "" in set(words):
        words.remove("")
    return words


def main_func(text):
    text = (
        text.lower()
        .replace("\n", " ")
        .replace("!", ".")
        .replace("?", ".")
        .replace("...", ".")
    )
    sentences = text.split(".")
    count_sent = text.count(".")
    while "" in set(sentences):
        sentences.remove("")
    word_list = []
    for sent in sentences:
        words = count_words(sent)
        for w in words:
            word_list.append(w)
    counter = {}
    for word in word_list:
        count = counter.get(word, 0)
        counter[word] = count + 1
    counter_list = counter.keys()
    for words in counter_list:
        print(words, "-", counter[words])
    print(count_sent)
    print("Average count words: ", round(len(word_list) / count_sent))
    print(
        "Median count words: ",
        round(
            statistics.median([len(sentence.split()) for sentence in text.split(".")])
        ),
    )
    choice_ngram = input(
        "\nThe default value of the number and length of the words used most frequently are K = 10 and N = 4."
        "\nDo you want to change them? (y/n)"
    )
    if choice_ngram == "y":
        n = int(input("Enter n: "))
        k = int(input("Enter k: "))
    else:
        n = 4
        k = 10

    words_dict = {}
    ngram_dict = {}
    for word in word_list:
        count = words_dict.get(word, 0)
        words_dict[word] = count + 1
    for word in words_dict.keys():
        if len(word) >= n:
            tmp_word = word
            n_count = 0
            n_ends = n
            for i in range(len(word) - n_ends + 1):
                ngram = tmp_word[n_count:n_ends]
                if ngram in ngram_dict.keys():  # if ngram already exist in ngram_dict
                    ngram_dict[ngram] += words_dict[word]
                else:
                    ngram_dict[ngram] = words_dict[word]
                n_count += 1
                n_ends += 1
    ngram_dict = {
        k: ngram_dict[k] for k in sorted(ngram_dict, key=ngram_dict.get, reverse=True)
    }
    tmp_k = 0
    print("\nTop", k, "n-gram")
    for words in ngram_dict:
        if tmp_k < k:
            print("  ", words, "-", ngram_dict[words])
            tmp_k += 1


def main():
    text = read_text()
    main_func(text)


if __name__ == "__main__":
    main()
