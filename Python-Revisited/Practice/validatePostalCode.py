# SOlution 1
import re
s = input()
print(s.isdigit() and 100000 <= int(s) <= 999999 and
      sum([s[i] == s[i+2] for i in range(0, 4)]) < 2)

# Solution 2
regex_integer_in_range = r"^[1-9]\d{5}$"
regex_alternating_repetitive_digit_pair = r"(.)(?=.\1)"

# Solution 3
s = input()
print(bool(re.match(r'^[1-9][\d]{5}$', s)
           and len(re.findall(r'(\d)(?=\d\1)', s)) < 2))
