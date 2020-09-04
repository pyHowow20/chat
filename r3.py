
lines = []
with open('3.txt', 'r', encoding="utf-8-sig") as f:
	for line in f:
		lines.append(line.strip())

for line in lines:
	s = line.split(' ')
	time = s[0][:5] #清單的切割也可以用於字串
	name = s[0][5:] #第5位開始到最後 
	print(name)