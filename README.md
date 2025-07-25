# Communication unit length

## How to use?
First, you need to download this folder by going to the green button `<> CODE` and press `Download ZIP`. Then, you need to unzip it on your computer. After that, open `communication_unit_length` in any text editor (preinstalled notepad on Windows is enough) and in the line `path = r"ENTER YOUR PATH HERE, INSTEAD OF THIS TEXT"` between quotation marks ( " " ) make sure you put the path to the folder with `.cha` data (e. g. `C:\Users\User\Desktop\my_folder` if the folder is on your Desktop). You can copy the path by opening the folder and clicking on the bar at the top where a similar path will be selected.

After you've successfully found and put your own path, in line `if line.startswith("*CHI:"):` feel free to replace `*CHI:` with what you need to analyse in your own project or thesis.

When all of that is done, just run your programm and the resulting data will pop up, called `results.txt`. The file will be found in the same folder where `communication_unit_length.py` is, i. e. in this folder.

## Warnings

This works for Windows only. Their might be certian problems when running this on Mac or Linux.