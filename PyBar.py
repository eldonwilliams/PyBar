from math import floor
from enum import Enum, auto

#used to get some thing uwu
def clamp(minimum, x, maximum):
    return max(minimum, min(x, maximum))

#changes the char at a position
def replace(string, pos, newValue):
    sep = list(string)
    sep[pos] = newValue
    return "".join(sep)

class FormatEnums(Enum):
    """
    Contains types of formats that are used by the represent method
    """
    #percent positions
    TOP_PERCENT = auto() #puts the percent / progress above the bar
    SIDE_PERCENT = auto() #puts the percent / progress on the same lines as the bar
    BELOW_PERCENT = auto() #puts the percent / progress below the bar
    INTEGRATED_PERCENT = auto() #puts the percent / progress in the bar, the length of bar must be longer than percent
    #side characters
    CURLY_SIDE = auto() #makes the edges {} respectively
    PARENTHESES_SIDE = auto() #makes the edges () respectively
    LINE_SIDE = auto() #makes the edges |
    BRACE_SIDE = auto() #makes the edges [] respectively
    NO_SIDE = auto() #makes the edges blank
    ANGLE_SIDE = auto() #makes the edges <> respectively "I could not think of better name for it other than angle side please make a github issue if you have a better one"
    #fill characters
    ONE_FILL = auto() #makes the filled area "1"
    SMALL_ASCII_FILL = auto() #makes the filled area "■"
    EQUAL_FILL = auto() #makes the filled area "="
    PLUS_FILL = auto() #makes the filled area "+"
    ASCII_FILL = auto() #makes the filled area "█"
    #empty characters
    ZERO_EMPTY = auto() #makes the empty area "0"
    SPACE_EMPTY = auto() #makes the empty area " "
    DASH_EMPTY = auto() #makes the empty area "-"



class ProgressBar(object):
    """
    Describes a bar that can progress, also offers a function to get a representation
    """

    def __init__(self):
        #init method
        self.progress = 0

    def addProgress(self, progress=1):
        #adds a given progress *default 1* to the self.progress
        self.progress = clamp(0, self.progress + progress, 100)
    
    def removeProgress(self, progress=1):
        #removes a given progress *default 1* from the self.progress
        self.progress = clamp(0, self.progress - progress, 100)

    def resetProgress(self):
        #resets self.progress to 0
        self.progress = 0

    def represent(self, *format, **specialFormat):
        """
        Returns a x segment *default 10* representation of the current progress of the member
        """

        returnValue = ""
        side_char = (specialFormat["side_char"] if "side_char" in specialFormat else ["[", "]"])
        fill_char = (specialFormat["fill_char"] if "fill_char" in specialFormat else "=")
        empty_char = (specialFormat["empty_char"] if "empty_char" in specialFormat else " ")
        segments = int((specialFormat["segments"] if "segments" in specialFormat else 10))

        if FormatEnums.TOP_PERCENT in format:
            returnValue +=  str(round(self.progress, 1)) + "%\n"

        if FormatEnums.CURLY_SIDE in format:
            side_char = ["{", "}"]
        elif FormatEnums.BRACE_SIDE in format:
            side_char = ["[", "]"]
        elif FormatEnums.PARENTHESES_SIDE in format:
            side_char = ["(", ")"]
        elif FormatEnums.LINE_SIDE in format:
            side_char = ["|", "|"]
        elif FormatEnums.NO_SIDE in format:
            side_char = ["", ""]
        elif FormatEnums.ANGLE_SIDE in format:
            side_char = ["<", ">"]

        if FormatEnums.EQUAL_FILL in format:
            fill_char = "="
        elif FormatEnums.PLUS_FILL in format:
            fill_char = "+"
        elif FormatEnums.ASCII_FILL in format:
            fill_char = "█"
        elif FormatEnums.SMALL_ASCII_FILL in format:
            fill_char = "■"
        elif FormatEnums.ONE_FILL in format:
            fill_char = "1"

        if FormatEnums.DASH_EMPTY in format:
            empty_char = "-"
        elif FormatEnums.SPACE_EMPTY in format:
            empty_char = " "
        elif FormatEnums.ZERO_EMPTY in format:
            empty_char = "0"

        filledSegments = int(self.progress//(100/segments))
        emptySegments = segments - filledSegments

        bar = side_char[0] + (fill_char * filledSegments) + (emptySegments * empty_char) + side_char[1]

        if FormatEnums.INTEGRATED_PERCENT in format:
            percent = str(round(self.progress, 1)) + "%"
            if not len(bar) < len(percent):
                middlePos = len(bar)//2
                if len(percent) == 2:
                    bar = replace(bar, middlePos - 1, percent[0])
                    bar = replace(bar, middlePos, percent[1])
                elif len(percent) == 3:
                    bar = replace(bar, middlePos - 1, percent[0])
                    bar = replace(bar, middlePos, percent[1])
                    bar = replace(bar, middlePos + 1, percent[2])
                elif len(percent) == 4:
                    bar = replace(bar, middlePos - 2, percent[0])
                    bar = replace(bar, middlePos - 1, percent[1])
                    bar = replace(bar, middlePos, percent[2])
                    bar = replace(bar, middlePos + 1, percent[3])


        returnValue += bar

        if FormatEnums.SIDE_PERCENT in format:
            returnValue += " " + str(round(self.progress, 1)) + "%"

        if FormatEnums.BELOW_PERCENT in format:
            returnValue += "\n" + str(round(self.progress, 1)) + "%"


        return returnValue