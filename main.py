#!/usr/bin/env python
# Simple atlas file generator for libGDX
# Original https://github.com/patwork/libgdx-sprite-sheet-to-atlas
# Reworked by Stefano Lupo Feb 2019
#

import sys
import os
import json

def createAtlas(args):
	spriteSheetFilenameWithPath = args[1]
	jsonFilename = args[2]

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

	rowInfo = metadata["row_info"]
	maxNumCols = max(rowInfo, key=lambda x : x["num_cols"])["num_cols"]
	numRows = len(rowInfo)
	spriteWidth = spriteSheetWidth / maxNumCols
	spriteHeight = spriteSheetHeight / numRows

	print("Using max number of columns: " + str(maxNumCols))
	print("Using sprite dimensions: %fx%f" % (spriteWidth, spriteHeight))
	
	headerFormat = "{}\nsize: {},{}\nformat: RGBA8888\nfilter: Linear,Linear\nrepeat: none\n"
	header = headerFormat.format(spriteSheetFileName, spriteSheetWidth, spriteSheetHeight)

	# Format with formattedName_colNumber, x, y, sizeX, sizeY, origX, origY, offsetX, offsetY
	bodyFormat = "{}_{:05d}\n\trotate: false\n\txy: {}, {}\n\tsize: {}, {}\n\torig: {}, {}\n\toffset: {}, {}\n\tindex: -1\n"

	with open(atlasFilename, "w+") as atlas:
		atlas.write(header)
		rowCounter = 0
		for row in rowInfo:
			name = row["name"]
			numCols = row["num_cols"]
			for i in range(0, numCols):
				x = i * spriteWidth
				y = rowCounter * spriteWidth
				body = bodyFormat.format(name, i, x, y, spriteWidth, spriteHeight, spriteWidth, spriteHeight, 0, 0)
				atlas.write(body)
		rowCounter = rowCounter + 1


if __name__ == '__main__':

	if len(sys.argv) != 3:
		sys.stderr.write("Invalid usage: Use python3 %s <sprite-sheet-filename> <json-filename>\n" % __file__)
		sys.exit(1)

	createAtlas(sys.argv)
	sys.exit(0)