s1 = input().strip()
s2 = input().strip()

s1_letter = s1.isalpha()
s1_digit = s1.isdigit()
s2_letter = s2.isalpha()
s2_digit = s2.isdigit()

if (s1_letter and s2_digit) or (s1_digit and s2_letter):
    print("YES")
else:
    print("NO")
