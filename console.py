'''
Created on 26 feb. 2019

@author: Revnic
'''
from dictionary import DoubleDictionary
class Console():
    def __init__(self,controller):
        self.__controller=controller
        self.__options=[1,2,3,4,5,6,7,8,9,10,11,12]
    def __printMenu(self):
        print()
        print("1.Read original")
        print("2.Read copy")   
        print("3.Get number of vertices")
        print("4.Iterate set of vertices")
        print("5.Check if there is an edge between two vertices")
        print("6.Get in/out degree")
        print("7.Iterate outbound edges")
        print("8.Iterate inbound edges")
        print("9.Retrieve/modify information for specified edge")
        print("10.Add/remove vertex/edge") 
        print("11.Save copy")
        print("12.BFS")
        print("13.Minimum cost Ford")
        print("14.Minimal spanning tree Kruskal")
        print("15.Hamiltonian cycle")
        
    def __readOriginal(self):
        self.__controller._Controller__readOriginal()
    def __readCopy(self):
        dictionary=DoubleDictionary(0,"copy.txt")
        self.__controller._Controller__dictionary=dictionary
        self.__controller._Controller__readCopy()
    def __numberVertices(self):
        print("There are ",self.__controller._Controller__numberVertices()," vertices.")
    def __iterateVertices(self):
        iterable=self.__controller._Controller__iterateVertices()
        for i in iterable:
            print(i)
    def __checkEdge(self):
        x=int(input("Give start vertex"))
        y=int(input("Give end vertex"))
        ok=self.__controller._Controller__checkEdge(x,y)
        if(ok):
            print("There is an edge between the given vertices.")
        else:
            print("There is no edge between the given vertices.")    
    def __getDegree(self):
        x=int(input("Give vertex"))
        print("Out degree",self.__controller._Controller__outDegree(x))
        print("In degree",self.__controller._Controller__inDegree(x))   
    def __outboundEdge(self):
        x=int(input("Give vertex"))
        print(self.__controller._Controller__outboundEdge(x))
    def __inboundEdge(self):
        x=int(input("Give vertex"))
        print(self.__controller._Controller__inboundEdge(x))
    def __cost(self):
        print("a.Retrieve information")
        print("b.Modify information")
        choice=input("Choose")
        x=int(input("Give start vertex"))
        y=int(input("Give end vertex"))
        if(choice=="a"):
            result=self.__controller._Controller__getCost(x,y)
            if result!=0:
                print("The cost is",result)
            else:
                print("There is no edge between the given vertices")    
        else:
            newCost=int(input("Give new cost"))
            result=self.__controller._Controller__changeCost(x,y,newCost)
            if result==0:
                print("There is no edge between the given vertices")    
    def __addRemove(self):
        print("a.Add vertex")
        print("b.Remove vertex")
        print("c.Add edge")
        print("d.Remove edge")
        choice=input("Choose option")
        if(choice=="a" or choice=="b"):
            x=int(input("Give vertex"))
            if(choice=="a"):
                result=self.__controller._Controller__addVertex(x)
                if result!=None:
                    print(result)
            else:
                result=self.__controller._Controller__removeVertex(x)
                if result!=None:
                    print(result)  
        else:
            x=int(input("Give start vertex"))
            y=int(input("Give end vertex"))
            if(choice=="c"):
                cost=int(input("Give cost"))
                result=self.__controller._Controller__addEdge(x,y,cost)
                if result==0:
                    print("Edge already exists")
            else:
                result=self.__controller._Controller__removeEdge(x,y)
                if result==0:
                    print("Edge doesn't exist")              
            
    def __save(self):    
        self.__controller._Controller__saveCopy()
    def __BFS(self):
        start=int(input("Give start vertex"))
        end=int(input("Give end vertex"))
        '''shortestPath=self.__controller._Controller__BFS1(start,end)
        if shortestPath==[]:
            print("Vertices don't exist or they are not connected")
        else:    
            print("Length is",len(shortestPath)-2)
            shortestPath.pop()
            print("Shortest path is",shortestPath)  '''
        path=self.__controller._Controller__BFS1(start,end)
        if path==False:
            print("No path")
        else:
            print("Length is ",len(path)-1)
            print("Path is ",path)    
    def __Ford(self):
        start=int(input("Give start vertex"))
        end=int(input("Give end vertex"))
        if(end not in self.__controller._Controller__dictionary._DoubleDictionary__dictIn.keys() or start not in self.__controller._Controller__dictionary._DoubleDictionary__dictIn.keys()):
            print("At least one vertex is not in the representation")
            return
        dist={}
        prev={}
        dist, prev=self.__controller._Controller__Ford(start,end)
        if(dist!={} and prev!={}):
            
            path=[]
            x=end
            while x!=start:
                if(x==-1):
                    print("There is no path")
                    return
                path.append(x)
                x=prev[x]
            print("Cost is ",dist[end])    
            path.append(x)
            path=list(reversed(path))    
            print("Path is ",path)
            #for vertex in path[::-1]:
             #   print(vertex)
            
    def __Kruskal(self):
        MST=[]
        MST=self.__controller._Controller__Kruskal()
        print("Cost is ",MST[-1])
        del MST[-1]
        print("Minimal spanning tree ")
        for list in MST:
            print(list[0].number,list[1].number)    
            
    def __Hamiltonian(self):
        HC=[]
        HC=self.__controller._Controller__Hamiltonian()  
        print("Hamiltonian ",HC)                                  
    def run(self):
        while True:
            self.__printMenu()
            choice=int(input("Choose option"))
            if choice==1:
                self.__readOriginal()
            elif choice==2:
                self.__readCopy()
            elif choice==3:
                self.__numberVertices()
            elif choice==4:
                self.__iterateVertices()
            elif choice==5:
                self.__checkEdge()
            elif choice==6:
                self.__getDegree()
            elif choice==7:
                self.__outboundEdge()
            elif choice==8:
                self.__inboundEdge()
            elif choice==9:
                self.__cost()
            elif choice==10:
                self.__addRemove()
            elif choice==11:
                self.__save()
            elif choice==12:
                self.__BFS()       
            elif choice==13:
                self.__Ford()        
            elif choice==14:
                self.__Kruskal()            
            elif choice==15:
                self.__Hamiltonian()    