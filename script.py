import pyautogui
import os
import sys
import keyboard
import time
import cv2

pyautogui.FAILSAFE = False
screenWidth, screenHeight = pyautogui.size()

if screenWidth != 1920 or screenHeight != 1080:
    pyautogui.alert(text='Screen Resolution must be 1920x1080, please rerun the script', title='Error', button='OK')
    sys.exit()

#mdAmount = pyautogui.prompt(text='How many MDs to do? (integers only)', default='1')
#teamType = pyautogui.prompt(text='Team type? (sinking only for now)', default='Sinking')
pyautogui.alert(text='Script will begin after you press OK. Hold ALT + S to force stop', title='Start', button='OK')

current_index = 1

# Dictionary to store image indices
image_indices = {
    "Drive.png": 1,
# Encounter Reward
    ## Cost Gift
    "Cost4.png": 7,
    "Cost3.png": 7,
    "Cost1.png": 7,
    ## Random Sink Gift
    "RandomSink5.png": 7,
    "RandomSink4.png": 7,
    ## Random Gift
    "RandomGift3.png": 7,
    "RandomGift2.png": 7,
    ## Least Resources
    "Resource4.png": 7,
    "Resource3.png": 7,
    "Resource2.png": 7,
    ## Indicators
    "GiftSelect.png": 7,
    "MainFloor.png": 7,
    "EGI.png": 7,
    "PostRewardFloor.png": 7,
    "BSI.png": 7,
# Shop
    ## Tier 3
    "DistantStar.png": 6,
    "MidwinterNightmare.png": 6,
    "BrokenCompass.png": 6,
    ## Tier 2
    "Nebulizer.png": 6,
    "Carmilla.png": 6,
    "TangledBones.png": 6,
    "LeakedEnkephalin.png": 6,
    "MCBG.png": 6,
    "Grandeur.png": 6,
    "SkeletalCrumbs.png": 6,
    ## Tier 1
    "PhlebotomyPack.png": 6,
    "ThornyPath.png": 6,
    "HeadlessPortrait.png": 6,
    "EldtreeSnare.png": 6,
    "Rags.png": 6,
    ## Shop Actions
    "KeywordRefresh.png": 6,
    "LeaveShop.png": 6,
# Theme Packs
    "41.png": 5,
    "40.png": 5,
    "39.png": 5,
    "38.png": 5,
    "37.png": 5,
    "36.png": 5,
    "35.png": 5,
    "34.png": 5,
    "33.png": 5,
    "32.png": 5,
    "31.png": 5,
    "30.png": 5,
    "29.png": 5,
    "28.png": 5,
    "27.png": 5,
    "26.png": 5,
    "25.png": 5,
    "24.png": 5,
    "23.png": 5,
    "22.png": 5,
    "21.png": 5,
    "20.png": 5,
    "19.png": 5,
    "18.png": 5,
    "17.png": 5,
    "16.png": 5,
    "15.png": 5,
    "14.png": 5,
    "13.png": 5,
    "12.png": 5,
    "11.png": 5,
    "10.png": 5,
    "9.png": 5,
    "8.png": 5,
    "7.png": 5,
    "6.png": 5,
    "5.png": 5,
    "4.png": 5,
    "3.png": 5,
    "2.png": 5,
    "1.png": 5,
# Battle
    "SkipBattle.png": 4,
    "WinRateBaby.png": 4,
    "PostBattleFloor.png": 4,
    "PostBattleGift.png": 4,
    "EncounterReward.png": 4,
    "VictoryIndicator.png": 4,
# Choice Encounter
    "VeryHigh.png": 8,
    "High.png": 8,
    "Normal.png": 8,
    "Low.png": 8,
    "VeryLow.png": 8,
    "CharChoice.png": 3,
    "Skip.png": 3,
    "Continue.png": 3,
    "CommenceBattle.png": 3,
    "Commence.png": 3,
    "Proceed.png": 3,
    "Enter.png": 1,
    "Halt.png": 1,
    "SinkingStarter.png": 1,
    "ConfirmGift.png": 1,
    "ConfirmGiftHighlighted.png": 1,
    "HardActivated.png": 1,
    "RewardIndicator.png": 1,
    "Defeat.png": 1,
    "Window.png": 1,
    "ThemePack.png": 1,
    "Self.png": 1,
    "RandomIndicator.png": 1,
    "ClearSelection.png": 1,
    "BattleIndicator.png": 1,
    "DoorEnter.png": 1,
    "GiftChoice.png": 1,
    "GiftFail.png": 1,
    "Finish.png": 1,
    "ClaimRewards.png": 1,
    "HomeScreen.png": 1,
    "SelectEvent.png": 1,
    "Shop.png": 1,
}

# Dictionary to store image priorities
image_priorities = {
# Encounter Reward
    ## Cost Gift
    "Cost4.png": 4,
    "Cost3.png": 3,
    "Cost1.png": 1,
    ## Random Sink Gift
    "RandomSink5.png": 5,
    "RandomSink4.png": 4,
    ## Random Gift
    "RandomGift3.png": 3,
    "RandomGift2.png": 2,
    ## Least Resources
    "Resource4.png": 3,
    "Resource3.png": 2,
    "Resource2.png": 1,
# Shop
    ## Tier 3
    "DistantStar.png": 6,
    "MidwinterNightmare.png": 6,
    "BrokenCompass.png": 6,
    ## Tier 2
    "Nebulizer.png": 5,
    "TangledBones.png": 5,
    "Carmilla.png": 4,
    "LeakedEnkephalin.png": 4,
    "MCBG.png": 4,
    "Grandeur.png": 4,
    "SkeletalCrumbs.png": 4,
    ## Tier 1
    "PhlebotomyPack.png": 6,
    "ThornyPath.png": 3,
    "HeadlessPortrait.png": 4,
    "EldtreeSnare.png": 3,
    "Rags.png": 3,
    ## Shop Actions
    "KeywordRefresh.png": 2,
    "LeaveShop.png": 1,
# Theme Packs
    "41.png": 1,
    "40.png": 2,
    "39.png": 3,
    "38.png": 4,
    "37.png": 5,
    "36.png": 6,
    "35.png": 7,
    "34.png": 8,
    "33.png": 9,
    "32.png": 10,
    "31.png": 11,
    "30.png": 12,
    "29.png": 13,
    "28.png": 14,
    "27.png": 15,
    "26.png": 16,
    "25.png": 17,
    "24.png": 18,
    "23.png": 19,
    "22.png": 20,
    "21.png": 21,
    "20.png": 22,
    "19.png": 23,
    "18.png": 24,
    "17.png": 25,
    "16.png": 26,
    "15.png": 27,
    "14.png": 28,
    "13.png": 29,
    "12.png": 30,
    "11.png": 31,
    "10.png": 32,
    "9.png": 33,
    "8.png": 34,
    "7.png": 35,
    "6.png": 36,
    "5.png": 37,
    "4.png": 38,
    "3.png": 39,
    "2.png": 40,
    "1.png": 41,
# Choice Encounter
    "VeryHigh.png": 6,
    "High.png": 5,
    "Normal.png": 4,
    "Low.png": 3,
    "VeryLow.png": 2,
}

paused_indices = set()

def kill_script():
    """Listen for the alt+s key to stop the script."""
    if keyboard.is_pressed('alt+s'):
        pyautogui.alert(text='Script has been stopped', title='Force Stop', button='OK')
        sys.exit()

def check_higher_priority(current_priority):
    """Check if a higher priority image is found within 0.10 seconds."""
    start_time = time.time()
    while time.time() - start_time < 0.05:
        for child in image_priorities:
            if image_priorities[child] > current_priority:
                try:
                    location = pyautogui.locateCenterOnScreen(os.path.join('Menu', child), confidence=0.95)
                    if location:
                        print(f"Found higher priority image: {child} at location {location}")
                        return True
                except pyautogui.ImageNotFoundException:
                    continue
        time.sleep(0.1)  # Sleep for a short time to avoid busy-waiting
    return False

def search_for_image(image_file, child):
    """Search for the image and perform actions based on it."""
    global current_index, paused_indices

    # Check if the image's index matches the current index
    if image_indices.get(child, -1) == current_index:
        try:
            # Re-enabled confidence with a value (e.g., 0.8 for 80% similarity)
            location = pyautogui.locateCenterOnScreen(image_file, confidence=0.8)
            if location:
                print(f"Found image: {child} at location {location}")

                # Check if the image has a priority value
                current_priority = image_priorities.get(child, 0)
                if current_priority > 0:
                    if check_higher_priority(current_priority):
                        print(f"Higher priority image found, skipping action for {child}")
                        return

                actions = get_image_actions(child, location)

                for action in actions:
                    action_type = action[0]

                    buffer_time = 0  # Default buffer_time to 0

                    if action_type == "move_click":
                        use_coords, click, *rest = action[1:]
                        buffer_time = rest[0] if rest else 0  # Get buffer time if specified
                        buffer_time += 0.15  # Increase buffer time by 0.25 seconds

                        if use_coords:
                            move_to_coordinates = use_coords
                        else:
                            move_to_coordinates = location  # Use the image's location

                        pyautogui.moveTo(move_to_coordinates)
                        print(f"Moved to coordinates: {move_to_coordinates}")

                        if click:
                            pyautogui.click()
                            print(f"Clicked at {move_to_coordinates}")

                    elif action_type == "drag":
                        use_coords, end_coords, duration = action[1:]
                        if use_coords:
                            start_coords = use_coords
                        else:
                            start_coords = location  # Use the image's location

                        pyautogui.moveTo(start_coords)
                        print(f"Dragging from {start_coords} to {end_coords} over {duration} seconds.")
                        pyautogui.mouseDown()  # Simulate pressing down the mouse
                        time.sleep(0.1)  # Reduced delay for smoother dragging
                        pyautogui.moveTo(end_coords, duration=duration)
                        pyautogui.mouseUp()  # Release the mouse at the end of the drag
                        print(f"Dragged from {start_coords} to {end_coords} over {duration} seconds.")

                    elif action_type == "press_enter":
                        pyautogui.press('enter')  # Simulate pressing the Enter key
                        print("Pressed Enter key.")

                    elif action_type == "press_p":
                        pyautogui.press('p')  # Simulate pressing the 'P' key
                        print("Pressed P key.")
                        time.sleep(0.3)  # Reduced sleep time after pressing 'p'

                    if buffer_time > 0:
                        print(f"Waiting for {buffer_time} seconds before next action...")
                        time.sleep(buffer_time)

                # Update the index based on the image found
                if child == "ThemePack.png":
                    current_index += 4
                elif child == "1.png":
                    current_index -= 4
                elif child == "2.png":
                    current_index -= 4
                elif child == "3.png":
                    current_index -= 4
                elif child == "4.png":
                    current_index -= 4
                elif child == "5.png":
                    current_index -= 4
                elif child == "6.png":
                    current_index -= 4
                elif child == "7.png":
                    current_index -= 4
                elif child == "8.png":
                    current_index -= 4
                elif child == "9.png":
                    current_index -= 4
                elif child == "10.png":
                    current_index -= 4
                elif child == "11.png":
                    current_index -= 4
                elif child == "12.png":
                    current_index -= 4
                elif child == "13.png":
                    current_index -= 4
                elif child == "14.png":
                    current_index -= 4
                elif child == "15.png":
                    current_index -= 4
                elif child == "16.png":
                    current_index -= 4
                elif child == "17.png":
                    current_index -= 4
                elif child == "18.png":
                    current_index -= 4
                elif child == "19.png":
                    current_index -= 4
                elif child == "20.png":
                    current_index -= 4
                elif child == "21.png":
                    current_index -= 4
                elif child == "22.png":
                    current_index -= 4
                elif child == "23.png":
                    current_index -= 4
                elif child == "24.png":
                    current_index -= 4
                elif child == "25.png":
                    current_index -= 4
                elif child == "26.png":
                    current_index -= 4
                elif child == "27.png":
                    current_index -= 4
                elif child == "28.png":
                    current_index -= 4
                elif child == "29.png":
                    current_index -= 4
                elif child == "30.png":
                    current_index -= 4
                elif child == "31.png":
                    current_index -= 4
                elif child == "32.png":
                    current_index -= 4
                elif child == "33.png":
                    current_index -= 4
                elif child == "34.png":
                    current_index -= 4
                elif child == "35.png":
                    current_index -= 4
                elif child == "36.png":
                    current_index -= 4
                elif child == "37.png":
                    current_index -= 4
                elif child == "38.png":
                    current_index -= 4
                elif child == "39.png":
                    current_index -= 4
                elif child == "40.png":
                    current_index -= 4
                elif child == "41.png":
                    current_index -= 4
                elif child == "ClearSelection.png":
                    current_index += 3
                elif child == "BattleIndicator.png":
                    current_index += 3
                elif child == "RandomIndicator.png":
                    current_index += 2
                elif child == "SkipBattle.png":
                    current_index -= 1
                elif child == "VictoryIndicator.png":
                    current_index -= 2
                elif child == "Proceed.png":
                    current_index -= 2
                elif child == "Continue.png":
                    current_index -= 2
                elif child == "CommenceBattle.png":
                    current_index += 1
                elif child == "Shop.png":
                    current_index += 5
                elif child == "LeaveShop.png":
                    current_index -= 5
                elif child == "EncounterReward.png":
                    current_index += 3
                elif child == "RewardIndicator.png":
                    current_index += 6
                elif child == "PostBattleFloor.png":
                    current_index -= 3
                elif child == "PostBattleGift.png":
                    current_index -= 3
                elif child == "GiftSelect.png":
                    current_index -= 6
                elif child == "EGI.png":
                    current_index -= 6
                elif child == "PostRewardFloor.png":
                    current_index -= 6
                elif child == "BSI.png":
                    current_index -= 6
                elif child == "MainFloor.png":
                    current_index -= 6
                elif child == "CharChoice.png":
                    current_index += 5
                elif child == "VeryHigh.png":
                    current_index -= 5
                elif child == "High.png":
                    current_index -= 5
                elif child == "Normal.png":
                    current_index -= 5
                elif child == "Low.png":
                    current_index -= 5
                elif child == "VeryLow.png":
                    current_index -= 5


        except pyautogui.ImageNotFoundException:
            print(f"Could not locate image: {child}")
            return
    else:
        # Pause searching for this index
        paused_indices.add(image_indices.get(child, -1))

def get_image_actions(image_name, image_location):
    """Return actions to be performed for an image."""
    actions_dict = {
         "Drive.png": [
            ("move_click", (1307, 963), True, 0.75),
            ("move_click", (660, 461), True, 0.4),
            ("move_click", (957, 527), True, 0.25),
        ],
        "1.png": [
            ("drag", None, (954, 948), 3),
        ],
        "2.png": [
            ("drag", None, (954, 948), 3),
        ],
        "3.png": [
            ("drag", None, (954, 948), 3),
        ],
        "4.png": [
            ("drag", None, (954, 948), 3),
        ],
        "5.png": [
            ("drag", None, (954, 948), 3),
        ],
        "6.png": [
            ("drag", None, (954, 948), 3),
        ],
        "7.png": [
            ("drag", None, (954, 948), 3),
        ],
        "8.png": [
            ("drag", None, (954, 948), 3),
        ],
        "9.png": [
            ("drag", None, (954, 948), 3),
        ],
        "10.png": [
            ("drag", None, (954, 948), 3),
        ],
        "11.png": [
            ("drag", None, (954, 948), 3),
        ],
        "12.png": [
            ("drag", None, (954, 948), 3),
        ],
        "13.png": [
            ("drag", None, (954, 948), 3),
        ],
        "14.png": [
            ("drag", None, (954, 948), 3),
        ],
        "15.png": [
            ("drag", None, (954, 948), 3),
        ],
        "16.png": [
            ("drag", None, (954, 948), 3),
        ],
        "17.png": [
            ("drag", None, (954, 948), 3),
        ],
        "18.png": [
            ("drag", None, (954, 948), 3),
        ],
        "19.png": [
            ("drag", None, (954, 948), 3),
        ],
        "20.png": [
            ("drag", None, (954, 948), 3),
        ],
        "21.png": [
            ("drag", None, (954, 948), 3),
        ],
        "22.png": [
            ("drag", None, (954, 948), 3),
        ],
        "23.png": [
            ("drag", None, (954, 948), 3),
        ],
        "24.png": [
            ("drag", None, (954, 948), 3),
        ],
        "25.png": [
            ("drag", None, (954, 948), 3),
        ],
        "26.png": [
            ("drag", None, (954, 948), 3),
        ],
        "27.png": [
            ("drag", None, (954, 948), 3),
        ],
        "28.png": [
            ("drag", None, (954, 948), 3),
        ],
        "29.png": [
            ("drag", None, (954, 948), 3),
        ],
        "30.png": [
            ("drag", None, (954, 948), 3),
        ],
        "31.png": [
            ("drag", None, (954, 948), 3),
        ],
        "32.png": [
            ("drag", None, (954, 948), 3),
        ],
        "33.png": [
            ("drag", None, (954, 948), 3),
        ],
        "34.png": [
            ("drag", None, (954, 948), 3),
        ],
        "35.png": [
            ("drag", None, (954, 948), 3),
        ],
        "36.png": [
            ("drag", None, (954, 948), 3),
        ],
        "37.png": [
            ("drag", None, (954, 948), 3),
        ],
        "38.png": [
            ("drag", None, (954, 948), 3),
        ],
        "39.png": [
            ("drag", None, (954, 948), 3),
        ],
        "40.png": [
            ("drag", None, (954, 948), 3),
        ],
        "41.png": [
            ("drag", None, (954, 948), 3),
        ],
        "VeryHigh.png": [
            ("move_click", None, 0.25),
        ],
        "High.png": [
            ("move_click", None, 0.25),
        ],
        "Normal.png": [
            ("move_click", None, 0.25),
        ],
        "Low.png": [
            ("move_click", None, 0.25),
        ],
        "VeryLow.png": [
            ("move_click", None, 0.25),
        ],
        "Enter.png": [
            ("move_click", (1116, 726), True, 1.25),
            ("move_click", (1704, 875), True, 2.25),
            ("move_click", (407, 417), True, 0.25),
            ("move_click", (682, 420), True, 0.25),
            ("move_click", (963, 395), True, 0.25),
            ("move_click", (1234, 400), True, 0.25),
            ("move_click", (1704, 1026), True, 0.75),
            ("move_click", (1121, 808), True, 0.25),
        ],
        "Halt.png": [
            ("move_click", (957, 665), True, 1.25),
            ("move_click", (1128, 720), True, 2.25),
            ("move_click", (573, 810), True, 1.25),
            ("move_click", (957, 527), True, 0.25),
        ],
        "SinkingStarter.png": [
            ("move_click", (308, 666), True, 0.5),
            ("move_click", (1437, 391), True, 0.25),
            ("move_click", (1456, 555), True, 0.5),
            ("move_click", (1624, 876), True, 0.25),
        ],
        "ConfirmGift.png": [
            ("move_click", (949, 796), True, 0.5),
        ],
        "EGI.png": [
            ("move_click", (949, 796), True, 0.5),
        ],
        "ConfirmGiftHighlighted.png": [
            ("move_click", (949, 796), True, 0.5),
        ],
        "HardActivated.png": [
            ("move_click", (1355, 69), True, 0.5),
        ],
        "Defeat.png": [
            ("move_click", (1653, 832), True, 1.25),
            ("move_click", (1678, 898), True, 1.25),
            ("move_click", (585, 811), True, 0.25),
        ],
        "Window.png": [
            ("move_click", (998, 956), True, 0.25),
        ],
        "Self.png": [
            ("move_click", (1083, 424), True, 0.25),
            ("move_click", (1081, 105), True, 0.25),
            ("move_click", (1085, 738), True, 0.25),
            ("press_enter",),
            ("move_click", (696, 414), True, 0.25),
        ],
        "RandomIndicator.png": [
            ("move_click", (893, 461), True, 0),
            ("move_click", (893, 461), True, 0),
            ("move_click", (893, 461), True, 0),
            ("move_click", (893, 461), True, 0),
            ("move_click", (1192, 335), True, 0.25),
        ],
        "Skip.png": [
            ("move_click", (893, 461), True, 0),
            ("move_click", (893, 461), True, 0),
            ("move_click", (893, 461), True, 0),
            ("move_click", (893, 461), True, 0),
            ("move_click", (1192, 335), True, 0.25),
        ],
        "SkipBattle.png": [
            ("move_click", (893, 461), True, 0),
            ("move_click", (893, 461), True, 0),
            ("move_click", (893, 461), True, 0),
            ("move_click", (893, 461), True, 0),
            ("move_click", (1192, 335), True, 0.25),
        ],
        "Continue.png": [
            ("move_click", (1688, 965), True, 0.25),
        ],
        "ClearSelection.png": [
            ("move_click", (1709, 716), True, 1),
            ("move_click", (1125, 737), True, 0.5),
            ("move_click", (437, 343), True, 0),
            ("move_click", (438, 635), True, 0),
            ("move_click", (642, 641), True, 0),
            ("move_click", (838, 630), True, 0),
            ("move_click", (1429, 637), True, 0),
            ("move_click", (1434, 336), True, 0),
            ("move_click", (1229, 632), True, 0),
            ("move_click", (1233, 343), True, 0),
            ("move_click", (1026, 340), True, 0),
            ("move_click", (841, 350), True, 0),
            ("move_click", (637, 342), True, 0),
            ("move_click", (1037, 630), True, 0),
            ("move_click", (1705, 868), True, 0),
        ],
        "WinRateBaby.png": [
            ("move_click", (0, 0), True, 0.05),
            ("press_p",),
            ("press_enter",)
        ],
        "Proceed.png": [
            ("move_click", (1691, 970), True, 0),
        ],
        "Commence.png": [
            ("move_click", (1691, 970), True, 0),
        ],
        "Cost4.png": [
            ("move_click", None, True, 0.25),
            ("move_click", (1185, 788), True, 0),
        ],
        "Cost3.png": [
            ("move_click", None, True, 0.25),
            ("move_click", (1185, 788), True, 0),
        ],
        "Cost1.png": [
            ("move_click", None, True, 0.25),
            ("move_click", (1185, 788), True, 0),
        ],
        "RandomSink5.png": [
            ("move_click", None, True, 0.25),
            ("move_click", (1185, 788), True, 0),
        ],
        "RandomSink4.png": [
            ("move_click", None, True, 0.25),
            ("move_click", (1185, 788), True, 0),
        ],
        "RandomGift3.png": [
            ("move_click", None, True, 0.25),
            ("move_click", (1185, 788), True, 0),
        ],
        "RandomGift2.png": [
            ("move_click", None, True, 0.25),
            ("move_click", (1185, 788), True, 0),
        ],
        "Resource4.png": [
            ("move_click", None, True, 0.25),
            ("move_click", (1185, 788), True, 0),
        ],
        "Resource3.png": [
            ("move_click", None, True, 0.25),
            ("move_click", (1185, 788), True, 0),
        ],
        "Resource2.png": [
            ("move_click", None, True, 0.25),
            ("move_click", (1185, 788), True, 0),
        ],
        "MidwinterNightmare.png": [
            ("move_click", None, True, 0),
            ("move_click", (1115, 723), True, 0.5),
            ("press_enter",),
            ("move_click", (0,0), True, 0),
        ],
        "BrokenCompass.png": [
            ("move_click", None, True, 0),
            ("move_click", (1115, 723), True, 0.5),
            ("press_enter",),
            ("move_click", (0,0), True, 0),
        ],
        "DistantStar.png": [
            ("move_click", None, True, 0),
            ("move_click", (1115, 723), True, 0.5),
            ("press_enter",),
            ("move_click", (0,0), True, 0),
        ],
        "TangledBones.png": [
            ("move_click", None, True, 0),
            ("move_click", (1115, 723), True, 0.5),
            ("press_enter",),
            ("move_click", (0,0), True, 0),
        ],
        "LeakedEnkephalin.png": [
            ("move_click", None, True, 0),
            ("move_click", (1115, 723), True, 0.5),
            ("press_enter",),
            ("move_click", (0,0), True, 0),
        ],
        "MCBG.png": [
            ("move_click", None, True, 0),
            ("move_click", (1115, 723), True, 0.5),
            ("press_enter",),
            ("move_click", (0,0), True, 0),
        ],
        "Grandeur.png": [
            ("move_click", None, True, 0),
            ("move_click", (1115, 723), True, 0.5),
            ("press_enter",),
            ("move_click", (0,0), True, 0),
        ],
        "SkeletalCrumbs.png": [
            ("move_click", None, True, 0),
            ("move_click", (1115, 723), True, 0.5),
            ("press_enter",),
            ("move_click", (0,0), True, 1),
        ],
        "Nebulizer.png": [
            ("move_click", None, True, 0),
            ("move_click", (1115, 723), True, 0.5),
            ("press_enter",),
            ("move_click", (0,0), True, 0),
        ],
        "Carmilla.png": [
            ("move_click", None, True, 0),
            ("move_click", (1115, 723), True, 0.5),
            ("press_enter",),
            ("move_click", (0,0), True, 0),
        ],
        "PhlebotomyPack.png": [
            ("move_click", None, True, 0),
            ("move_click", (1115, 723), True, 0.5),
            ("press_enter",),
            ("move_click", (0,0), True, 0),
        ],
        "ThornyPath.png": [
            ("move_click", None, True, 0),
            ("move_click", (1115, 723), True, 0.5),
            ("press_enter",),
            ("move_click", (0,0), True, 0),
        ],
        "HeadlessPortrait.png": [
            ("move_click", None, True, 0),
            ("move_click", (1115, 723), True, 0.5),
            ("press_enter",),
            ("move_click", (0,0), True, 0),
        ],
        "EldtreeSnare.png": [
            ("move_click", None, True, 0),
            ("move_click", (1115, 723), True, 0.5),
            ("press_enter",),
            ("move_click", (0,0), True, 0),
        ],
        "Rags.png": [
            ("move_click", None, True, 0),
            ("move_click", (1115, 723), True, 0.5),
            ("press_enter",),
            ("move_click", (0,0), True, 0),
        ],
        "KeywordRefresh.png": [
            ("move_click", None, True, 0.25),
            ("move_click", (1417, 454), True, 0),
            ("move_click", (1116, 841), True, 0),
        ],
        "LeaveShop.png": [
            ("move_click", None, True, 1),
        ],
        "DoorEnter.png": [
            ("press_enter",),
        ],
        "GiftChoice.png": [
            ("move_click", (953, 493), True, 0.15),
            ("press_enter",),
        ],
        "GiftFail.png": [
            ("move_click", (803, 691), True, 0.15),
        ],
        "CommenceBattle.png": [
            ("move_click", (1691, 970), True, 0),
        ],
        "Finish.png": [
            ("move_click", (1662, 834), True, 1),
            ("move_click", (1684, 901), True, 1),
            ("move_click", (1317, 817), True, 1),
            ("move_click", (1131, 740), True, 1),
            ("move_click", (951, 706), True, 1),
            ("move_click", (951, 706), True, 1),
        ],
        "ClaimRewards.png": [
            ("move_click", (1311, 812), True, 1),
            ("move_click", (1158, 743), True, 1),
            ("move_click", (951, 706), True, 1),
            ("move_click", (951, 706), True, 1),
        ],
        "HomeScreen.png": [
            ("move_click", (893, 461), True, 0),
            ("move_click", (893, 461), True, 0),
            ("move_click", (893, 461), True, 0),
            ("move_click", (893, 461), True, 0),
        ],
        "SelectEvent.png": [
            ("move_click", (1158, 743), True, 1),
            ("move_click", (959, 771), True, 0),
        ],
    }
    return actions_dict.get(image_name, [
        ("move_click", (0, 0), False, 0)  # Default action
    ])

def menu_nav():
    """Search through the menu images."""
    global current_index, paused_indices

    script_dir = os.path.dirname(os.path.realpath(__file__))
    menu_path = os.path.join(script_dir, 'Menu')
    children = os.listdir(menu_path)

    for child in children:
        image_file = os.path.join(menu_path, child)

        if image_file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            print(f"Searching for image: {image_file}")
            if image_indices.get(child, -1) not in paused_indices:
                search_for_image(image_file, child)

    # Resume paused indices if current_index matches
    paused_indices = {idx for idx in paused_indices if idx != current_index}

def main():
    """Main function to initialize and run the script."""
    print("Starting continuous image search...")

    while True:
        kill_script()  # Check for script termination
        menu_nav()  # Search for images in the menu folder
        time.sleep(0.5)  # Reduced sleep for quicker iteration through images

    print("Script is exiting (this won't happen unless manually stopped).")

main()