'''
Created on 26 feb. 2019

@author: Revnic
'''
import copy 
import math
import queue
class Vertex():
    def __init__(self,x):
        self.number=x
        self.integer=x
        self.parent=0
        self.rank=0
        
class DoubleDictionary():
    def __init__(self,n,fileName):
        '''
        Function that creates a graph with n vertices(numbered from 0 to n-1)
        '''
        file=open(fileName,"r")
        line=file.readline().strip(" ")
        attributes=line.split(" ")
        n=int(attributes[0])
        self.__n=n
        file.close()
        self.__dictIn={}
        self.__dictOut={}
        self.__dictCost={}
        if fileName=="original.txt":
            for index in range(n):
                self.__dictOut[index]=[]
                self.__dictIn[index]=[]
         
    def iterateVertices(self):
        '''
        Function that returns an iterable structure containing all the vertices
        '''
        return list(self.__dictOut.keys())
    def existsEdge(self,x,y):
        '''
        Function that returns True if there is an edge from x to y and False otherwise
        '''
        if x in self.__dictOut.keys() and y in self.__dictOut.keys():
            return y in self.__dictOut[x]
        return 0
    def numberVertices(self):
        '''
        Function that counts the number of vertices 
        '''
        return len(self.__dictOut.keys())
    def addEdge(self,x,y):
        '''
        Function that adds an edge
        '''
        if(not self.existsEdge(x,y)):
            self.__dictIn[y].append(x)
            self.__dictOut[x].append(y)
            return 1
        return 0
    def outDegree(self,x):
        '''
        Function that returns the out degree of the given vertex
        '''
        if x in self.__dictOut.keys():
            return len(self.__dictOut[x])
    def inDegree(self,x):
        '''
        Function that returns the in degree of the given vertex
        '''
        if x in self.__dictIn.keys():
            return len(self.__dictIn[x])  
    def addCost(self,x,y,cost):
        '''
        Function that adds a cost
        '''
        self.__dictCost[(x,y)]=[cost]  
    def changeCost(self,x,y,cost):
        '''
        Function that changes a cost
        '''
        if self.existsEdge(x, y):
            self.__dictCost[(x,y)]=[cost]
            return 1
        return 0
    def getCost(self,x,y):
        '''
        Function that returns a cost
        '''
        if self.existsEdge(x,y):
            if(x<y):
                return self.__dictCost[(x,y)][0]
            else:
                return self.__dictCost[(y,x)][0] 
        return 0
    def addVertex(self,x):
        '''
        Function that adds a vertex
        '''
        if (not x in self.__dictIn.keys()):
            self.__dictIn[x]=[]
            self.__dictOut[x]=[]
            self.__n+=1
            return True
        return False
    def removeEdge(self,x,y):
        '''
        Function that removes an edge
        '''
        if(self.existsEdge(x, y)):
            self.__dictIn[y].remove(x)
            self.__dictOut[x].remove(y)
            del self.__dictCost[(x,y)]
            return 1
        return 0
    def removeVertex(self,x):
        '''
        Function that removes a vertex
        '''
        if not x in self.__dictIn.keys():
            return False
        else:
            for i in self.__dictIn[x]:
                del self.__dictCost[(i,x)]
                self.__dictOut[i].remove(x)
            del self.__dictIn[x]
            for i in self.__dictOut[x]:
                del self.__dictCost[(x,i)]
                self.__dictIn[i].remove(x)
            del self.__dictOut[x]
            self.__n-=1
            return True   
    def inEdges(self,x):
        '''
        Function that returns the inbound edges of x
        '''
        if x in self.__dictIn.keys():
            return list(self.__dictIn[x])
    def outEdges(self,x):
        '''
        Function that returns the outbound edges of x
        '''
        if x in self.__dictOut.keys():
            return list(self.__dictOut[x])                              
    def __readOriginal(self):
        '''
        Function that reads original file
        '''
        file=open("original.txt","r")
        line=file.readline().strip(" ")
        attributes=line.split(" ")
        '''dictionary=DoubleDictionary(int(attributes[0]))'''
        line=file.readline().strip(" ")
        while line!="":
            attributes=line.split(" ")
            self.addEdge(int(attributes[0]),int(attributes[1]))
            self.addEdge(int(attributes[1]), int(attributes[0]))
            if(int(attributes[0])<int(attributes[1])):
                self.addCost(int(attributes[0]),int(attributes[1]),int(attributes[2]))
            else:
                self.addCost(int(attributes[1]),int(attributes[0]),int(attributes[2]))    
            line=file.readline().strip()
        file.close()               
    def __readCopy(self):
        '''
        Function that reads copy file
        '''
        file=open("copy.txt","r")
        line=file.readline().strip(" ")
        attributes=line.split(" ")
        line=file.readline().strip(" ")
        while line!="":
            attributes=line.split(" ")
            if not int(attributes[0]) in self.__dictIn.keys():
                self.__dictIn[int(attributes[0])]=[]
                self.__dictOut[int(attributes[0])]=[]
            if int(attributes[1])>=0:    
                if not int(attributes[1]) in self.__dictIn.keys():
                    self.__dictIn[int(attributes[1])]=[]
                    self.__dictOut[int(attributes[1])]=[]    
            if(int(attributes[1])>=0):
                self.addEdge(int(attributes[0]),int(attributes[1]))    
                self.addEdge(int(attributes[1]), int(attributes[0]))    
                self.addCost(int(attributes[0]),int(attributes[1]),int(attributes[2])) 
            line=file.readline().strip(" ")
        file.close()   
    def __saveCopy(self):
        file=open("copy.txt","w")
        edges=len(self.__dictCost.keys())  
        firstLine=str(str(self.__n)+" "+str(edges)+"\n")
        file.write(firstLine)
        for vertex in self.__dictOut.keys():
            if(len(self.__dictOut[vertex])==0):
                stringToFile=str(str(vertex)+" "+"-1"+" "+"-1"+"\n")
                file.write(stringToFile)
            else:    
                for targetVertex in self.__dictOut[vertex]:
                    stringToFile=str(str(vertex)+" "+str(targetVertex)+" "+str(self.__dictCost[(vertex,targetVertex)][0])+"\n")
                    file.write(stringToFile)        
        file.close()        
        
        
    def __BFS(self,start,end):
        dist={}
        prev={}
        x=end
        visited=[x]
        y=-1
        distance=1;
        for i in self.__dictIn.keys():
            dist[i]=-1
            prev[i]=-1        
        dist[x]=0;   
        index=0
        position=0
        ok=0
        while y!=end and position<len(visited):
            x=visited[position]
            if index< len(self.__dictIn[x]):
                y=self.__dictIn[x][index]
                if not y in visited:
                    ok=1
                    dist[y]=distance
                    prev[y]=x
                    visited.append(y)
                index+=1
            else:
                index=0
                if(ok==1):
                    distance+=1
                position+=1
                ok=0;                      
        length=dist[start]
        shortestPath=[start]
        x=prev[start]
        while x!=end:
            if(x==-1):
                return []
            shortestPath.append(x)
            nextVertex=prev[x]
            x=nextVertex
        shortestPath.append(x)
        shortestPath.append(length)
        return shortestPath    
                 
    def __BFS1(self,start,end):
        
        #computes the lowest length path between two vertices
        #input: start and end vertice
        #output: path from start to end
        next = dict()
        path = []
        q = queue.Queue(20)
        visited = set()
        q.put(end)
        visited.add(end)
        true=0
        while not q.empty():
            vertice = q.get()
            print("pathh ", path)
            for v in self.__dictIn[vertice]:
                if v not in visited:
                    q.put(v)
                    visited.add(v)
                    next[v] = vertice
                    if (v == start):
                        true+=1
                        path.append(v)
                        while (v != end):
                            v = next[v]
                            path.append(v)
                        return path
        if true==0:
            return False               
                    
                
            
    def Ford(self,start,target):
        
        #initialisation                       
        dist={}
        prev={}                       
        for vertex in self.__dictIn.keys():
            dist[vertex]=math.inf
            prev[vertex]=-1
        dist[start]=0    
        
        #relaxation        
        changed=True
        while changed:
            changed=False
            for (x,y) in self.__dictCost.keys():
                if dist[y]>dist[x]+self.__dictCost[(x,y)][0]:
                    dist[y]=dist[x]+self.__dictCost[(x,y)][0]
                    prev[y]=x
                    changed=True
        #check negative cycles
        for (x,y) in self.__dictCost.keys():
                if dist[y]>dist[x]+self.__dictCost[(x,y)][0]:
                    print("Graph has negative cycles")
                    dist={}
                    prev={}          
        return dist, prev                
    def union(self,x,y):
        if x.rank>y.rank:
            y.parent=copy.deepcopy(x.integer)
        elif x.rank<y.rank:
            x.parent=copy.deepcopy(y.integer)
        else:
            y.parent=copy.deepcopy(x.integer)
            x.rank+=1
    def find(self,x):
        if x.integer!=x.parent:
            x.integer=copy.deepcopy(x.parent)
        return x.integer             
    def makeCloud(self,x):
        x.parent=copy.deepcopy(x.integer)
        x.rank=0
    def Kruskal(self):
        #do something        
        #for vertex in self.__dictIn.keys():
        #    self.makeCloud(Vertex(vertex))
        MST=[]
        edges=[]
        for (x,y) in self.__dictCost.keys():
            verx=Vertex(x)
            self.makeCloud(verx)
            very=Vertex(y)
            self.makeCloud(very)
            currentEdge=[verx,very,self.__dictCost[(x,y)][0]]
            edges.append(currentEdge)
            
        for i in range(0,len(edges)-1):
            for j in range(i+1,len(edges)):
                if(edges[i][2]>edges[j][2]):
                    auxiliary=edges[i]
                    edges[i]=edges[j]
                    edges[j]=auxiliary
                elif (edges[i][2]==edges[j][2]):
                    if(edges[i][0].integer>edges[j][0].integer):
                        auxiliary=edges[i]
                        edges[i]=edges[j]
                        edges[j]=auxiliary
                    elif(edges[i][0].integer==edges[j][0].integer):
                        if(edges[i][1].integer>edges[j][1].integer):
                            auxiliary=edges[i]
                            edges[i]=edges[j]
                            edges[j]=auxiliary
                            
        #for list in edges:
         #   print("element in edges:  ",list[0].integer,list[1].integer,list[2])        
        #a=Vertex(5)
        #print("fffff",self.find(a)) 
        cost=0        
        for i in range(0,len(edges)):
            if(self.find(edges[i][0])!=self.find(edges[i][1])):
                #print("x==",edges[i][0].number, "  y==",edges[i][1].number)
                #print("i=",i,"de x=",self.find(edges[i][0]),"de y=",self.find(edges[i][1]))
                currentEdge=[edges[i][0],edges[i][1]]
                MST.append(currentEdge)
                cost+=edges[i][2]
                self.union(edges[i][0], edges[i][1])
                for j in range(i+1,len(edges)):
                    
                    if edges[j][0].number==edges[i][0].number:
                        edges[j][0].parent=copy.deepcopy(edges[i][0].parent)
                        edges[j][0].rank=copy.deepcopy(edges[i][0].rank)
                    elif edges[j][1].number==edges[i][0].number:
                        edges[j][1].parent=copy.deepcopy(edges[i][0].parent)
                        edges[j][1].rank=copy.deepcopy(edges[i][0].rank)
                    elif edges[j][1].number==edges[i][1].number:
                        edges[j][1].parent=copy.deepcopy(edges[i][1].parent)
                        edges[j][1].rank=copy.deepcopy(edges[i][1].rank)
                    elif edges[j][0].number==edges[i][1].number:
                        edges[j][0].parent=copy.deepcopy(edges[i][1].parent)
                        edges[j][0].rank=copy.deepcopy(edges[i][1].rank)            
                #make sure you change it for every vertex
        MST.append(cost)        
        #for list in MST:
        #    print("element in MST:   ",list[0].number,list[1].number)        
        return MST                    
    def Hamiltonian(self):
        path=[]
        path.append(next(iter(self.__dictIn))) 
        #pana aici am adaugat primul vertex
        MST=self.Kruskal()
        minimumCost=MST[-1]
        print("Minimum cost is ",minimumCost)
        localCost=0
        for vertex in self.__dictIn.keys():
            if self.existsEdge(path[-1], vertex)==1 and vertex not in path:
                path.append(vertex)
                print("vertices are ",path[-2],vertex,"Cost is ",self.getCost(path[-2], vertex))
                localCost=localCost+self.getCost(path[-2], vertex)
        vertex=next(iter(self.__dictIn))        
        if self.existsEdge(path[-1], vertex)==1:
            path.append(vertex)      
            print("vertices are ",path[-2],vertex,"Cost is ",self.getCost(path[-2], vertex))
            localCost=localCost+self.getCost(path[-2], vertex)    
        print("Local cost ",localCost)
        return path        