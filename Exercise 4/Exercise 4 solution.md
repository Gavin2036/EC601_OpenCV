# Exercise 4
1. Look at Threshold.cpp and implement the code in Python, and observe the results for different threshold values. Comment on the results.

2. What are the disadvantages of binary threshold?

3. When is Adaptive Threshold useful?

##1.
In the binary threshold, we used a global value as threshold value.
But it may not be good in all the conditions where image has different lighting conditions in different areas. 
In that case, we go for adaptive thresholding. In this, the algorithm calculate the threshold for a small regions of the image.
So we get different thresholds for different regions of the same image and
it gives us better results for images with varying illumination.

##2.
### Limited application: 
as the representation is only a silhouette, application is restricted to tasks where internal detail is not required as a distinguishing characteristic.
### Does not extend to 3D: 
the 3D nature of objects can rarely be represented by silhouettes. (The 3D equivalent of binary processing uses
### Specialised lighting is required for silhouettes: 
it is difficult to obtain reliable binary images without restricting the environment. The simplest example is an overhead projector or light box.

##3.
Adaptive thresholding changes the threshold dynamically over the image. This more sophisticated version of thresholding can accommodate changing lighting conditions in the image.
