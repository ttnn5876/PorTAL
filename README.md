# PorTAL

Simple python GUI app that lets me launch my favorite programs using keyboard shortcuts.
Launch the program, push the right hotkey and it opens your program.

![](https://github.com/ttnn5876/PorTAL/blob/main/PorTAL.gif)

## Why?

I like my desktop clean, so no shortcuts are allowed.

## Customizability

You can edit the ```links.json``` file to add more links -
 - name: will be displayed on the button
 - path: a path to a ```.lnk``` file that will run your program
 - hotkey: a key that will be used to run your program.

Example:
```
{
    "links": [
      {
        "name": "Discord",
        "path": "C:\\Users\\ttnn5\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Discord Inc\\Discord.lnk",
        "hotkey": "D"
      },
	  .....
    ]
  }
```

## Running PorTAL
I run it with Python 3.9.11 on a Windows 11 21H2 machine
Dependencies:
 - [pywin32](https://pypi.org/project/pywin32/)
 - [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) (Making a simple modern-looking GUI with this is way easier than with good ol' Tkinter
 - [keyboard](https://pypi.org/project/keyboard/)

Just put the source in a folder with the ```links.json```  file.
I prefer to run it with ```pythonw``` to avoid the nasty black console window.

You can also use something like [AutoHotKey](https://www.autohotkey.com/) to run it using a keyboard shortcut.
This script does the trick for me:
```
dir    := "c:\porTAL\"
script  = %dir%\porTAL.pyw
#f::Run, pythonw "%script%"
WinSet,  AlwaysOnTop, On, ahk_pid %CMD%
Return
```
I also put it under ```%USERPROFILE%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup``` to make it run when I turn my PC on.
