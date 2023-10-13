# 1.2 Write a program that determines whether a year entered by the user is a leap year or not using ifelif-else statement


def LeapYearCheck(input_year):
  if (input_year % 4) == 0:
    if (input_year % 100) == 0:
      if (input_year % 400) == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False


# Driver Code
input_year = int(input("Enter the Year to be checked: "))
if (LeapYearCheck(input_year)):
  print("Leap Year")
else:
  print("Not a Leap Ykear")
