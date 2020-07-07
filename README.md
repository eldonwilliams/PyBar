# PyBar
pybar is a simple lib that offers a progress bar, pretty simple.

## Documentation
PyBar.py contains two classes, one is a progressbar and one is a enum class.
I used enums just cuz. I'll go over each enum in a minute
ProgressBar contains 4 methods.

## 1 | Methods of ProgressBar [source](https://github.com/MrTops/PyBar/blob/master/PyBar.py#L43)
this chapter will go over the methods of ProgressBar

### 1.1 | ``addProgress(progress=1)`` [source](https://github.com/MrTops/PyBar/blob/master/PyBar.py#L52)
adds a given amount of progress to the member's progress value.
The default is 1 and the limit for progress is 100

### 1.2 | ``removeProgress(progress=1)`` [source](https://github.com/MrTops/PyBar/blob/master/PyBar.py#L56)
removes a given amount of progress from the member's progress value.
The default is 1 and the limit for removing is 0

### 1.3 | ``resetProgress()`` [source](https://github.com/MrTops/PyBar/blob/master/PyBar.py#L60)
removes all progress from the member's progress value, and sets it to 0

### 1.4 | ``represent(*format, **specialFormat)`` [source](https://github.com/MrTops/PyBar/blob/master/PyBar.py#L64)
returns a string object which represents the state of the ProgressBar
format takes in enums from FormatEnums, specialFormat allows you to specify exact values for things used by the represent method

#### 1.4.1 | specialFormat > side_char
Default: ["[", "]"]
side_char is a array object which defines the characters to be at the edges of the progress bar.
index 0 is the character for the left edge
index 1 is the character for the right edge

#### 1.4.2 | specialFormat > fill_char
Default: "="
fill_char is the character to be displayed for a filled section

#### 1.4.3 | specialFormat > empty_char
Default: " "
empty_char is the character to be displayed for a empty section

#### 1.4.4 | specialFormat > segments
Default: 10
the amount of segments / sections to use

## 2 | FormatEnums [source](https://github.com/MrTops/PyBar/blob/master/PyBar.py#L14)

### 2.1 | Percent Positions [source](https://github.com/MrTops/PyBar/blob/master/PyBar.py#L18)
```py
    TOP_PERCENT = auto() #puts the percent / progress above the bar
    SIDE_PERCENT = auto() #puts the percent / progress on the same lines as the bar
    BELOW_PERCENT = auto() #puts the percent / progress below the bar
    INTEGRATED_PERCENT = auto() #puts the percent / progress in the bar, the length of bar must be longer than percent
```

### 2.2 | Side Characters [source](https://github.com/MrTops/PyBar/blob/master/PyBar.py#L23) 
```py
    CURLY_SIDE = auto() #makes the edges {} respectively
    PARENTHESES_SIDE = auto() #makes the edges () respectively
    LINE_SIDE = auto() #makes the edges |
    BRACE_SIDE = auto() #makes the edges [] respectively
    NO_SIDE = auto() #makes the edges blank
    ANGLE_SIDE = auto() #makes the edges <> respectively "I could not think of better name for it other than angle side please make a github issue if you have a better one"
```

### 2.3 | Fill Characters [source](https://github.com/MrTops/PyBar/blob/master/PyBar.py#L30)
```py
    ONE_FILL = auto() #makes the filled area "1"
    SMALL_ASCII_FILL = auto() #makes the filled area "■"
    EQUAL_FILL = auto() #makes the filled area "="
    PLUS_FILL = auto() #makes the filled area "+"
    ASCII_FILL = auto() #makes the filled area "█"
```

### 2.4 | Empty Characters [source](https://github.com/MrTops/PyBar/blob/master/PyBar.py#L36)
```py
    ZERO_EMPTY = auto() #makes the empty area "0"
    SPACE_EMPTY = auto() #makes the empty area " "
    DASH_EMPTY = auto() #makes the empty area "-"
```
