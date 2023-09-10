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
def printVerbose(string):
	if args.verbose:
		print("Debug: " + string)

def createDirIfNotFound(filePath):
	dirPath = os.path.dirname(filePath)
	if not os.path.exists(dirPath):
		os.makedirs(dirPath)

def deleteDuplicateFilesInDir(directory):
	filenames = sorted([filename for filename in os.listdir(directory) if os.path.isfile(os.path.join(directory, filename))]) # Get a list of filenames to process, sorted alphabetically

	fileHashes = {} # Dictionary to store file hashes

	for filename in filenames:
		# Calculate the MD5 hash of the file's content. Exported pngs have minimal metadata so we can compare their hashes to look for duplicates
		with open(os.path.join(directory, filename), 'rb') as file:
			fileHash = hashlib.md5(file.read()).hexdigest()

		# Check if the hash is already in the dictionary
		if fileHash in fileHashes:
			print(f'Duplicate files: Deleting: {filename} (Matched with {fileHashes[fileHash]})')
			os.remove(os.path.join(directory, filename))
		else:
			# Store the hash and filename in the dictionary
			fileHashes[fileHash] = filename

def combineImages_pagesList(listPagePath):
	if len(listPagePath) == 1: # One page
		return Image.open(listPagePath[0])
	elif 2 <= len(listPagePath) <= 6: # Two to six pages
		# Open the pages
		listPagesImage = []
		for i in range(0, len(listPagePath)):
			listPagesImage.append(Image.open(listPagePath[i]))

		# Crop the rows from each page
		listPagesImageCropped = []
		listPagesImageCropped.append(  listPagesImage[0].crop((0, 0,  160, 138))  ) # Rows 1  to 138 of the first  image (138 pixels high)
		for i in range(1, len(listPagePath)-1): # Use range(1, len(listPagePath)-1) to process page 2 to one from the last page. For two pages in total, we skip this loop entirely
			listPagesImageCropped.append(  listPagesImage[i].crop((0, 16, 160, 32 ))  ) # Rows 17 to 32  of the image (16 pixels high)
			listPagesImageCropped.append(  listPagesImage[i].crop((0, 80, 160, 138))  ) # Rows 81 to 138 of the image (58 pixels high)
		listPagesImageCropped.append(  listPagesImage[-1].crop((0, 80, 160, 144))  ) # Rows 81 to 144 of the last image (64 pixels high)

		# Create a new image with the desired size
		finalWidth = 160
		finalHeight = 138 + (len(listPagePath)-2) * ((32 - 16) + (138 - 80)) + (144 - 80)
		#printVerbose('finalHeight = ' + str(finalHeight))
		finalImage = Image.new('RGB', (finalWidth, finalHeight))

		# Paste the cropped pages onto the final image
		finalImage.paste(listPagesImageCropped[0], (0, 0)) # First page
		for i in range(0, len(listPagePath)-2): # Loop for pages n+1 to n-1
			finalImage.paste(listPagesImageCropped[(i+1) * 2 - 1], (0, 138 + i * ((32 - 16) + (138 - 80)))) # Paste even-numbered pages (if zero-indexed. Odd-numbered pages if one-indexed)
			finalImage.paste(listPagesImageCropped[(i+1) * 2], (0, 138 + i * ((32 - 16) + (138 - 80)) + (32 - 16))) # Paste odd-numbered pages (if zero-indexed. Even-numbered pages if one-indexed)

		finalImage.paste(listPagesImageCropped[-1],   (0, 138 + (len(listPagePath)-2) * ((32 - 16) + (138 - 80)))) # Last page

		# Save the final image as a PNG
		#finalImage.save(outputPath, 'PNG')

		return finalImage
	else: # More than 6 pages, which shouldn't happen
		print("Warning: Invalid number of pages sent to combineImages_pagesList()")
		return Image.new('RGB', (1, 1)) # Return a blank 1x1 pixel image


#################
# Main Function #
#################
def main():
	###################
	# Parse Arguments #
	###################
	parser = argparse.ArgumentParser(description='description')

	parser.add_argument('-v', '--verbose', help='Be Verbose and print debug output', action='store_true')

	global args
	args = parser.parse_args()


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
	deleteDuplicateFilesInDir(screenshotDirectory) # We have to do this as the lua script from before will have created duplicates
	print('Duplicate files: Done!')

	print('Processing images: Cropping and stitching them together...')
	for firstLetter in FirstLetterList: # Go through each starting letter
		cardNumber = 1
		while(os.path.isfile(os.path.join(screenshotDirectory, firstLetter + f'{cardNumber:02d}' + '_1.png'))): # Loop through until we exceed the number of card numbers in this letter's set
			#printVerbose('Creating: ' + outputDirectory + firstLetter + f'{cardNumber:02d}' + '.png')

			matchingFiles = glob.glob(os.path.join(screenshotDirectory, firstLetter + f'{cardNumber:02d}' + '_*')) # Get list of files to process
			matchingFiles = sorted(matchingFiles) # Make sure the files are in alphabetical order

			combineImages_pagesList(matchingFiles).save(outputDirectory + firstLetter + f'{cardNumber:02d}' + '.png', 'PNG') # Crop and combine the images, then save them to a new file in outputDirectory

			cardNumber = cardNumber + 1 # Increment to the next card

		printVerbose('Processed ' + str(cardNumber-1) + ' cards beginning with ' + firstLetter)

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
