# 4. Напишите программу, которая по заданному номеру четверти, показывает
# диапазон возможных координат точек в этой четверти (x и y).

print('Enter quater number: ')
n=int(input())
if n==1:
    print('x>0;y>0')
elif n==2:
    print('x<0;y>0')
elif n==3:
    print('x<0;y<0')
elif n==4:
    print('x>0;y<0')
elif n>4 or n<1:
    print('The quater is entered incorrectly!')    