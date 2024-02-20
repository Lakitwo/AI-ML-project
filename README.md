# Realtime Voice Command Recognition

This is inspired by the [GitHub Project of Patrick Loeber](https://github.com/AssemblyAI-Examples/realtime-voice-command-recognition) and adapted by Lukas Kofler

## how the program works
The program differenciates between the keywords 'go', 'right', 'left', 'stop' and noise.
To start/stop listening to keywords, press the SPACE-KEY
To restart the program, press the RETURN-KEY
To remove the last recognized keyword from the recognized keywords list, press X-KEY

### see also the attatched tutorial video

## prepare the program
the commands array in main.py has to hold the keywords in exactly the same order as they are printed in the [colab-repository](https://colab.research.google.com/drive/17YWAlm38g1Nx-prpqqwo4MSdd9fVdDI9?usp=sharing), because after importing, augmenting and shuffeling the keywords, the order of the labels can change

Start the main.py using ```python main.py```
