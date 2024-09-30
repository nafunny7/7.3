class WordsFinder():
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, "r", encoding="utf-8") as file:
                words = []
                for line in file:
                    line = line.lower()
                    punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']
                    for pun in punctuation:
                        line = line.replace(pun, "")
                    line = line.replace(" - ", "-")
                    words.extend(line.split())
                    all_words[file_name] = words
        return all_words

    def find(self, word):
        lamba = {}
        for key, volue in self.get_all_words().items():
            if word.lower() in volue:
                lamba[key] = volue.index(word.lower()) + 1

        return lamba

    def count(self, word):
        perdole = {}
        for value, key in self.get_all_words().items():
            word_count = key.count(word.lower)
            perdole[value] = word_count

        return perdole


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего