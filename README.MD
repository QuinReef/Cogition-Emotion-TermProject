# PsychoPy Color Sequence Experiment README

## Overview

This project is a PsychoPy experiment that presents a sequence of colors for the participant to remember after watching a video and listening to audio based on the participant's mood (happy or sad). The experiment collects and saves data on the participant's responses.

## Requirements

To run this application, you need:

- Python 3.x (preferably 3.7 or later)
- PsychoPy
- Required media files: `happy.mp4`, `sad.mp4`, `happy.mp3`, and `sad.mp3` in the `media/videos` directory.

## Setting Up the Environment

### 1. Install Python

Make sure you have Python installed on your system. You can download it from the official [Python website](https://www.python.org/downloads/).

### 2. Create a Virtual Environment If Not Availible Already

Open a terminal (or Command Prompt) and navigate to your project directory. Then, create a virtual environment with the following command:

```bash
python -m venv venv
```
This will create a folder named venv in your project directory.

### 3. Activate the Virtual Environment
To start using the virtual environment, you need to activate it:

On Windows:

```bash
venv\Scripts\activate
```
On macOS and Linux:

```bash
source venv/bin/activate
```
After activation, your terminal prompt should change to indicate that you are now in the virtual environment.

### 4. Install Required Packages
Install the necessary packages using pip. You can do this with the following command:

```bash
pip install psychopy
```
This command will install PsychoPy and its dependencies.

5. Organize Your Project Files
Make sure your project directory has the following structure:

```bash
/your_project_directory
│
├── /media
│   └── /videos
│       ├── happy.mp4
│       ├── sad.mp4
│   └── /audio
│       ├── happy.mp3
│       └── sad.mp3
│
├── experiment.py  
└── ...
```
### 6. Running the Experiment
Once you have set up your environment and organized your files, you can run the experiment by executing the following command in your terminal:

``` bash
python experiment.py
```
### 7. Deactivating the Virtual Environment
After you finish running your experiment, you can deactivate the virtual environment by simply typing:

```bash
deactivate
```

## Data Output
The experiment will save the participant's responses and other relevant data to a CSV file named ```color_sequence_data.csv``` in the root of your project directory.
