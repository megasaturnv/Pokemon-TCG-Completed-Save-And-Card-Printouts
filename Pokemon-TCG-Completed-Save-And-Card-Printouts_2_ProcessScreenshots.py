#!/usr/bin/python3

# Pokemon-TCG-Completed-Save-And-Card-Printouts_2_ProcessScreenshots.py by MegaSaturnv

###########
# Imports #
###########
import argparse, glob, hashlib, os, time
from datetime import datetime
from datetime import timedelta
from PIL import Image
from shutil import copyfile


#############
# Functions #
#############
def createDirIfNotFound(filePath):
	dirPath = os.path.dirname(filePath)
	if not os.path.exists(dirPath):
		os.makedirs(dirPath)

def calculateMd5(filename):
	hasher = hashlib.md5()
	with open(filename, 'rb') as f:
		while True:
			data = f.read(4096)
			if not data:
				break
			hasher.update(data)
	return hasher.hexdigest()

def deleteDuplicateFilesInDir(directory):
	filenames = sorted([filename for filename in os.listdir(directory) if os.path.isfile(os.path.join(directory, filename))]) # Get a list of filenames to process, sorted alphabetically

	fileHashes = {} # Dictionary to store file hashes

	for filename in filenames:
		# Calculate the MD5 hash of the file's content
		with open(os.path.join(directory, filename), 'rb') as file:
			fileHash = hashlib.md5(file.read()).hexdigest()

		# Check if the hash is already in the dictionary
		if fileHash in fileHashes:
			print(f'Duplicate files: Deleting: {filename} (Matched with {fileHashes[fileHash]})')
			os.remove(os.path.join(directory, filename))
		else:
			# Store the hash and filename in the dictionary
			fileHashes[fileHash] = filename

def combineImages_2pages(output_path, page1Path, page2Path):
	# Open the three pages
	page1 = Image.open(page1Path)
	page2 = Image.open(page2Path)

	# Crop the rows from each page
	croppedPage1   = page1.crop((0, 0,  160, 138)) # Rows 1  to 138 of the first  image (138 pixels high)
	croppedPage2   = page2.crop((0, 80, 160, 144)) # Rows 81 to 144 of the second image (64 pixels high)

	# Create a new image with the desired size
	finalWidth = 160
	finalHeight = 138 + (144 - 80)
	#print('finalHeight = ' + str(finalHeight)) # Should be 276
	finalImage = Image.new('RGB', (finalWidth, finalHeight))

	# Paste the cropped pages onto the final image
	finalImage.paste(croppedPage1,   (0, 0))
	finalImage.paste(croppedPage2,   (0, 138))

	# Save the final image as a PNG
	finalImage.save(output_path, 'PNG')

def combineImages_3pages(output_path, page1Path, page2Path, page3Path):
	# Open the three pages
	page1 = Image.open(page1Path)
	page2 = Image.open(page2Path)
	page3 = Image.open(page3Path)

	# Crop the rows from each page
	croppedPage1   = page1.crop((0, 0,  160, 138)) # Rows 1  to 138 of the first  image (138 pixels high)
	croppedPage2_1 = page2.crop((0, 16, 160, 32))  # Rows 17 to 32  of the second image (16 pixels high)
	croppedPage2_2 = page2.crop((0, 80, 160, 138)) # Rows 81 to 138 of the second image (58 pixels high)
	croppedPage3   = page3.crop((0, 80, 160, 144)) # Rows 81 to 144 of the third  image (64 pixels high)

	# Create a new image with the desired size
	finalWidth = 160
	finalHeight = 138 + (32 - 16) + (138 - 80) + (144 - 80)
	#print('finalHeight = ' + str(finalHeight)) # Should be 276
	finalImage = Image.new('RGB', (finalWidth, finalHeight))

	# Paste the cropped pages onto the final image
	finalImage.paste(croppedPage1,   (0, 0))
	finalImage.paste(croppedPage2_1, (0, 138))
	finalImage.paste(croppedPage2_2, (0, 138 + 16))
	finalImage.paste(croppedPage3,   (0, 138 + 16 + 58))

	# Save the final image as a PNG
	finalImage.save(output_path, 'PNG')

def combineImages_4pages(output_path, page1Path, page2Path, page3Path, page4Path):
	# Open the four pages
	page1 = Image.open(page1Path)
	page2 = Image.open(page2Path)
	page3 = Image.open(page3Path)
	page4 = Image.open(page4Path)

	# Crop the rows from each page
	croppedPage1   = page1.crop((0, 0,  160, 138)) # Rows 1  to 138 of the first  image (138 pixels high)
	croppedPage2_1 = page2.crop((0, 16, 160, 32))  # Rows 17 to 32  of the second image (16 pixels high)
	croppedPage2_2 = page2.crop((0, 80, 160, 138)) # Rows 81 to 138 of the second image (58 pixels high)
	croppedPage3_1 = page3.crop((0, 16, 160, 32))  # Rows 17 to 32  of the third  image (16 pixels high)
	croppedPage3_2 = page3.crop((0, 80, 160, 138)) # Rows 81 to 138 of the third  image (58 pixels high)
	croppedPage4   = page4.crop((0, 80, 160, 144)) # Rows 81 to 144 of the forth  image (64 pixels high)

	# Create a new image with the desired size
	finalWidth = 160
	finalHeight = 138 + (32 - 16) + (138 - 80) + (32 - 16) + (138 - 80) + (144 - 80)
	#print('finalHeight = ' + str(finalHeight)) # Should be 350
	finalImage = Image.new('RGB', (finalWidth, finalHeight))

	# Paste the cropped pages onto the final image
	finalImage.paste(croppedPage1,   (0, 0))
	finalImage.paste(croppedPage2_1, (0, 138))
	finalImage.paste(croppedPage2_2, (0, 138 + 16))
	finalImage.paste(croppedPage3_1, (0, 138 + 16 + 58))
	finalImage.paste(croppedPage3_2, (0, 138 + 16 + 58 + 16))
	finalImage.paste(croppedPage4,   (0, 138 + 16 + 58 + 16 + 58))

	# Save the final image as a PNG
	finalImage.save(output_path, 'PNG')

def combineImages_5pages(output_path, page1Path, page2Path, page3Path, page4Path, page5Path):
	# Open the five pages
	page1 = Image.open(page1Path)
	page2 = Image.open(page2Path)
	page3 = Image.open(page3Path)
	page4 = Image.open(page4Path)
	page5 = Image.open(page5Path)

	# Crop the rows from each page
	croppedPage1   = page1.crop((0, 0,  160, 138)) # Rows 1  to 138 of the first  image (138 pixels high)
	croppedPage2_1 = page2.crop((0, 16, 160, 32))  # Rows 17 to 32  of the second image (16 pixels high)
	croppedPage2_2 = page2.crop((0, 80, 160, 138)) # Rows 81 to 138 of the second image (58 pixels high)
	croppedPage3_1 = page3.crop((0, 16, 160, 32))  # Rows 17 to 32  of the third  image (16 pixels high)
	croppedPage3_2 = page3.crop((0, 80, 160, 138)) # Rows 81 to 138 of the third  image (58 pixels high)
	croppedPage4_1 = page4.crop((0, 16, 160, 32))  # Rows 17 to 32  of the forth  image (16 pixels high)
	croppedPage4_2 = page4.crop((0, 80, 160, 138)) # Rows 81 to 138 of the forth  image (58 pixels high)
	croppedPage5   = page5.crop((0, 80, 160, 144)) # Rows 81 to 144 of the fifth  image (64 pixels high)

	# Create a new image with the desired size
	finalWidth = 160
	finalHeight = 138 + (32 - 16) + (138 - 80) + (32 - 16) + (138 - 80) + (32 - 16) + (138 - 80) + (144 - 80)
	#print('finalHeight = ' + str(finalHeight)) # Should be 424
	finalImage = Image.new('RGB', (finalWidth, finalHeight))

	# Paste the cropped pages onto the final image
	finalImage.paste(croppedPage1,   (0, 0))
	finalImage.paste(croppedPage2_1, (0, 138))
	finalImage.paste(croppedPage2_2, (0, 138 + 16))
	finalImage.paste(croppedPage3_1, (0, 138 + 16 + 58))
	finalImage.paste(croppedPage3_2, (0, 138 + 16 + 58 + 16))
	finalImage.paste(croppedPage4_1, (0, 138 + 16 + 58 + 16 + 58))
	finalImage.paste(croppedPage4_2, (0, 138 + 16 + 58 + 16 + 58 + 16))
	finalImage.paste(croppedPage5,   (0, 138 + 16 + 58 + 16 + 58 + 16 + 58))

	# Save the final image as a PNG
	finalImage.save(output_path, 'PNG')

def combineImages_6pages(output_path, page1Path, page2Path, page3Path, page4Path, page5Path, page6Path):
	# Open the five pages
	page1 = Image.open(page1Path)
	page2 = Image.open(page2Path)
	page3 = Image.open(page3Path)
	page4 = Image.open(page4Path)
	page5 = Image.open(page5Path)
	page6 = Image.open(page6Path)

	# Crop the rows from each page
	croppedPage1   = page1.crop((0, 0,  160, 138)) # Rows 1  to 138 of the first  image (138 pixels high)
	croppedPage2_1 = page2.crop((0, 16, 160, 32))  # Rows 17 to 32  of the second image (16 pixels high)
	croppedPage2_2 = page2.crop((0, 80, 160, 138)) # Rows 81 to 138 of the second image (58 pixels high)
	croppedPage3_1 = page3.crop((0, 16, 160, 32))  # Rows 17 to 32  of the third  image (16 pixels high)
	croppedPage3_2 = page3.crop((0, 80, 160, 138)) # Rows 81 to 138 of the third  image (58 pixels high)
	croppedPage4_1 = page4.crop((0, 16, 160, 32))  # Rows 17 to 32  of the forth  image (16 pixels high)
	croppedPage4_2 = page4.crop((0, 80, 160, 138)) # Rows 81 to 138 of the forth  image (58 pixels high)
	croppedPage5_1 = page5.crop((0, 16, 160, 32))  # Rows 17 to 32  of the fifth  image (16 pixels high)
	croppedPage5_2 = page5.crop((0, 80, 160, 138)) # Rows 81 to 138 of the fifth  image (58 pixels high)
	croppedPage6   = page6.crop((0, 80, 160, 144)) # Rows 81 to 144 of the sixth  image (64 pixels high)

	# Create a new image with the desired size
	finalWidth = 160
	finalHeight = 138 + (32 - 16) + (138 - 80) + (32 - 16) + (138 - 80) + (32 - 16) + (138 - 80) + (32 - 16) + (138 - 80) + (144 - 80)
	#print('finalHeight = ' + str(finalHeight)) # Should be 424
	finalImage = Image.new('RGB', (finalWidth, finalHeight))

	# Paste the cropped pages onto the final image
	finalImage.paste(croppedPage1,   (0, 0))
	finalImage.paste(croppedPage2_1, (0, 138))
	finalImage.paste(croppedPage2_2, (0, 138 + 16))
	finalImage.paste(croppedPage3_1, (0, 138 + 16 + 58))
	finalImage.paste(croppedPage3_2, (0, 138 + 16 + 58 + 16))
	finalImage.paste(croppedPage4_1, (0, 138 + 16 + 58 + 16 + 58))
	finalImage.paste(croppedPage4_2, (0, 138 + 16 + 58 + 16 + 58 + 16))
	finalImage.paste(croppedPage5_1, (0, 138 + 16 + 58 + 16 + 58 + 16 + 58))
	finalImage.paste(croppedPage5_2, (0, 138 + 16 + 58 + 16 + 58 + 16 + 58 + 16))
	finalImage.paste(croppedPage6,   (0, 138 + 16 + 58 + 16 + 58 + 16 + 58 + 16 + 58))

	# Save the final image as a PNG
	finalImage.save(output_path, 'PNG')


#################
# Main Function #
#################
def main():
	###################
	# Parse Arguments #
	###################
	parser = argparse.ArgumentParser(description='description')

	parser.add_argument('-v', '--verbose', help='Be Verbose and print debug output', action='store_true')

	args = parser.parse_args()

	if args.verbose:
		print('Argument verbose: ' + str(args.verbose))


	############
	# Settings #
	############
	screenshotDirectory = '/home/megasaturnv/Pictures/Pokemon-TCG-Completed-Save-And-Card-Printouts_Screenshots/'
	outputDirectory = '/home/megasaturnv/Pictures/Pokemon-TCG-Completed-Save-And-Card-Printouts_Output/'


	#################################
	# Variable setup & Calculations #
	#################################
	FirstLetterList = ['A', 'B', 'C', 'D', 'E', 'P']


	################
	#  Main script #
	################
	createDirIfNotFound(outputDirectory)

	print('Duplicate files: Deleting duplicate files in screenshot directory.')
	deleteDuplicateFilesInDir(screenshotDirectory)
	print('Duplicate files: Done!')

	print('Processing images: Cropping and stitching them together...')
	for firstLetter in FirstLetterList:
		cardNumber = 1
		while(os.path.isfile(os.path.join(screenshotDirectory, firstLetter + f'{cardNumber:02d}' + '_1.png'))):
			#print('Creating: ' + outputDirectory + firstLetter + f'{cardNumber:02d}' + '.png')
			matchingFiles = glob.glob(os.path.join(screenshotDirectory, firstLetter + f'{cardNumber:02d}' + '_*'))
			matchingFiles = sorted(matchingFiles)
			match len(matchingFiles):
				case 1: # The card has 1 page, so it is a trainer or energy card. Nothing to do except copy it to the output directory
					copyfile(matchingFiles[0], outputDirectory + firstLetter + f'{cardNumber:02d}' + '.png')
				case 2: # Only B45, C48 and D48 have two pages
					combineImages_2pages(outputDirectory + firstLetter + f'{cardNumber:02d}' + '.png', matchingFiles[0], matchingFiles[1])
				case 3: # The card has 3 pages, so it is a Pokemon that knows 1 move
					combineImages_3pages(outputDirectory + firstLetter + f'{cardNumber:02d}' + '.png', matchingFiles[0], matchingFiles[1], matchingFiles[2])
				case 4: # The card has 4 pages, so it is a Pokemon that knows 2 moves
					combineImages_4pages(outputDirectory + firstLetter + f'{cardNumber:02d}' + '.png', matchingFiles[0], matchingFiles[1], matchingFiles[2], matchingFiles[3])
				case 5: # The card has 5 pages, so it is a Pokemon that knows 2 moves + an extra page for detail
					combineImages_5pages(outputDirectory + firstLetter + f'{cardNumber:02d}' + '.png', matchingFiles[0], matchingFiles[1], matchingFiles[2], matchingFiles[3], matchingFiles[4])
				case 6:	# P19 is the only card which has 6 pages
					combineImages_6pages(outputDirectory + firstLetter + f'{cardNumber:02d}' + '.png', matchingFiles[0], matchingFiles[1], matchingFiles[2], matchingFiles[3], matchingFiles[4], matchingFiles[5])
				case _:
					print('Warning: ' + matchingFiles[0] + ' has ' + str(len(matchingFiles)) + ' pages')
			cardNumber = cardNumber + 1
	print('Processing images: Done!')


#############################
# if __name__ == '__main__' #
#############################
if __name__ == '__main__':
	main()

#	try:
#		main()
#	except Exception as e:
#		...
