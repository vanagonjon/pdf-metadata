#!/usr/bin/env python
# coding: utf-8

import json
import glob
import os
import logging
from PyPDF2 import PdfFileReader, PdfFileWriter
from datetime import datetime

def edit_metadata(path, custom_metadata):
    fin = open(path, 'rb')
    reader = PdfFileReader(fin)
    metadata = reader.getDocumentInfo()
    number_of_pages = reader.getNumPages()
    metadata = reader.getDocumentInfo()
    fin.close()

    writer = PdfFileWriter()
    writer.appendPagesFromReader(reader)
    writer.addMetadata(metadata)

    # Write custom metadata here:
    writer.addMetadata(custom_metadata)

    fout = open('Output/' + os.path.basename(path), 'wb')
    writer.write(fout)
    fout.close()

def append_metadata():
    #remove existing logging handlers
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)
    #configure logging
    LOG_FILENAME = datetime.now().strftime(os.getcwd() + '/logfile_%H_%M_%S_%d_%m_%Y.log')
    logging.basicConfig(filename=LOG_FILENAME, level=logging.INFO)
    
    logging.info("Starting")
    
    #check that output directory exists, if not make one
    if not os.path.isdir(os.getcwd()+"/Output") :
        os.mkdir(os.getcwd()+"/Output")

    #get list of dictionaries containing metadata for all report targets
    with open('metadata_list.json', 'r') as f:
        report_dict_list = json.load(f)

    #Loop through dictionaries of metadata and look for matching pdfs in Sources directory
        total_found = 0
        total_not_found = 0
    for report_dict in report_dict_list:
        #generate name of target file using value of 'Report Number' key. any file containg this number in
        #the titel is an acceptable target
        fileName = (os.getcwd()+"/Sources/*"+ report_dict['Report Number']+"*.pdf")
        logging.info("Searching for target file: " + fileName)
        metadata = ({'/Keywords': report_dict["Keywords"],
                    '/Alloy': report_dict["Alloy"]})
        fileFound = False

        #scan for target file, if found call edit_metadata function
        for file in glob.glob(fileName):
            logging.info("File found: " + file)
            fileFound = True
            edit_metadata(file,metadata)
            total_found = total_found + 1
        if not fileFound:
            logging.info("File not found")
            total_not_found = total_not_found + 1
            
    logging.info(datetime.now().strftime('Search complete at %H_%M_%S_%d_%m_%Y with ' + str(total_found) + 
                                         ' files found, ' + str(total_not_found) + ' files not found'))
        
if __name__ == "__main__":
    append_metadata()





