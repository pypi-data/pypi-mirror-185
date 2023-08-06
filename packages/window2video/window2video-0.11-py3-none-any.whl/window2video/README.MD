# Record Window (hwnd) and save the recording as mp4 (normalized fps) - Works even with background windows


```python
# Tested with:
# Python 3.9.13
# Windows 10


$pip install window2video

from window2video import start_recorder
# starts the recording directly
start_recorder(hwnd=985666, outputfolder='c:\\testrecording', exit_keys='ctrl+alt+k')

# interactive mode 
start_recorder_in_console()
	
```




