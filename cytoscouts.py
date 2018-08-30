# -*- coding: utf-8 -*-
"""
author: Petra Wijngaard
latest version 8 30 2018

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
version = 'v0.9.0'


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
    evidenceCol = int(config['INTERACTOME']['column_evidence'])
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
                        edgeList.append([row[id1], row[id2], row[evidenceCol]])
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
    evidenceCol = int(config['INTERACTOME']['column_evidence'])
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
                        edgeList.append([row[id1], row[id2], row[evidenceCol]])
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
    fileName = re.sub('\.(.*)', '', fileName)  # removes endings
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

        # make histograms and csvs
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
        refDict = 0

        while True:
            accession = input('Enter accession ID here: ')
            if accession in nodeSet:
                break
            print('Error:', accession, 'is not in the interactome.\
                   \nEnter another acession ID.')

        nNodes, nNodesE = neighbors(accession, edgeList)
        deg = getSubDegree(nNodes, edgeList)
        degList = makeDegList(nNodes, nNodesE, deg, collapsed, refDict)
        makeDegreeFile(degList, accession, collapsed, fileName)

        hist, x, y = getHisto(deg)
        lx, ly = computeLog(x, y)
        plotter2(x, y, lx, ly, accession, fileName)

        printOptions(edgeList, nodeSet, fileName)

    if menuOption == '3':
        # TODO: make file with AcIDs grouped by common name
        collapsed = True

        # collapse the inteactome
        refDict = importDictionary()
        print('Collapsing the interactome...\n')
        cListListEM, sEdgeList = collapseEdgeList(refDict, edgeList)
        cNodeSet, sNodeSet = collapseNodeSet(refDict, nodeSet)
        print(len(sEdgeList), 'edges skipped.')
        print(len(sNodeSet), 'nodes skipped.')
        print('# of edges in collapsed interactome:', len(cListListEM))
        print('# of nodes collapsed interactome:', len(cNodeSet))

        # make a file of the skipped edges
        pSEdgeList = processsList(sEdgeList)
        pSNodeSet = processsList(sNodeSet)
        makeSkippedFile(pSEdgeList, pSNodeSet,
                        fileName)

        # make histogram pdfs and csvs
        deg = getDegree(cListListEM, cNodeSet)
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

        # collapse the inteactome
        refDict = importDictionary()
        print('Collapsing the interactome...\n')
        cListListEM, sEdgeList = collapseEdgeList(refDict, edgeList)
        cNodeSet, sNodeSet = collapseNodeSet(refDict, nodeSet)
        print(len(sEdgeList), 'edges skipped.')
        print(len(sNodeSet), 'nodes skipped.')
        print('# of edges in collapsed interactome:', len(cListListEM))
        print('# of nodes collapsed interactome:', len(cNodeSet))

        # get common name
        while True:
            commonName = input('Enter common name here: ')
            if commonName in cNodeSet:
                break
            print('Error:', commonName, 'is not in the interactome. \
                   \n Enter another name.')

        # find neighbors of common name
        nNodes, nNodesE = neighbors(commonName, cListListEM)
        deg = getSubDegree(nNodes, cListListEM)
        # print histo and csv
        hist, x, y = getHisto(deg)
        lx, ly = computeLog(x, y)
        plotter4(x, y, lx, ly, commonName, fileName)
        degList = makeDegList(nNodes, nNodesE, deg, collapsed, refDict)
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
            nNodes, nNodesE = neighbors(accession, edgeList)
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
    useEvidence = config['INTERACTOME']['use_evidence']
    nNodes = set()  # a set of tuples each containing node w/ edge w/ accession
    nNodesE = set()  # set of tuples like nNodes but with evidence too

    # if one half of an edge is accession, then the other is added to nNodes
    # if useEvidence is selected, the evidence is included in the tuple
    for row in edgeList:
        pair = []
        if row[0] == accession and useEvidence == '1':
            pair.append(row[1])
            pair.append(row[2])
            pair = tuple(pair)
            nNodes.add(row[1])
            nNodesE.add(pair)
        elif row[0] == accession and useEvidence != '1':
            nNodes.add(row[1])

        pair = []
        if row[1] == accession and useEvidence == '1':
            nNodes.add(row[0])
            pair.append(row[0])
            pair.append(row[2])
            pair = tuple(pair)
            nNodesE.add(pair)
        elif row[1] == accession and useEvidence != '1':
            nNodes.add(row[0])

    if tuple(accession) in nNodes:
        print('Be aware,', accession, 'is neighbors with itself!')
    return nNodes, nNodesE


def getSubDegree(nNodes, edgeList):
    deg = {}  # dictionary of node:degree
    # for every node in nNodes increase deg[node] when node is in an edge
    for key in nNodes:
        deg[key] = 0
    for row in edgeList:
        if row[0] in nNodes:
            deg[row[0]] += 1
        if row[1] in nNodes:
            deg[row[1]] += 1
    return deg


def makeDegList(nNodes, nNodesE, deg, collapsed, refDict):
    useEvidence = config['INTERACTOME']['use_evidence']
    degList = []  # a list containing [commonName,acID,degree,evidence]

    if useEvidence == '1' and collapsed:
        for node in nNodesE:
            degList.append(str(node[0])  # commonName
                           + ','
                           + acIDsByCName(refDict,node[0])  # acID
                           + ','
                           + str(deg[node[0]])  # degree
                           + ','
                           + str(node[1])  # evidence
                           + '\n')

    elif useEvidence != '1' and collapsed:
        for node in nNodes:
            degList.append(str(node[0])  # commonName
                           + ','
                           + acIDsByCName(refDict[node[0]])  # acID
                           + ','
                           + str(deg[node[0]])  # degree
                           + '\n')

        if useEvidence == '1' and not collapsed:
            for node in nNodesE:
                degList.append(str(node[0])
                               + ','
                               + str(deg[node[0]])
                               + ','
                               + str(node[1])
                               + '\n')

        elif useEvidence != '1' and not collapsed:
            for node in nNodes:
                degList.append(str(node[0])
                               + ','
                               + str(deg[node[0]])
                               + '\n')
    return degList


def acIDsByCName(refDict, commonName):
    acIDList = []
    pairList = refDict.items()  # list of every key:value pair

    for pair in pairList:
        if pair[1] == commonName:  # if value == commonName
            acIDList.append(pair[0])  # append key
    acIDs = ' '.join(acIDList)
    return acIDs


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


def useDictionary(refDict, nNodes, deg):  # TODO: redundant unused function
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
        file.write('Common Name, Accession ID(s), Degree, Evidence\n')
    for row in nodeNames:  # wites the items from a list of strings
        file.write(row)
    file.close()
    print(fileName, targetName, 'neigbors.csv saved to local directory')
    return ()


def makeSkippedFile(pSEdgeList, pSNodeSet, fileName):
    file = open(fileName + '_' + config['HISTOGRAM-3']['histogram_csv_name']
                + '_skipped_edges.csv', 'w')
    file.write('Accession ID 1, Accession ID 2, Evidence\n')
    for row in pSEdgeList:
        file.write(row)
    file.close()
    print(fileName, config['HISTOGRAM-3']['histogram_csv_name'],
          'skipped_edges.csv saved to local directory')

    file = open(fileName + '_' + config['HISTOGRAM-3']['histogram_csv_name']
                + '_skipped_nodes.csv', 'w')
    file.write('Skipped Nodes\n')
    for row in pSNodeSet:
        file.write(row)
    file.close()
    print(fileName, config['HISTOGRAM-3']['histogram_csv_name'],
          'skipped_edges.csv saved to local directory')

    return ()


def processsList(sList):
    import re
    pSList = []  # processed list of skipped values, stripped of junk

    for item in sList:
        pSList.append(re.sub('\'|\[|\]', '', str(item)) + '\n')
    return pSList


def collapseEdgeList(refDict, edgeList):
    # TODO: find out what cyclomatic complexity is and reduce it
    useEvidence = config['INTERACTOME']['use_evidence']
    cTupleSet = set()  # collapsed tuple set of edges
    cTupleSetE = set()  # cTupleSet with evidence
    sEdgeList = []  # list of skipped edge
    cTupleListE = []  # TODO cTupleSetE as a list <- can this be skipped?
    cListListE = []  # cTupleListE as a list of lists
    cListListEM = []  # list of all tuple with evidence, without redundancies

    # gathering the edges and evidence, if selected in config file
    # if both nodes are keys in reference make tuple with values
    # add to set cTupleSet to remove duplicate tuples
    # use cTupleSetE to keep track of evidence, but only accept tuples
    # not in cTupleSet.
    # If use evidence is not selected, cTupleSetE is still used as the returned
    # variable, even though it contains no evidence
    for row in edgeList:
        if useEvidence == '1' and row[0] in refDict and row[1] in refDict:
            if (refDict[row[1]], refDict[row[0]]) not in cTupleSet:
                    cTupleSet.add((refDict[row[0]], refDict[row[1]]))
                    cTupleSetE.add((refDict[row[0]], refDict[row[1]], row[2]))
        elif useEvidence != '1' and row[0] in refDict and row[1] in refDict:
            if (refDict[row[1]], refDict[row[0]]) not in cTupleSet:
                cTupleSetE.add((refDict[row[0]], refDict[row[1]]))
        elif row[0] not in refDict or row[1] not in refDict:
            sEdgeList.append(row)
        else:
            continue

    # combining the redundant evidence for collapsed nodes
    # if the list of edge&evidence is the same as the one adjacent to it
    # combine the evidence index and delete the preceding/succeeding list

    cTupleListE = sorted(cTupleSetE)
    for row in range(0, len(cTupleListE)):
        cListListE.append(list(cTupleListE[row]))

    for row in range(0, len(cListListE)):
        if row == 0 and cListListE[row][0:2] == cListListE[row + 1][0:2]\
                    and cListListE[row][2] != cListListE[row + 1][2]:
                        cListListE[row + 1][2] = cListListE[row + 1][2]\
                                                  + '+'\
                                                  + cListListE[row][2]
                        cListListE[row] = ['0']

        elif row > 0 and cListListE[row][0:2] == cListListE[row - 1][0:2]\
                     and cListListE[row][2] != cListListE[row - 1][2]:
                        cListListE[row][2] = cListListE[row - 1][2]\
                                                  + '+'\
                                                  + cListListE[row][2]
                        cListListE[row - 1] = [0]

        elif row < 0:
            print('Negative rows?!?!?!')

        else:
            continue

    for i in cListListE:
        if i != [0]:
            cListListEM.append(i)

    return cListListEM, sEdgeList


def collapseNodeSet(refDict, nodeSet):
    cNodeSet = set()
    sNodeSet = []
    for node in nodeSet:
        if node in refDict:
            cNodeSet.add(refDict[node])
        else:
            sNodeSet.append(node)
    return cNodeSet, sNodeSet


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
