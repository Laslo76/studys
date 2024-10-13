# Bogushev V.V.

class WordsFinder:
    file_names = []

    def __init__(self, *args):
        self.file_names = args

    def get_all_words(self) -> dict:
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, "r", encoding='utf-8') as file:
                str_file = file.read()
                prepared_line = str_file.lower().replace('\n', ' ')
                for old_str in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    prepared_line = prepared_line.replace(old_str, '')
                all_words[file_name] = prepared_line.split()
        return all_words

    def find(self, word: str) -> dict:
        result_dict = {}
        prepared_word = word.lower()
        all_words = self.get_all_words()
        for namefile, words in all_words.items():
            seek_num = 1
            for current_word in words:
                if current_word == prepared_word:
                    result_dict[namefile] = seek_num
                    break
                seek_num += 1
        return result_dict

    def count(self, word: str) -> dict:
        result_dict = {}
        prepared_word = word.lower()
        all_words = self.get_all_words()
        for namefile, words in all_words.items():
            seek_count = 0
            for current_word in words:
                if current_word == prepared_word:
                    seek_count += 1
            result_dict[namefile] = seek_count
        return result_dict


if __name__ == '__main__':
    finder2 = WordsFinder('test_file.txt')
    print(finder2.get_all_words())  # Все слова
    print(finder2.find('TEXT'))  # 3 слово по счёту
    print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
