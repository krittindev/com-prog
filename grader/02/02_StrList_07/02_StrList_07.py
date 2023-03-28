s = input()
yellow = ''.join([e for e in s[3::7]])
blue = ''.join([e for e in s[7::5]])
pink = str(int(yellow) + int(blue) + 10000)[-4:-1]
blue = sum([int(e) for e in pink]) % 10 + 1
print(pink+chr(ord('A') - 1 + blue))