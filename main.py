# main.py

import numpy as np
from tensorflow.keras import models
from recording_helper import record_audio, terminate, start_recording, stop_recording
from tf_helper import preprocess_audiobuffer, get_optimizer
import tkinter as tk
from turtle_helper import move_turtle, setup_turtle, reset_turtle
from tkinter import messagebox # for alert after recognizing "stop" 

is_listening = False # set it with the spacebar

# !! Modify this in the correct order
commands = ['left', 'noise', 'go', 'right', 'stop']

#left : 90 degree left
#right : 90 degree right
#go: 1 step forward
#stop: stop listening and stop at the position

loaded_model = models.load_model("saved_model-v2")

# Set the optimizer for the loaded model
optimizer = get_optimizer()
loaded_model.compile(optimizer=optimizer, loss='sparse_categorical_crossentropy', metrics=['accuracy'])

def predict_mic():
    audio = record_audio()
    spec = preprocess_audiobuffer(audio)
    prediction = loaded_model(spec)
    label_pred = np.argmax(prediction, axis=1)
    command = commands[label_pred[0]]
    print("Predicted label:", command)
    return command

def execute_actions():
    confirm = messagebox.askyesno("Confirm Execution", "Do you want to execute all actions?")
    if confirm:
    # Execute actions based on the accumulated recognized words
        for word in displayed_keywords:
            # Add your logic to execute actions for each recognized word
            print(f"Executing action for: {word}")
            move_turtle(word)

        # Clear the array after "go" is recognized
        recognized_words.clear()
    else:
        recognized_words.remove("stop")
        print("Execution cancelled, continue programming.")

def on_close():
    terminate()
    root.destroy()  # Close the Tkinter window

def update_display():
    live_content.set(", ".join(displayed_keywords))
    root.after(1000, update_display)  # Update every 1000 milliseconds (1 second)

def handle_keypress(event):
    global is_listening
    if event.char == 'x' and displayed_keywords:
        removed_word = displayed_keywords.pop()
        print(f"Removed word: {removed_word}")
    elif event.keysym == 'Return':
        restart_application()
    elif event.keysym == 'space':
        if not is_listening:
            print("Starting listening")
            start_recording()
            is_listening = True
        else:
            print("Stopping listening")
            stop_recording()
            is_listening = False

def restart_application():
    global recognized_words, displayed_keywords
    recognized_words.clear()
    displayed_keywords.clear()
    reset_turtle()
    print("Application restarted")

if __name__ == "__main__":
    recognized_words = []
    displayed_keywords = []
    #displayed_keywords = ['left', 'go', 'go', 'right', 'go', 'go', 'right', 'go', 'go', 'left', 'go', 'go','left', 'go', 'go']
    #displayed_keywords = ['go', 'go', 'left', 'go', 'go', 'right', 'go', 'right', 'go', 'right', 'go', 'go', 'go', 'left', 'go']

    root = tk.Tk()
    root.title("Recognized Words Display")

    live_content = tk.StringVar()
    live_content.set("No recognized words yet.")

    label = tk.Label(root, textvariable=live_content)
    label.pack()

    canvas = tk.Canvas(root, width=600, height=600)
    canvas.pack()

    # Setup Turtle to use the same canvas
    setup_turtle(canvas)

    root.after(1000, update_display)  # Start the display update loop
    root.protocol("WM_DELETE_WINDOW", on_close)  # Handle window close event

    root.bind('<KeyPress>', handle_keypress)

    while True:
        if is_listening:
            command = predict_mic()

            recognized_words.append(command)
            if command in ['go', 'right', 'left']:
                # Accumulate recognized words in the array
                displayed_keywords.append(command)
                print(displayed_keywords)

            if "stop" in recognized_words:
                execute_actions()

        root.update()  # Update the Tkinter window
