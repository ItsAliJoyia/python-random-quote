import random

def my_fun():
  # print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  
  last = len(quotes) - 1
  rnd = random.randint(0, last)

  print(quotes[rnd-1])


if __name__== "__main__":
  my_fun()
