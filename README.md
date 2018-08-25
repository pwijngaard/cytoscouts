# cytoscouts

Cytoscouts is a Python script that can be run on any computer with Python 3. It takes an interactome in .csv format, specified by user input, and processes the interactome. Processing can include 'collapsing' the interactome, a feature that takes nodes that have discrete accession IDs but identical common names and combines them based on their common name. From the interactome, cytoscouts can make lists of neighbors of a given node and print histograms for the uncollapsed or collapsed interactome. Options are accessible through a configuration file that is spawned in the local directory of wherever cytscouts is first run.

When using the script the user has five options: 

1 Get a histogram of the entire uncollapsed interactome and save it to a file in the current directory. 

2 Get a list of the neighbors of a given accession ID in the uncollapsed interactome along with a histogram of the neighbors of the accession ID in the uncollapsed interactome and save each to a file in the current the directory. 

3 Collapse the interactome and then save a histogram of the collapsed interactome to a file in the current the directory. 

4 Collapse the interactome then get a list of the neighbors of a given common name in the collapsed interactome along with a histogram of the neighbors of the common name in the collapsed interactome and save each to file in the current the directory.

99 Get a list of the neighbors of neighbors of a accession ID (this function is deprecated since I did not find it useful). 

A more thorough explanation of cytoscouts can be found in section two of wijngaard_thesis.pdf, however it was written for cytoscouts v0.4 and thus lacks documentation of added features such as the configuration file.


