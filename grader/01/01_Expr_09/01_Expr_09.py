def str2hms(hms_str):
	t = hms_str.split(':')
	return int(t[0]),int(t[1]),int(t[2])
def hms2str(h,m,s):
	return ('0'+str(h))[-2:] + ':' + ('0'+str(m))[-2:] + ':' + ('0'+str(s))[-2:]
def to_sec(h,m,s):
	return h * 60 ** 2 + m * 60 + s
def to_hms(s):
	return s // 60**2, (s % 60**2) // 60, s % 60
def diff(h1,m1,s1,h2,m2,s2):
	return to_hms(abs(to_sec(h1, m1, s1) - to_sec(h2, m2, s2)))
def main():
	hms_start = input()
	hms_end = input()
	h1,m1,s1 = str2hms(hms_start)
	h2,m2,s2 = str2hms(hms_end)
	h, m, s = diff(h1,m1,s1,h2,m2,s2)
	print(hms2str(h, m, s))
exec(input()) # DON'T remove this line