import os
import argparse
import pathlib

def rename(directory, number):
    i = number
    flist = os.listdir(directory)
    for fitem in flist:
        os.rename(directory+"/"+fitem, directory+"/"+"s_"+str(i)+".png")
        i = i + 1




if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Rescale images")
    parser.add_argument('-d', '--directory', type=str, required=True, help='Directory containing the images to be renamed')
    parser.add_argument('-n', '--number', type=int, required=True, help='begin number to rename picture files')
    args = parser.parse_args()
    directory = args.directory
    number = args.number
    rename(directory, number)


