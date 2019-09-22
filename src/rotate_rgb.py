#coding: utf-8

import numpy
from PIL import Image, ImageOps

if __name__ == '__main__':
	rotate = [[1, 0], [0, 1]]
	output_fname = "./outimg.jpg"

	boffset_x = 128
	boffset_y = 128
	bmax_x = 256
	bmax_y = 256
	aoffset_x = 128 * 2
	aoffset_y = 128 * 2
	amax_x = 256 * 2
	amax_y = 256 * 2
	bpic = numpy.empty((bmax_x, bmax_y, 3), dtype = "uint8")
	apic = numpy.empty((amax_x, amax_y, 3), dtype = "uint8")


	for i in range(0, bmax_x, 1):
		for j in range(0, bmax_y, 1):
			bpic[i, j, 0] = i - 128 #折り返される。(uint8)
			bpic[i, j, 1] = j - 128 #折り返される。(uint8)
			bpic[i, j, 2] = 255

	apic[ : , : , : ] = 255

	for i in range(0, bmax_x, 1):
		for j in range(0, bmax_y, 1):
			x = rotate[0][0] * (i - boffset_x) + rotate[0][1] * (j - boffset_y)
			y = rotate[1][0] * (i - boffset_x) + rotate[1][1] * (j - boffset_y)
			x = int(x) + aoffset_x
			y = int(y) + aoffset_y
			if( 0 <= x and x < amax_x and  0 <= y and y < amax_y):
				apic[x, y, :] = bpic[i, j, :]
	
	apic[aoffset_x, : , : ] =(0, 0, 0)
	apic[ : , aoffset_y, : ] =(0, 0, 0)
	
	output_pic = Image.fromarray(apic)
	output_pic = output_pic.rotate(90, expand = True)
	output_pic.save(output_fname)

	print("出力画像ファイル: " + output_fname)
	print("下記行列にて一次変換が完了しました。")
	print( "(" + str(rotate[0][0]) + "," + str(rotate[0][1])  + ")\n" + "(" + str(rotate[1][0]) + "," + str(rotate[1][1]) + ")")
