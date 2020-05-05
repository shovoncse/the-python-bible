sentence = input("Enter your sentence: ").strip()

words = sentence.split(" ")

new_words = []

for word in words:
    if word[0] in 'aeiou':
        new_word = word + 'aye'
        new_words.append(new_word)
    else:
        vowel_pos = 0
        for letter in word:
            if letter not in 'aeiou':
                vowel_pos = vowel_pos + 1
            else:
                break

        con_side = word[:vowel_pos] 
        rest_side = word[vowel_pos:]
        new_word = rest_side + con_side + 'ay'
        new_words.append(new_word)

# Join words back to a sentence
output = " ".join(new_words)

print(output)

