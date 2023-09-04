local screenshotDirectory = "/home/megasaturnv/Pictures/Pokemon-TCG-Completed-Save-And-Card-Printouts_Screenshots/" --Todo: Move to separate config file. Create folder if it doesn't exist. ~ and $HOME do not work here. Need to be an absolute path

function sleepFrames(frames)
	for i=1,frames do
		emu:runFrame()
	end
end

function pressAndRelease(key)
	emu:addKey(key)
	sleepFrames(1)
	emu:clearKey(key)
	sleepFrames(1)
end

function zeroPadTwoDigits(number)
	return string.format("%02d", number)
end

function screenshotSelectedCardInList(cardReference, pages)
	pressAndRelease(C.GB_KEY.A) --Press A to see summary of pokemon
	sleepFrames(20)

	for i=1,pages do --Todo: Replace with pressing the A button instead, then checking each screenshot until the page changes back to the list
		emu:screenshot(screenshotDirectory .. "/" .. cardReference .. "_" .. tostring(i) .. ".png")
		sleepFrames(10)
		if i ~= pages then --If we're on the final page, no need to go to the next screen
			pressAndRelease(C.GB_KEY.RIGHT) --Press right to see first move
			sleepFrames(20)
		end
	end

	pressAndRelease(C.GB_KEY.B) --Finally, press B to return to the list
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
pressAndRelease(C.GB_KEY.A) --Enter "Colosseum"
sleepFrames(20)



for i=1,10 do --50 Axx cards in the colosseum pack
	screenshotSelectedCardInList("A" .. zeroPadTwoDigits(i), 4)
	pressAndRelease(C.GB_KEY.DOWN) --Go down to the next card
	sleepFrames(20)
end


--[[
for i=1,38 do --50 Axx cards in the colosseum pack
	screenshotSelectedPokemonInList("A" .. zeroPadTwoDigits(i))
	pressAndRelease(C.GB_KEY.DOWN) --Go down to the next card
	sleepFrames(20)
end
for i=39,50 do --50 Axx cards in the colosseum pack
	screenshotSelectedCardInList("A" .. zeroPadTwoDigits(i))
	pressAndRelease(C.GB_KEY.DOWN) --Go down to the next card
	sleepFrames(20)
end
for i=1,6 do --6 Exx cards in the colosseum pack
	screenshotSelectedCardInList("E" .. zeroPadTwoDigits(i))
	pressAndRelease(C.GB_KEY.DOWN) --Go down to the next card
	sleepFrames(20)
end
--]]

console:log("Finished Pokemon-TCG-Completed-Save-And-Printouts.lua")
