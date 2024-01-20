# imageEditor
Take one image and resize and add an unsharp mask.

The image will be resized to a 200x200, 120x120, and 85x85, and then the 200x200 image will have a canvas
size change to make it 300x200. The first three resized images will each be given an unsharp mask to increase
the quality of the photo.

Two folders, imgs and editedImgs, need to be present in the directory of the script. Images put in the
imgs folder will be turned into 4 separate, edited images and placed into the editedImgs folder.
