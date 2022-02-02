# (How Big Can Python Integers Be?) We’ll answer this question later in the book.
# For now, use the exponentiation operator ** with large and very large exponents to produce
# some huge integers and assign those to the variable number to see if Python accepts
# them. Did you find any integer value that Python won’t accept?

number = (673383545448**90000)
print(number)


#Python accepted all my huge integers and the large exponents too, though it took a while before it started to process the number value
#I did not find any integer value that Python won't accept