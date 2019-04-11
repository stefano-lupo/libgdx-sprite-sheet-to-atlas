#!/usr/bin/env python
# Simple atlas file generator for libGDX
# Original https://github.com/patwork/libgdx-sprite-sheet-to-atlas
# Reworked by Stefano Lupo Feb 2019 to use a JSON file instead of CL args
#

import sys
import os
import json

def createAtlas(args):
	spriteSheetFilenameWithPath = args[1]
	jsonFilename = args[2]
	isSpriteType = not args[3]

	directory = os.path.dirname(spriteSheetFilenameWithPath)
	spriteSheetFileName = os.path.basename(spriteSheetFilenameWithPath)
	extension = os.path.splitext(spriteSheetFileName)[1]
	spriteName = spriteSheetFileName[:len(extension)]
	atlasFilename = os.path.join(directory, spriteName + ".atlas")

	print("Directory: " + directory)
	print("SpriteSheet Filename: " + spriteSheetFileName)
	print("Extension: " + extension)
	print("Spritename: " + spriteName)
	print("Atlas Filename: " + atlasFilename)
	
	with open(jsonFilename, "r") as f:
		metadata = json.load(f)

	spriteSheetWidth = metadata["width"]
	spriteSheetHeight = metadata["height"]

	rowInfo = metadata["rowInfo"]
	maxNumCols = max(rowInfo, key=lambda x : x["numCols"])["numCols"]
	numRows = len(rowInfo)

	if isSpriteType:
		spriteWidth = int(spriteSheetWidth / maxNumCols)
		spriteHeight = int(spriteSheetHeight / numRows)
	else:
		spriteWidth = int(args[4])
		spriteHeight = int(args[5])

	print("Using max number of columns: " + str(maxNumCols))
	print("Using sprite dimensions: %fx%f" % (spriteWidth, spriteHeight))
	
	headerFormat = "{}\nsize: {},{}\nformat: RGBA8888\nfilter: Linear,Linear\nrepeat: none\n"
	header = headerFormat.format(spriteSheetFileName, spriteSheetWidth, spriteSheetHeight)

	# Format with formattedName_colNumber, x, y, sizeX, sizeY, origX, origY, offsetX, offsetY
	bodyFormat = "{}_{:05d}\n\trotate: false\n\txy: {}, {}\n\tsize: {}, {}\n\torig: {}, {}\n\toffset: {}, {}\n\tindex: -1\n"

	with open(atlasFilename, "w+") as atlas:
		atlas.write(header)

		if (isSpriteType):	
			rowCounter = 0
			for row in rowInfo:
				name = row["name"]
				numCols = row["numCols"]
				for i in range(0, numCols):
					x = i * spriteWidth
					y = rowCounter * spriteWidth
					body = bodyFormat.format(name, i, x, y, spriteWidth, spriteHeight, spriteWidth, spriteHeight, 0, 0)
					atlas.write(body)
				rowCounter = rowCounter + 1
		else:
			x = 0
			y = 0
			for row in rowInfo:
				name = row["name"]
				body = bodyFormat.format(name, 0, x, y, spriteWidth, spriteHeight, spriteWidth, spriteHeight, 0, 0)
				atlas.write(body)
				x = x + spriteWidth
				if (x == spriteSheetWidth):
					x = 0
					y = y + spriteHeight
				

if __name__ == '__main__':

	if len(sys.argv) != 4 and len(sys.argv) != 6:
		sys.stderr.write("Invalid usage: Use python3 %s <sprite-sheet-filename> <json-filename> <0|1 for sprite/texture> <sprite_width> <sprite_height>\n" % __file__)
		sys.exit(1)

	createAtlas(sys.argv)
	sys.exit(0)
