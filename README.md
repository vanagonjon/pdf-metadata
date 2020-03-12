In order to use this module take the following steps:

- In a terminal navigate to the directory contiaing this file and run 'pip3 install -r requirements.txt'
- Copy the source PDF files to the 'Sources' directory
- Run 'python3 metamod.py', or run the module directly from a python editor

Once finished the there will now be an 'Output' directory containing the a copy of the source files with the modified metadata. There should also be a log file with details on which files were and weren't found

Only files with names containing the "Report Number" field from the metadata_list.json will be copied and edited. If the metadata_list.json file is incomplete it will need to be editied. I can help with this if needed.