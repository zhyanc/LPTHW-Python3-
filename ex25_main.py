import ex25

sentence = "All good things come to those who wait."

words = ex25.break_words(sentence)
print (words, "\n-----------------\n")

sorted_words = ex25.sort_words(words)
print(sorted_words, "\n-----------------\n")

ex25.print_first_word(words)
ex25.print_last_word(words)
print ("\n-----------------\n")

print(words, "\n-----------------\n")

ex25.print_first_word(sorted_words)
ex25.print_last_word(sorted_words)
print ("\n-----------------\n")

print(sorted_words, "\n-----------------\n")

sorted_words = ex25.sort_sentence(sentence)
print(sorted_words, "\n-----------------\n")

ex25.print_first_and_last(sentence)
print ("\n-----------------\n")

ex25.print_first_and_last_sorted(sentence)
