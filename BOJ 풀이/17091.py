import sys
input = sys.stdin.readline

hour = int(input())
minute = int(input())

if minute > 30:
    back_flag = True
else:
    back_flag = False
    
word_dict = {
    1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four',
    5 : 'five', 6 : 'six', 7 : 'seven', 8 : 'eight',
    9 : 'nine', 10 : 'ten', 11 : 'eleven', 12 : 'twelve',
    13 : 'thirteen', 14 : 'fourteen', 15 : 'quarter', 16 : 'sixteen',
    17 : 'seventeen', 18 : 'eighteen', 19 : 'nineteen', 20 : 'twenty',
    30 : 'half'
}
for i in range(21, 30):
    word_dict[i] = word_dict[20] + " " + word_dict[i-20]

if minute == 0:
    answer = word_dict[hour] + " " + "o' clock"
elif not back_flag:
    if minute != 15 and minute != 30 and minute != 1:
        answer = word_dict[minute] + " " + "minutes" + " " + "past" + " " + word_dict[hour]
    elif minute == 1:
        answer = word_dict[minute] + " " + "minute" + " " + "past" + " " + word_dict[hour]       
    elif minute == 15 or minute == 30:
        answer = word_dict[minute] + " " + "past" + " " + word_dict[hour]
else:
    hour += 1
    if hour == 13:
        hour = 1
    minute = 60 - minute
    if minute != 15 and minute != 30 and minute != 1:
        answer = word_dict[minute] + " " + "minutes" + " " + "to" + " " + word_dict[hour]
    elif minute == 1:
        answer = word_dict[minute] + " " + "minute" + " " + "to" + " " + word_dict[hour]       
    elif minute == 15 or minute == 30:
        answer = word_dict[minute] + " " + "to" + " " + word_dict[hour]
print(answer)