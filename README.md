# cytoscouts

Cytoscouts is a Python script that can be run on any computer with Python 3. It has a rudimentary user interface where commands are entered by keyboard. It takes an interactome in .csv format, specified by user input, and processes the interactome. From the interactome, cytoscouts can make lists of neighbors of a given node and print histograms, which are bar graphs that show the distribution of nodes with a given degree, for the uncollapsed or collapsed interactome.

When using the script the user has five options: 

0 Get a histogram of the entire uncollapsed interactome and save it to a file in the current directory. 

1 Get a list of the neighbors of a given UniProt ID in the uncollapsed interactome along with a histogram of the neighbors of the UniProt ID in the uncollapsed interactome and save each to a file in the current the directory. 

2 Get a list of the neighbors of neighbors of a UniProt ID (this function is largely deprecated since I did not find it useful). 

3 Collapse the interactome and then save a histogram of the collapsed interactome to a file in the current the directory. 

4 Collapse the interactome then get a list of the neighbors of a given common name in the collapsed interactome along with a histogram of the neighbors of the common name in the collapsed interactome and save each to file in the current the directory.

A more thorough explanation of cytoscouts can be found in section two of thesis.pdf.


