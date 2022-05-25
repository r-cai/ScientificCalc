
def sqrt1(n,guess):
  if (abs((guess**2)-n)/n)>0.0000001:
    guess=((n/guess)+guess)/2;
    return sqrt1(n,guess)
  else:
    return guess
  
def sqrt(n):
  if n==0:
    return 0
  return sqrt1(n,1.0)

#TESTS

sqrt(4)
sqrt(16)
sqrt(144)
