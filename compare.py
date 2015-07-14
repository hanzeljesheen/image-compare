from skimage.measure import structural_similarity as ssim
import numpy as np
import cv2
import urllib2

def fetchImg(url):
    req = urllib2.urlopen(url)
    arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
    img = cv2.imdecode(arr,-1)
    image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    dim = (100, 100)
    resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
    return resized;

def compare_images(imageA, imageB):
	s = ssim(imageA, imageB)
	return abs(round(s*100))
	
def getSimilar(img1, img2):
    print 'Fetching,', img1, "..."
    img1 = fetchImg(img1)
    print 'Fetching,', img2, "..."
    img2 = fetchImg(img2)
    print "Processing..."
    return compare_images(img1, img2)
