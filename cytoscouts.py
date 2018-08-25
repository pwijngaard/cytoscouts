# -*- coding: utf-8 -*-
"""
@author: Petra Wijngaard
latest version 8 24 2018

TODO
[] make it not crash when given invalid inputs on option 1 and 4
[] enable a config file with include configparser
    options to include:
        [X]default interactome
        []remove header
        histogram variables
            []1
            []2
            []3
            []4
        []reference dictionary
"""
version = 'v0.6.5'
import configparser
import csv
import math
import matplotlib.pyplot as plt
import os.path
import time #testing purposes remove from final

'''
Default Configuration Section
TODO
expand help section
[]expand histogram section
'''
config = configparser.ConfigParser(allow_no_value=True)

# Setting up the default configuration file

config.add_section('HELP')
config.set('HELP', '# comment here')

config['INTERACTOME'] = {
    'default_interactome' : 'e.csv',
    'skip_header' : '1',
    'csv_dialect' : 'excel-tab',
}

config['REFERENCE'] = {
    'reference_file' : 'nodes-uniprot.csv',
    'skip_header' : '1',
    'csv_dialect' : 'excel-tab',
}

config['HISTOGRAM'] = {
    '(1-1)':'(1-1)',
    'print_figure1-1' : '1',
    'figure1-1_name' : 'uncollapsed_histogram_1.pdf',
    'figure1-1_autoscale' : '1',
    'figure1-1_xlim_left' : '-50',
    'figure1-1_xlim_right' : '8000',
    'figure1-1_ylim_bottom' : '-50',
    'figure1-1_ylim_top' : '1750',
    'figure1-1_xlabel' : 'Degree of nodes',
    'figure1-1_ylabel' : 'Number of nodes',
    '(1-2)':'(1-2)',
    'print_figure1-2' : '1',
    'figure1-2_name' : 'uncollapsed_histogram_2.pdf',
    'figure1-2_autoscale' : '1 #excludes xlims',
    'figure1-2_xlim_left' : '0',
    'figure1-2_xlim_right' : '25',
    'figure1-2_ylim_bottom' : '-50',
    'figure1-2_ylim_top' : '1750',
    'figure1-2_xlabel' : 'Degree of nodes',
    'figure1-2_ylabel' : 'Number of nodes',
    '(1-3)':'(1-3)',
    'print_figure1-3' : '1',
    'figure1-3_name' : 'uncollapsed_histogram_3.pdf',
    'figure1-3_autoscale' : '1',
    'figure1-3_xlim_left' : '-0.5',
    'figure1-3_xlim_right' : '9',
    'figure1-3_ylim_bottom' : '-0.5',
    'figure1-3_ylim_top' : '9',
    'figure1-3_xlabel' : 'log (Degree of nodes)',
    'figure1-3_ylabel' : 'log (Number of nodes)',
    '(2-1)':'(2-1)',
    '(2-2)':'(2-2)',
    '(2-3)':'(2-3)',
    '(3-1)':'(3-1)',
    '(3-2)':'(3-2)',
    '(3-3)':'(3-3)',

}


if os.path.isfile('cytoscouts_config.ini') != True:
    # check to see if there's a config file already
    print('No cytoscouts_config.ini file found, \
    so one was written with default settings.')
    with open('cytoscouts_config.ini', 'w') as configfile:
        # if there isnt write one to file
        config.write(configfile)
config.read('cytoscouts_config.ini')

'''
Functions Section
'''


def main():
    '''
    Displays banner, takes interactome, provides summary statistics
    and calls options function for further analysis
    '''
    print('*✭˚･ﾟ✧*･ﾟ   it\'s cytoscouts   ', version, '* ✭˚･ﾟ✧*･ﾟ*')
    edgeList, nodeSet = checkDefaultInteractome()
    # checks for a default interactome and if there isnt one asks for one
    print('\nThis interactome has', (len(edgeList)),\
     'edges and contains', len(nodeSet), 'nodes.')
    printoptions(edgeList, nodeSet)  # the options menu
    return


def checkDefaultInteractome():
    if config['INTERACTOME']['default_interactome'] == '0':
        # checks for a default interactome in config.ini
        print('No default interactome set.\
         To set one, edit cytoscouts_config.ini .')
        edgeList, nodeSet = importCSV()
        # asks for an interactome if none is found
    else:
        # if there is an interactome asks if you want to keep using it
        print('Default interactome is set to',\
         config['INTERACTOME']['default_interactome'],
              '\n Press 1 to continue using it.\
              \n Press 0 to enter a new one.\
              \n You can change the default interactome in\
              cytoscouts_config.ini')
        while True:  # loop in case of bad inputs
            chooseDefault = input()
            if chooseDefault == '1':
                edgeList, nodeSet = defaultCSV()
                break
            elif chooseDefault == '0':
                edgeList, nodeSet = importCSV()  # asks for an interactome
                break
            else:
                print('Invalid Choice')

    return edgeList, nodeSet


def importCSV():  # get the CSV
    '''
    TO DO
        [X] program doesnt crash if not supplied an ending
        [X]accept files with .txt and .tsv endings
        [x]enable skip header <=================================
        [x]config for header and dialect
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
                if config['INTERACTOME']['skip_header'] == '1':
                    next(cSVFile)
                reader = csv.reader(cSVFile,\
                 dialect=config['INTERACTOME']['csv_dialect'])
                for r in reader:
                    edgeList.append([r[0], r[1]])  # pair of nodes, aka an edge
                    nodeSet.add(r[0])  # node 1
                    nodeSet.add(r[1])  # node2

            break

        except OSError:
            print("Could not read file.\
             Did you remember the extension? Invalid file:", fileName)

    # print(edgeList[0:10])#shows us some edges
    return edgeList, nodeSet  # saves these two variables


def defaultCSV():  # get the CSV
    '''
    TO DO:
        [x]enable skip header
        []count number of columns

    '''

    nodeSet = set()
    edgeList = []
    while True:
        try:
            fileName = config['INTERACTOME']['default_interactome']
            with open(fileName, newline='') as cSVFile:
                if config['INTERACTOME']['skip_header'] == '1':
                    next(cSVFile)
                reader = csv.reader(cSVFile,\
                 dialect=config['INTERACTOME']['csv_dialect'])
                for r in reader:
                    edgeList.append([r[0], r[1]])  # pair of nodes, aka an edge
                    nodeSet.add(r[0])  # node 1
                    nodeSet.add(r[1])  # node2

            break

        except OSError:
            print(
                'Could not read default file, \
                please enter a valid filename for now\
                 and change cytoscouts_config.ini when you have the chance. \
                 Invalid file: ',fileName)
        edgeList, nodeSet = importCSV()  # defaults to manual entry

    return edgeList, nodeSet  # saves these two variables


def printoptions(edgeList, nodeSet):
    printIt = input(
        '\nPress:\
         \n 1 to print histograms of the uncollapsed interactome,\
         \n 2 to get neighbors of an ID, \
         \n 3 to collapse the interactome, \
         \n 4 to input common name node for collapsed interactome \
         \n 99 (DEPRECATED) to get secondary neighbors of an ID, \
         \n otherwise any key to exit: ')

    if printIt == '1':
        t0 = time.time()
        deg = getDegree(edgeList, nodeSet)  # calculates the degree
        t1 = time.time()
        degtime = t1-t0
        print('deg took', degtime)
        t0=time.time()
        hist, x, y = getHisto(deg)  # makes a histogram
        t1=time.time()
        histotime = t1-t0
        print('getHisto took', histotime)
        t0=time.time()
        lx, ly = computeLog(x, y)  # log transformation of x y values
        t1=time.time()
        logtime = t1-t0
        print('computeLog took', logtime)
        plotter1(x, y, lx, ly)  # makes it a plot

    if printIt == '2':  # asks for uniprot id and list of list of edges
        '''
        [x] rename degList to make it make more sense
        [x] validate inputs
        '''
        collapsed = False
        while True:  # a loop to ensure the inputted ID is in the interactome
            uniprot = input('Enter ID here: ')
            if uniprot in nodeSet:
                break
            print('Error: ', uniprot, 'is not in the interactome. \
            Enter another ID.')

        nNodes = neighbors(uniprot, edgeList)

        # edgeSub = subsetEdges(uniprot,edgeList,nNodes)
        # print(nNodes)
        # print (len(nNodes))
        # print (type(nNodes))
        deg = getSubDegree(nNodes, edgeList, uniprot, collapsed)
        degList = makeDegList(nNodes, deg)
        makeFile(degList, uniprot)
        print('Neighbors list saved to', uniprot, 'neighbors.csv')

        hist, x, y = getHisto(deg)
        lx, ly = computeLog(x, y)
        plotter2(x, y, lx, ly, uniprot)

    if printIt == '3':
        '''
        TODO
            []make file that shows what IDs the common names correspond to

        '''
        collapsed = True
        dictionary = importDictionary()
        # creates a common name dictionary from an attached reference file
        collapsedTupleSet, skipped = collapseInteractome(dictionary, edgeList)
        collapsedNodeSet, skipped2 = collapseNodes(dictionary, nodeSet)
        print('\n Collapsing the interactome...\n', skipped, 'edges skipped.', \
        skipped2, 'nodes skipped.')
        print('# of edges in collapsed interactome: ', len(collapsedTupleSet))
        print('# of nodes collapsed interactome: ', len(collapsedNodeSet), \
        '\n Histogram saved to .pdf.')
        deg = getDegree(collapsedTupleSet, collapsedNodeSet)
        hist, x, y = getHisto(deg)
        lx, ly = computeLog(x, y)
        plotter3(x, y, lx, ly)

    if printIt == '4':
        '''
        [x]make it so it doesnt crash when fed wrong inputs
        '''
        collapsed = True
        dictionary = importDictionary()
        # creates a common name dictionary from an attached reference file
        collapsedTupleSet, skipped = collapseInteractome(dictionary, edgeList)
        collapsedNodeSet, skipped2 = collapseNodes(dictionary, nodeSet)
        print(skipped, 'tuples skipped.')
        print('# of tuples: ', len(collapsedTupleSet))
        print(skipped2, 'nodes skipped.')
        print('# of nodes: ', len(collapsedNodeSet))
        while True:
            commonName = input('Enter common name here: ')
            if commonName in collapsedNodeSet:
                break
            print('Error: ', commonName, 'is not in the interactome. \
            Enter another name.')
        # edgeSub = subsetEdges(uniprot,edgeList,nNodes)

        nNodes = neighbors(commonName, collapsedTupleSet)
        deg = getSubDegree(nNodes, collapsedTupleSet, commonName, collapsed)
        hist, x, y = getHisto(deg)
        lx, ly = computeLog(x, y)
        plotter4(x, y, lx, ly, commonName)
        degList = makeDegList(nNodes, deg)
        makeFile(degList, commonName)
        print('Neighbors list saved to', commonName, 'neighbors.csv')
        # print(deg)
        # tupleSettoLoL(collapsedTupleSet)

        if printIt == '99':  # asks for uniprot id and list of list of edges
            collapsed = False
            while True:  # a loop to ensure the inputted ID is in the interactome
                uniprot = input('Enter ID here: ')
                if uniprot in nodeSet:
                    break
                print('Error: ', uniprot, 'is not in the interactome. \
                Enter another ID.')
            nNodes = neighbors(uniprot, edgeList)
            nNodes2 = neighbor2(nNodes, edgeList)
            print("primary neighbors")
            print(nNodes)
            print(len(nNodes))
            print("secondary neighbors")
            print(len(nNodes2))


        return


def getDegree(edgeList, nodeSet):  # gather nodes by number of edges
    """
    pseudocode:
    for {X} from nodeSet
    degree = find all lists in edgeLists where {X}
    d['X']= degree

    """
    deg = {}
    for item in nodeSet:
        deg[item] = 0
    for row in edgeList:
        deg[row[0]] += 1
        deg[row[1]] += 1
    return deg


def neighbors(uniprot, edgeList):
    nNodes = set()
    for row in edgeList:
        # a for loop in which if a row is the uniprot id,
        # then the other row is added to a set
        if row[0] == uniprot:
            nNodes.add(row[1])
        if row[1] == uniprot:
            nNodes.add(row[0])
    return nNodes


def getSubDegree(nNodes, edgeList, proteinName, collapsed):
    # gather nodes by number of edges
    """
    pseudocode:
    for {X} from nNodes
    degree = find all lists in edgeLists where {X}
    d['X']= degree

    """
    deg = {}
    for item in nNodes:
        deg[item] = 0
        # adds key and sets value to zero, key value pair
    for row in edgeList:
        if row[0] in nNodes:
            deg[row[0]] += 1
            # increase value by one if a given nNodes key is row 0 in edgeList
        if row[1] in nNodes:
            deg[row[1]] += 1
            # increase value by one if a given nNodes key is row 1 in edgeList
        if collapsed == True \
        and (row[1], row[0]) in edgeList and row[0] == proteinName:
            print('Be aware,', proteinName, 'is neighbors with itself!')
    return deg


def makeDegList(nNodes, deg):
    # makes a list of strings containing uniprot,
    # common name and degree then a new line
    degList = []
    for node in nNodes:
        degList = degList + [node + ',' + str(deg[node]) + '\n']
    return degList


def makeFile(commonNames, uniprot):
    '''
    TODO:
        have it automatically pick between Uniprot ID and common name
    '''
    file = open(uniprot + " neighbors.csv", "w")
    file.write('Uniprot ID/Common Name, Degree\n')  # wirtes the header
    for row in commonNames:  # wites the items from a list of strings
        file.write(row)
    file.close()
    return ()


'''
this one makes it as a list
def useDictionary (dictionary,nNodes,deg):
    commonNames=[]
    for key in dictionary:
            for node in nNodes:
                if key == node:
                    commonNames=commonNames\
                    +[node]+[dictionary[node]]+[deg[key]]+[';']
    return commonNames
'''


def collaspedDegs(nNodes, deg):
    return


def useDictionary(dictionary, nNodes, deg):
    # makes a list of strings containing uniprot, common name
    # and degree then a new line
    commonNames = []
    for key in dictionary:
        for node in nNodes:
            if key == node:
                commonNames = commonNames \
                + [node + ',' + dictionary[node] + ',' + str(deg[key]) + '\n']
    return commonNames


def collapseInteractome(dictionary, edgeList):
    collapsedTupleSet = set()
    skipped = 0
    for row in edgeList:
        if row[0] in dictionary and row[1] in dictionary:
            if (dictionary[row[1]], dictionary[row[0]]) not in collapsedTupleSet:
                collapsedTupleSet.add(tuple((dictionary[row[0]], dictionary[row[1]])))
        else:
            skipped += 1
    return collapsedTupleSet, skipped


def collapseNodes(dictionary, nodeSet):
    collapsedNodeSet = set()
    skipped2 = 0
    for key in nodeSet:
        if key in dictionary:
            collapsedNodeSet.add(dictionary[key])
        else:
            skipped2 += 1
    return collapsedNodeSet, skipped2


# def tupleSettoLoL(collapsedTupleSet):
#a function to turn the set of tuples back into a list of lists
#so it can be processed by getDegree
#    tuplesList=[]
#    tuplesLoL=[]
#    for ituple in collapsedTupleSet:
#        for value in ituple:
#            tuplesList+=[value] #make a list of every value in each tuple
#    for i in range(len(tuplesList)):
#turn that list into a list of lists pairing every value in the list
#        tuplesLoL+=[tuplesList[i:i+1]]
#currently only makes a list of values not a list of lists
#    print(tuplesLoL)
#    return
#
def importDictionary():  # get the TSV
    '''
    TODO
    []Apply the config file properties here
        [X] Header
        [X] ref name
        [X] dialect
        [ ] reference columns
    '''
    fName = config['REFERENCE']['reference_file']
    dictionary = {}
    with open(fName, newline='') as cSVFile:
        reader = csv.reader(cSVFile, dialect=config['REFERENCE']['csv_dialect'])
        if config['REFERENCE']['skip_header'] == '1':
            next(cSVFile)
        for r in reader:
            dictionary[r[0]] = r[2]
    # makes a dictionary from index 0 as the key and index 2 as the value
    return dictionary


def neighbor2(nNodes, edgeList):
    nNodes2 = set()
    # if something frod edgeList matches something in nNodes,put it in nNodes2
    for row in edgeList:
        for item in nNodes:
            if row[0] == item:
                nNodes2.add(row[1])
            if row[1] == item:
                nNodes2.add(row[0])
    return nNodes2


'''
These plotters need to go in the config file
'''


def plotter1(x, y, lx, ly):

    if config['HISTOGRAM']['print_figure1-1'] == '1':
        plt.figure(1)
        if config['HISTOGRAM']['figure1-1_autoscale'] != '1':
            plt.xlim([int(config['HISTOGRAM']['figure1-1_xlim_left']),int(config['HISTOGRAM']['figure1-1_xlim_right'])])
            plt.xlim([int(config['HISTOGRAM']['figure1-1_ylim_bottom']),int(config['HISTOGRAM']['figure1-1_ylim_top'])])
        plt.xlabel(config['HISTOGRAM']['figure1-1_xlabel'])
        plt.ylabel(config['HISTOGRAM']['figure1-1_ylabel'])
        plt.scatter(x, y, marker='.')
        plt.savefig(config['HISTOGRAM']['figure1-1_name'], bbox_inches='tight')
        print(config['HISTOGRAM']['figure1-1_name'],"was printed to file.")

    if config['HISTOGRAM']['print_figure1-2'] == '1':
        plt.figure(2)
        plt.xlim([int(config['HISTOGRAM']['figure1-2_xlim_left']),int(config['HISTOGRAM']['figure1-2_xlim_right'])])
        if config['HISTOGRAM']['figure1-2_autoscale'] != '1':
            plt.xlim([int(config['HISTOGRAM']['figure1-2_ylim_bottom']),int(config['HISTOGRAM']['figure1-2_ylim_top'])])
        plt.xlabel(config['HISTOGRAM']['figure1-2_xlabel'])
        plt.ylabel(config['HISTOGRAM']['figure1-2_ylabel'])
        plt.scatter(x, y, marker='.')
        plt.savefig(config['HISTOGRAM']['figure1-2_name'], bbox_inches='tight')
        print(config['HISTOGRAM']['figure1-2_name'],"was printed to file.")

    if config['HISTOGRAM']['print_figure1-3'] == '1':
        plt.figure(3)
        if config['HISTOGRAM']['figure1-3_autoscale'] != '1':
            plt.xlim([int(config['HISTOGRAM']['figure1-3_xlim_left']),int(config['HISTOGRAM']['figure1-3_xlim_right'])])
            plt.xlim([int(config['HISTOGRAM']['figure1-3_ylim_bottom']),int(config['HISTOGRAM']['figure1-3_ylim_top'])])
        plt.xlabel(config['HISTOGRAM']['figure1-3_xlabel'])
        plt.ylabel(config['HISTOGRAM']['figure1-3_ylabel'])
        plt.scatter(lx, ly, marker='.')
        plt.savefig(config['HISTOGRAM']['figure1-3_name'], bbox_inches='tight')
        print(config['HISTOGRAM']['figure1-3_name'],"was printed to file.")

def plotter2(x, y, lx, ly, uniprot):  # plots for uniprot id of choice
    plt.figure(1)
    plt.ylim([1, 21])
    plt.xlabel('Degree of nodes')
    plt.ylabel('Number of nodes')
    plt.scatter(x, y)
    plt.yticks([0, 1, 2, 3, 4, 5, 10, 15, 20])
    plt.savefig(uniprot + '_1.pdf', bbox_inches='tight')

    plt.figure(2)
    plt.xlim([0, 2000])
    plt.ylim([1, 6])
    plt.scatter(x, y, marker='.')
    plt.xlabel('Degree of nodes')
    plt.ylabel('Number of nodes')
    plt.yticks([0, 1, 2, 3, 4, 5])
    plt.savefig(uniprot + '_2.pdf', bbox_inches='tight')

    plt.figure(3)
    plt.xlim([0, 10])
    plt.xlabel('log(Degree of nodes)')
    plt.ylabel('log(Number of nodes)')
    plt.scatter(lx, ly, marker='.')
    plt.savefig(uniprot + '_3.pdf', bbox_inches='tight')

    return


def plotter3(x, y, lx, ly):  # plots for whole histogram

    plt.figure(1)
    plt.xlim([-80, 8000])
    plt.ylim([-80, 1750])
    plt.xlabel('Degree of nodes')
    plt.ylabel('Number of nodes')
    plt.scatter(x, y, marker='.')
    plt.savefig('collapsedhistogram1.pdf', bbox_inches='tight')

    plt.figure(2)
    plt.ylim([0, 1750])
    plt.xlim([0, 26])
    plt.scatter(x, y, marker='.')
    plt.xlabel('Degree of nodes')
    plt.ylabel('Number of nodes')
    plt.savefig('collapsedhistogram2.pdf', bbox_inches='tight')

    plt.figure(3)
    plt.ylim([-0.5, 8])
    plt.xlim([-0.5, 9])
    plt.xlabel('log(Degree of nodes)')
    plt.ylabel('log(Number of nodes)')
    plt.scatter(lx, ly, marker='.')
    plt.savefig('collapsedhistogram3.pdf', bbox_inches='tight')


def plotter4(x, y, lx, ly, commonName):  # plots for common name of choice
    plt.figure(1)
    plt.yticks([0, 1, 2, 3])
    plt.xlabel('Degree of nodes')
    plt.ylabel('Number of nodes')
    plt.scatter(x, y)
    plt.savefig(commonName + '_1.pdf', bbox_inches='tight')

    plt.figure(2)
    plt.xlim([0, 1500])
    plt.scatter(x, y, marker='.')
    plt.xlabel('Degree of nodes')
    plt.ylabel('Number of nodes')
    plt.yticks([0, 1, 2, 3])
    plt.savefig(commonName + '_2.pdf', bbox_inches='tight')

    plt.figure(3)
    plt.xlim([0, 10])
    plt.xlabel('log(Degree of nodes)')
    plt.ylabel('log(Number of nodes)')
    plt.scatter(lx, ly, marker='.')
    plt.savefig(commonName + '_3.pdf', bbox_inches='tight')


def computeLog(x, y):
    lx = []
    ly = []
    for i in range(len(x)):
        if y[i] > 0:
            lx.append(math.log(x[i]))
            ly.append(math.log(y[i]))
    return (lx, ly)


def getHisto(deg):  # gather nodes by number of edges
    """
THIS NEEDS TO BE FASTER
for histogram use the same function in a different order
d2 starts empty and then for item in nodelist d= deg[item] is d a key in d2?
if is then ratchet up the counter
if not then put in a new pair
"""
    hist = {}  # empty dictionary
    key = 1  # the first x value in our histogram
    maxdeg = max(deg.values())  # the last x value in the histogram
    x = []  # list for x value in histogram
    y = []  # list for y value in histogram
    while key <= maxdeg:  # while we havent reached the end of the dictionary
        val = 0  # include edge counts with no nodes
        for node in deg.keys():  # take the node !! this is the time bottleneck
            if deg[node] == key:  # if the node has key number of edges
                val += 1  # add one to the y axis for that edge number
        hist[key] = val  # putting that number that into the dictionary
        x.append(key)  # building the x value list
        y.append(val)  # building the y value list
        key += 1  # move to the next x value in the histogram
    return hist, x, y


def subsetEdges(uniprot, edgeList, nNodes):
    # to get the subset of edges for the histogram of neighbors of the PoI
    # a list of edges containing the neighbor nodes of uniprot
    edgeSub = []
    for row in edgeList:
        for node in nNodes:
            # a for loop in which if a row is the uniprot id,
            # then the the row is added to a list, edgeSub
            if row[0] == node:
                edgeSub.append([row[0], row[1]])
            if row[1] == node:
                edgeSub.append([row[0], row[1]])
    return edgeSub

def slowGetHisto(deg):  # gather nodes by number of edges
    """
THIS NEEDS TO BE FASTER
for histogram use the same function in a different order
d2 starts empty and then for item in nodelist d= deg[item] is d a key in d2?
if is then ratchet up the counter
if not then put in a new pair
"""
    hist = {}  # empty dictionary
    key = 1  # the first x value in our histogram
    maxdeg = max(deg.values())  # the last x value in the histogram
    x = []  # list for x value in histogram
    y = []  # list for y value in histogram
    while key <= maxdeg:  # while we havent reached the end of the dictionary
        val = 0  # include edge counts with no nodes
        for node in deg.keys():  # take the node !! this is the time bottleneck
            if deg[node] == key:  # if the node has key number of edges
                val += 1  # add one to the y axis for that edge number
        hist[key] = val  # putting that number that into the dictionary
        x.append(key)  # building the x value list
        y.append(val)  # building the y value list
        key += 1  # move to the next x value in the histogram
    return hist, x, y
main()
