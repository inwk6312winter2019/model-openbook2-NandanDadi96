file=open("Street_Centrelines.csv","r")

def tuplelist():
	for line in file:
		line=line.split(',')
		word=(line[2],line[4],line[6],line[7])
		print(wo
def histogram():
	hist=dict()
	for line in file:
		line=line.split(',')
		word=(line[12])
		if word not in hist:
			hist[word]=1
		else:
			hist[word]+=1
	print(hist)

def uniquelist():
	ulist=[]
	for line in file:
		line=line.split(',')
		word=line[11]
		if word not in ulist:
			ulist.append(word)
	print(ulist)

def Strclass():
	stclass=[]
	for line in file:
		line=line.split(',')
		word=line[10]
		if word not in stclass:
			stclass.append(word)
	print(stclass)
	
Strclass()


