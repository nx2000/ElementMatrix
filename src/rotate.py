#coding: utf-8

import numpy
from PIL import Image, ImageOps
import math

if __name__ == '__main__':
	cos = math.cos
	sin = math.sin
	pi = math.pi
	theta = pi / 6
	rotate = [[cos(theta), -sin(theta)], [sin(theta), cos(theta)]]
	input_fname = "./img.jpg"
	output_fname = "./outimg.jpg"

	input_pic = Image.open(input_fname)

	input_pic = input_pic.rotate(-90, expand = True)
	bpic = numpy.array(input_pic)
	size = bpic.shape
	offset_x = size[0] * 2
	offset_y = size[1] * 2
	max_x = size[0] * 4
	max_y = size[1] * 4
	apic = numpy.empty((max_x , max_y, size[2]), dtype = "uint8")

	apic[ : , : , : ] = 255
	apic[offset_x, : , : ] =(0, 0, 0)
	apic[ : , offset_y, : ] =(0, 0, 0)
	for i in range(0, size[0], 1):
		for j in range(0, size[1], 1):
			x = rotate[0][0] * i + rotate[0][1] * j + offset_x
			y = rotate[1][0] * i + rotate[1][1] * j + offset_y
			x = int(x)
			y = int(y)
			if( 0 <= x and x < max_x and  0 <= y and y < max_y):
				apic[x, y, :] = bpic[i, j, :]
		
	output_pic = Image.fromarray(apic)
	output_pic = output_pic.rotate(90, expand = True)
	output_pic.save(output_fname)
	print("入力画像ファイル: " + input_fname)
	print("出力画像ファイル: " + output_fname)
	print("下記行列にて一次変換が完了しました。")
	print( "(" + str(rotate[0][0]) + "," + str(rotate[0][1])  + ")\n" + "(" + str(rotate[1][0]) + "," + str(rotate[1][1]) + ")")
