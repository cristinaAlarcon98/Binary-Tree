
def isValidBinaryTree(binaryTreeStr):
	binaryTree=parseBinaryTree(binaryTreeStr)

	if checkPairsAreEqual(binaryTree)==True:
		print('a')
		return False
	if checkChildHasDifferentParents(binaryTree)==True:
		print('b')
		return False
	if checkParentHasMoreThanTwoChildren(binaryTree)==True:
		print('c')
		return False
	if checkChildAndParentAreEqual(binaryTree)==True:
		print('d')
		return False
	if checkThereAreMoreThanOneTree(binaryTree)==True:
		print('e')
		return False
	if checkPalindromic(binaryTree)==True:
		print('f')
		return False
	if checkIfChildrenAreSmallerOrBigger(binaryTree)==True:
		print('g')
		return False
	else:
		return True
	

#Converts string values to int values of a given array
def parseBinaryTree(binaryTreeStr):

	binaryTreeInt=[]
	for pairStr in binaryTreeStr:

		#Makes a new array with a child and a parent deleting patenthesis
		pairInt=[]
		pairStrReplaced=pairStr.replace('(','')
		pairStrReplaced=pairStrReplaced.replace(')','')
		pairReplacedSplited=pairStrReplaced.split(',')

		#Parses to Int each number of the pair
		pairInt.append(int(pairReplacedSplited[0]))
		pairInt.append(int(pairReplacedSplited[1]))
		binaryTreeInt.append(pairInt)

	return binaryTreeInt



def checkChildHasDifferentParents(binaryTree):

	#Makes a new array with every children
	childrenArray=[]
	for pair in binaryTree:
		childrenArray.append(pair[0])
		
	#Checks if there are more than one child in the childrenArray, that means a child has more than one parent
	for i in range(len(childrenArray)):
		for j in range(i+1,len(childrenArray)):
			if childrenArray[i]==childrenArray[j]:
				return True
	return False



def checkParentHasMoreThanTwoChildren(binaryTree):

	#Makes a new array with every parent
	parentsArray=[]
	for i in binaryTree:
		parentsArray.append(i[1])

	
	#Counts how many parents are in the parents array
	for i in range(len(parentsArray)):
		counter=0
		for j in range(i+1,len(parentsArray)):
			if parentsArray[i]==parentsArray[j]:
				counter+=1
		if counter>=2:
			return True
	
	return False


def checkChildAndParentAreEqual(binaryTree):
	for pair in binaryTree:
		if pair[0]==pair[1]:
			return True
	return False
	

#Checks if any pair of the input array are equal
def checkPairsAreEqual(binaryTree):		

	for i in range(len(binaryTree)):
		for j in range( i+1, len(binaryTree)):
			if binaryTree[i]==binaryTree[j]:
				return True
	return False



#Checks the relation between pairs to see if there are more than one tree
def checkThereAreMoreThanOneTree(binaryTree):

	#Makes an array of children and parents
	childrenArray=[]
	parentsArray=[]
	endAndBeginningOfTree=0
	threshold=2
	repeated=False
	for i in binaryTree:
		childrenArray.append(i[0])
		parentsArray.append(i[1])
	
	#If a parent is repeated the threshold is increased by one
	for i in range(len(parentsArray)):
		for j in range(i+1, len(parentsArray)):
			if parentsArray[i]==parentsArray[j]:
				threshold+=1
	
	#If  a child does not have an equal parent in the parents array, then the counter is increased by one
	for i in childrenArray:
		for j in parentsArray:
			if i==j:
				repeated=True
		if repeated==False:
			endAndBeginningOfTree+=1

	#If at parent does not have an equal child in the children array, then the counter is increased by one
	for i in parentsArray:
		for j in childrenArray:
			if i==j:
				repeated=True
		if repeated==False:
			endAndBeginningOfTree+=1

	#counts if there are more beginnings and endings than there should be
	if endAndBeginningOfTree>threshold:
		return True
	else:
		return False
			
#Cheks if a pair is a palindromic of other one		
def checkPalindromic(binaryTree):
	for i in range(len(binaryTree)):
		for j in range( i+1, len(binaryTree)):
			if binaryTree[i][0]==binaryTree[j][1] and binaryTree[i][1]==binaryTree[j][0] :
				return True
	return False

		
#Checks if a parent has two smaller or bigger children 
def checkIfChildrenAreSmallerOrBigger(binaryTree):
	
	
	for i in range(len(binaryTree)):
		for j in range(i+1,len(binaryTree)):
			if binaryTree[i][1]==binaryTree[j][1]:
				if binaryTree[i][0] < binaryTree[i][1] and binaryTree[j][0] < binaryTree[i][1]:
					return True
				elif binaryTree[i][0]>binaryTree[i][0] and binaryTree[i][0]>binaryTree[i][1]: 
					return True
	return False


	


