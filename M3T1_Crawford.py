# CTI 110
# M3T1 - Areas of Rectangles
# 9/13
# Crawford

# get the dimentsion of rectangle 1

length1 = int(input('Enter the length of rectangle 1: '))
width1 = int(input('Enter the width of rectangle 1:'))

# get the dimentsion of rectangle 2

length2 = int(input('Enter the length of rectangle 2: '))
width2 = int(input('Enter the width of rectangle 2:'))

# calculate the areas of the rectangles

area1 = length1 * width1
area2 = length2 * width2

# Determine with rectangle has a bigger area

if area1 > area2:
    print('Rectangle 1 has the bigger area.')
elif area2 > area1:
    print ('Rectangle 2 has the bigger area.')
else:
    print('Both rectangle have equal area.')
