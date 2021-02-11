
#4) Generate a list of four digit numbers in a given range with all their digits even and the number is a perfect square.

for i in range(1000,10000):
  for j in range(32,100):
    if i==j*j:
      a=str(i)
      if (int(a[0])%2==0 and int(a[1])%2==0 and int(a[2])%2==0 and int(a[3])%2==0):
        print(i)