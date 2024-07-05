# Bad Apple to Ascii Art
### Converting Bad Apple to Ascii Art

[中文](readme.md)

![Cover](/Assets/cover.png)

## Introduction

![Workflow](/Assets/workflow.png)

This project is aiming at generating an ascii-art version of the well known touhou themed silhouette anime *Bad Apple*.


## Prerequisites

#### Python IDE

Python3

#### Python Libraries

+ numpy
```bash
pip install numpy
```

+ Pillow
```bash
pip install Pillow
```

+ opencv-python
```bash
pip install opencv-python
```


## Usage

#### Step 1
Install python3 IDE and the libraries refered [before](#python-libraries). Then clone this repository to your device.

#### Step 2
Open `main.py`. In line 6, function `vidOpen()` uses the file path of the original video on your device:

```python
ORIGINAL_PATH = 'BadApple.mp4'
```

You can modify the example file path "BadApple.mp4" to make it in accordance with the actual local directory.

#### Step 3
Run `main.py`. The program will ask you whether you want to read the ascii-art by frame converted from the original video in terminal window or save them as a .mp4 video file.

```bash
Read(r) or Save(s): 
```

Type `r` or `s` to choose, and press `Enter` to continue. 

If this is the first time you run the code, the program will read original video by frame and write the generated the ascii version frames in a .txt file named `FILM.txt` in this folder. This process may take few minutes, please wait patiently.

If you ran the code before, the program will directly read the existed `FILM.txt` file rather than replace it. So if you want to create a new one, please rename the old `FILM.txt` or move it to other directory, or delete it if you don't need it anymore.

> [!TIPS]
> You can open `FILM.txt` when the program is not running. It is supposed to be like the following figure shows:
> ![FILM.txt belikes](/Assets/film.png)
> It does resemble the real film, isn't it?

#### Step 4
Time to check out the result!

##### Chose 'read' in [Step 3](#step-3):

The program will read each ascii-art frame stored in `FILM.txt`, and print in the terminal window, like playing sildes.

The code was tested in a full screen(1920*1080) IDLE Shell window with size 12 consolas font. You can resize the terminal window for a better display effect, or [adjust the output parameters](/FRAMES/FRAMES.md/#2-frame-size).

##### Chose 'save' in [Step 3](#step-3):

The program will save each ascii-art frame stored in `FILM.txt` as .png file in `FRAMES` folder. Next, a video named `VIDEO.mp4` will be created in `FRAMES/VID` folder by connecting the .png pictures.

The font used as example is consolas installed on Windows platform. If the program reports an error like this:

```bash
FileNotFoundError: Font missing:<FONT_PATH>
```

Please open `savefilm.py`, see line 7:

```python
FONT_PATH = 'C:\Windows\Fonts\consola.ttf'
```

Change the font path according to its actual location on your machine. It may be in `/System/Library/Fonts` on Mac OS, or `/usr/share/fonts` on Linux. You can switch to other **monospaced** font as you like.

## Advanced configuration
See [FRAMES.md](/FRAMES/FRAMES.md) and [VID.md](/FRAMES/VID/VID.md).

## References

- [OpenCV Tutorials](https://docs.opencv.org/4.10.0/d9/df8/tutorial_root.html)
- [Pillow Documentation](https://pillow.readthedocs.io/en/stable/)
