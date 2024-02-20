import pyaudio
import numpy as np

FRAMES_PER_BUFFER = 3200
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
p = pyaudio.PyAudio()

stream = None

def start_recording():
    global stream
    stream = p.open(
        format=FORMAT,
        channels=CHANNELS,
        rate=RATE,
        input=True,
        frames_per_buffer=FRAMES_PER_BUFFER
    )

def stop_recording():
    global stream
    if stream:
        stream.stop_stream()
        stream.close()

def record_audio(seconds=1):
    if stream is None:
        raise RuntimeError("Recording stream not started")

    frames = []
    for _ in range(0, int(RATE / FRAMES_PER_BUFFER * seconds)):
        data = stream.read(FRAMES_PER_BUFFER, exception_on_overflow = False)
        frames.append(data)

    return np.frombuffer(b''.join(frames), dtype=np.int16)

def terminate():
    p.terminate()


#def record_audio():
#    stream = p.open(
#        format=FORMAT,
#        channels=CHANNELS,
#        rate=RATE,
#        input=True,
#        frames_per_buffer=FRAMES_PER_BUFFER
#    )
#
#    # start recording
#    frames = []
#    seconds = 1
#    for i in range(0, int(RATE / FRAMES_PER_BUFFER * seconds)):
#        data = stream.read(FRAMES_PER_BUFFER)
#        frames.append(data)
#    # stop recording
#
#    stream.stop_stream()
#    stream.close()
#    
#    return np.frombuffer(b''.join(frames), dtype=np.int16)
#
#
#def terminate():
#    p.terminate()