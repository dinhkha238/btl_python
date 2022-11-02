import cv2
def cropImage(self,img,x1,y1,x2,y2):
        img_crop = img[y1:y2, x1:x2]  # [ y1:y2 , x1:x2 ]
        return img_crop
def click_event(event, x, y, flags, params):
	if event == cv2.EVENT_LBUTTONDOWN:
		# self.x1 = x
		# self.y1 = y
		print(x, ' ', y)
		
	if event==cv2.EVENT_LBUTTONUP:
		print(x, ' ', y)
		# cv2.destroyWindow("image")
		# img = self.cropImage(self.img_changed,self.x1,self.y1,x,y)
		# self.default = self.cropImage(self.default,self.x1,self.y1,x,y)
		# self.img_changed = img

	# img = self.cropImage(self.img_changed)
	# self.default = self.cropImage(self.default)
	# self.img_changed = img
	# self.setPhoto(self.img_changed)
img = cv2.imread('R.jpg')
# imgSeted = cv2.resize(img,(640, 640))
cv2.imshow('image', img)
cv2.setMouseCallback('image',click_event)
cv2.waitKey(0)