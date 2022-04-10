s = "India is a country of agriculture and farmers are the pillar"
d = {}
for a in s:
    if a in d:
        d[a] = d[a]+1
    else:
        d[a]=1

print(d)