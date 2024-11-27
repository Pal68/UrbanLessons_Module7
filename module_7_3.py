import string

class WordsFinder:

    def __init__(self, *args):
        self.file_names = []
        for a in args:
            self.file_names.append(a)

    def get_all_words(self):
        all_words ={}
        for f in self.file_names:
            words = []
            with open(f, encoding='utf-8') as file:
                for line in file:
                    line = line.lower()
                    line = line.translate(str.maketrans('', '', string.punctuation))
                    words.extend(line.split())
            all_words[f] = words
        return all_words

    def find(self, word):
        return_value ={}
        all_words = self.get_all_words()
        for k, v in all_words.items():
            if word.lower() in v:
                return_value[k] = v.index(word.lower()) + 1
        return return_value

    def count(self, word):
        return_value ={}
        all_words = self.get_all_words()
        for k, v in all_words.items():
            count_words = len(list(filter(lambda w: w == word.lower(), v)))
            return_value[k] = count_words
        return return_value

finder2 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder2.get_all_words())
print(finder2.find('the'))
print(finder2.count('the'))

# finder2 = WordsFinder('test_file.txt')
# print(finder2.get_all_words()) # Все слова
# print(finder2.find('TEXT')) # 3 слово по счёту
# print(finder2.count('teXT')) # 4 слова teXT в тексте всего
