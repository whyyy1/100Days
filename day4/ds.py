#Merge Sort 

def mergeSort(list):
    if len(list) > 1:
        mid = len(list) //2
        left = list[:mid]
        right = list[mid:]

        #Recursive to go through the whole list
        mergeSort(left)
        mergeSort(right)

        #traverse throught the halves
        i = 0 
        j = 0
        #travers main list 
        k = 0 

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                list[k] = left[i]
                i+=1
            else:
                list[k] = right[j]
                j+=1
            k += 1
        while i < len(left):
            list[k]=left[i]
            i+=1
            k+=1
        while j < len(right):
            list[k]=left[j]
            j+=1
            k+=1

#Linked List
#Creates a Node that holds a value and may have a val its pointing to

class Node: 
    def __init__(self,data):
        self.data = data
        self.nextVal = None
#Start node is setting the starting value of the node and then adding to it

class startNode:

    def __init__(self):
        self.headVal = None

    def printList(self):
        pVal = self.headVal
        while pVal is not None: 
            print(pVal.data)
            pVal = pVal.nextVal
    
    def atBeginning(self,newD):
        newNode = Node(newD)
    
        newNode.nextVal = self.headVal
        self.headVal = newNode

        

        
    
         