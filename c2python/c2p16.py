#16)Create a single string separated with space from two strings by swapping the character at position 1.
def chars_mix_up(a, b):  
  new_a = b[:1] + a[1:]  
  new_b = a[:1] + b[1:]  
  
  return new_a + ' ' + new_b 
first=input("Enter word1:")
second=input("Enter word2:")   
print(chars_mix_up(first,second ))