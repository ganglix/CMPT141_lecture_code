#      [           ]
#    _______
#    7654321
#    0123456
s = "Fiction"
print(
s[1:3],

s[-4:10],

s[0:len(s):2],

s[0:len(s):-1],    # ""

s[len(s):-8:-1],
sep="\n"
)

s = "Green Arrow"

# (a) the first five characters of s, i.e. "Green"
print(s[0: 5])
# (b) the fourth to eighth characters of s inclusive, i.e. "en Ar"

# (c) the last five characters of s, i.e. "Arrow"
print(s[-5 : ])
# (d) every third character of s from the second character
# onwards, i.e. "rnrw"
print(s[1 : :3])
# (e) the last five characters of s in reverse, i.e. "worrA".
print(s[-1:-(5+1):-1])