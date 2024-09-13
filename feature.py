from process_of_cleaning import *




def data_cleaning():
    inputfile='Raw_File.csv'
    outputfile='DE_Task1.csv'
    
    cleaned_file(inputfile,outputfile)



if __name__=='__main__':
    data_cleaning()