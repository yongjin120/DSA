from Node import Node

class SinglyLinkedList:
    nodeHead=''
    nodeTail=''
    SL_list=''
    size = 0
    def __init__(self):
        self.nodeTail = Node(binTail=True)
        self.nodeHead = Node(binHead=True, nodeNext=self.nodeTail)
        
        
    def insertAt(self, objInsert, idxInsert):
        if(self.size<idxInsert):
            print('size over ')
            raise NotImplementedError

        else:            
            nodeNew = Node(objValue = objInsert)
            nodePrev = self.get(idxInsert - 1)
            nodeNext = nodePrev.getNext()
            nodePrev.setNext(nodeNew)
            nodeNew.setNext(nodeNext)
            self.size = self.size+1
            print('insert : ', objInsert)
            
            
            
    def removeAt(self, idxRemove):
        nodePrev = self.get(idxRemove - 1)
        nodeRemove = nodePrev.getNext()
        nodeNext = nodeRemove.getNext()
        nodePrev.setNext(nodeNext)
        self.size = self.size-1
        return nodeRemove.getValue()
            
    
    def get(self, idxRetrieve):
        nodeReturn = self.nodeHead
        for itr in range(idxRetrieve+1):
            nodeReturn = nodeReturn.getNext()
        return nodeReturn
    
    def printStatus(self):
        nodeCurrent = self.nodeHead
        while(nodeCurrent.getNext().isTail()==False):
            nodeCurrent =nodeCurrent.getNext()
            
            print(nodeCurrent.getValue())
    
    def getSize(self):
        return self.size