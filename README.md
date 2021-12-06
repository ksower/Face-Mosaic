# Face-Mosaic

This project is to develop a program that detects faces and mosaics them in a selected image or video. For face detection, cvlib was used, and it was developed with python opencv.


## Main Function
1. mosaic
2. sticker
3. color box

Use the above methods to mask the detected face in the image.


## Language
- python
- library : tkinter, cvlib, opencv


## Manual
![mosaicImg_ui](https://user-images.githubusercontent.com/67861728/144836425-36670444-1633-477a-a31c-664f2ff53702.png)

1. Select file to process.
2. Select the option to process. Set the fps for mosaic ratio and video. Choose from mosaics, stickers, and colorboxes. For stickers, choose the image you want to use. For colorbox, choose a color.
3. If you click the process button, processing proceeds, and the completed image or video is saved as result.jpg or result.avi file in the same directory.
