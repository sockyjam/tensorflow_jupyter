import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET


def xml_to_csv(path):
    xml_list = []
    for xml_file in glob.glob(path + '/*.xml'):
        tree = ET.parse(xml_file)
        root = tree.getroot()

        value = ["./tinydataset/"+root.find('filename').text]

        # for member in root.findall('object'):
        #     if member[0].text == 'iphone':
        #         class_id = 0
        #     elif member[0].text == 'kindle':
        #         class_id = 1
        #     elif member[0].text == 'mouse':
        #         class_id = 2
        #     value.append(int(member[4][0].text))
        #     value.append(int(member[4][1].text))
        #     value.append(int(member[4][2].text))
        #     value.append(int(member[4][3].text))
        #     value.append(class_id)
        #     value.append(" +++ ")
        xml_list.append(value)
    # column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pd.DataFrame(xml_list)
    return xml_df


def main():
    for folder in ['train', 'test']:
        image_path = os.path.join(os.getcwd(), ('image/' + folder))
        xml_df = xml_to_csv(image_path)
        xml_df.to_csv(('./image/'+folder+'_file.txt'), index=None)
    print('Successfully converted xml to csv.')

if __name__ == '__main__':
    main()

