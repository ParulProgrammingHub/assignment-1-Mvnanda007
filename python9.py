a=input("enter the value of 1st subject:");
b=input("enter the value of 2nd subject:");
c=input("enter the value of 3rd subject:");
d=input("enter the value of 4th subject:");
e=input("enter the value of 5th subject:");
mean=(a+b+c+d+e)/5
p=((a+b+c+d+e)*100)/500
print "Mean is:",mean,"Percentage is:",p,"%";
if (p<35):
  print "Fail!" ;
else:
  print "Pass!" ;
