# Author: Mack Mason mjm8542@psu.print

def digit_sum(n):
  if(n > 0):
    remainder = (n % 10)
    return remainder + digit_sum(n//10)
  else:
    return 0

def run():
  userInt  = input("Enter an int: ")
  userInt = int(userInt)
  digitSum = digit_sum(userInt)
  print(f"sum of digits of {userInt} is {digitSum}.")

if __name__ == "__main__":
  run()