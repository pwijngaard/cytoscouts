# -*- coding: utf-8 -*-
"""
author: Petra Wijngaard
latest version 8 27 2018

TODO
[x] make it not crash when given invalid inputs on option 1 and 4
[] enable a config file with include configparser
    options to include:
        [X]default interactome
        [x]remove header
        histogram variables
            [x]1
            []2
                []customizable pdf names
            [X]3
            []4
                []customizable pdf names

        [x]reference refDict
        [x] select columns
[] make folders for  results to go in
"""


import configparser
import csv
import matplotlib.pyplot as plt
import os.path
version = 'v0.8.1'


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
    'default_interactome': 'interactome-uniprot.txt',
    'csv_dialect': 'excel-tab',
    'skip_header': '1',
    'use_evidence': '1',
    'column_accession_id_1': '0',
    'column_accession_id_2': '1',
    'column_evidence': '4',
}

config['REFERENCE'] = {
    'reference_file': 'nodes-uniprot.csv',
    'csv_dialect': 'excel-tab',
    'skip_header': '1',
    'column_ref_accession_id': '0',
    'column_ref_common_name': '2',

}

config['HISTOGRAM-1'] = {
    '(1-0)': '(1-0)',
    'save_histogram_csv': '0',
    'histogram_csv_name': 'uncollapsed_interactome',
    '(1-1)': '(1-1)',
    'print_figure1-1': '1',
    'figure1-1_name': 'uncollapsed_histogram_1',
    'figure1-1_autoscale': '1',
    'figure1-1_xlim_left': '-50',
    'figure1-1_xlim_right': '8000',
    'figure1-1_ylim_bottom': '-50',
    'figure1-1_ylim_top': '1750',
    'figure1-1_xlabel': 'Degree of nodes',
    'figure1-1_ylabel': 'Number of nodes',
    '(1-2)': '(1-2)',
    'print_figure1-2': '1',
    'figure1-2_name': 'uncollapsed_histogram_2',
    'figure1-2_autoscale': '0',
    'figure1-2_xlim_left': '0',
    'figure1-2_xlim_right': '25',
    'figure1-2_ylim_bottom': '-50',
    'figure1-2_ylim_top': '1750',
    'figure1-2_xlabel': 'Degree of nodes',
    'figure1-2_ylabel': 'Number of nodes',
    '(1-3)': '(1-3)',
    'print_figure1-3': '1',
    'figure1-3_name': 'uncollapsed_histogram_3',
    'figure1-3_autoscale': '1',
    'figure1-3_xlim_left': '-0.5',
    'figure1-3_xlim_right': '9',
    'figure1-3_ylim_bottom': '-0.5',
    'figure1-3_ylim_top': '9',
    'figure1-3_xlabel': 'log (Degree of nodes)',
    'figure1-3_ylabel': 'log (Number of nodes)',
    }

config['HISTOGRAM-2'] = {
    '(2-1)': '(2-1)',
    'print_figure2-1': '1',
    'figure2-1_autoscale': '1',
    'figure2-1_xlim_left': '-50',
    'figure2-1_xlim_right': '8000',
    'figure2-1_ylim_bottom': '-50',
    'figure2-1_ylim_top': '1750',
    'figure2-1_xlabel': 'Degree of nodes',
    'figure2-1_ylabel': 'Number of nodes',
    '(2-2)': '(2-2)',
    'print_figure2-2': '1',
    'figure2-2_autoscale': '0',
    'figure2-2_xlim_left': '-50',
    'figure2-2_xlim_right': '25',
    'figure2-2_ylim_bottom': '-50',
    'figure2-2_ylim_top': '1750',
    'figure2-2_xlabel': 'Degree of nodes',
    'figure2-2_ylabel': 'Number of nodes',
    '(2-3)': '(2-3)',
    'print_figure2-3': '1',
    'figure2-3_autoscale': '1',
    'figure2-3_xlim_left': '-0.5',
    'figure2-3_xlim_right': '9',
    'figure2-3_ylim_bottom': '-0.5',
    'figure2-3_ylim_top': '9',
    'figure2-3_xlabel': 'log (Degree of nodes)',
    'figure2-3_ylabel': 'log (Number of nodes)',
    }

config['HISTOGRAM-3'] = {
    '(3-0)': '(3-0)',
    'save_histogram_csv': '0',
    'histogram_csv_name': 'collapsed_interactome',
    '(3-1)': '(3-1)',
    'print_figure3-1': '1',
    'figure3-1_name': 'collapsed_histogram_1',
    'figure3-1_autoscale': '1',
    'figure3-1_xlim_left': '-50',
    'figure3-1_xlim_right': '8000',
    'figure3-1_ylim_bottom': '-50',
    'figure3-1_ylim_top': '1750',
    'figure3-1_xlabel': 'Degree of nodes',
    'figure3-1_ylabel': 'Number of nodes',
    '(3-2)': '(3-2)',
    'print_figure3-2': '1',
    'figure3-2_name': 'collapsed_histogram_2',
    'figure3-2_autoscale': '0',
    'figure3-2_xlim_left': '0',
    'figure3-2_xlim_right': '25',
    'figure3-2_ylim_bottom': '-50',
    'figure3-2_ylim_top': '1750',
    'figure3-2_xlabel': 'Degree of nodes',
    'figure3-2_ylabel': 'Number of nodes',
    '(3-3)': '(3-3)',
    'print_figure3-3': '1',
    'figure3-3_name': 'collapsed_histogram_3',
    'figure3-3_autoscale': '1',
    'figure3-3_xlim_left': '-50',
    'figure3-3_xlim_right': '8000',
    'figure3-3_ylim_bottom': '-50',
    'figure3-3_ylim_top': '1750',
    'figure3-3_xlabel': 'log (Degree of nodes)',
    'figure3-3_ylabel': 'log (Number of nodes)',
    }

config['HISTOGRAM-4'] = {
    '(4-1)': '(4-1)',
    'print_figure4-1': '1',
    'figure4-1_autoscale': '1',
    'figure4-1_xlim_left': '-50',
    'figure4-1_xlim_right': '8000',
    'figure4-1_ylim_bottom': '-50',
    'figure4-1_ylim_top': '1750',
    'figure4-1_xlabel': 'Degree of nodes',
    'figure4-1_ylabel': 'Number of nodes',
    '(4-2)': '(4-2)',
    'print_figure4-2': '1',
    'figure4-2_autoscale': '0',
    'figure4-2_xlim_left': '-5',
    'figure4-2_xlim_right': '25',
    'figure4-2_ylim_bottom': '-50',
    'figure4-2_ylim_top': '1750',
    'figure4-2_xlabel': 'Degree of nodes',
    'figure4-2_ylabel': 'Number of nodes',
    '(4-3)': '(4-3)',
    'print_figure4-3': '1',
    'figure4-3_autoscale': '1',
    'figure4-3_xlim_left': '-0.5',
    'figure4-3_xlim_right': '9',
    'figure4-3_ylim_bottom': '-0.5',
    'figure4-3_ylim_top': '9',
    'figure4-3_xlabel': 'log (Degree of nodes)',
    'figure4-3_ylabel': 'log (Number of nodes)',
    }


if not os.path.isfile('cytoscouts_config.ini'):
    # check to see if there's a config file already
    print('No cytoscouts_config.ini file found, '
          + 'so one was written with default settings.')
    with open('cytoscouts_config.ini', 'w') as configfile:
        # if there isnt write one to file
        config.write(configfile)
config.read('cytoscouts_config.ini')


'''
Functions Section
'''


def main():
    print('*✭˚･ﾟ✧*･ﾟ   it\'s cytoscouts   ', version, '* ✭˚･ﾟ✧*･ﾟ*')
    edgeList, nodeSet, fileName = checkDefaultInteractome()
    # checks for a default interactome and if there isnt one asks for one
    print('\nThis interactome has', (len(edgeList)),
          'edges and contains', len(nodeSet), 'nodes.')
    fileName = cleanFileName(fileName)
    printOptions(edgeList, nodeSet, fileName)  # main menu
    return


def checkDefaultInteractome():
    if config['INTERACTOME']['default_interactome'] == '0':
        # checks for a default interactome in config.ini
        print('No default interactome set.'
              + 'To set one, edit cytoscouts_config.ini .')
        edgeList, nodeSet, fileName = importCSV()
        # asks for an interactome if none is found
    else:
        # if there is an interactome asks if you want to keep using it
        print('Default interactome is set to',
              config['INTERACTOME']['default_interactome'],
              '\n Press 1 to continue using it.\
               \n Press 0 to enter a new one.\
               \n You can change the default interactome in '
              + 'cytoscouts_config.ini')
        while True:
            chooseDefault = input()
            if chooseDefault == '1':
                edgeList, nodeSet, fileName = defaultCSV()
                break
            elif chooseDefault == '0':
                edgeList, nodeSet, fileName = importCSV()
                break
            else:
                print('Invalid Choice')

    return edgeList, nodeSet, fileName


def importCSV():  # get the CSV
    '''
    We know edgeList is the right stuff
    TODO
        [X] program doesnt crash if not supplied an ending
        [X]accept files with .txt and .tsv endings
        [x]enable skip header <=================================
        [x]config for header and dialect
        []column select
        [x]save interactome name

    '''
    edgeList = []
    nodeSet = set()
    id1 = int(config['INTERACTOME']['column_accession_id_1'])
    id2 = int(config['INTERACTOME']['column_accession_id_2'])
    evidence = int(config['INTERACTOME']['column_evidence'])
    while True:
        try:
            fileName = config['INTERACTOME']['default_interactome']
            with open(fileName, newline='') as cSVFile:
                if config['INTERACTOME']['skip_header'] == '1':
                    next(cSVFile)
                reader = csv.reader(cSVFile,
                                  dialect=config['INTERACTOME']['csv_dialect'])
                for row in reader:
                    if config['INTERACTOME']['use_evidence'] == '1':
                        edgeList.append([row[id1], row[id2], row[evidence]])
                    else:
                        edgeList.append([row[id1], row[id2]])
                    nodeSet.add(row[id1])
                    nodeSet.add(row[id2])
                break

        except OSError:
            print('Could not read file. '
                  + 'Did you remember the extension? Invalid file:', fileName)

    return edgeList, nodeSet, fileName


def defaultCSV():  # get the CSV
    '''
    TO DO:
        [x]enable skip header
        [x]count number of columns

    '''
    edgeList = []
    nodeSet = set()
    id1 = int(config['INTERACTOME']['column_accession_id_1'])
    id2 = int(config['INTERACTOME']['column_accession_id_2'])
    evidence = int(config['INTERACTOME']['column_evidence'])
    while True:
        try:
            fileName = config['INTERACTOME']['default_interactome']
            with open(fileName, newline='') as cSVFile:
                if config['INTERACTOME']['skip_header'] == '1':
                    next(cSVFile)
                reader = csv.reader(cSVFile,
                                  dialect=config['INTERACTOME']['csv_dialect'])
                for row in reader:
                    if config['INTERACTOME']['use_evidence'] == '1':
                        edgeList.append([row[id1], row[id2], row[evidence]])
                    else:
                        edgeList.append([row[id1], row[id2]])
                    nodeSet.add(row[id1])
                    nodeSet.add(row[id2])
                break

        except OSError:
            print('Could not read default file,'
                  + ' please enter a valid filename for now'
                  + ' and change cytoscouts_config.ini'
                  + ' when you have the chance. Invalid file: ', fileName)
        edgeList, nodeSet = importCSV()  # defaults to manual entry
    return edgeList, nodeSet, fileName


def cleanFileName(fileName):
    import re
    fileName = re.sub('\.(.*)', '', fileName)
    return fileName


def printOptions(edgeList, nodeSet, fileName):
    menuOption = input(
        '''\nPress:
          1 to print histograms of the uncollapsed interactome,
          2 to get neighbors of an accession ID,
          3 to collapse the interactome and print histograms,
          4 to input common name node for collapsed interactome,
          99 (DEPRECATED) to get secondary neighbors of an accession ID,
          otherwise any key to exit: ''')

    if menuOption == '1':
        collapsed = False
        deg = getDegree(edgeList, nodeSet)
        hist, x, y = getHisto(deg)
        lx, ly = computeLog(x, y)
        plotter1(x, y, lx, ly, fileName)
        if config['HISTOGRAM-1']['save_histogram_csv'] == '1':
            histoList = makeHistoList(hist)
            makeDegreeFile(histoList,
                           config['HISTOGRAM-1']['histogram_csv_name'],
                           collapsed, fileName)
        printOptions(edgeList, nodeSet, fileName)

    if menuOption == '2':
        collapsed = False
        while True:
            accession = input('Enter accession ID here: ')
            if accession in nodeSet:
                break
            print('Error:', accession, 'is not in the interactome.\
                   \nEnter another acession ID.')
        nNodes, nNodesKeys = neighbors(accession, edgeList)
        deg = getSubDegree(nNodes, edgeList, accession, collapsed, nNodesKeys)
        degList = makeDegList(nNodes, deg)
        makeDegreeFile(degList, accession, collapsed, fileName)
        hist, x, y = getHisto(deg)
        lx, ly = computeLog(x, y)
        plotter2(x, y, lx, ly, accession, fileName)
        printOptions(edgeList, nodeSet, fileName)

    if menuOption == '3':
        '''
        TODO
            []make file that shows what IDs the common names correspond to
            []make file that shows what accession IDs were skipped

        '''
        collapsed = True
        refDict = importDictionary()
        collapsedTupleSet, skippedEdgeList\
            = collapseEdgeList(refDict, edgeList)
        collapsedNodeSet, skippedNodeList\
            = collapseNodeSet(refDict, nodeSet)
        print('Collapsing the interactome...\n',
              len(skippedEdgeList), 'edges skipped.',
              len(skippedNodeList), 'nodes skipped.')
        print('# of edges in collapsed interactome:', len(collapsedTupleSet))
        print('# of nodes collapsed interactome:', len(collapsedNodeSet))
        processedSkippedEdgeList = processSkippedList(skippedEdgeList)
        processedSkippedNodeList = processSkippedList(skippedNodeList)
        makeSkippedFile(processedSkippedEdgeList, processedSkippedNodeList,
                        fileName)
        deg = getDegree(collapsedTupleSet, collapsedNodeSet)
        hist, x, y = getHisto(deg)  
        lx, ly = computeLog(x, y)
        plotter3(x, y, lx, ly, fileName)
        histoList = makeHistoList(hist)
        makeDegreeFile(histoList,
                       config['HISTOGRAM-3']['histogram_csv_name'],
                       collapsed, fileName)
        printOptions(edgeList, nodeSet, fileName)

    if menuOption == '4':
        collapsed = True
        refDict = importDictionary()
        collapsedTupleSet, skippedEdgeCount, skippedEdgeList\
            = collapseEdgeList(refDict, edgeList)
        collapsedNodeSet, skippedNodeCount, skippedNodeList\
            = collapseNodeSet(refDict, nodeSet)
        print('\n Collapsing the interactome...\n',
              len(skippedEdgeList), 'edges skipped.',
              len(skippedNodeList), 'nodes skipped.')
        print('# of edges in collapsed interactome:', len(collapsedTupleSet))
        print('# of nodes collapsed interactome:', len(collapsedNodeSet))
        while True:
            commonName = input('Enter common name here: ')
            if commonName in collapsedNodeSet:
                break
            print('Error:', commonName, 'is not in the interactome. \
                   \n Enter another name.')
        nNodes, nNodesKeys = neighbors(commonName, collapsedTupleSet)
        deg = getSubDegree(nNodes, collapsedTupleSet, commonName, collapsed,
                           nNodesKeys)
        hist, x, y = getHisto(deg)
        lx, ly = computeLog(x, y)
        plotter4(x, y, lx, ly, commonName, fileName)
        degList = makeDegList(nNodes, deg)
        makeDegreeFile(degList, commonName, collapsed, fileName)
        printOptions(edgeList, nodeSet, fileName)

        if menuOption == '99':
            collapsed = False
            while True:
                accession = input('Enter ID here: ')
                if accession in nodeSet:
                    break
                print('Error: ', accession, 'is not in the interactome. \
                       \n Enter another ID.')
            nNodes, nNodesKeys = neighbors(accession, edgeList)
            nNodes2 = neighbor2(nNodes, edgeList)
            print("primary neighbors")
            print(nNodes)
            print(len(nNodes))
            print("secondary neighbors")
            print(len(nNodes2))
            printOptions(edgeList, nodeSet, fileName)

        return


def getDegree(edgeList, nodeSet):
    deg = {}
    for item in nodeSet:
        deg[item] = 0
    for row in edgeList:
        deg[row[0]] += 1
        deg[row[1]] += 1
    return deg


def getHisto(deg):
    import itertools
    hist = sorted(deg.items(), key=lambda x: x[1])  # become sorted /tuples/
    x = []
    y = []
    for value, items in itertools.groupby(hist, lambda x: x[1]):  # by 'value'
        for i in items:  # items itself is just a memory object
            x.append(i[1])  # populate list of refDict values
    for i in x:  # a better way to do this? idk
        y.append(x.count(i))  # populate the fequency of said dict vals
    hist = list(hist)
    return hist, x, y


def makeHistoList(hist):
    import re
    histoList = [0]*len(hist)
    for t in range(0, len(hist)):
        hist[t] = list(hist[t])
        key = re.sub('\'', '', hist[t][0])
        value = str(hist[t][1])
        histoList[t] = key + ',' + value + '\n'
    return(histoList)


def neighbors(accession, edgeList):
    nNodes = set()
    nNodesKeys = set()
    for row in edgeList:
        pair = []
        if row[0] == accession:
            pair.append(row[1])
            if config['INTERACTOME']['use_evidence'] == '1':
                pair.append(row[2])
            pair = tuple(pair)
            nNodes.add(pair)
            nNodesKeys.add(pair[0])
        pair = []
        if row[1] == accession:
            pair.append(row[0])
            if config['INTERACTOME']['use_evidence'] == '1':
                pair.append(row[2])
            pair = tuple(pair)
            nNodes.add(pair)
            nNodesKeys.add(pair[0])
    return nNodes, nNodesKeys


def getSubDegree(nNodes, edgeList, proteinName, collapsed, nNodesKeys):
    deg = {}
    for key in nNodesKeys:
        deg[key] = 0
    for row in edgeList:
        if row[0] in nNodesKeys:
            deg[row[0]] += 1
        if row[1] in nNodesKeys:
            deg[row[1]] += 1
        if collapsed and (row[1], row[0]) in edgeList\
           and row[0] == proteinName:
            print('Be aware,', proteinName, 'is neighbors with itself!')

    return deg


def makeDegList(nNodes, deg):
    degList = []
    for node in nNodes:
        if config['INTERACTOME']['use_evidence'] == '1':
            degList.append(str(node[0])
                           + ','
                           + str(deg[node[0]])
                           + ','
                           + str(node[1])
                           + '\n')
        else:
            degList.append(str(node[0])
                           + ','
                           + str(deg[node[0]])
                           + '\n')
    return degList


def importDictionary():
    ref1 = int(config['REFERENCE']['column_ref_accession_id'])
    ref2 = int(config['REFERENCE']['column_ref_common_name'])
    fName = config['REFERENCE']['reference_file']
    refDict = {}
    with open(fName, newline='') as cSVFile:
        reader = csv.reader(cSVFile,
                            dialect=config['REFERENCE']['csv_dialect'])
        if config['REFERENCE']['skip_header'] == '1':
            next(cSVFile)
        for r in reader:
            refDict[r[ref1]] = r[ref2]
    return refDict


def useDictionary(refDict, nNodes, deg):
    nodeNames = []
    for key in refDict:  # accession ID with common name
        for node in nNodes:  # (neighbor accession IDs, evidence) tuple
            if key == node[0]:
                nodeNames.append(str(node)
                                 + ','
                                 + str(refDict[node[0]])  # common name
                                 + ','
                                 + str(deg[key])  # degree
                                 + ','
                                 + str(refDict[node[1]])  # evidence
                                 + '\n')
    return nodeNames


def makeDegreeFile(nodeNames, targetName, collapsed, fileName):
    file = open(fileName + '_' + targetName + "_neighbors.csv", "w")
    if not collapsed:
        file.write('Accession ID, Degree, Evidence\n')
    else:
        file.write('Common Name, Degree, Evidence\n')
    for row in nodeNames:  # wites the items from a list of strings
        file.write(row)
    file.close()
    print(fileName, targetName, 'neigbors.csv saved to local directory')
    return ()


def makeSkippedFile(processedSkippedEdgeList, processedSkippedNodeList,
                    fileName):
    file = open(fileName + '_' + config['HISTOGRAM-3']['histogram_csv_name']
                + '_skipped_edges.csv', 'w')
    file.write('Accession ID 1, Accession ID 2, Evidence\n')
    for row in processedSkippedEdgeList:
        file.write(row)
    file.close()
    print(fileName, config['HISTOGRAM-3']['histogram_csv_name'],
          'skipped_edges.csv saved to local directory')

    file = open(fileName + '_' + config['HISTOGRAM-3']['histogram_csv_name']
                + '_skipped_nodes.csv', 'w')
    file.write('Skipped Nodes\n')
    for row in processedSkippedNodeList:
        file.write(row)
    file.close()
    print(fileName, config['HISTOGRAM-3']['histogram_csv_name'],
          'skipped_edges.csv saved to local directory')

    return ()


def processSkippedList(skippedList):
    import re
    processedSkippedList = []
    for item in skippedList:
        processedSkippedList.append(re.sub('\'|\[|\]', '', str(item)) + '\n')
    return processedSkippedList


def collapseEdgeList(refDict, edgeList):
    # TODO: find out why collapsedTupleSetEvidence is so much larger
    # collapsedTupleSetEvidence should be the same size as collapsedTupleSet
    #
    # import pdb; pdb.set_trace()
    collapsedTupleSet = set()
    collapsedTupleSetEvidence = set()
    skippedEdgeList = []
    for row in edgeList:
        if config['INTERACTOME']['use_evidence'] == '1':
            if row[0] in refDict and row[1] in refDict:
                if (refDict[row[1]], refDict[row[0]])\
                 not in collapsedTupleSet:
                    collapsedTupleSet.add((refDict[row[0]],
                                           refDict[row[1]]))
                    collapsedTupleSetEvidence.add((refDict[row[0]],
                                                   refDict[row[1]],
                                                   row[2]))
            else:
                skippedEdgeList.append(row)
        else:
            if row[0] in refDict and row[1] in refDict:
                if (refDict[row[1]], refDict[row[0]])\
                 not in collapsedTupleSet:
                    collapsedTupleSetEvidence.add(tuple((refDict[row[0]],
                                                         refDict[row[1]])))
            else:
                skippedEdgeList.append(row)
    print(len(collapsedTupleSet), len(collapsedTupleSetEvidence))
    return collapsedTupleSetEvidence, skippedEdgeList


def collapseNodeSet(refDict, nodeSet):
    collapsedNodeSet = set()
    skippedNodeList = []
    for node in nodeSet:
        if node in refDict:
            collapsedNodeSet.add(refDict[node])
        else:
            skippedNodeList.append(node)
    return collapsedNodeSet, skippedNodeList


def neighbor2(nNodes, edgeList):
    nNodes2 = set()
    # if something from edgeList matches something in nNodes,put it in nNodes2
    for row in edgeList:
        for item in nNodes:
            if row[0] == item:
                nNodes2.add(row[1])
            if row[1] == item:
                nNodes2.add(row[0])
    return nNodes2


def subsetEdges(accession, edgeList, nNodes):
    # to get the subset of edges for the histogram of neighbors of the PoI
    # a list of edges containing the neighbor nodes of accession
    edgeSub = []
    for row in edgeList:
        for node in nNodes:
            # a for loop in which if a row is the accession id,
            # then the the row is added to a list, edgeSub
            if row[0] == node:
                edgeSub.append([row[0], row[1]])
            if row[1] == node:
                edgeSub.append([row[0], row[1]])
    return edgeSub


def computeLog(x, y):
    import math
    lx = []
    ly = []
    for i in range(len(x)):
        if y[i] > 0 and x[i] > 0:
            lx.append(math.log(x[i]))
            ly.append(math.log(y[i]))
    return (lx, ly)


'''
Histogram Section
'''


def plotter1(x, y, lx, ly, fileName):
    if config['HISTOGRAM-1']['print_figure1-1'] == '1':
        plt.figure()
        if config['HISTOGRAM-1']['figure1-1_autoscale'] != '1':
            plt.xlim([int(config['HISTOGRAM-1']['figure1-1_xlim_left']),
                      int(config['HISTOGRAM-1']['figure1-1_xlim_right'])])
            plt.ylim([int(config['HISTOGRAM-1']['figure1-1_ylim_bottom']),
                      int(config['HISTOGRAM-1']['figure1-1_ylim_top'])])
        plt.xlabel(config['HISTOGRAM-1']['figure1-1_xlabel'])
        plt.ylabel(config['HISTOGRAM-1']['figure1-1_ylabel'])
        plt.scatter(x, y, marker='.')
        plt.savefig(fileName + '_' + config['HISTOGRAM-1']['figure1-1_name']
                    + '.pdf', bbox_inches='tight')
        print(fileName, config['HISTOGRAM-1']['figure1-1_name'], '.pdf',
              'was printed to file.')

    if config['HISTOGRAM-1']['print_figure1-2'] == '1':
        plt.figure()
        if config['HISTOGRAM-1']['figure1-2_autoscale'] != '1':
            plt.xlim([int(config['HISTOGRAM-1']['figure1-2_xlim_left']),
                      int(config['HISTOGRAM-1']['figure1-2_xlim_right'])])
            plt.ylim([int(config['HISTOGRAM-1']['figure1-2_ylim_bottom']),
                      int(config['HISTOGRAM-1']['figure1-2_ylim_top'])])
        plt.xlabel(config['HISTOGRAM-1']['figure1-2_xlabel'])
        plt.ylabel(config['HISTOGRAM-1']['figure1-2_ylabel'])
        plt.scatter(x, y, marker='.')
        plt.savefig(fileName + '_' + config['HISTOGRAM-1']['figure1-2_name']
                    + '.pdf', bbox_inches='tight')
        print(fileName, config['HISTOGRAM-1']['figure1-2_name'], '.pdf',
              'was printed to file.')

    if config['HISTOGRAM-1']['print_figure1-3'] == '1':
        plt.figure()
        if config['HISTOGRAM-1']['figure1-3_autoscale'] != '1':
            plt.xlim([int(config['HISTOGRAM-1']['figure1-3_xlim_left']),
                      int(config['HISTOGRAM-1']['figure1-3_xlim_right'])])
            plt.ylim([int(config['HISTOGRAM-1']['figure1-3_ylim_bottom']),
                      int(config['HISTOGRAM-1']['figure1-3_ylim_top'])])
        plt.xlabel(config['HISTOGRAM-1']['figure1-3_xlabel'])
        plt.ylabel(config['HISTOGRAM-1']['figure1-3_ylabel'])
        plt.scatter(lx, ly, marker='.')
        plt.savefig(fileName + '_' + config['HISTOGRAM-1']['figure1-3_name']
                    + '.pdf', bbox_inches='tight')
        print(fileName, config['HISTOGRAM-1']['figure1-3_name'], '.pdf',
              'was printed to file.')


def plotter2(x, y, lx, ly, accession, fileName):
    if config['HISTOGRAM-2']['print_figure2-1'] == '1':
        plt.figure()
        if config['HISTOGRAM-2']['figure2-1_autoscale'] != '1':
            plt.xlim([int(config['HISTOGRAM-2']['figure2-1_xlim_left']),
                      int(config['HISTOGRAM-2']['figure2-1_xlim_right'])])
            plt.ylim([int(config['HISTOGRAM-2']['figure2-1_ylim_bottom']),
                      int(config['HISTOGRAM-2']['figure2-1_ylim_top'])])
        plt.xlabel(config['HISTOGRAM-2']['figure2-1_xlabel'])
        plt.ylabel(config['HISTOGRAM-2']['figure2-1_ylabel'])
        plt.scatter(x, y, marker='.')
        plt.savefig(fileName + '_' + accession + 'neighbors_1.pdf',
                    bbox_inches='tight')
        print(fileName, accession, 'neighbors 1.pdf was printed to file.')

    if config['HISTOGRAM-2']['print_figure2-2'] == '1':
        plt.figure()
        if config['HISTOGRAM-2']['figure2-2_autoscale'] != '1':
            plt.xlim([int(config['HISTOGRAM-2']['figure2-2_xlim_left']),
                      int(config['HISTOGRAM-2']['figure2-2_xlim_right'])])
            plt.ylim([int(config['HISTOGRAM-2']['figure2-2_ylim_bottom']),
                      int(config['HISTOGRAM-2']['figure2-2_ylim_top'])])
        plt.xlabel(config['HISTOGRAM-2']['figure2-2_xlabel'])
        plt.ylabel(config['HISTOGRAM-2']['figure2-2_ylabel'])
        plt.scatter(x, y, marker='.')
        plt.savefig(fileName + '_' + accession + ' neighbors 2.pdf',
                    bbox_inches='tight')
        print(fileName, accession, 'neighbors_2.pdf was printed to file.')

    if config['HISTOGRAM-2']['print_figure2-3'] == '1':
        plt.figure()
        if config['HISTOGRAM-2']['figure2-3_autoscale'] != '1':
            plt.xlim([int(config['HISTOGRAM-2']['figure2-3_xlim_left']),
                      int(config['HISTOGRAM-2']['figure2-3_xlim_right'])])
            plt.ylim([int(config['HISTOGRAM-2']['figure2-3_ylim_bottom']),
                      int(config['HISTOGRAM-2']['figure2-3_ylim_top'])])
        plt.xlabel(config['HISTOGRAM-2']['figure2-3_xlabel'])
        plt.ylabel(config['HISTOGRAM-2']['figure2-3_ylabel'])
        plt.scatter(lx, ly, marker='.')
        plt.savefig(fileName + '_' + accession + ' neighbors 3.pdf',
                    bbox_inches='tight')
        print(fileName, accession, 'neighbors_3.pdf was printed to file.')

    return


def plotter3(x, y, lx, ly, fileName):
    if config['HISTOGRAM-3']['print_figure3-1'] == '1':
        plt.figure()
        if config['HISTOGRAM-3']['figure3-1_autoscale'] != '1':
            plt.xlim([int(config['HISTOGRAM-3']['figure3-1_xlim_left']),
                      int(config['HISTOGRAM-3']['figure3-1_xlim_right'])])
            plt.ylim([int(config['HISTOGRAM-3']['figure3-1_ylim_bottom']),
                      int(config['HISTOGRAM-3']['figure3-1_ylim_top'])])
        plt.xlabel(config['HISTOGRAM-3']['figure3-1_xlabel'])
        plt.ylabel(config['HISTOGRAM-3']['figure3-1_ylabel'])
        plt.scatter(x, y, marker='.')
        plt.savefig(fileName + '_' + config['HISTOGRAM-3']['figure3-1_name']
                    + '.pdf', bbox_inches='tight')
        print(fileName, config['HISTOGRAM-3']['figure3-1_name'] + '.pdf',
              'was printed to file.')

    if config['HISTOGRAM-3']['print_figure3-2'] == '1':
        plt.figure()
        if config['HISTOGRAM-3']['figure3-2_autoscale'] != '1':
            plt.xlim([int(config['HISTOGRAM-3']['figure3-2_xlim_left']),
                      int(config['HISTOGRAM-3']['figure3-2_xlim_right'])])
            plt.ylim([int(config['HISTOGRAM-3']['figure3-2_ylim_bottom']),
                      int(config['HISTOGRAM-3']['figure3-2_ylim_top'])])
        plt.xlabel(config['HISTOGRAM-3']['figure3-2_xlabel'])
        plt.ylabel(config['HISTOGRAM-3']['figure3-2_ylabel'])
        plt.scatter(x, y, marker='.')
        plt.savefig(fileName + '_' + config['HISTOGRAM-3']['figure3-2_name']
                    + '.pdf', bbox_inches='tight')
        print(fileName, config['HISTOGRAM-3']['figure3-2_name'] + '.pdf',
              'was printed to file.')

    if config['HISTOGRAM-3']['print_figure3-3'] == '1':
        plt.figure()
        if config['HISTOGRAM-3']['figure3-3_autoscale'] != '1':
            plt.xlim([int(config['HISTOGRAM-3']['figure3-3_xlim_left']),
                      int(config['HISTOGRAM-3']['figure3-3_xlim_right'])])
            plt.ylim([int(config['HISTOGRAM-3']['figure3-3_ylim_bottom']),
                      int(config['HISTOGRAM-3']['figure3-3_ylim_top'])])
        plt.xlabel(config['HISTOGRAM-3']['figure3-3_xlabel'])
        plt.ylabel(config['HISTOGRAM-3']['figure3-3_ylabel'])
        plt.scatter(lx, ly, marker='.')
        plt.savefig(fileName + '_' + config['HISTOGRAM-3']['figure3-3_name']
                    + '.pdf', bbox_inches='tight')
        print(fileName, config['HISTOGRAM-3']['figure3-3_name'] + '.pdf',
              'was printed to file.')
    return


def plotter4(x, y, lx, ly, commonName, fileName):
    if config['HISTOGRAM-4']['print_figure4-1'] == '1':
        plt.figure()
        if config['HISTOGRAM-4']['figure4-1_autoscale'] != '1':
            plt.xlim([int(config['HISTOGRAM-4']['figure4-1_xlim_left']),
                      int(config['HISTOGRAM-4']['figure4-1_xlim_right'])])
            plt.ylim([int(config['HISTOGRAM-4']['figure4-1_ylim_bottom']),
                      int(config['HISTOGRAM-4']['figure4-1_ylim_top'])])
        plt.xlabel(config['HISTOGRAM-4']['figure4-1_xlabel'])
        plt.ylabel(config['HISTOGRAM-4']['figure4-1_ylabel'])
        plt.scatter(x, y, marker='.')
        plt.savefig(fileName + '_' + commonName + '_neighbors_histogram_1.pdf',
                    bbox_inches='tight')
        print(fileName, commonName,
              'neighbors_histogram_1.pdf was printed to file.')

    if config['HISTOGRAM-4']['print_figure4-2'] == '1':
        plt.figure()
        if config['HISTOGRAM-4']['figure4-2_autoscale'] != '1':
            plt.xlim([int(config['HISTOGRAM-4']['figure4-2_xlim_left']),
                      int(config['HISTOGRAM-4']['figure4-2_xlim_right'])])
            plt.ylim([int(config['HISTOGRAM-4']['figure4-2_ylim_bottom']),
                      int(config['HISTOGRAM-4']['figure4-2_ylim_top'])])
        plt.xlabel(config['HISTOGRAM-4']['figure4-2_xlabel'])
        plt.ylabel(config['HISTOGRAM-4']['figure4-2_ylabel'])
        plt.scatter(x, y, marker='.')
        plt.savefig(fileName + '_' + commonName + '_neighbors_histogram_2.pdf',
                    bbox_inches='tight')
        print(fileName, commonName,
              'neighbors_histogram_2.pdf was printed to file.')

    if config['HISTOGRAM-4']['print_figure4-3'] == '1':
        plt.figure()
        if config['HISTOGRAM-4']['figure4-3_autoscale'] != '1':
            plt.xlim([int(config['HISTOGRAM-4']['figure4-3_xlim_left']),
                      int(config['HISTOGRAM-4']['figure4-3_xlim_right'])])
            plt.ylim([int(config['HISTOGRAM-4']['figure4-3_ylim_bottom']),
                      int(config['HISTOGRAM-4']['figure4-3_ylim_top'])])
        plt.xlabel(config['HISTOGRAM-4']['figure4-3_xlabel'])
        plt.ylabel(config['HISTOGRAM-4']['figure4-3_ylabel'])
        plt.scatter(lx, ly, marker='.')
        plt.savefig(fileName + '_' + commonName + '_neighbors_histogram_3.pdf',
                    bbox_inches='tight')
        print(fileName, commonName,
              'neighbors_histogram_3.pdf was printed to file.')
    return


main()
