# ---- Loops, Conditionals, and Strings! ----

word = 'bag'

# 1. Set up a loop to iterate through the string of lowercase vowels, 'aeiou'.

vowels = "aeiou"
for char in vowels:
	print(char)
print("-------------")

# 2 & 3. Inside the loop, create and print a new string from 'word', but with a different vowel. Use the replace() method.

for vowel in vowels:
	print(word.replace("a", vowel))

#the book had this solution 
#for vowel in vowels:
   #new_word = word.replace("a", vowel)
   #print(new_word)


# 4. After you have your code working, try other words besides 'bag'.