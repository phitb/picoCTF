s = "jU5t_a_sna_3lpm18gb41_u_4_mfr340"
lst = []

for a in range(8):
      lst.insert(a, s[a])

for b in range(8,16):
      lst.insert(b, s[23 - b])

for c in range(16, 32, 2):
      lst.insert(c, s[46 - c])

for d in range(17, 32, 2):
      lst.insert(d, s[d])

flag = 'picoCTF{'
for v in lst:
      flag += v

print(flag + '}')