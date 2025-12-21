def valid_word_abbreviation(word, abbr):
    word_pointer = 0
    for abbr_pointer in range(len(abbr)):
        abbr_character = abbr[abbr_pointer]
        word_character = word[word_pointer]
        if abbr_character == word_character:
            word_pointer += 1
        elif abbr_character.isdigit():
            if int(abbr_character) == 0:
                return False
            elif not abbr[abbr_pointer - 1].isdigit():
                return False
            else:
                word_pointer += int(abbr_character)
    return True

if __name__ == '__main__':
    print(valid_word_abbreviation("internationalization", "i18n"))