# Removing-Hand-Written-Annotations
Repository for the project of removing hand-written annotations from scanned document.

* Firstly, we are using OTSU algorithm in the OpenCV library to binarize the image of the document and saving it as imgnew.jpg.

### Image before Binarization
<img src="imgchk.jpeg" width="50%" height="auto" data-rotate="90"/>

### Image after Binarization
<img src="imgnew.jpg" width="50%" height="auto"/>

* Now, after this, we are using the Breadth First Search(BFS) to find the connected components by first converting the binarized image to a list of RGB values and then applying the BFS algorithm to find the heights and widths of the connected components and then storing the result in <a href="heightandwidth.txt">heightandwidth.txt</a>
