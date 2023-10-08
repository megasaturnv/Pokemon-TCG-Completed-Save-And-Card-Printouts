local screenshotDirectory = "/home/megasaturnv/Pictures/Pokemon-TCG-Completed-Save-And-Card-Printouts_Screenshots/" --Todo: Move to separate config file. Create folder if it doesn't exist. ~ and $HOME do not work here. Need to be an absolute path

function sleepFrames(frames) --Sleep for this number of frames
	for i=1,frames do
		emu:runFrame()
	end
end

function pressAndRelease(key) --Press a key for 1 frame, then release for 1 frame
	emu:addKey(key)
	sleepFrames(1)
	emu:clearKey(key)
	sleepFrames(1)
end

function zeroPadTwoDigits(number) --Return a number as a zero-padded 2-digit string
	return string.format("%02d", number)
end

function screenshotSelectedCardInList(cardReference, pages)
	sleepFrames(20)
	for i=1,pages do --Todo: Replace with pressing the A button instead, then checking each screenshot until the page changes back to the list
		emu:screenshot(screenshotDirectory .. "/" .. cardReference .. "_" .. tostring(i) .. ".png")
		sleepFrames(10)
		if i ~= pages then --If we're on the final page, no need to go to the next screen
			pressAndRelease(C.GB_KEY.RIGHT) --Press right to see first move
			sleepFrames(20)
		end
	end
end

function screenshotColosseumPack()
	pressAndRelease(C.GB_KEY.A) --Enter Colosseum
	sleepFrames(20)
	pressAndRelease(C.GB_KEY.A) --Enter first card
	sleepFrames(20)

	for i=1,38 do --38 Pokemon Cards in the Colosseum pack. There are 50 Axx cards in total
		screenshotSelectedCardInList("A" .. zeroPadTwoDigits(i), 5) --Pokemon cards usually have 3 to 5 pages, except P19. We will assume 5 pages for this set
		pressAndRelease(C.GB_KEY.DOWN) --Go down to the next card
		sleepFrames(20)
	end

	for i=39,50 do --12 Trainer Cards in the Colosseum pack. There are 50 Axx cards in total
		screenshotSelectedCardInList("A" .. zeroPadTwoDigits(i), 1) --Trainer cards usually have 1 page, but B45, C48 and D48 have two pages
		pressAndRelease(C.GB_KEY.DOWN) --Go down to the next card
		sleepFrames(20)
	end

	for i=1,6 do --6 Energy Cards in the Colosseum pack. There are 7 Exx cards in total (6 in the Colosseum pack)
		screenshotSelectedCardInList("E" .. zeroPadTwoDigits(i), 1) --Energy cards have 1 page
		pressAndRelease(C.GB_KEY.DOWN) --Go down to the next card
		sleepFrames(20)
	end

	pressAndRelease(C.GB_KEY.B) --Return to Card list
	sleepFrames(20)
	pressAndRelease(C.GB_KEY.B) --Return to Booster Pack list
	sleepFrames(20)
end

function screenshotEvolutionPack()
	pressAndRelease(C.GB_KEY.A) --Enter Evolution
	sleepFrames(20)
	pressAndRelease(C.GB_KEY.A) --Enter first card
	sleepFrames(20)

	for i=1,42 do --42 Pokemon Cards in the Evolution pack. There are 50 Bxx cards in total
		screenshotSelectedCardInList("B" .. zeroPadTwoDigits(i), 5)  --Pokemon cards usually have 3 to 5 pages, except P19. We will assume 5 pages for this set
		pressAndRelease(C.GB_KEY.DOWN) --Go down to the next card
		sleepFrames(20)
	end

	for i=43,50 do --8 Trainer Cards in the Evolution pack. There are 50 Bxx cards in total
		screenshotSelectedCardInList("B" .. zeroPadTwoDigits(i), 2) --Trainer cards usually have 1 page, but B45, C48 and D48 have two pages
		pressAndRelease(C.GB_KEY.DOWN) --Go down to the next card
		sleepFrames(20)
	end

	pressAndRelease(C.GB_KEY.B) --Return to Card list
	sleepFrames(20)
	pressAndRelease(C.GB_KEY.B) --Return to Booster Pack list
	sleepFrames(20)
end

function screenshotMysteryPack()
	pressAndRelease(C.GB_KEY.A) --Enter Mystery
	sleepFrames(20)
	pressAndRelease(C.GB_KEY.A) --Enter first card
	sleepFrames(20)

	for i=1,46 do --46 Pokemon Cards in the Mystery pack. There are 50 Cxx cards in total
		screenshotSelectedCardInList("C" .. zeroPadTwoDigits(i), 5)  --Pokemon cards usually have 3 to 5 pages, except P19. We will assume 5 pages for this set
		pressAndRelease(C.GB_KEY.DOWN) --Go down to the next card
		sleepFrames(20)
	end

	for i=47,50 do --4 Trainer Cards in the Mystery pack. There are 50 Cxx cards in total
		screenshotSelectedCardInList("C" .. zeroPadTwoDigits(i), 2) --Trainer cards usually have 1 page, but B45, C48 and D48 have two pages
		pressAndRelease(C.GB_KEY.DOWN) --Go down to the next card
		sleepFrames(20)
	end

	screenshotSelectedCardInList("E" .. zeroPadTwoDigits(7), 1) --1 Energy Card in the Mystery pack. There are 7 Exx cards in total (1 in the Mystery pack). Energy cards have 1 page
	pressAndRelease(C.GB_KEY.DOWN) --Go down to the next card
	sleepFrames(20)

	pressAndRelease(C.GB_KEY.B) --Return to Card list
	sleepFrames(20)
	pressAndRelease(C.GB_KEY.B) --Return to Booster Pack list
	sleepFrames(20)
end

function screenshotLaboratoryPack()
	pressAndRelease(C.GB_KEY.A) --Enter Laboratory
	sleepFrames(20)
	pressAndRelease(C.GB_KEY.A) --Enter first card
	sleepFrames(20)

	for i=1,43 do --43 Pokemon Cards in the Laboratory pack. There are 51 Dxx cards in total
		screenshotSelectedCardInList("D" .. zeroPadTwoDigits(i), 5) --Pokemon cards usually have 3 to 5 pages, except P19. We will assume 5 pages for this set
		pressAndRelease(C.GB_KEY.DOWN) --Go down to the next card
		sleepFrames(20)
	end

	for i=44,51 do --8 Trainer Cards in the Laboratory pack. There are 51 Dxx cards in total
		screenshotSelectedCardInList("D" .. zeroPadTwoDigits(i), 2) --Trainer cards usually have 1 page, but B45, C48 and D48 have two pages
		pressAndRelease(C.GB_KEY.DOWN) --Go down to the next card
		sleepFrames(20)
	end

	pressAndRelease(C.GB_KEY.B) --Return to Card list
	sleepFrames(20)
	pressAndRelease(C.GB_KEY.B) --Return to Booster Pack list
	sleepFrames(20)
end

function screenshotPromotionalCardPack()
	pressAndRelease(C.GB_KEY.A) --Enter Promotional Card
	sleepFrames(20)
	pressAndRelease(C.GB_KEY.A) --Enter first card
	sleepFrames(20)

	for i=1,20 do --18 Pokemon Cards and 2 Trainer cards in the Promotional Card pack. There are 20 Pxx cards in total
		screenshotSelectedCardInList("P" .. zeroPadTwoDigits(i), 6) --Pokemon cards usually have 3 to 5 pages, except P19. Trainer cards usually have 1 page. To simplify things, we will assume 6 pages for everything in this set
		pressAndRelease(C.GB_KEY.DOWN) --Go down to the next card
		sleepFrames(20)
	end

	pressAndRelease(C.GB_KEY.B) --Return to Card list
	sleepFrames(20)
	pressAndRelease(C.GB_KEY.B) --Return to Booster Pack list
	sleepFrames(20)
end

console:log("\n\n\n\n\n\n\n\nRunning Pokemon-TCG-Completed-Save-And-Printouts.lua")
console:log(emu:getGameTitle()) -- Should be POKECARD. Todo: Check for this
console:log(emu:getGameCode()) -- Should be DMG-AXQE. Todo: Check for this
console:log(tostring(emu:platform())) -- Should be 0. Todo: Possibly check for this, or at least check if different platforms produce the same results or have advantages/disadvantages. For example, the gameboy player may have a border which we don't want
--console:log(emu:checksum()) -- Should be ��S. Todo: Get HEX value for this and check



emu:reset()
sleepFrames(20)
pressAndRelease(C.GB_KEY.A) --Skip intro
sleepFrames(80)
pressAndRelease(C.GB_KEY.A) --Title Screen
sleepFrames(20)
pressAndRelease(C.GB_KEY.A) --Continue From Diary
sleepFrames(40)
pressAndRelease(C.GB_KEY.A) --Turn on the PC
sleepFrames(20)
pressAndRelease(C.GB_KEY.A) --Acknowledge message
sleepFrames(20)
pressAndRelease(C.GB_KEY.A) --Enter "Card Album"
sleepFrames(20)

-- Colosseum Pack
screenshotColosseumPack()

-- Evolution Pack
pressAndRelease(C.GB_KEY.DOWN) --Go down to the next pack
screenshotEvolutionPack()

-- Mystery Pack
pressAndRelease(C.GB_KEY.DOWN) --Go down to the next pack
screenshotMysteryPack()

-- Laboratory Pack
pressAndRelease(C.GB_KEY.DOWN) --Go down to the next pack
screenshotLaboratoryPack()

-- Promotional Card Pack
pressAndRelease(C.GB_KEY.DOWN) --Go down to the next pack
screenshotPromotionalCardPack()



console:log("Finished Pokemon-TCG-Completed-Save-And-Printouts.lua")
