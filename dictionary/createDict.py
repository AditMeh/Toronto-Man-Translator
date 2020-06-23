import pickle


def load_dictionary(path):
    file = open(path, "r")
    dictionary = {}
    while True:
        line = file.readline().strip("\n")
        if not line:
            break
        colonIndex = line.index(':')
        dictionary[line[:colonIndex]] = line[colonIndex + 1:]
    return dictionary


dictionary = load_dictionary("dictionary.txt")

pickle_out = open("dict.pickle", "wb")
pickle.dump(dictionary, pickle_out)
