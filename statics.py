import math
# Dynamic input for basic math operations
num = float(input("Enter a number for mathematical operations: "))
# Arithmetic Operations
print("\nBasic Operations:")
print(f"Square root of {num}: {math.sqrt(num)}")
print(f"Factorial of {int(num)} (if integer): {math.factorial(int(num)) if num.is_integer() and num >= 0 else
'Factorial not defined for this input.'}")
print(f"{num} raised to the power 3: {math.pow(num, 3)}")
# Trigonometric Functions
print("\nTrigonometric Functions:")
angle = float(input("Enter an angle (in degrees): "))
radians = math.radians(angle)
print(f"Sine of {angle} degrees: {math.sin(radians)}")
print(f"Cosine of {angle} degrees: {math.cos(radians)}")
print(f"Tangent of {angle} degrees: {math.tan(radians)}")
# Logarithmic and Exponential Functions
print("\nLogarithmic and Exponential Functions:")
log_base = float(input(f"Enter a base for logarithm of {num}: "))
print(f"Logarithm of {num} to base {log_base}: {math.log(num, log_base)}")
print(f"Natural logarithm (ln) of {num}: {math.log(num)}")
print(f"Exponential of {num}: {math.exp(num)}")
# Rounding Functions
print("\nRounding Functions:")
print(f"Ceiling of {num}: {math.ceil(num)}")
print(f"Floor of {num}: {math.floor(num)}")