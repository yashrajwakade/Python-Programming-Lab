#Eligible for voting or not
n = int(input())

if(n>=18):
  print("The person is eligible to vote")
else:
  print("The person is not eligible to vote ")
  print("Eligible to vote after",18-n,"years")