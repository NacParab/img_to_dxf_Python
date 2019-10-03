import ezdxf
import numpy
import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", type=str, default="input_img.png", help="path to input jpg drawing")
ap.add_argument("-o", "--output", type=str, default="output_dxf.dxf", help="path to output dxf drawing")
ap.add_argument("-l", "--lower_range", type=str, default="(0,0,0)", help="Lower range in BGR format for the mask")
ap.add_argument("-u", "--upper_range", type=str, default="(200,200,200)", help="Upper range in BGR format for the mask")

args = vars(ap.parse_args())

upper_B, upper_G, upper_R = int(args["upper_range"].replace("(","").replace(")","").split(",")[0]), int(args["upper_range"].replace("(","").replace(")","").split(",")[1]), int(args["upper_range"].replace("(","").replace(")","").split(",")[2])
lower_B, lower_G, lower_R = int(args["lower_range"].replace("(","").replace(")","").split(",")[0]), int(args["lower_range"].replace("(","").replace(")","").split(",")[1]), int(args["lower_range"].replace("(","").replace(")","").split(",")[2])

upper_range_tuple = (upper_B,upper_G,upper_R)
lower_range_tuple = (lower_B,lower_G,lower_R)

doc = ezdxf.new('R2010')
msp = doc.modelspace() 
opened_jpg = cv2.imread(args["input"])
masked_jpg = cv2.inRange(opened_jpg,lower_range_tuple, upper_range_tuple)

for i in range(0,masked_jpg.shape[0]):
    for j in range(0,masked_jpg.shape[1]):
        if masked_jpg[i][j] == 255:
            msp.add_line((j,masked_jpg.shape[0] - i), (j,masked_jpg.shape[0] - i))

doc.saveas('output_dxf.dxf')


