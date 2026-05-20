def vow_count(word):
 count = 0
 vowels = "aeiouAEIOU"

 for letter in word:
    if letter in vowels:
        count = count + 1

    return count
  

usser_word = input(" what  is your word ? ")
result = vow_count(usser_word)
print("number of vowels " , result)
