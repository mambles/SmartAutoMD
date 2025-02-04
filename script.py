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

# Predefined teams
teams = {
    "Sinking": ["YiSang", "Heathcliff", "Ishmael", "Rodya", "Gregor", "HongLu", "Outis", "Ryoshu", "Don", "Meursault", "Sinclair", "Faust"],
    "Charge": ["YiSang", "Faust", "Don", "Ryoshu", "Heathcliff", "Outis", "Meursault", "Ishmael", "HongLu", "Sinclair", "Rodya", "Gregor"],
    "Bleed": ["Don", "YiSang", "Rodya", "Meursault", "Gregor", "Outis", "HongLu", "Faust", "Heathcliff", "Ishmael", "Ryoshu", "Sinclair"],
    "Burn": ["Outis", "Sinclair", "Rodya", "Ishmael", "Meursault", "Ryoshu", "Faust",  "Heathcliff", "Don", "YiSang", "Gregor", "HongLu"],
    "Tremor": ["Ishmael", "Faust", "Heathcliff", "Don", "Outis", "HongLu", "Rodya", "Meursault", "Ryoshu", "YiSang", "Sinclair", "Gregor"]
}

# Dictionary to map character names to their coordinates
character_coordinates = {
    "YiSang": (435, 339),
    "Faust": (637, 331),
    "Don": (838, 340),
    "Ryoshu": (1026, 343),
    "Meursault": (1238, 345),
    "HongLu": (1429, 352),
    "Heathcliff": (436, 647),
    "Ishmael": (634, 640),
    "Rodya": (842, 636),
    "Sinclair": (1041, 628),
    "Outis": (1232, 639),
    "Gregor": (1432, 646),
}

# Function to click on all character locations
def click_all_characters():
    for character in character_list:
        if character in character_coordinates:
            coords = character_coordinates[character]
            pyautogui.moveTo(coords)
            pyautogui.click()
            time.sleep(0.15)  # Wait for the click to be registered
    pyautogui.press('enter')  # Press Enter after all characters have been clicked

# Save the selected team to a file
def save_team(team_name):
    with open('selected_team.txt', 'w') as file:
        file.write(team_name)

# Load the saved team from a file
def load_team():
    if os.path.exists('selected_team.txt'):
        with open('selected_team.txt', 'r') as file:
            return file.read().strip()
    return None

# Check if Shift is held down
def is_shift_held():
    return keyboard.is_pressed('shift')

# Load the saved team
saved_team = load_team()

# Prompt the user for the team keyword or custom list of characters
if saved_team and not is_shift_held():
    # Check if the saved team is a predefined team keyword
    if saved_team in teams:
        character_list = teams[saved_team]
        selected_tag = saved_team  # Use the team name as the tag
        print(f"Loaded saved team: {saved_team}")
    else:
        # Treat the saved team as a custom list of characters
        character_list = [char.strip() for char in saved_team.split(',')]
        selected_tag = pyautogui.prompt(
            text='Enter the tag for the custom team:', title='Tag Selection', default='Sinking')
        print(f"Loaded custom team: {character_list}")
else:
    while True:
        user_input = pyautogui.prompt(
            text='Enter the team keyword (e.g., "Sinking" or "Charge") or a custom list of characters (e.g., "YiSang, Heathcliff, Ishmael, Rodya, Gregor, HongLu, Outis, Ryoshu, Don, Meursault, Sinclair, Faust"):', title='Team Selection', default='Sinking')

        # Convert user input to lowercase for case-insensitive comparison
        user_input_lower = user_input.lower()

        # Check if the input is a predefined team keyword
        if user_input_lower in (key.lower() for key in teams):
            character_list = teams[next(key for key in teams if key.lower() == user_input_lower)]
            selected_tag = user_input  # Use the team name as the tag
            save_team(user_input)
            break
        else:
            # Otherwise, treat the input as a custom list of characters
            custom_list = [char.strip() for char in user_input.split(',')]
            if all(character in character_coordinates for character in custom_list):
                character_list = custom_list
                selected_tag = pyautogui.prompt(
                    text='Enter the tag for the custom team:', title='Tag Selection', default='Sinking')
                save_team(user_input)
                break
            else:
                pyautogui.alert(text='Invalid input. Please try again.', title='Error', button='OK')

pyautogui.alert(text='Script will begin after you press OK. Hold ALT + S to force stop', title='Start', button='OK')
print("Script has started successfully")
current_index = 1
print("current_index is:", current_index)

# index, priority, index_change, tag, gift
combined_dict = {
    "Drive.png": (1, None, None, None, None),
    "Cost4.png": (7, 4, None, None, None),
    "Cost3.png": (7, 3, None, None, None),
    "Cost1.png": (7, 1, None, None, None),
    "RandomGift4.png": (7, 4, None, None, None),
    "RandomGift3.png": (7, 3, None, None, None),
    "RandomGift2.png": (7, 2, None, None, None),
    "Resource4.png": (7, 3, None, None, None),
    "Resource3.png": (7, 2, None, None, None),
    "Resource2.png": (7, 1, None, None, None),
    "Resource1.png": (7, 1, None, None, None),
    "GiftSelect.png": (7, None, -6, None, None),
    "MainFloor.png": (7, None, -6, None, None),
    "EGI.png": (7, None, -6, None, None),
    "PostRewardFloor.png": (7, None, -6, None, None),
    "BSI.png": (7, None, -6, None, None),
# Shop
    ## Sinking Tier 3
    "DistantStar.png": (6, 6, None, "Sinking", "Gift"),
    "MidwinterNightmare.png": (6, 6, None, "Sinking", "Gift"),
    "BrokenCompass.png": (6, 6, None, "Sinking", "Gift"),
    ## Sinking Tier 2
    "TangledBones.png": (6, 5, None, "Sinking", "Gift"),
    "FrozenCries.png": (6, 5, None, "Sinking", "Gift"),
    "LeakedEnkephalin.png": (6, 4, None, "Sinking", "Gift"),
    "MCBG.png": (6, 4, None, "Sinking", "Gift"),
    "Grandeur.png": (6, 4, None, "Sinking", "Gift"),
    "SkeletalCrumbs.png": (6, 4, None, "Sinking", "Gift"),
    ## Sinking Tier 1
    "ThornyPath.png": (6, 3, None, "Sinking", "Gift"),
    "HeadlessPortrait.png": (6, 4, None, "Sinking", "Gift"),
    "EldtreeSnare.png": (6, 3, None, "Sinking", "Gift"),
    "Rags.png": (6, 3, None, "Sinking", "Gift"),

    ## Tremor Tier 3
    "BellofTruth.png": (6, 7, None, "Tremor", "Gift"),
    "ClockworkSpring.png": (6, 6, None, "Tremor", "Gift"),
    "MeltedEyeball.png": (6, 6, None, "Tremor", "Gift"),
    "BioVial.png": (6, 5, None, "Tremor", "Gift"),
    ## Tremor Tier 2
    "InterlockedCogs.png": (6, 5, None, "Tremor", "Gift"),
    "OscillatingBracelet.png": (6, 4, None, "Tremor", "Gift"),
    "Reverberation.png": (6, 4, None, "Tremor", "Gift"),
    "MirrorTactile.png": (6, 4, None, "Tremor", "Gift"),
    "SourAroma.png": (6, 4, None, "Tremor", "Gift"),
    ## Tremor Tier 1
    "NixieDivergence.png": (6, 4, None, "Tremor", "Gift"),
    "VenomousSkin.png": (6, 3, None, "Tremor", "Gift"),
    "GreenSpirit.png": (6, 3, None, "Tremor", "Gift"),

    ## Burn Tier 3
    "ArdentFlower.png": (6, 6, None, "Burn", "Gift"),
    "CharredDisk.png": (6, 6, None, "Burn", "Gift"),
    "DusttoDust.png": (6, 6, None, "Burn", "Gift"),
     ## Burn Tier 2
    "StifledRage.png": (6, 4, None, "Burn", "Gift"),
    "LogicCircuit.png": (6, 4, None, "Burn", "Gift"),
    "DecaStewpot.png": (6, 4, None, "Burn", "Gift"),
    ## Burn Tier 1
    "Ashes.png": (6, 3, None, "Burn", "Gift"),
    "BurningIntellect.png": (6, 3, None, "Burn", "Gift"),
    "MeltedParaffin.png": (6, 3, None, "Burn", "Gift"),
    "Polarization.png": (6, 3, None, "Burn", "Gift"),

    ## Bleed Tier 3
    "SmokesandWires.png": (6, 6, None, "Bleed", "Gift"),
    "Respite.png": (6, 6, None, "Bleed", "Gift"),
    "RustedKnife.png": (6, 6, None, "Bleed", "Gift"),
    ## Bleed Tier 2
    "Millarca.png": (6, 4, None, "Bleed", "Gift"),
    "Awe.png": (6, 4, None, "Bleed", "Gift"),
    ## Bleed Tier 1
    "ArrestedHymn.png": (6, 4, None, "Bleed", "Gift"),
    "GrimyIronStake.png": (6, 3, None, "Bleed", "Gift"),
    "RustedMuzzle.png": (6, 3, None, "Bleed", "Gift"),
    "TangledBundle.png": (6, 3, None, "Bleed", "Gift"),

    ## General Goodies
    "Nebulizer.png": (6, 5, None, None, "Gift"),
    "PhlebotomyPack.png": (6, 6, None, None, "Gift"),
    "Carmilla.png": (6, 4, None, None, "Gift"),
    ## Actions
    "KeywordRefresh.png": (6, 2, 4, None, None),
    "LeaveShop.png": (6, 1, -5, None, None),
    "Burn.png": (10, None, -4, "Burn", None),
    "Charge.png": (10, None, -4, "Charge", None),
    "Bleed.png": (10, None, -4, "Bleed", None),
    "Poise.png": (10, None, -4, "Poise", None),
    "Rupture.png": (10, None, -4, "Rupture", None),
    "Sinking.png": (10, None, -4, "Sinking", None),
    "Tremor.png": (10, None, -4, "Tremor", None),
# Theme Packs
    "41.png": (5, 1, -4, None, None),
    "40.png": (5, 2, -4, None, None),
    "39.png": (5, 3, -4, None, None),
    "38.png": (5, 4, -4, None, None),
    "37.png": (5, 5, -4, None, None),
    "36.png": (5, 6, -4, None, None),
    "35.png": (5, 7, -4, None, None),
    "34.png": (5, 8, -4, None, None),
    "33.png": (5, 9, -4, None, None),
    "32.png": (5, 10, -4, None, None),
    "31.png": (5, 11, -4, None, None),
    "30.png": (5, 12, -4, None, None),
    "29.png": (5, 13, -4, None, None),
    "28.png": (5, 14, -4, None, None),
    "27.png": (5, 15, -4, None, None),
    "26.png": (5, 16, -4, None, None),
    "25.png": (5, 17, -4, None, None),
    "24.png": (5, 18, -4, None, None),
    "23.png": (5, 19, -4, None, None),
    "22.png": (5, 20, -4, None, None),
    "21.png": (5, 21, -4, None, None),
    "20.png": (5, 22, -4, None, None),
    "19.png": (5, 23, -4, None, None),
    "18.png": (5, 24, -4, None, None),
    "17.png": (5, 25, -4, None, None),
    "16.png": (5, 26, -4, None, None),
    "15.png": (5, 27, -4, None, None),
    "14.png": (5, 28, -4, None, None),
    "13.png": (5, 29, -4, None, None),
    "12.png": (5, 30, -4, None, None),
    "11.png": (5, 31, -4, None, None),
    "10.png": (5, 32, -4, None, None),
    "9.png": (5, 33, -4, None, None),
    "8.png": (5, 34, -4, None, None),
    "7.png": (5, 35, -4, None, None),
    "6.png": (5, 36, -4, None, None),
    "5.png": (5, 37, -4, None, None),
    "4.png": (5, 38, -4, None, None),
    "3.png": (5, 39, -4, None, None),
    "2.png": (5, 40, -4, None, None),
    "1.png": (5, 41, -4, None, None),
    "SkipBattle.png": (4, None, -1, None, None),
    "WinRateBaby.png": (4, None, None, None, None),
    "PostBattleFloor.png": (4, None, -3, None, None),
    "PostBattleGift.png": (4, None, -3, None, None),
    "EncounterReward.png": (4, None, 3, None, None),
    "VictoryIndicator.png": (4, None, -3, None, None),
    "VeryHigh.png": (8, 6, -5, None, None),
    "High.png": (8, 5, -5, None, None),
    "Normal.png": (8, 4, -5, None, None),
    "Low.png": (8, 3, -5, None, None),
    "VeryLow.png": (8, 2, -5, None, None),
    "CharChoice.png": (3, None, 5, None, None),
    "Skip.png": (3, None, None, None, None),
    "Continue.png": (3, None, -2, None, None),
    "CommenceBattle.png": (3, None, 1, None, None),
    "Commence.png": (3, None, None, None, None),
    "Proceed.png": (3, None, -2, None, None),
    "Enter.png": (1, None, None, None, None),
    "Halt.png": (1, 1, None, None, None),
    "Resume.png": (1, None, None, None, None),
    "SinkingStarter.png": (1, None, None, "Sinking", None),
    "ChargeStarter.png": (1, None, None, "Charge", None),
    "BleedStarter.png": (1, None, None, "Bleed", None),
    "BurnStarter.png": (1, None, None, "Burn", None),
    "TremorStarter.png": (1, None, None, "Tremor", None),
    "ConfirmGift.png": (1, None, None, None, None),
    "ConfirmGiftHighlighted.png": (1, None, None, None, None),
    "HardActivated.png": (1, None, None, None, None),
    "RewardIndicator.png": (1, None, 6, None, None),
    "Defeat.png": (1, None, None, None, None),
    "Window.png": (1, None, None, None, None),
    "ThemePack.png": (1, None, 4, None, None),
    "Self.png": (1, None, None, None, None),
    "RandomIndicator.png": (1, None, 2, None, None),
    "ClearSelection.png": (1, None, 3, None, None),
    "BattleIndicator.png": (1, None, 3, None, None),
    "DoorEnter.png": (1, None, None, None, None),
    "GiftChoice.png": (1, None, None, None, None),
    "GiftFail.png": (1, None, None, None, None),
    "Finish.png": (1, None, None, None, None),
    "ClaimRewards.png": (1, None, 1, None, None),
    "HomeScreen.png": (1, None, None, None, None),
    "SelectEvent.png": (1, None, None, None, None),
    "Shop.png": (1, None, 5, None, None),
}

# Dictionary to store actions for images
actions_dict = {
    "Drive.png": [
        ("move_click", (1307, 963), True, 0.75),
        ("move_click", (660, 461), True, 0.4),
        ("move_click", (957, 527), True, 0.25),
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
    "ThemePack.png": [
        ("move_click", (0,0), False, 0.25),
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
    "Resume.png": [
        ("move_click", None, True, 0),
    ],
    "SinkingStarter.png": [
        ("move_click", None, True, 0.5),
        ("move_click", (1437, 391), True, 0.25),
        ("move_click", (1456, 555), True, 0.5),
        ("move_click", (1624, 876), True, 0.25),
    ],
    "ChargeStarter.png": [
        ("move_click", None, True, 0.5),
        ("move_click", (1437, 391), True, 0.25),
        ("move_click", (1458, 712), True, 0.5),
        ("move_click", (1624, 876), True, 0.25),
    ],
    "BurnStarter.png": [
        ("move_click", None, True, 0.5),
        ("move_click", (1437, 391), True, 0.25),
        ("move_click", (1369, 548), True, 0.5),
        ("move_click", (1624, 876), True, 0.25),
    ],
    "BleedStarter.png": [
        ("move_click", None, True, 0.5),
        ("move_click", (1437, 391), True, 0.25),
        ("move_click", (1456, 555), True, 0.5),
        ("move_click", (1624, 876), True, 0.25),
    ],
    "TremorStarter.png": [
        ("move_click", None, True, 0.5),
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
    "RandomGift4.png": [
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
    "Resource1.png": [
        ("move_click", None, True, 0.25),
        ("move_click", (1185, 788), True, 0),
    ],
    "KeywordRefresh.png": [
        ("move_click", None, True, 0.25),
    ],
    "Burn.png": [
        ("move_click", None, True, 0.25),
        ("move_click", (1182, 842), True, 0),
    ],
    "Charge.png": [
        ("move_click", None, True, 0.25),
        ("move_click", (1182, 842), True, 0),
    ],
    "Bleed.png": [
        ("move_click", None, True, 0.25),
        ("move_click", (1182, 842), True, 0),
    ],
    "Poise.png": [
        ("move_click", None, True, 0.25),
        ("move_click", (1182, 842), True, 0),
    ],
    "Rupture.png": [
        ("move_click", None, True, 0.25),
        ("move_click", (1182, 842), True, 0),
    ],
    "Sinking.png": [
        ("move_click", None, True, 0.25),
        ("move_click", (1182, 842), True, 0),
    ],
    "Tremor.png": [
        ("move_click", None, True, 0.25),
        ("move_click", (1182, 842), True, 0),
    ],
    "LeaveShop.png": [
        ("move_click", None, True, 1),
        ("press_enter",),
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

# Generate actions for 1.png to 41.png dynamically
for i in range(1, 42):
    actions_dict[f"{i}.png"] = [("drag", None, (954, 948), 3)]

paused_indices = set()

def kill_script():
    """Listen for the alt+s key to stop the script."""
    if keyboard.is_pressed('alt+s'):
        pyautogui.alert(text='Script has been stopped', title='Force Stop', button='OK')
        sys.exit()

def check_higher_priority(current_priority, selected_tag):
    """Check if a higher priority image is found within 0.05 seconds."""
    start_time = time.time()
    while time.time() - start_time < 0.05:
        for child in combined_dict:
            if combined_dict[child][3] == selected_tag or combined_dict[child][3] is None:
                priority = combined_dict[child][1]
                if priority is not None and priority > current_priority:
                    try:
                        location = pyautogui.locateCenterOnScreen(os.path.join('Menu', child), confidence=0.8)
                        if location:
                            return True
                    except pyautogui.ImageNotFoundException:
                        continue
        time.sleep(0.1)  # Sleep for a short time to avoid busy-waiting
    return False

def search_for_image(image_file, child):
    global current_index, paused_indices

    # Check if the image's index matches the current index
    if combined_dict[child][0] == current_index:
        try:
            # Re-enabled confidence with a value (e.g., 0.8 for 80% similarity)
            location = pyautogui.locateCenterOnScreen(image_file, confidence=0.8)
            if location:
                # Check if the image has a priority value
                current_priority = combined_dict[child][1] if combined_dict[child][1] is not None else 0
                if current_priority > 0:
                    if check_higher_priority(current_priority, selected_tag):
                        return

                # Check if the image has a tag and if it matches the selected tag
                image_tag = combined_dict[child][3]
                if image_tag is not None and image_tag != selected_tag:
                    return

                # Check if the image has the "Gift" tag
                if combined_dict[child][4] == "Gift":
                    actions = [
                        ("move_click", None, True, 0),
                        ("move_click", (1115, 723), True, 0.5),
                        ("press_enter",),
                        ("move_click", (0, 0), True, 0),
                    ]
                else:
                    actions = actions_dict.get(child, [])

                print(f"Found image: {child} with priority: {current_priority}")

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

                        if click:
                            pyautogui.click()

                    elif action_type == "drag":
                        use_coords, end_coords, duration = action[1:]
                        if use_coords:
                            start_coords = use_coords
                        else:
                            start_coords = location  # Use the image's location

                        pyautogui.moveTo(start_coords)

                        pyautogui.mouseDown()  # Simulate pressing down the mouse
                        time.sleep(0.1)  # Reduced delay for smoother dragging
                        pyautogui.moveTo(end_coords, duration=duration)
                        pyautogui.mouseUp()  # Release the mouse at the end of the drag

                    elif action_type == "press_enter":
                        pyautogui.press('enter')  # Simulate pressing the Enter key

                    elif action_type == "press_p":
                        pyautogui.press('p')  # Simulate pressing the 'P' key
                        time.sleep(0.3)  # Reduced sleep time after pressing 'p'

                    if buffer_time > 0:
                        time.sleep(buffer_time)

                # Update the index based on the image found
                old_index = current_index  # Store the old index value
                index_change = combined_dict[child][2] if combined_dict[child][2] is not None else 0
                current_index += index_change  # Use dictionary to update index

                # Print the current_index value if it has changed
                if old_index != current_index:
                    print(f"current_index changed to: {current_index}")

                # If ClearSelection.png is detected, click all character locations
                if child == "ClearSelection.png":
                    click_all_characters()

        except pyautogui.ImageNotFoundException:
            return
    else:
        # Pause searching for this index
        paused_indices.add(combined_dict[child][0])

def menu_nav():
    """Search through the menu images."""
    global current_index, paused_indices

    script_dir = os.path.dirname(os.path.realpath(__file__))
    menu_path = os.path.join(script_dir, 'Menu')
    children = os.listdir(menu_path)

    for child in children:
        image_file = os.path.join(menu_path, child)

        if image_file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            # Filter out images that do not match the selected tag
            if combined_dict[child][3] == selected_tag or combined_dict[child][3] is None:
                if combined_dict[child][0] not in paused_indices:
                    search_for_image(image_file, child)

    # Resume paused indices if current_index matches
    paused_indices = {idx for idx in paused_indices if idx != current_index}

def main():
    start_time = time.time()
    while True:
        kill_script()  # Check for script termination
        menu_nav()  # Search for images in the menu folder
        time.sleep(0.5)  # Reduced sleep for quicker iteration through images

        # Check if no image is found within 2 minutes and reset index
        if time.time() - start_time > 120:
            print("No image found within 2 minutes. Resetting index to 1.")
            current_index = 1
            start_time = time.time()

    print("Script is exiting (this won't happen unless manually stopped).")

main()