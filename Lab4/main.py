if __name__ == '__main__':
    print('Task 1')
    sentence = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit,' \
               ' sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'.lower()

    longest_word = ''
    for word in sentence.split():
        if len(word) > len(longest_word):
            longest_word = word

    print(f'Longest word: {longest_word}, its length: {len(longest_word)}')

    print('Task 2')
    vowel_letters = ('a', 'e', 'i', 'o', 'u', 'y')
    sentence = sentence.replace(' ', '').replace(',', '')

    vowel_count = 0
    for letter in sentence:
        if letter in vowel_letters:
            vowel_count += 1

    if vowel_count > len(sentence) - vowel_count:
        print(f'Vowel letters more ({vowel_count} of {len(sentence)})')
    elif vowel_count < len(sentence) - vowel_count:
        print(f'Consonant letters more ({len(sentence) - vowel_count} of {len(sentence)})')
    else:
        print(f'Count of vowel and consonant letters count is the same ({vowel_count})')

    print('Task 3')
    for letter in sorted(vowel_letters):
        if letter in sentence:
            print(letter)
