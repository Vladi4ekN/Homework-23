import string


class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names
        self.all_words = {}
        self.report = {}

    def get_all_words(self):
        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    content = file.read().lower()
                    content = content.translate(str.maketrans('', '', string.punctuation))
                    words = content.split()

                    self.all_words[file_name] = words

                    # Формируем отчет
                    unique_words_count = len(set(words))  # Количество уникальных слов
                    total_words_count = len(words)  # Общее количество слов
                    self.report[file_name] = (total_words_count, unique_words_count)

            except FileNotFoundError:
                print(f"Файл {file_name} не найден.")
            except Exception as e:
                print(f"Произошла ошибка при обработке файла {file_name}: {e}")

        return self.all_words, self.report

    def find(self, word):
        found_in_files = {}
        for file_name, words in self.all_words.items():
            if word in words:
                found_in_files[file_name] = words.count(word)
        return found_in_files

    def count(self, word):
        total_count = 0
        for words in self.all_words.values():
            total_count += words.count(word)
        return total_count


finder = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                     'Rudyard Kipling - If.txt',
                     'Mother Goose - Monday’s Child.txt')

print(finder.get_all_words())
print(finder.find('the'))
print(finder.count('the'))
