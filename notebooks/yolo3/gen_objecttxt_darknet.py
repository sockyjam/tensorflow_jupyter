import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET
from pathlib import Path

def xml_to_txt(xml_file):


    fname = "."+xml_file.split(".")[-2]+".txt"
    print(fname)
    with open(fname, 'a') as file:   #只需要将之前的”w"改为“a"即可，代表追加内容
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for member in root.findall('object'):
            if member[0].text == 'hand':
                class_id = 0

            width = int(root.find('size')[0].text)
            height = int(root.find('size')[1].text)

            xmin = int(member[4][0].text)
            ymin = int(member[4][1].text)
            xmax = int(member[4][2].text)
            ymax = int(member[4][3].text)

            xcenter = round(((xmin + xmax) / 2) / width, 6)
            ycenter = round(((ymin + ymax) / 2) / height, 6)
            xwidth = round((xmax - xmin) / width, 6)
            yheight = round((ymax - ymin) / height, 6)

            print("%d %.6f %.6f %.6f %.6f" % (class_id, xcenter, ycenter, xwidth, yheight))

            file.write("%d %.6f %.6f %.6f %.6f" % (class_id, xcenter, ycenter, xwidth, yheight))
            file.write("\n")

                    # value = [class_id]
                    # value.append(int(member[4][0].text))
                    # value.append(int(member[4][1].text))
                    # value.append(int(member[4][2].text))
                    # value.append(int(member[4][3].text))
                    # xml_list.append(value)
                # column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
                # xml_df = pd.DataFrame(xml_list)



def main():
    for folder in ['train', 'test']:
        flist = glob.glob("./images/"+folder+"/*.xml")
        for xmlfile in flist:
            xml_df = xml_to_txt(xmlfile)
            # xml_df.to_csv("."+xmlfile.split(".")[-2]+".txt", index=None)

        # image_path = os.path.join(os.getcwd(), ('image/' + folder))
        # xml_df = xml_to_csv(image_path)
        # xml_df.to_csv(('image/'+folder+'_file.txt'), index=None)
    print('Successfully converted xml to txt.')

if __name__ == '__main__':
    main()

