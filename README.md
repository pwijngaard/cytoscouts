# cytoscouts

Cytoscouts is a Python script that can be run on any computer with Python 3 and the module matplotlib. It takes an interactome in .txt or .csv format, specified by user input, and processes the interactome to give the degree of the nodes in the interactome as well as evidence for edges in the interactome. With the addition of a reference file, processing can include 'collapsing' the interactome, a feature that takes nodes that have discrete accession IDs but identical common names and combines them based on their common name. From the interactome, cytoscouts can make lists of neighbors of a given node and print histograms for the uncollapsed or collapsed interactome. Cytoscousts is configured to read an interactome through a file that is spawned in the local directory of wherever cytscouts is first run.

## Requirements
Cytoscouts requires matplotlib. To install matplotlib, enter the following command from cmd on Windows or terminal on Mac or Linux:
```
pip install matplotlib
```
## Install

Unizip cytoscouts.zip to wherever you would like to install cytoscouts.

## Setup
To set up cytoscouts, first place the interactome(s) you wish to process into the cytoscouts folder.

If you wish to collapse the interactome, also place the reference file in the cytoscouts folder.

Then open cytoscouts_config.ini and follow the guide comments to configure cytoscouts to read your interactome and reference file.

## Running
### Windows
To run cytoscouts open a cmd window in the cytoscouts folder by shift+right clicking the cytoscouts folder and entering:
```
python cytoscouts.py
```

### Mac and Linux
To run cytoscouts open a terminal window in the cytoscouts folder by right clicking the cytoscouts folder and entering:
```
python3 cytoscouts.py
```

When using the script the user has four options: 

1 Get a .pdf histogram of the entire uncollapsed interactome and save it in the cytoscouts folder. 

2 Get a .csv list of the neighbors of a given accession ID in the uncollapsed interactome along with a .pdf histogram of the neighbors of the accession ID in the uncollapsed interactome and save in the cytoscouts folder.

3 Collapse the interactome and then save a .pdf histogram of the collapsed interactome to the cytoscouts folder. 

4 Collapse the interactome then get a .csv list of the neighbors of a given common name in the collapsed interactome along with a .pdf histogram of the neighbors of the common name in the collapsed interactome and save them to the cytoscouts folder.

## More

A more thorough explanation of cytoscouts can be found in section two of wijngaard_thesis.pdf, however it was written for cytoscouts v0.4 and thus lacks documentation of added features such as the configuration file.


