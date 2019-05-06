"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
from itertools import chain
from collections import deque
from datetime import datetime
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".
"""

telphone_numbers_in_calls = list(chain.from_iterable(
    [(caller, reciever) for caller, reciever, _, _ in calls]))

unique_telephone_numbers_in_calls = set(telphone_numbers_in_calls)

que_of_numbers = deque(unique_telephone_numbers_in_calls)

numbers_with_call_time = []

while que_of_numbers:
    number = que_of_numbers.popleft()
    total_time = 0
    for caller, reciever, timestamp, duration in calls:
        date = datetime.strptime(timestamp, "%d-%m-%Y %H:%M:%S")
        if number in (caller, reciever) and date.year == 2016 and date.month == 9:
            total_time += int(duration)
    numbers_with_call_time.append((number, total_time))


highest_duration = sorted(numbers_with_call_time, key=lambda x: x[1])[-1]

template = "{} spent the longest time, {} seconds, on the phone during September 2016."

print(template.format(*highest_duration))
