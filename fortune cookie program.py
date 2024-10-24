import random

lucky_number = random.randint(1,50)

fortune_message = random.randint(1,3)

if fortune_message == 1:
    print ("An exciting opportunity lies in front of you. Your lucky number is: " + str(lucky_number))
if fortune_message == 2:
    print ("When one door closes, another opens. Your lucky number is: " + str(lucky_number))
else:
    print ("Don't live beyond your means. Your lucky number is: " + str(lucky_number))


