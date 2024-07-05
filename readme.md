# Bad Apple to Ascii Art
### 将Bad Apple转换为字符画

[English](en-readme.md)

![Cover](/Assets/cover.png)

## 介绍

![Workflow](/Assets/workflow.png)

本项目旨在为著名的东方主题影绘动画Bad Apple生成其字符画版本。


## 前提

#### 安装 Python IDE

Python3

#### 安装 Python 依赖库

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


## 使用方法

#### 第1步
安装python 3 IDE 和[上述](#python-libraries)依赖库。然后将本仓库克隆到本地。

#### 第2步
打开 `main.py`。 在第6行，函数 `vidOpen()` 使用你的设备上原视频的文件路径：

```python
ORIGINAL_PATH = 'BadApple.mp4'
```

你可以把示例文件路径"BadApple.mp4"改为需要转换的视频的本地实际路径。

#### 第3步
运行 `main.py`。程序会询问你想要在终端窗口逐帧读取（read）从原视频转换的字符画，还是保存（save）它们为.mp4视频文件：

```bash
Read(r) or Save(s): 
```

输入 `r` 或 `s` 进行选择，然后按下回车键继续。

如果代码是首次运行，程序将逐帧读取原视频并将转换的字符画全部写入这个文件夹内名为 `FILM.txt` 的文本文档。这个过程可能需要几分钟，请耐心等待。

如果你运行过代码，程序将直接读取已经存在的 `FILM.txt` 而不是替换它。因此，如果你想要创建一个新的文本文档，请重命名老的 `FILM.txt` 或者把它移动到其他文件夹中，如果你不再需要的话，也可以直接删除。

> [!TIP]
> 当程序不是正在运行时，你可以打开 `FILM.txt`文件。它应该类似下图这样： <br>
> ![FILM.txt belikes](/Assets/film.png)<br>
> 它真的很像胶卷（film），对吧？

#### 第4步
是时候检查成果如何了！

##### 在[第3步](#step-3)选择了读取（read）的话：

程序会逐帧读取储存在 `FILM.txt` 里的字符画，并在终端窗口中打印出来，就像播放幻灯片一样。

代码是在全屏（1920*1080）的IDLE Shell窗口中用12号consolas字体测试的。你可以根据实际情况调整窗口大小来改善播放效果，或者[调整输出参数](/FRAMES/FRAMES.md/#2-frame-size)。

##### 在[第3步](#step-3)选择了保存（save）的话：

程序会逐帧将 `FILM.txt` 中储存的字符画保存为.png图片文件。接下来会把这些图片帧连接起来，在 `FRAMES/VID` 文件夹中创建名为 `VIDEO.mp4` 的视频文件。

导出图片所用的示例字体是Windows平台上安装的consolas字体。如果程序产生类似报错：

```bash
FileNotFoundError: Font missing:<FONT_PATH>
```

请打开 `savefilm.py` 查看第7行：

```python
FONT_PATH = 'C:\Windows\Fonts\consola.ttf'
```

把字体路径改为你设备上安装的字体的实际路径。在Mac系统可能是 `/System/Library/Fonts` ，在Linux系统上可能是 `/usr/share/fonts` 。你可以改为你想使用的其他**等宽**字体。

## 高级配置
见 [FRAMES.md](/FRAMES/FRAMES.md) 和 [VID.md](/FRAMES/VID/VID.md)。

## 参考

- [OpenCV Tutorials](https://docs.opencv.org/4.10.0/d9/df8/tutorial_root.html)
- [Pillow Documentation](https://pillow.readthedocs.io/en/stable/)
