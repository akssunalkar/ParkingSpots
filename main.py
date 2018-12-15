import cv2
from PIL import Image
import numpy as np
import os.path
import matplotlib.pyplot as plt
from scipy.misc import imsave
import city_segment
import parking_detection
import vehicle_segment


if __name__ == "__main__":
    

    border = 700
    n_clust = 9


    filename = "example.jpg"

    # High level segmentation using pre-trained network
    if not os.path.isfile("output.npy"):
        city_segment.segmentation(filename, "output.png")

    # Create mask for only largest road segment
    mask = city_segment.largest_connected_component(filename="output.npy")
    #mask = city_segment.dilation(mask, 200)

    # Apply traditional CV to masked image
    img = cv2.imread(filename)
    lines = parking_detection.get_lines(img, mask, [1, 0.001, 10, 60, 40])
    #line_image = parking_detection.draw_lines(img, lines)
        
    # Detect vehicles in image
    car_lines = vehicle_segment.segmentation(filename)
    line_image = parking_detection.draw_lines(img, car_lines)

    # Post-processing on lines 
    h_lines = parking_detection.lines_processing(lines)
    parking_detection.get_scatter(h_lines)
    x, y, n = parking_detection.hc(n_clust)
    clust_lines = parking_detection.parking_spots(x, y, n)
    clust_lines = parking_detection.lines_processing(clust_lines)
    clust_lines_ext = parking_detection.extend_lines(clust_lines,border)

    line_image = parking_detection.draw_lines(img.copy(), clust_lines)
    cv2.imwrite("Outputs/parking_lines.png",line_image)

    # Getting parking spots
    blank = np.zeros(img.shape)
    parking_detection.highlight_spots(blank, clust_lines_ext, car_lines,border)

    # Creating output images
    blank = cv2.bitwise_and(blank.astype(np.uint8), 
                    np.dstack((mask, mask, mask)).astype(np.uint8))
    img = cv2.bitwise_or(img.astype(np.uint8), blank.astype(np.uint8))
    
    

    cv2.imshow("", img)
    cv2.waitKey(-1)
    cv2.imwrite("Outputs/final.png", img)


        
    