from pprint import pprint
sent = "This is a common interview question"

char_freq = {}

for char in sent:
    if char in char_freq:
        char_freq[char] += 1
    else:
        char_freq[char] = 1
pprint(char_freq, width=1)

char_freq_sorted = sorted(
    char_freq.items(), key=lambda kv: kv[1], reverse=True)
print(char_freq_sorted[0][0])


sent = "This is a very common interview question"

char_freq = {}

for char in sent:
    if char in char_freq:
        char_freq[char] += 1
    else:
        char_freq[char] = 1
pprint(char_freq, width=1)
pprint(sorted(char_freq.items(), key=lambda kv: kv[1], reverse=True))

char_freq_sorted = sorted(
    char_freq.items(), key=lambda kv: kv[1], reverse=True)

print("Maximum Repeating Character ::", char_freq_sorted[0])
