# 🏏 Cricket Scoreboard Data Extraction from Video
A Computer Vision and OCR-based solution developed for the **Round 1 – Computer Vision Engineer Assessment at FOG**.

The project processes the provided `bowling_scoreboard.mp4` cricket video, samples video frames, extracts the configured scoreboard region, performs OCR using **EasyOCR**, parses the recognized scoreboard text, and generates structured **JSON** and **CSV** output.

## 🎯 Objective
The objective of this project is to extract scoreboard information from the supplied cricket video as accurately as possible using a Python-based Computer Vision and OCR pipeline.

The implementation focuses on:
- Video processing using OpenCV
- Frame sampling
- Configured Scoreboard Region of Interest (ROI)
- OCR-based text extraction
- OCR confidence collection
- Scoreboard text parsing
- Structured data generation
- JSON and CSV output

## 🔄 Processing Pipeline

                  ┌──────────────────────┐
                  │      Input Video     │
                  │  bowling_scoreboard  │
                  │         .mp4         │
                  └──────────┬───────────┘
                             │
                             ▼
                   ┌──────────────────────┐
                   │  OpenCV Video Read   │
                   └──────────┬───────────┘
                              │
                              ▼
                  ┌──────────────────────┐
                  │   Frame Sampling     │
                  └──────────┬───────────┘
                             │
                             ▼
                  ┌──────────────────────┐
                  │Configured Scoreboard │
                  │        ROI           │
                  └──────────┬───────────┘
                             │
                             ▼
                  ┌──────────────────────┐
                  │       EasyOCR        │
                  │  Text + Confidence   │
                  └──────────┬───────────┘
                             │
                             ▼
                  ┌──────────────────────┐
                  │   Scoreboard Parser  │
                  └──────────┬───────────┘
                             │
                             ▼
              ┌──────────────────────────────┐
              │     Structured Results       │
              └─────────────┬─┬──────────────┘
                            / \
                           /   \
                          ▼     ▼
                    ┌────────┐ ┌────────┐
                    │  JSON  │ │  CSV   │
                    └────────┘ └────────┘

🛠️ Technology Stack
Core
Python 3.10+
Computer Vision & Video Processing
OpenCV
OCR
EasyOCR
Data Processing
NumPy
Pandas
Output
JSON
CSV
Development & Version Control
Visual Studio Code
Git
GitHub


📂 Project Structure
COMPUTER-VISION-ENGINEER-PROJECT/
│
├── data/
│   └── bowling_scoreboard.mp4
│
├── outputs/
│   ├── results.json
│   └── results.csv
│
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── main.py
│   └── parser.py
│
├── tests/
│   └── __init__.py
│
├── .gitignore
├── README.md
├── requirements.txt
└── sample_frame.jpg


Component Description

data/bowling_scoreboard.mp4	Input cricket scoreboard video
src/main.py	Main video-processing and OCR execution pipeline
src/config.py	Project configuration including video path, ROI and frame sampling settings
src/parser.py	Converts OCR text into structured scoreboard information
outputs/results.json	Structured JSON results
outputs/results.csv	Tabular CSV results
sample_frame.jpg	Sample input frame
tests/	Test package directory


⚙️ Implementation Details
1. Video Processing
The input video is loaded using OpenCV.
data/bowling_scoreboard.mp4
The application reads the video frame-by-frame and obtains the video properties required for processing.


2. Frame Sampling
To reduce unnecessary OCR processing, the implementation samples frames at a configured interval.

The current configuration uses:

FRAME_SAMPLE_RATE = 5

The current execution processes up to the first 200 frames, resulting in a maximum of 40 sampled frames.

This provides multiple observations of the scoreboard while avoiding OCR execution on every frame.

3. Scoreboard ROI
The current implementation uses a predefined/configured Region of Interest (ROI) for the supplied video.

The ROI is configured in:

src/config.py

Current configuration:

ROI = (0, 0, 1280, 720)

The selected region is passed to the OCR pipeline.

> Important: The current implementation uses a configured ROI based on the supplied video's scoreboard layout. It does not use a trained object-detection model or automatic scoreboard localization.

4. OCR Processing
The project uses EasyOCR to recognize text from the selected scoreboard region.

For each processed frame, OCR provides:
Recognized text
OCR confidence
Detection information
The recognized text is then passed to the scoreboard parser.

5. Scoreboard Parsing
The OCR output is processed by:

src/parser.py

The parser uses text patterns to identify scoreboard information relevant to the supplied video.

The current parser is designed around the scoreboard format and OCR text patterns observed in the provided assessment video.

The extracted information can include fields such as:
Player
Runs
Balls
Fours
Overs
depending on the recognized OCR text.

6. OCR Confidence
The application records OCR confidence values returned by EasyOCR.

The confidence value represents the OCR model's confidence in the recognized text.

It should not be interpreted as the overall accuracy percentage of the complete scoreboard extraction system.

📊 Output
The application generates:
outputs/
├── results.json
└── results.csv

JSON Output

The JSON file stores structured results from the processed frames.

Example:

{
  "frame": 0,
  "text": "TARUN ...",
  "confidence": 0.65,
  "parsed": {
    "player": "TARUN",
    "overs": "2.5"
  }
}

The exact values depend on the OCR results produced from the input video.
CSV Output
The CSV file provides a tabular representation of the extracted results.
It can be used to review:
Frame numbers
OCR text
OCR confidence
Parsed scoreboard information

🚀 Installation
Prerequisites
Install:

Python 3.10 or later
Git
Clone Repository
git clone https://github.com/Mohitraikwar121/COMPUTER-VISION-ENGINEER-PROJECT.git
cd COMPUTER-VISION-ENGINEER-PROJECT

Create Virtual Environment

Windows

python -m venv .venv
.venv\Scripts\activate

macOS / Linux

python3 -m venv .venv
source .venv/bin/activate

Install Dependencies
pip install -r requirements.txt

The dependency file should contain the packages actually used by the implementation, including:
opencv-python
numpy
pandas
easyocr
pytest


▶️ Run the Application
Make sure the input video exists at:
data/bowling_scoreboard.mp4

Run:
python src/main.py

The application will:
1. Load the input video.
2. Sample the configured video frames.
3. Extract the configured scoreboard ROI.
4. Run EasyOCR on the selected region.
5. Collect recognized text and confidence values.
6. Parse the OCR text.
7. Generate structured results.
8. Save JSON and CSV output.

Generated files:
outputs/results.json
outputs/results.csv

📈 Demonstrated Assessment Result
For the submitted assessment run, the documented output contains:
Frames Processed: 40
The demonstrated extracted scoreboard information includes information such as:
Player: TARUN
Overs: 2.5
The generated JSON and CSV files additionally contain OCR text, confidence values and parsed information for the processed frames.

📷 Documentation
The assessment documentation PDF contains screenshots demonstrating the project workflow, including:

Input video/frame

Project structure

Code execution

Scoreboard ROI

OCR/extracted text

JSON output

CSV output
Final extracted results
GitHub repository


🎥 Demo Video
The submitted demo demonstrates the complete execution flow:

Input Video
     ↓
Project Execution
     ↓
Frame Processing
     ↓
Scoreboard ROI
     ↓
    OCR
     ↓
Text Parsing
     ↓
Extracted Scoreboard Data
     ↓
JSON / CSV Output


📌 Current Scope and Limitations
This implementation is specifically developed for the supplied assessment video and its scoreboard layout.

Current limitations include:

The scoreboard ROI is configured manually rather than automatically detected.

Frames are sampled rather than every video frame being processed.

The current execution processes up to the first 200 frames.

OCR accuracy depends on scoreboard visibility, image quality and EasyOCR recognition.

Scoreboard parsing is tailored to the text format observed in the supplied video.

OCR confidence is a recognition-confidence measure and is not equivalent to complete system accuracy.

The current parser is not intended to generalize automatically to arbitrary scoreboard designs.

These limitations are documented to accurately represent the implemented solution.


🔮 Future Improvements
The solution could be extended with:

Automatic scoreboard localization

Object detection for scoreboard detection

Processing of the complete video

Advanced image preprocessing

Perspective correction

Temporal consistency across consecutive frames

Duplicate-result filtering

Confidence-based validation

Dynamic player-name extraction

More robust scoreboard field detection

Cricket-score validation rules

Comprehensive unit and integration testing

Support for different scoreboard layouts and video resolutions


🧪 Testing
The repository contains a tests/ package.

Future test coverage can include:

OCR parser validation

Scoreboard field extraction

Invalid OCR text handling

Confidence handling

JSON generation

CSV generation

End-to-end pipeline validation

👤 Candidate
Mohit Raikwar
Round 1 – Computer Vision Engineer Assessment

📄 Assessment Submission
This repository was developed as part of the Round 1 Computer Vision Engineer assessment at FOG.
The complete submission consists of:

GitHub repository

Working project source code

Input assessment video

Generated JSON and CSV results

Demonstration video

Documentation PDF containing screenshots and execution evidence

📜 License
This project was developed specifically for assessment and evaluation purposes.
