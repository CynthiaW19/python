from random import randint
def randlist(r,usedlist,done):
	sum = 0
	alpha = ["a","b","c","d","e","f","g","h","i","j",
			 "k","l","m","n","o","p","q","r","s","t"
			 "t","u","v","w","x","y","z"]
	usedlist[r] = 1
	c = alpha[r]
	
	for i in range(len(usedlist)):
		sum = sum + usedlist[i]
	#print (c,usedlist," sum ",sum)
	if sum == 6:
		done = True
	return c,usedlist,done
	
def main():
	used = [0,0,0,0,0,0]
	done = False
	while done == False:
		r = randint(0,5)
		c,used,done = randlist(r,used,done)
		
		print(used)
		print(c,end="")
		

main()

