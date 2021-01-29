#(c) Form a list of vowels selected from a given word
word=input("Enter the word:")
vowel=[]
i=0
while(i<len(word)):
    if (word[i]=='a' or word[i]=='A' or word[i]=='e' or word[i]=='E'
   or word[i]=='i' or word[i]=='I' or word[i]=='o' or word[i]=='O'
   or word[i]=='u' or word[i]=='U'):
       temp=word[i]
       vowel.append(temp)
    i=i+1
print(vowel)