import cv2
def distance(p1, p2):
	# D8 distance
	return max(abs(p1[0] - p2[0]), abs(p1[1] - p2[1]))


def gamma(img):
	totalpixels = img.shape[0] * img.shape[1]
	color_dict = {}
	for i in range(len(img)):
		for j in range(len(img[i])):
			tc = tuple(img[i][j])
			if (tc in color_dict):
				color_dict[tc].append((i, j))
			else:
				color_dict[tc] = [(i, j)]

	probability = {}

	for d in range(8):
		for color in color_dict:
			count = 0
			k = color_dict[color]
			for p1 in range(len(k)):
				for p2 in range(p1, len(k)):
					if (distance(k[p1], k[p2]) == d):
						count += 1
			if color not in probability:
				probability[color] = [0 for i in range(8)]

			probability[color][d] = float(count) / totalpixels

	return probability


img = cv2.imread("bed.jpg")
img2 = cv2.imread("img2.jpg")

g1 = gamma(img)
g2 = gamma(img2)

s = 0
m = 0
for color in g1:
	if color not in g2:
		continue
	m += 1
	for d in range(8):
		s += abs(g1[color][d] - g2[color][d]) / float(1 + g1[color][d] + g2[color][d])

s /= float(m)
print(s)