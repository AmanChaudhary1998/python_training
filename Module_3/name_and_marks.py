s = list(input("enter the name of the student and the marks obtained in 5 subjects along with marks 3 pratical subject\n").split(','))
p = list(map(int, s[1:]))
sum1  = sum(p[2:5])
sum2 = sum(p[6:8])
perc = ((sum1+sum2)/590)*100
print(sum1,' ',sum2,' percentage is ',perc)
