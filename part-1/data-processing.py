sentence = input("Please enter a sentence: ")
print(sentence.upper())

paragraph = input("\nPlease enter a paragraph: ")
print(f"The paragraph has {len(paragraph.split())} words.")

digit_string = input("\nPlease enter a string: ")
result = print(digit_string.isdigit())

replace_string = input("\nPlease enter another string: ")
print(replace_string.replace('a', 'o').replace('A', 'O'))

full_name = input("\nPlease enter your full name: ")
initials = [_[0] for _ in full_name.split()]
print(f"Your initials are: {''.join(initials)}")

string = input("\nPlease enter a string: ")
print(f"The length of your string is: {len(string)}")
