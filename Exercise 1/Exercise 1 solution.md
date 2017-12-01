# Exercise 1
How does a program read the cvMat object, in particular, what is the
order of the pixel structure?

## Answer:
The cvMat is a matrix structure that represents the pixels in the image. It stores pixel values of an image in the matrix. 
We can read the pixel values in cvMat by using cvMat at the particular pixel point (x,y), from entry point(0,0) at the top left of the matrix. Then it will read the type of the data.
If the pixel has multiple color channels, we can access a pixel by using cvMat at(x,y)[index], where index allows us to process pixel values of the color channels. Then we do image tranversal to get the pixel values.

The order of the pixel structure
should be bit depth, colorspaces, number of different color channels.
