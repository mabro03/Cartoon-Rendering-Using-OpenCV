import cv2

# 강아지 사진 이미지 로드
img = cv2.imread('Mong.jpg')

#회색조로 변환
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#노이즈 제거를 위한 가우시안 블러 적용
gray = cv2.GaussianBlur(gray, (5, 5), 0)

#엣지 검출을 위한 thresholding 적용
edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 10)

#컬러 이미지를 부드럽게 하기 위해 bilateral filter 적용
color = cv2.bilateralFilter(img, 9, 250, 250)

#엣지와 컬러 결합
cartoon = cv2.bitwise_and(color, color, mask=edges)

#이미지 띄우기
cv2.namedWindow("Cartoon Rendering", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Cartoon Rendering", 600, 600)
cv2.imshow("Cartoon Rendering", cartoon)
#키보드 기다리기
cv2.waitKey(0)
#창 닫기
cv2.destroyAllWindows()
