"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""
first_text = texts[0]
last_call = calls[-1]

first_text_template = "First record of texts, {} texts {} at time {}"
last_call_template = "Last record of calls, {} calls {} at time {}, lasting {} seconds"

print(first_text_template.format(*first_text))
print(last_call_template.format(*last_call))
