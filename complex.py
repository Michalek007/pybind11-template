from complex import Complex

complex_number = Complex(1, 2)
complex_number2 = Complex(2, 4)
print(complex_number)

complex_number.print()
complex_number.add(complex_number2).print()
complex_number.subtract(complex_number2).print()
complex_number.multiply(complex_number2).print()
complex_number.divide(complex_number2).print()
complex_number.conjugate().print()

print(complex_number.modulus())
