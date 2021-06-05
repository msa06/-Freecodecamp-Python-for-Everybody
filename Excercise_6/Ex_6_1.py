'''
Exercise 5: Take the following Python code that stores a string:
str = 'X-DSPAM-Confidence:0.8475'
Use find and string slicing to extract the portion of the string after the
colon character and then use the float function to convert the extracted
string into a floating point number.

'''

str = 'X-DSPAM-Confidence:0.8475'
atpos = str.find(":")
extract = str[atpos+1:]
result = float(extract)
print(f"Extracted {extract}")
print(f"Result : {result}")
