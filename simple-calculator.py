def add(a, b):
  """Returns the sum of two numbers."""
  return a + b

def subtract(a, b):
  """Returns the difference of two numbers."""
  return a - b

def multiply(a, b):
  """Returns the product of two numbers."""
  return a * b

def divide(a, b):
  """Returns the quotient of two numbers."""
  return a / b

def power(a, b):
  """Returns the result of raising a to the power of b."""
  return a ** b

def calculate(operation, a, b):
  """Performs the specified operation on the two given numbers and returns the result."""
  if operation == "+":
    return add(a, b)
  elif operation == "-":
    return subtract(a, b)
  elif operation == "*":
    return multiply(a, b)
  elif operation == "/":
    return divide(a, b)
  elif operation == "^":
    return power(a, b)
  else:
    raise ValueError("Invalid operation.")

def main():
  """Prompts the user for two numbers and an operation, then performs the operation and prints the result."""

  print("Welcome to the calculator!")

  a = float(input("Enter the first number: "))
  b = float(input("Enter the second number: "))
  operation = input("Enter the operation (+, -, *, /, or ^): ")

  result = calculate(operation, a, b)

  print(f"The result is: {result}")

if __name__ == "__main__":
  main()
