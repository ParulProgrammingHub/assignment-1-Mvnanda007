def compound_interest ( a , t , r ):
  compound_interest = ( a * ( 1 + ( r / 100 )) ** t ) - a
  return compound_interest;

print "Compound interest:",compound_interest ( 10000 , 2 , 1200 )