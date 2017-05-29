#import all needed libraires
from helper import *
from moviepy.editor import VideoFileClip
from IPython.display import HTML
import os
# read image
def process_image(image):
    # NOTE: The output you return should be a color image (3 channel) for processing video below
    # TODO: put your pipeline here,
    # you should return the final output (image where lines are drawn on lanes)
    # Grayscale
    gray = grayscale(image)
    # Guassian smoothing
    blur_gray = gaussian_blur(gray, 5)

    # Apply canny edge detection
    low_threshold = 50
    high_threshold = 150
    edges = canny(blur_gray, low_threshold, high_threshold)
    # Next we'll create a masked edges image
    imshape = image.shape
    vertices = np.array([[(0,imshape[0]),(450, 310), (492, 320), (imshape[1],imshape[0])]], dtype=np.int32)
    masked_edges = region_of_interest(edges, vertices)

    # Define the Hough transform parameters

    # Make a blank the same size as our image to draw on
    rho = 2 # distance resolution in pixels of the Hough grid
    theta = np.pi/180 # angular resolution in radians of the Hough grid
    threshold = 15     # minimum number of votes (intersections in Hough grid cell)
    min_line_length = 40 #minimum number of pixels making up a line
    max_line_gap = 20   # maximum gap in pixels between connectable line segments
    lines_edges = hough_lines(masked_edges, rho, theta, threshold, min_line_length, max_line_gap)
    # Combine
    result = weighted_img(lines_edges, image)
    # showing result
    return result


white_output = 'output.mp4'
#read the test vedio
clip1 = VideoFileClip("solidWhiteRight.mp4")
white_clip = clip1.fl_image(process_image)

white_clip.write_videofile(white_output, audio=False)
