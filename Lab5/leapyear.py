
year=int(raw_input("Enter a year to check if it is leap year: "))
print"Your input was: ",
print(year)

if((year%4==0) and (year%100!=0) and (year%400)):
  print("The year you entered is a leap year.")
else:
  print("The year you entered is NOT a leap year.")
