#This code was written as part of the course Cognition and Emotion at University Utrecht 2024
# Student numbers: 2565889, ...

from psychopy import visual, core, event, data, sound,monitors
import random

mon = monitors.Monitor('testMonitor', width=40, distance=60)
mon.setSizePix((1680, 1050))
monitor_size = mon.getSizePix()  # Get monitor size in pixels
window_size = (monitor_size[0], monitor_size[1])  # Use monitor dimensions for window size

# Set up window in full screen
win = visual.Window(monitor=mon,  color="white", units="pix", size=window_size)


# Define colors and mapping for input keys
color_options = ["red", "green", "blue", "purple"]
abbrev_to_color = {'r': "red", 'g': "green", 'b': "blue", 'p': "purple"}  # Key abbreviations

data_file_path = "./data/trials/color_sequence_data"
# Set up Experiment Handler for saving data
data_file = data.ExperimentHandler(dataFileName=data_file_path)

# Ask the researcher to set the sequence length
sequence_length_text = visual.TextStim(win, text="Enter the length of the color sequence (default is 4):", color="black", pos=(0, 100))
sequence_length_text.draw()
win.flip()


# Capture the sequence length input
sequence_length_keys = event.waitKeys(keyList=[str(i) for i in range(1, 10)] + ['return'])  # Accept numbers 1-9 or return

# Extract sequence length if a number key was pressed; otherwise, default to 4
if sequence_length_keys and sequence_length_keys[0].isdigit():
    sequence_length = int(sequence_length_keys[0])
else:
    sequence_length = 4  # Default length

# Run multiple trials
for trial in range(100):
    
    
    
    start_text = visual.TextStim(win, text="Press 's' or 'h' to start the trial in a sad(s) or happy(h) mood, or 'q' to quit and save data.", color="black")
    start_text.draw()
    win.flip()
    
    # Wait for researcher input for mood selection
    trail_key = event.waitKeys(keyList=['h', 's', 'q'])[0]
    if trail_key == 'q':
        print("Experiment terminated early by researcher.")
        break
    
    mood = "happy" if trail_key == 'h' else "sad"

    # Display appropriate video and audio based on mood
    video_path = "happy.mp4" if mood == "happy" else "sad.mp4"  
    audio_path = "happy.wav" if mood == "happy" else "sad.wav"  
    
    movie = visual.MovieStim(win, filename=f"./media/videos/{video_path}", noAudio=False)  # Load video with audio


    # Play the video with an explicit timeout (10 seconds in this example)
    start_video_time = core.getTime()
    video_duration_limit = 10  # Set a maximum duration for the video

    # Play the video until it finishes/set timeout as FINISHED is not always captured. 
    while movie.status != visual.FINISHED:
        movie.draw()
        win.flip()
        
        # Check for a timeout to ensure the program doesn't get stuck
        if core.getTime() - start_video_time > video_duration_limit:
            break  # Force exit if video exceeds expected duration
    movie.stop()

    # Generate a random color sequence
    color_sequence = [random.choice(color_options) for _ in range(sequence_length)]

    # Intro Screen
    intro_text = visual.TextStim(win, text="Remember the sequence of colors shown on screen. Press 'space' when ready.", color="black")
    intro_text.draw()
    win.flip()
    event.waitKeys()  # Wait for user to press any key
    audio = sound.Sound(f"./media/audio/{audio_path}")  # Load audio

    # Play audio at the start of the trial
    audio.play()


    # Display the color sequence
    for color in color_sequence:
        stim = visual.Rect(win, width=200, height=200, fillColor=color)
        stim.draw()
        win.flip()
        core.wait(1.0)  # Show each color for 1 second
        win.flip()
        core.wait(0.2)  # Pause for 0.2 seconds between colors

    # Prompt for input
    input_prompt = visual.TextStim(win, text="Type the color sequence (r for red, g for green, b for blue, p for purple)", color="black", pos=(0, 100))
    input_prompt.draw()
    win.flip()

    # Capture user input for sequence and measure response time
    typed_colors = []
    start_time = core.getTime()  # Start timing
    while True:
        user_response = event.waitKeys(keyList=list(abbrev_to_color.keys()) + ['return'], timeStamped=True)
        if user_response[-1][0] == 'return':  # End input on 'return'
            break
        color_abbrev = user_response[-1][0]
        if color_abbrev in abbrev_to_color:
            typed_colors.append(abbrev_to_color[color_abbrev])  # Convert abbreviation to color name
    end_time = core.getTime()  # End timing
    response_time = end_time - start_time  # Calculate time taken for input

    # Determine if the response matches the sequence
    feedback = ""
    if len(typed_colors) == len(color_sequence):
        if typed_colors == color_sequence:
            feedback = "Correct!"
        else:
            feedback = "Incorrect!"
    else:
        feedback = "Incomplete sequence."

    # Display feedback
    feedback_text = visual.TextStim(win, text=feedback, color="black")
    feedback_text.draw()
    win.flip()
    core.wait(2)

    audio.stop()  # Stop the audio after the video ends 
    
    # Store data for this trial
    data_file.addData("trial", trial + 1)
    data_file.addData("mood", mood)
    data_file.addData("color_sequence", color_sequence)
    data_file.addData("user_response", typed_colors)
    data_file.addData("feedback", feedback)
    data_file.addData("response_time", response_time)
    data_file.nextEntry()  # Record the data for this trial

# Save data to a file at the end
data_file.saveAsWideText(data_file_path)

# Close the window and quit PsychoPy
win.close()
core.quit()
