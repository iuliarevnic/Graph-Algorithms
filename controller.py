'''
Created on 7 mar. 2019

@author: Revnic
'''

class Controller():
    def __init__(self,dictionary):
        self.__dictionary=dictionary;
    def __readOriginal(self):
        '''
        Function that reads the original file
        '''
        self.__dictionary._DoubleDictionary__readOriginal()   
    def __numberVertices(self):
        '''
        Function that gets the number of vertices
        '''
        return self.__dictionary.numberVertices()
    def __checkEdge(self,x,y):
        '''
        Function that checks if there is an edge between two given vertices
        '''     
        return self.__dictionary.existsEdge(x,y)
    def __outDegree(self,x):
        '''
        Function that returns the out degree of the given vertex
        '''
        return self.__dictionary.outDegree(x)
    def __inDegree(self,x):
        '''
        Function that returns the in degree of the given vertex
        '''
        return self.__dictionary.inDegree(x)    
    def __iterateVertices(self):
        '''
        Function that returns an iterable of the set of vertices
        '''
        return self.__dictionary.iterateVertices()    
    def __getCost(self,x,y):
        '''
        Function that returns the cost of a given edge 
        '''
        return self.__dictionary.getCost(x,y)
    def __changeCost(self,x,y,cost):
        '''
        Function that changes the cost of a given edge 
        '''
        return self.__dictionary.changeCost(x,y,cost)
    def __addVertex(self,x):
        '''
        Function that adds a vertex
        '''
        if(self.__dictionary.addVertex(x)==False):
            return "Vertex already exists."
    def __removeVertex(self,x):
        '''
        Function that removes a vertex
        '''
        if(self.__dictionary.removeVertex(x)==False):
            return "Vertex doesn't exist."
        
    def __addEdge(self,x,y,cost):
        '''
        Function that adds an edge
        '''
        if(not self.__dictionary.existsEdge(x,y)):
            self.__dictionary.addCost(x,y,cost)
        return self.__dictionary.addEdge(x,y)
    def __removeEdge(self,x,y):
        '''
        Function that removes an edge
        '''
        return self.__dictionary.removeEdge(x,y)        
    def __outboundEdge(self,x):
        '''
        Function that returns the outbound edges of x
        '''
        return self.__dictionary.outEdges(x)
    def __inboundEdge(self,x):
        '''
        Function that returns the inbound edges of x
        '''
        return self.__dictionary.inEdges(x)                
    def __readCopy(self):
        self.__dictionary._DoubleDictionary__readCopy()
    def __saveCopy(self):
        self.__dictionary._DoubleDictionary__saveCopy()    
    def __BFS(self,start,end):
        if(not start in self.__dictionary._DoubleDictionary__dictIn.keys() or not end in self.__dictionary._DoubleDictionary__dictIn.keys()):
            return []
        shortestPath=self.__dictionary._DoubleDictionary__BFS(start,end)
        return shortestPath    
    def __BFS1(self,start,end):
        print(self.__dictionary._DoubleDictionary__BFS1(start,end))
        return self.__dictionary._DoubleDictionary__BFS1(start,end)
    def __Ford(self,start,end):
        dist={}
        prev={}
        dist,prev=self.__dictionary.Ford(start,end)    
        return dist, prev
    def __Kruskal(self):
        return self.__dictionary.Kruskal()
    def __Hamiltonian(self):
        return self.__dictionary.Hamiltonian()