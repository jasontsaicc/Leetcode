s = input()
dict_a = {}
for i in range(len(s)):
    dict_a[s[i]] = s.count(s[i])

for m in dict_a:
    print(m, dict_a[m])