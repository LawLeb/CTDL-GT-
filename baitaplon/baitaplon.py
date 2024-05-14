class Dictionary:
    def __init__(self):
        self.entries = []

    def add_entry(self, word, meanings):
        self.entries.append((word, meanings))

    def remove_entry(self, word):
        for entry in self.entries:
            if entry[0] == word:
                self.entries.remove(entry)
                return True
        return False

    def lookup_word(self, word):
        for entry in self.entries:
            if entry[0] == word:
                return entry[1]
        return None

    def save_to_file(self, filename):
        with open(filename, 'w', encoding='utf-8') as file:
            for word, meanings in self.entries:
                file.write(word + ":\n")
                for meaning in meanings:
                    word_type, meaning_desc, example = meaning
                    file.write("- Loại từ: {}\n".format(word_type))
                    file.write("  Nghĩa: {}\n".format(meaning_desc))
                    file.write("  Ví dụ: {}\n".format(example))
                file.write("\n")

    def load_from_file(self, filename):
        with open(filename, 'r', encoding='utf-8') as file:
            word = None
            meanings = []
            for line in file:
                line = line.strip()
                if line:
                    if line.endswith(':'):
                        if word:
                            self.add_entry(word, meanings)
                            word = line[:-1]
                            meanings = []
                        else:
                            word = line[:-1]
                    elif line.startswith("- Loại từ:"):
                        word_type = line.split(": ")[1]
                    elif line.startswith("  Nghĩa:"):
                        meaning_desc = line.split(": ")[1]
                    elif line.startswith("  Ví dụ:"):
                        example = line.split(": ")[1]
                        meanings.append((word_type, meaning_desc, example))
            if word:
                self.add_entry(word, meanings)

def main():
    dictionary = Dictionary()

    while True:
        print("\n1. Thêm một mục từ mới vào từ điển")
        print("2. Loại bỏ một mục từ của từ điển")
        print("3. Tra cứu các nghĩa của một mục từ trong từ điển")
        print("4. Lưu từ điển vào tập tin")
        print("5. Nạp từ điển từ tập tin")
        print("6. Kết thúc chương trình")

        choice = input("Nhập lựa chọn của bạn: ")

        if choice == '1':
            word = input("Nhập từ mới: ")
            meanings = []
            while True:
                word_type = input("Loại từ (danh từ, động từ, tính từ, ...): ")
                meaning_desc = input("Nghĩa của từ: ")
                example = input("Ví dụ: ")
                meanings.append((word_type, meaning_desc, example))
                add_another = input("Thêm nghĩa khác cho từ này? (yes/no): ")
                if add_another.lower() != 'yes':
                    break
            dictionary.add_entry(word, meanings)
            print("Từ mới đã được thêm vào từ điển.")

        elif choice == '2':
            word = input("Nhập từ muốn loại bỏ: ")
            if dictionary.remove_entry(word):
                print("Từ đã được loại bỏ khỏi từ điển.")
            else:
                print("Từ không tồn tại trong từ điển.")

        elif choice == '3':
            word = input("Nhập từ muốn tra cứu: ")
            meanings = dictionary.lookup_word(word)
            if meanings:
                print("Nghĩa của từ '{}' là:".format(word))
                for i, (word_type, meaning_desc, example) in enumerate(meanings, start=1):
                    print("{}. Loại từ: {}".format(i, word_type))
                    print("   Nghĩa: {}".format(meaning_desc))
                    print("   Ví dụ: {}".format(example))
            else:
                print("Từ '{}' không tồn tại trong từ điển.".format(word))

        elif choice == '4':
            filename = "N21DCDT025.dict.txt"
            dictionary.save_to_file(filename)
            print("Từ điển đã được lưu vào tập tin '{}'.".format(filename))

        elif choice == '5':
            filename = "N21DCDT025.inp.txt"
            dictionary.load_from_file(filename)
            print("Từ điển đã được nạp từ tập tin '{}'.".format(filename))

        elif choice == '6':
            print("Kết thúc chương trình.")
            break

        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

if __name__ == "__main__":
    main()                