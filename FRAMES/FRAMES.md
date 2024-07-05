# Advanced Usage Part I
### Frame Settings

## 1. Modify file path

| File | Var name | Default path | Where |
| :----: | :----: | :----: | :----: |
| ascii text file | EXPORT_PATH | `/FILM.txt` | `makefilm.py`, line 6 |
| ascii frame pictures | FRAME_PATH | `/FRAMES/frame{i}.png` | `makefilm.py`, line 9 |
| ascii video | VIDEO_PATH | `/{FRAME_PATH}\VID\VIDEO.mp4 ` | `vidwrite.py`, line 4 |
| original video | ORIGINAL_PATH | `/BadApple.mp4` | `main.py`, line 6 |
| font file | FONT_PATH | `C:\Windows\Fonts\consola.ttf` | `savefilm.py`, line 7 |

This table lists all the file paths used in this project. You can edit and adjust them.

## 2. Frame size

The variables that control the number of characters per line and the number of line in each frame are the `SCREEN_X` and `SCREEN_Y` defined in `makefilm.py`, line 15 and 16. The larger they are, the bigger the frame is. Bigger frame expresses the shape better, but slows down rendering speed. 

Frame size is also influenced by font size, which is defined in `savefilm.py`, line 8.

## 3. Grayscale Mapping

The key process of this project is grayscale mapping, namely, select an appropriate ascii character to represent the original pattern according to its grayscale value.

![Mesh grid](/Assets/mesh.png)

Initially, the colored frames are converted into grayscale frames. After that, each frame is divided into small rectangle areas. Every pixel in an area owns a grayscale value ranging from 0 to 255, then the average grayscale of an area are able to be calculated.

The ascii characters to be used are grouped by the complexity of their shape. For instance, a dot `.` looks "whiter" than `@` when background is white and font color is black. And vice versa if you are reading this page in dark mode. More specifically, we are going to link the "white degree" of a character with the average grayscale of an area, like the chart below:

| Grayscale | 0-49 | 50-99 | 100-149 | 150-199 | 200-249 | 250-255 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Ascii char | ` ` (whitespace) | `.` | `-` | `v` | `g` | `@` |

The character bank is in `makefilm.py`, line 24-39. Change the combinations and make a better scheme by yourself! Smoothing the transition from black to white by adding character group, which can be realised by increasing the value of NUM_STEP defined in `makefilm.py`, line 21. A black to white gradient picture is provided, run `makefilm.py` to test how your scheme performs.

To make the final ascii art less monotonous, more characters are added in the groups. Eventually we can replace the pixels in area with a character randomly picked out from a certain group.
