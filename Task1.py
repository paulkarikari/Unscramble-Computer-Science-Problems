"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
from itertools import chain
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records?
Print a message:
"There are <count> different telephone numbers in the records."
"""

telphone_numbers_in_texts = list(chain.from_iterable(
    [(sender, reciever) for sender, reciever, _ in texts]))

unique_telephone_numbers_in_texts = set(telphone_numbers_in_texts)

telphone_numbers_in_calls = list(chain.from_iterable(
    [(caller, reciever) for caller, reciever, _, _ in calls]))

unique_telephone_numbers_in_calls = set(telphone_numbers_in_calls)

all_unique_numbers = unique_telephone_numbers_in_calls | unique_telephone_numbers_in_texts

print("There are {} different telephone numbers in the records.".format(
    len(all_unique_numbers)))
