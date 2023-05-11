from textblob import TextBlob

def conv_string(string):
    li = list(string.split())
    return li

str1 = input("Enter your word : ")
words = conv_string(str1)
correct_word = []

for i in words :
    correct_word.append(TextBlob(i))

print("Wrong word : ", words)
print("Correct word is  :")
for i in correct_word:
    print(i.correct(), end=" ")

