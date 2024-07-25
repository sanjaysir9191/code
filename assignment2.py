




# Q1. Write a python program to check whether @ and . is present in a string or not.
string=input("enter  a string:")
if '@' in string and  '.' in  string:
    print("valid") 
else :
    print("invalid ")
# Q2. Write a python program to find mean, median, mode, standard deviation, and variance.


import statistics
givenList=[1,2,3,4,5,6,7,5,9,5]
mean = statistics.mean(givenList)
median = statistics.median(givenList)
mode=statistics.mode(givenList)
stdDeviation=statistics.stdev(givenList)
var=statistics.variance(givenList)

print("The mean is: ", mean)
print("The Median is: ", median)
print("The Mode is: ", mode)
print("The standard Deviation is: ", stdDeviation)
print("The variance is: ", var)

# Q3. Write a python program to find the occurrence of 'the' in a given string replace it with 'is'.
str= input("enter a string:")
new_str=str.replace("the","is" )
print(new_str)
# Q4. Write a python program to find the number of vowels, consonents and digits in a string.
str=input("enter your string : ")
lower= str.lower()
vowel=0;
consonent=0;
digit=0;
for i in range(0,len(str)):
    if str[i] in ("'a','e','i','o','u'"):
        vowel=vowel+1;
    elif (str[i] >= 'a' and str[i] <= 'z'):  
        consonent = consonent+1;
    elif str[i] in ("'1','2','3','4','5','6','7','8','9'"):
        digit=digit +1


print("vowels",vowel)
print("consonants" ,consonent)
print("digits" ,digit)
