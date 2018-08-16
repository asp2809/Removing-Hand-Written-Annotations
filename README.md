# Removing-Hand-Written-Annotations
Repository for the project of removing hand-written annotations from scanned document.


## Task-1: Binarizing the Image

* For this task, we are using OTSU algorithm in the OpenCV library to binarize the image of the document and saving it as imgnew.jpg.

### Image before Binarization
<img src="imgchk.jpeg" width="50%" height="auto" data-rotate="90"/>

### Image after Binarization
<img src="imgnew.jpg" width="50%" height="auto"/>


## Task-2: Finding the connected components in the Image

* Now, for proceeding further, we are using the Breadth First Search(BFS) to find the connected components by first converting the binarized image to a list of RGB values and then applying the BFS algorithm to find the heights and widths of the connected components and then storing the result in <a href="heightandwidth.txt">heightandwidth.txt</a>

## Task-3: Extracting the annotations part from the Image

* In the <a href="blackpixels.py">blackpixels.py</a> file, we are first calculating the number of black pixels in a row and then by setting a threshold, we are extracting the part in which only the annotations and white gaps between the lines are present.

* After this, we are using the matplotlib imshow to generate an image consisting only the rows which we got as an output from the above approach.

### Image containing the Annotations and the Blank Spaces between the Lines
<img src="annotations.png">

## Task-4: Smoothening of the Annnotations retrieved from the Document

* We are using the <a href="connectedcompusingbfs.py">connectedcompusingbfs.py</a> to find the lengths and widths of the connected components in the <a href="annotations.png">annotations.png</a>. Then, the annotations which have the lengths greater than a given threshold and then extracting the selected ones only.

### Output of connectedcompusingbfs.py
<img src="annotations1.png">

* After this, using <a href="smoothing.py">smoothing.py</a>, we have joined the broken lines using a slab of array for which we are calculating the sum of the pixel values and then using a threshold above which if the summation value goes, then the complete slab is filled with black pixels.

### Output after Smoothening using smoothing.py
<img src="smoothen.png">
