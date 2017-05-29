# Finding Lane Lines on the Road

The goals / steps of this project are the following:
* Finding lane lines on the road from a vedio

# Overview

A viedio is made of a series of images, if we can detect lines in images, we can do it for vedios as well. 
The steps are as follows: 

**Grayscale**
![gray](https://cloud.githubusercontent.com/assets/15232969/26561653/0e0c85c2-448e-11e7-920c-627a855c620c.jpg)

**Canny edge detection**
![edges](https://cloud.githubusercontent.com/assets/15232969/26561652/0b746b9a-448e-11e7-8e46-7603a213761d.jpg)

**Hough_lines transformation**
![lines_edges](https://cloud.githubusercontent.com/assets/15232969/26561654/11b89396-448e-11e7-869c-b5ff8a1df7f8.jpg)

**Finally if we combine the result with the original image**
![output](https://cloud.githubusercontent.com/assets/15232969/26561657/1357633a-448e-11e7-9e82-3ccb1807e8b0.jpg)



