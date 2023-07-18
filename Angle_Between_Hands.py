hour,minutes=map(int,input().split(':'))
angle=(hour+minutes/60)*30-minutes*6
if angle<0: angle=-angle
if angle>180.0: angle=360-angle
print(angle)