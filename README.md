# Parking_Spot_Detection

These codes were written on and compiled on Linux (Ubuntu 18.04.1 LTS)

Take a picture from the Sample Images folder. Paste it to the main directory and rename it
to example.png. One such example image is already given in the main folder.

If you are running the Cardamom image, then set border = 700 and n_clust = 9



Open the terminal from the main folder and run the command "python3 main.py"

If it prompts you to install any dependencies, then please install them using 
"pip3 install dependency-name"

## OUTPUTS:

*All Outputs are stores in the Outputs folder off the main directory

cannyed_image.png - The output of the canny edge detector on the image

image_bbox_floor.png - The image with the floors of the bounding boxes of the cars

mask_image.png - This outputs the road that is segmented from the image

parking_lines.png - The detected parking lines marked on the original image

final.png - The image with the vacant parking spots highlighted as green and the occupied
	parking spots highlighted as red

 
