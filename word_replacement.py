def replace_word():
    my_word = input('Enter your word: ')
    if not my_word:
        print('Text is empty')
        return
    word_to_replace = input('Enter Word To Replace: ')       
    replaced_word = input('Enter the word replacement: ')
    print(my_word.replace(word_to_replace, replaced_word))


# def replace_word():
#     text = input("Enter the text: ")
#     word_to_replace = input("Enter the word to replace: ")
#     new_word = input("Enter the new word: ")
#     replaced_text = text.replace(word_to_replace, new_word)
#     print("Replaced text: ", replaced_text)

replace_word()

