def getInput():
  """
    Get input from user.
    """

  # Get input from user
  userInput = int(
      input("\nEnter the number corresponding to the mode you like: "))

  return userInput

def add(num1, num2):
  """
  Add two numbers.
  """
  
  print("\nAdding " + str(num1) + " and " + str(num2) + "...")
  sum = num1 + num2
  return sum

def subtract(num1,num2):
  """
  Subtract two numbers.
  """
  
  print("\nSubtracting " + str(num2) + " from " + str(num1) +
        "...")
  difference = num1 - num2
  return difference

def multiply(num1, num2):
  """
  Multiply two numbers.
  """
  
  print("\nMultiplying " + str(num1) + " and " + str(num2) + "...")
  product = num1 * num2
  return product

def divide(num1, num2):
  """
  Divide two numbers.
  """
  
  print("\nDividing " + str(num1) + " by " + str(num2) + "...")
  quotient = num1 / num2
  return quotient
  
def operation(modeInput):
  """
  Perform arithmetic operation
  """
  #Variable initialization
  result = 0
  numInput1 = 0
  numInput2 = 0
  
  if modeInput == 1:  # Get the sum of two numbers from user input
    numInput1 = int(input("\nEnter the first number: "))
    numInput2 = int(input("Enter the second number: "))
    result = add(numInput1, numInput2)  
  elif modeInput == 2:  # Get the difference of two numbers from user input
    numInput1 = int(input("\nEnter the first number: "))
    numInput2 = int(input("Enter the second number: "))
    result = subtract(numInput1, numInput2)
  elif modeInput == 3:  # Get the product of two numbers from user input

    numInput1 = int(input("\nEnter the first number: "))
    numInput2 = int(input("Enter the second number: "))
    result = multiply(numInput1, numInput2)
  elif modeInput == 4:  # Get the quotient of two numbers from user input
    numInput1 = int(input("\nEnter the first number (dividend): "))
    numInput2 = int(input("Enter the second number (divisor): "))
    result = divide(numInput1, numInput2)
  else:
    print("\nChoose a valid mode!!!")
  
  # Return result
  return result


def main():
  """
  Main function
  """
  print("HI! I am your personal calculator")
  print("\nWhat arithmetic operation would you like to do?")
  print("Enter the number/integer corresponding to the operation")
  print("\n(1) Addition  (2) Subtraction  (3) Multiplication  (4) Division")
  #exitFlag = True
  while True:
    # Get input from user
    try:
      modeInput = getInput()
      try:
        result = operation(modeInput)
        if modeInput in [1, 2, 3, 4]:
          print("\nThe answer is " + str(result))
        else:
          print("\nTry again.")
      except ValueError:
        print("\nEnter integers only! Try again.")
      except ZeroDivisionError:
        print("\nYou cannot divide by zero! Try again.")
    except ValueError:
      print("\nEnter integers only! Try again.")

    exitFlagInput = input("\nWould you like to Exit? Yes or No?: ").upper()

    if exitFlagInput == "YES":
      print("\nGoodbye!")
      break
    else:
      continue


main()
