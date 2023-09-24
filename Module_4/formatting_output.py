# format specifiers = {value:flags} format a value based on which flags are inserted

# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces 
# :< = left justify
# :> = right justify
# :^ = center alignment
# :+ = use a plus sign to indicate a positive value
# := = place sign to leftmost position
# :  = insert a space before positive numbers
# :, = comma separator

# Example

price1 = 3.14159
price2 = -987.65
price3 = 12.34
price4 = 65.33
price5 = 4.38
price6 = 739.64
price7 = 84.02
price8 = 5.91
price9 = 1000.89
price10 = 764.29
price11 = 3012.26
price12 = 93781.99632

print(f"Price 1 is ${price1:.2f}") # the price will have 2 decimals in a floating point number
# result --> Price 1 is $3.14
print(f"Price 2 is ${price2:.3f}") # will concatenate an additional zero
# result --> Price 2 is $-987.650
print(f"Price 3 is ${price3:10}") # will give space between the $ and the value
# result --> Price 3 is $     12.34
print(f"Price 4 is ${price4:010}") # will add zero padding to the price
# result --> Price 4 is $0000065.33
print(f"Price 5 is ${price5:<10}") # will justify the value to the left
# result --> Price 5 is $4.38
print(f"Price 6 is ${price6:>10}") # will justify the value to the right
# result --> Price 6 is $    739.64
print(f"Price 7 is ${price7:^10}") # will center align the price
# result --> Price 7 is $  84.02 
print(f"Price 8 is ${price8:+}") # will display the value as positive
# result --> Price 8 is $+5.91
print(f"Price 9 is ${price9:=}") # will place sign to leftmost position
# result --> Price 9 is $1000.89
print(f"Price 10 is ${price10: }") # will insert a space before positive numbers
# result --> Price 10 is $ 764.29
print(f"Price 11 is ${price11:,}") # will display a thousands separator
# result --> Price 11 is $3,012.26
print(f"Price 12 is ${price12:+,.2f}") # can use more than one flag
# result --> Price 12 is $+93,782.00

