#Q1 :-  Extracting a Substring:
# Given the string "Hello, World!", extract the substring "World" using slicing.
greeting = "Hello, World!"
world_substring = greeting[7:12]
print(world_substring)

#Q2 :-Reversing a String:
# Write a slice operation to reverse the string "Python".
language = "Python"
reversed_language = language[::-1]
print(reversed_language)

#Q3 :- Skipping Characters:
# From the string "abcdefgh", extract every second character starting from the first.
a = "abcdefgh"
print(a[::2])

#Q4 :- First and Last Characters:
# Slice and print the first and last characters from the string "SDET".
a = "SDET"
print(a[0] + a[-1])

#Q5 :-  Remove First n Characters:
# Given the string "OpenAI", write a slice operation to remove the first 2 characters.\
a = "OpenAI"
result = a[2:]
print(result)
