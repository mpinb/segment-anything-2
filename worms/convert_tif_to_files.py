# this python script converts a tif file that it gets as input to a series of jpg files
# and saves them in the directory whose path is given as second argument
# the tif file is assumed to be a multi-page tif file
# the jpg files are named as the number of the page in the tif file
# the jpg files are saved in the directory whose path is given as second argument

import sys
import os
import tifffile as tiff
from PIL import Image

from skimage import img_as_ubyte, exposure

# the images are in a 16-bit format we will convert the images to 8-bit format and save them as jpg
def convert_tif_to_jpg(tif_file_path, jpg_dir_path):
    with tiff.TiffFile(tif_file_path) as tif:
        images = tif.asarray()
        padding = len(str(images.shape[0]))
        for indx, img in enumerate(images):
            # convent the 16-bit grayscale image to an 8-bit grayscale image
            img_8bit = img_as_ubyte(exposure.rescale_intensity(img))
            image = Image.fromarray(img_8bit)
            # save the image as jpg
            frame_number = str(indx).zfill(padding)
            #image.save(os.path.join(jpg_dir_path, f'frame_{frame_number}.jpg'), format='JPEG')
            image.save(os.path.join(jpg_dir_path, f'{frame_number}.jpg'), format='JPEG')
        
    print(f'Conversion completed. {images.shape[0]} jpg files were created.')
    print(f'The jpg files are saved in the directory: {jpg_dir_path}')
    
# extract the tif array and save the frames as tif files
def convert_tif_to_tif(tif_file_path, tif_dir_path):
    with tiff.TiffFile(tif_file_path) as tif:
        images = tif.asarray()
        padding = len(str(images.shape[0]))
        for i in range(images.shape[0]):
            frame_number = str(i).zfill(padding)
            tiff.imwrite(os.path.join(tif_dir_path, f'frame_{frame_number}.tif'), images[i])
        
    print(f'Conversion completed. {images.shape[0]} tif files were created.')
    print(f'The tif files are saved in the directory: {tif_dir_path}')
        
if __name__ == '__main__':
    
    with tiff.TiffFile(sys.argv[1]) as tif:
        images = tif.asarray()
        print(images.shape)  # This will show the dimensions of the stack    
    
    # if the output directory does not exist, create it
    if not os.path.exists(sys.argv[2]):
        os.makedirs(sys.argv[2])
        
    #convert_tif_to_tif(sys.argv[1], sys.argv[2])
    convert_tif_to_jpg(sys.argv[1], sys.argv[2])

    
# Usage: python convert_tif_to_files.py <tif_file_path> <files_dir_path>
