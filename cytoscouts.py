# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 09:55:28 2017
@author: Petra Wijngaard
latest version 4 26 2018
"""
import sys
import csv
import math
import matplotlib.pyplot as plt
#print(fname)
def main():#print the outputs
    '''
    This is the main function.
    '''
    print('*✭˚･ﾟ✧*･ﾟ   it\'s cytoscouts   v.5    * ✭˚･ﾟ✧*･ﾟ*')
    edgeList,nodeSet = importtsv()
    print('\nThis interactome has', (len(edgeList)),'edges and contains', len(nodeSet)  , 'nodes.')
    deg=get_degree (edgeList,nodeSet)
    #print('Here is a list of nodes and the number of their edges: ', deg)
    dictionary=importdictionary() #outputs the whole dictionary
    #print(dictionary)
    
    printit=input('\nPress:\n 0 to print histogram, \n 1 to get neighbors of an id, \n 2 to get secondary neighbors, \n 3 to collapse the interactome, \n 4 to input node for collapsed interactome, \n otherwise any key to exit: ')
    if printit == '0':
        hist,x,y=get_histo(deg)
        lx,ly=computeLog(x,y)
        plotter1(x,y,lx,ly)
    if printit == '1': #asks for uniprot id and list of list of edges
        uniprot=input('type id here: ')
        nNodes = neighbors(uniprot,edgeList)
        #edgeSub = subsetEdges(uniprot,edgeList,nNodes)
        print("primary neighbors")
        print(nNodes)
        print (len(nNodes))
        print (type(nNodes))
        deg=getSubDegree(nNodes,edgeList,uniprot)
        hist,x,y=get_histo(deg)
        lx,ly=computeLog(x,y)
        plotter2(x,y,lx,ly,uniprot)
        commonNames=useDictionary(dictionary,nNodes,deg)
#        for item in commonNames: #print a line from a list of strings rather than the list 
#            print(item)
        makeFile(commonNames,uniprot)
    if printit == '2': #asks for uniprot id and list of list of edges
        uniprot=input('type id here: ')
        nNodes = neighbors(uniprot,edgeList)
        nNodes2=neighbor2 (nNodes,edgeList)
        print("primary neighbors")
        print(nNodes)
        print (len(nNodes))
        print("secondary neighbors")
        print (len(nNodes2))
    if printit == '3':
        collapsedTupleSet, skipped = collapseInteractome (dictionary,edgeList)
        collapsedNodeSet, skipped2 = collapseNodes (dictionary,nodeSet)
        print('\n Collapsing the interactome...\n',skipped,'edges skipped.',skipped2,'nodes skipped.')   
        print('# of edges in collapsed interactome: ',len(collapsedTupleSet) )   
        print('# of nodes collapsed interactome: ',len(collapsedNodeSet),'\n Histogram saved to .pdf.' )
        deg=get_degree (collapsedTupleSet,collapsedNodeSet)
        hist,x,y=get_histo(deg)
        lx,ly=computeLog(x,y)
        plotter3(x,y,lx,ly)
    if printit == '4':
        commonName=input('type common name here: ')
        collapsedTupleSet, skipped = collapseInteractome (dictionary,edgeList)
        collapsedNodeSet, skipped2 = collapseNodes (dictionary,nodeSet)
        nNodes = neighbors(commonName,collapsedTupleSet)
        #edgeSub = subsetEdges(uniprot,edgeList,nNodes)
        print("primary neighbors")
        print(nNodes)
        print (len(nNodes))
        print (type(nNodes))
        print(skipped,' skipped.')   
        print('# of tuples: ',len(collapsedTupleSet) )
        print(skipped2,' skipped.')   
        print('# of nodes: ',len(collapsedNodeSet) )
        deg=getSubDegree (nNodes,collapsedTupleSet,commonName)
        hist,x,y=get_histo(deg)
        lx,ly=computeLog(x,y)
        plotter4(x,y,lx,ly,commonName)
        commonDegs=makeCollapsedDeg(nNodes,deg)
        makeFile(commonDegs,commonName)
        print(deg)
        #tupleSettoLoL(collapsedTupleSet)

def makeCollapsedDeg (nNodes,deg):
    #makes a list of strings containing uniprot, common name, and degree then a new line
    commonDegs=[]
    for node in nNodes:
        commonDegs=commonDegs+[node+ ','+ str(deg[node])+'\n']
    return commonDegs

def makeFile (commonNames,uniprot):
   file= open(uniprot+" neighbors.csv", "w")
   file.write ('Uniprot ID, Common Name, Degree\n')#wirtes the header
   for row in commonNames:#wites the items from a list of strings
       file.write (row)
   file.close()
   return ()
'''
this one makes it as a list
def useDictionary (dictionary,nNodes,deg):
    commonNames=[]
    for key in dictionary:
            for node in nNodes:
                if key == node:
                    commonNames=commonNames+[node]+[dictionary[node]]+[deg[key]]+[';']
    return commonNames
'''
def collaspedDegs (nNodes,deg):
    return
def useDictionary (dictionary,nNodes,deg):
    #makes a list of strings containing uniprot, common name, and degree then a new line
    commonNames=[]
    for key in dictionary:
            for node in nNodes:
                if key == node:#if the neighbor is the same as the dictionary key
                    commonNames=commonNames+[node+ ','+ dictionary[node]+ ','+ str(deg[key])+'\n']
    return commonNames
def collapseInteractome (dictionary,edgeList):
   collapsedTupleSet = set()
   skipped = 0
   for row in edgeList:
       if row[0] in dictionary and row[1] in dictionary:
           if (dictionary[row[1]],dictionary[row[0]]) not in collapsedTupleSet:
               collapsedTupleSet.add(tuple((dictionary[row[0]],dictionary[row[1]])))
       else: 
           skipped +=1
   return collapsedTupleSet, skipped
def collapseNodes (dictionary,nodeSet):
    collapsedNodeSet = set()
    skipped2 = 0
    for key in nodeSet:
        if key in dictionary:
            collapsedNodeSet.add(dictionary[key])
        else: 
            skipped2 += 1
    return collapsedNodeSet, skipped2
#def tupleSettoLoL(collapsedTupleSet): #a function to turn the set of tuples back into a list of lists so it can be processed by getDegree
#    tuplesList=[]
#    tuplesLoL=[]
#    for ituple in collapsedTupleSet:
#        for value in ituple:
#            tuplesList+=[value] #make a list of every value in each tuple
#    for i in range(len(tuplesList)): #turn that list into a list of lists pairing every value in the list 
#        tuplesLoL+=[tuplesList[i:i+1]] #currently only makes a list of values not a list of lists
#    print(tuplesLoL)
#    return
#            
def importdictionary ():#get the TSV
    fname = 'nodes-uniprot.csv'
    dictionary={}
    with open(fname, newline='') as csvfile:
        reader = csv.reader(csvfile,dialect="excel-tab")
        for r in reader:
            if r[0]=='uniprot':#skip header
                continue
            if r[2]=='Aliases':#skip header
                continue
            dictionary[r[0]]=r[2]
    #makes a dictionary from index 0 as the key and index 2 as the value 
    return dictionary
def neighbor2 (nNodes,edgeList):
    nNodes2 =set()
    #if something frod edgeList matches something in nNodes,put it in nNodes2
    for row in edgeList: 
        for item in nNodes:
            if row[0]==item:
                nNodes2.add(row[1])
            if row[1]==item:
                nNodes2.add(row[0])
    return nNodes2
def neighbors(uniprot,edgeList):
    nNodes=set()
    for row in edgeList: 
        #a for loop in which if a row is the uniprot id, 
        #then the other row is added to a set
        if row[0] == uniprot:
            nNodes.add(row[1])
        if row[1] == uniprot:
            nNodes.add(row[0])
    return nNodes#

def plotter1(x,y,lx,ly):#plots for whole histogram
    
    
    plt.figure(1)
    plt.xlabel('Degree of nodes')
    plt.ylabel('Number of nodes')
    plt.scatter(x,y,marker='.')
    plt.savefig('histogram1.pdf', bbox_inches='tight')
    
    plt.figure(2)    
    plt.xlim([0,26])
    plt.scatter(x,y,marker='.')
    plt.xlabel('Degree of nodes')
    plt.ylabel('Number of nodes')
    plt.savefig('histogram2.pdf', bbox_inches='tight')

    plt.figure(3)    
    plt.xlabel('log(Degree of nodes)')
    plt.ylabel('log(Number of nodes)')
    plt.scatter(lx,ly,marker='.')
    plt.savefig('histogram3.pdf', bbox_inches='tight')
def plotter2(x,y,lx,ly,uniprot):#plots for uniprot id of choice
    plt.figure(1)
    plt.ylim([1,21]) 
    plt.xlabel('Degree of nodes')
    plt.ylabel('Number of nodes')
    plt.scatter(x,y)
    plt.yticks([0,1,2,3,4,5,10,15,20])
    plt.savefig(uniprot+'_1.pdf', bbox_inches='tight')
    
    plt.figure(2)    
    plt.xlim([0,2000])
    plt.ylim([1,6]) 
    plt.scatter(x,y,marker='.')
    plt.xlabel('Degree of nodes')
    plt.ylabel('Number of nodes')
    plt.yticks([0,1,2,3,4,5])
    plt.savefig(uniprot+'_2.pdf', bbox_inches='tight')

    plt.figure(3)
    plt.xlim([0,10])
    plt.xlabel('log(Degree of nodes)')
    plt.ylabel('log(Number of nodes)')
    plt.scatter(lx,ly,marker='.')
    plt.savefig(uniprot+'_3.pdf', bbox_inches='tight')
    
    return
def plotter3(x,y,lx,ly):#plots for whole histogram
    
    
    plt.figure(1)
    plt.xlabel('Degree of nodes')
    plt.ylabel('Number of nodes')
    plt.scatter(x,y,marker='.')
    plt.savefig('collapsedhistogram1.pdf', bbox_inches='tight')
    
    plt.figure(2)    
    plt.xlim([0,26])
    plt.scatter(x,y,marker='.')
    plt.xlabel('Degree of nodes')
    plt.ylabel('Number of nodes')
    plt.savefig('collapsedhistogram2.pdf', bbox_inches='tight')

    plt.figure(3)    
    plt.xlabel('log(Degree of nodes)')
    plt.ylabel('log(Number of nodes)')
    plt.scatter(lx,ly,marker='.')
    plt.savefig('collapsedhistogram3.pdf', bbox_inches='tight')

def plotter4(x,y,lx,ly,commonName):#plots for common name of choice
    plt.figure(1)
    plt.yticks([0,1,2,3])
    plt.xlabel('Degree of nodes')
    plt.ylabel('Number of nodes')
    plt.scatter(x,y)
    plt.savefig(commonName+'_1.pdf', bbox_inches='tight')
    
    plt.figure(2)    
    plt.xlim([0,1500]) 
    plt.scatter(x,y,marker='.')
    plt.xlabel('Degree of nodes')
    plt.ylabel('Number of nodes')
    plt.yticks([0,1,2,3])
    plt.savefig(commonName+'_2.pdf', bbox_inches='tight')

    plt.figure(3)
    plt.xlim([0,10])
    plt.xlabel('log(Degree of nodes)')
    plt.ylabel('log(Number of nodes)')
    plt.scatter(lx,ly,marker='.')
    plt.savefig(commonName+'_3.pdf', bbox_inches='tight')

def computeLog(x,y):
    lx=[]
    ly=[]
    for i in range(len(x)):
        if y[i] >0:
            lx.append(math.log(x[i]))
            ly.append(math.log(y[i]))
    return (lx,ly)
def importtsv ():#get the TSV
    fname = input('Please type .csv file here: ')
    nodeSet = set()
    edgeList = []
    with open(fname, newline='') as csvfile:
        reader = csv.reader(csvfile,dialect="excel-tab")
        for r in reader:
            if r[0]=='UniProt1':#skip header
                continue
            if r[1]=='UniProt2':#skip header
                continue
            edgeList.append([r[0],r[1]])#pair of nodes, aka an edge
            nodeSet.add(r[0])#node 1
            nodeSet.add(r[1])#node2
    #print(edgeList[0:10])#shows us some edges
    return edgeList,nodeSet#saves these two variables
def get_degree (edgeList,nodeSet):#gather nodes by number of edges
    """
    pseudocode:
    for {X} from nodeSet
    degree = find all lists in edgeLists where {X}
    d['X']= degree

    """
    deg = {}
    for item in nodeSet:
        deg[item]=0
    for row in edgeList:
        deg[row[0]]+=1
        deg[row[1]]+=1
    return deg
def get_histo (deg):#gather nodes by number of edges
    """
 
for histogram use the same function in a different order
d2 starts empty and then for item in nodelist d= deg[item] is d a key in d2?
if is then ratchet up the counter
if not then put in a new pair
"""
    hist = {} #empty dictionary
    key = 1 # the first x value in our histogram
    maxdeg = max(deg.values()) #the last x value in the histogram
    x = [] #list for x value in histogram
    y = [] #list for y value in histogram
    while key <= maxdeg: #while we havent reached the end of the dictionary
        val = 0 #include edge counts with no nodes
        for node in deg.keys(): #take the node
            if deg[node] == key: #if the node has key number of edges
                val += 1 #add one to the y axis for that edge number
        hist[key]=val #putting that number that into the dictionary
        x.append(key) #building the x value list
        y.append(val) #building the y value list
        key += 1 #move to the next x value in the histogram 
    return hist,x,y
def subsetEdges(uniprot,edgeList,nNodes): 
    #to get the subset of edges for the histogram of neighbors of the PoI
    #a list of edges containing the neighbor nodes of uniprot
    edgeSub=[]
    for row in edgeList:
        for node in nNodes:
        #a for loop in which if a row is the uniprot id, 
        #then the the row is added to a list, edgeSub
            if row[0] == node:
                edgeSub.append([row[0],row[1]])
            if row[1] == node:
                edgeSub.append([row[0],row[1]])
    return edgeSub
def getSubDegree (nNodes,edgeList,proteinName):#gather nodes by number of edges
    """
    pseudocode:
    for {X} from nNodes
    degree = find all lists in edgeLists where {X}
    d['X']= degree

    """
    deg = {}
    for item in nNodes:
        deg[item]=0 #adds key and sets value to zero, key value pair 
    for row in edgeList:
        if row[0] in nNodes:
            deg[row[0]]+=1 #increase value by one if a given nNodes key is row 0 in edgeList 
            if (row[1],row[0]) in edgeList and row[0] == proteinName:
                print(row,'!')
        if row[1] in nNodes:
            deg[row[1]]+=1 #increase value by one if a given nNodes key is row 1 in edgeList 
            if (row[1],row[0]) in edgeList and row[0] == proteinName:
                print(row,'!')
    return deg


if __name__ == '__main__':
    main()
