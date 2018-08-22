# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 09:55:28 2017
@author: Petra Wijngaard
latest version 8 22 2018

TODO:
[] make it not crash when given invalid inputs on option 1 and 4
[] enable a config file with include configparser
    options to include:
        [X]default interactome
        [x]remove header
        histogram variables
            []1
            []2
            []3
            []4
        []reference dictionary
"""
import configparser
import csv
import math
import matplotlib.pyplot as plt
import os.path
'''
Default Configuration Section
'''
config = configparser.ConfigParser(allow_no_value=True)

#Setting up the default configuration file

config.add_section('HELP')
config.set('HELP', '# comment here')
       
config['BASIC']= {
        'default_interactome':0,
        'skip_header':1,
        'reference_dictionary':0,
        }
config['HISTOGRAM'] = {
        }


if os.path.isfile('cytoscouts_config.ini') != True:  #check to see if there's a config file already
    print('No cytoscouts_config.ini file found, so one was written with default settings.')
    with open('cytoscouts_config.ini', 'w') as configfile: #if there isnt write one to file
        config.write(configfile)
config.read('cytoscouts_config.ini')


'''
Functions Section
'''


def main():
    '''
    Displays banner, takes interactome, provides summary statistics and calls options function for further analysis
    '''
    print('*✭˚･ﾟ✧*･ﾟ   it\'s cytoscouts   v0.6.2    * ✭˚･ﾟ✧*･ﾟ*')
    edgeList,nodeSet=checkDefaultInteractome() #checks for a default interactome and if there isnt one asks for an interactome
    print('\nThis interactome has', (len(edgeList)),'edges and contains', len(nodeSet)  , 'nodes.')
    deg=getDegree (edgeList,nodeSet) #calculates the degree
    printoptions(edgeList,nodeSet,deg) #the options menu
    return

def checkDefaultInteractome ():
    if config['BASIC']['default_interactome'] == '0':#checks for a default interactome in config.ini
        print('No default interactome set. To set one, edit cytoscouts_config.ini .')
        edgeList,nodeSet = importCSV()#asks for an interactome if none is found
    else:#if there is an interactome asks if you want to keep using it
        print('Default interactome is set to',config['BASIC']['default_interactome'],'\n Press 1 to continue using it.\n Press 0 to enter a new one.\n You can change the default interactome in cytoscouts_config.ini')
        while True:#loop in case of bad inputs
            chooseDefault = input()
            if chooseDefault == '1':
                edgeList,nodeSet = defaultCSV()
                break
            elif chooseDefault == '0':
                edgeList,nodeSet = importCSV()#asks for an interactome
                break
            else:
                print('Invalid Choice')
                    
    return edgeList,nodeSet

def importCSV ():#get the CSV
    '''
    TO DO:
        [X] program doesnt crash if not supplied an ending
        [X]accept files with .txt and .tsv endings
        [x]enable skip header <=================================
        []count number of columns


    '''
#    validateFileName = None
#    while validateFileName == None:

#        validate = re.compile(r'.*.csv') #(r'.csv|.tsv|.txt')
#        validateFileName = validate.search(fileName)
    nodeSet = set()
    edgeList = []
    while True:
        try:
            fileName = input('Please type .csv file here: ')
            with open(fileName, newline='') as cSVFile:
                if config['BASIC']['skip_header'] == '1':
                    next(cSVFile)
                reader = csv.reader(cSVFile,dialect="excel-tab")
                for r in reader:
                   edgeList.append([r[0],r[1]])#pair of nodes, aka an edge
                   nodeSet.add(r[0])#node 1
                   nodeSet.add(r[1])#node2

            break

        except OSError:
            print ("Could not read file. Did you remember the extension? Invalid file:", fileName)

    #print(edgeList[0:10])#shows us some edges
    return edgeList,nodeSet#saves these two variables

def defaultCSV ():#get the CSV
    '''
    TO DO:
        [x]enable skip header
        []count number of columns

    '''

    nodeSet = set()
    edgeList = []
    while True:
        try:
            fileName = config['BASIC']['default_interactome']
            with open(fileName, newline='') as cSVFile:
                if config['BASIC']['skip_header'] == '1':
                    next(cSVFile)
                reader = csv.reader(cSVFile,dialect="excel-tab")
                for r in reader:
                   edgeList.append([r[0],r[1]])#pair of nodes, aka an edge
                   nodeSet.add(r[0])#node 1
                   nodeSet.add(r[1])#node2

            break

        except OSError:
                print ("Could not read default file, please enter a valid filename for now and change cytoscouts_config.ini when you have the chance. Invalid file:", fileName)
        edgeList,nodeSet=importCSV()#defaults to manual entry
    

    return edgeList,nodeSet#saves these two variables


def printoptions (edgeList,nodeSet,deg):
    printit=input('\nPress:\n 1 to print histograms of the uncollapsed interactome, \n 2 to get neighbors of an ID, \n 3 (DEPRECATED) to get secondary neighbors of an ID, \n 4 to collapse the interactome (requires reference CSV), \n 5 to input common name node for collapsed interactome (requires reference CSV), \n otherwise any key to exit: ')
    if printit == '1':
        hist,x,y=get_histo(deg)
        lx,ly=computeLog(x,y)
        plotter1(x,y,lx,ly)
    if printit == '2': #asks for uniprot id and list of list of edges
        '''
        [] rename commonDegs to make it make more sense
        '''
        uniprot=input('Enter id here: ')
        nNodes = neighbors(uniprot,edgeList)
        collapsed = False #this is a workaround so that getSubDegree doesnt hang when using option 1
        #edgeSub = subsetEdges(uniprot,edgeList,nNodes)
        print("Primary neighbors")
        #print(nNodes)
        #print (len(nNodes))
        #print (type(nNodes))
        deg=getSubDegree(nNodes,edgeList,uniprot,collapsed)
        print('Neighbors list saved to',uniprot,'neighbors.csv')
        commonDegs=makeCollapsedDeg(nNodes,deg)#it's still uncollapsed, i know, ill change it
        makeFile(commonDegs,uniprot)
        hist,x,y=get_histo(deg)
        lx,ly=computeLog(x,y)
        plotter2(x,y,lx,ly,uniprot)

    if printit == '3': #asks for uniprot id and list of list of edges
        uniprot=input('type id here: ')
        nNodes = neighbors(uniprot,edgeList)
        nNodes2=neighbor2 (nNodes,edgeList)
        collapsed = False
        print("primary neighbors")
        print(nNodes)
        print (len(nNodes))
        print("secondary neighbors")
        print (len(nNodes2))
    if printit == '4':
        '''
        TODO
            []make file that shows what IDs the common names correspond to
        '''
        collapsed = True
        dictionary=importdictionary() #creates a common name dictionary from an attached reference file
        collapsedTupleSet, skipped = collapseInteractome (dictionary,edgeList)
        collapsedNodeSet, skipped2 = collapseNodes (dictionary,nodeSet)
        print('\n Collapsing the interactome...\n',skipped,'edges skipped.',skipped2,'nodes skipped.')
        print('# of edges in collapsed interactome: ',len(collapsedTupleSet) )
        print('# of nodes collapsed interactome: ',len(collapsedNodeSet),'\n Histogram saved to .pdf.' )
        deg=getDegree (collapsedTupleSet,collapsedNodeSet)
        hist,x,y=get_histo(deg)
        lx,ly=computeLog(x,y)
        plotter3(x,y,lx,ly)
#        commonNames=useDictionary(dictionary,nNodes,deg)
#        for item in commonNames: #print a line from a list of strings rather than the list print(item)
#       makeFile(commonNames,uniprot)
    if printit == '5':
        collapsed = True
        commonName=input('type common name here: ')
        dictionary=importdictionary() #creates a common name dictionary from an attached reference file
        collapsedTupleSet, skipped = collapseInteractome (dictionary,edgeList)
        collapsedNodeSet, skipped2 = collapseNodes (dictionary,nodeSet)
        nNodes = neighbors(commonName,collapsedTupleSet)
        #edgeSub = subsetEdges(uniprot,edgeList,nNodes)
        '''
        print("primary neighbors")
        print(nNodes)
        print (len(nNodes))
        print (type(nNodes))
        '''
        print(skipped,' skipped.')
        print('# of tuples: ',len(collapsedTupleSet) )
        print(skipped2,' skipped.')
        print('# of nodes: ',len(collapsedNodeSet) )
        print('Neighbors list saved to',commonName,'neighbors.csv')
        deg=getSubDegree (nNodes,collapsedTupleSet,commonName,collapsed)
        hist,x,y=get_histo(deg)
        lx,ly=computeLog(x,y)
        plotter4(x,y,lx,ly,commonName)
        commonDegs=makeCollapsedDeg(nNodes,deg)
        makeFile(commonDegs,commonName)
        #print(deg)
        #tupleSettoLoL(collapsedTupleSet)
        return

def makeCollapsedDeg (nNodes,deg):
    #makes a list of strings containing uniprot, common name, and degree then a new line
    commonDegs=[]
    for node in nNodes:
        commonDegs=commonDegs+[node+ ','+ str(deg[node])+'\n']
    return commonDegs

def makeFile (commonNames,uniprot):
    '''
    TODO:
        have it automatically pick between Uniprot ID and common name
    '''
    file= open(uniprot+" neighbors.csv", "w")
    file.write ('Uniprot ID/Common Name, Degree\n')#wirtes the header
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
    fName = 'nodes-uniprot.csv'
    dictionary={}
    with open(fName, newline='') as cSVFile:
        reader = csv.reader(cSVFile,dialect="excel-tab")
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
    return nNodes

'''
These plotters need to go in the config file
'''

def plotter1(x,y,lx,ly):#plots for whole histogram


    plt.figure(1)
    plt.ylim([-80,1750])
    plt.xlim([-80,8000])
    plt.xlabel('Degree of nodes')
    plt.ylabel('Number of nodes')
    plt.scatter(x,y,marker='.')
    plt.savefig('histogram1.pdf', bbox_inches='tight')

    plt.figure(2)
    plt.ylim([0,1750])
    plt.xlim([0,26])
    plt.scatter(x,y,marker='.')
    plt.xlabel('Degree of nodes')
    plt.ylabel('Number of nodes')
    plt.savefig('histogram2.pdf', bbox_inches='tight')

    plt.figure(3)
    plt.ylim([-0.5,8])
    plt.xlim([-0.5,9])
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
    plt.xlim([-80,8000])
    plt.ylim([-80,1750])
    plt.xlabel('Degree of nodes')
    plt.ylabel('Number of nodes')
    plt.scatter(x,y,marker='.')
    plt.savefig('collapsedhistogram1.pdf', bbox_inches='tight')

    plt.figure(2)
    plt.ylim([0,1750])
    plt.xlim([0,26])
    plt.scatter(x,y,marker='.')
    plt.xlabel('Degree of nodes')
    plt.ylabel('Number of nodes')
    plt.savefig('collapsedhistogram2.pdf', bbox_inches='tight')

    plt.figure(3)
    plt.ylim([-0.5,8])
    plt.xlim([-0.5,9])
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

def getDegree (edgeList,nodeSet):#gather nodes by number of edges
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
def getSubDegree (nNodes,edgeList,proteinName,collapsed):#gather nodes by number of edges
    """
    pseudocode:
    for {X} from nNodes
    degree = find all lists in edgeLists where {X}
    d['X']= degree

    """
    print(proteinName)
    deg = {}
    for item in nNodes:
        deg[item]=0 #adds key and sets value to zero, key value pair
    for row in edgeList:
        if row[0] in nNodes:
            deg[row[0]]+=1 #increase value by one if a given nNodes key is row 0 in edgeList
        if row[1] in nNodes:
            deg[row[1]]+=1 #increase value by one if a given nNodes key is row 1 in edgeList
        if collapsed == True and (row[1],row[0]) in edgeList and row[0] == proteinName:
            print('Be aware,',proteinName,'is neighbors with itself!')#this breaks option 1
    return deg
main()
