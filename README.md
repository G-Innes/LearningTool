# Python Learning Tool Program

## Introduction

The Learning Tool program is designed to help users practice and test their knowledge using a set of questions.
It provides various features such as practice mode, test mode, question management, and statistics tracking.


## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)

## Features

It provides different modes such as practice and test mode, along with statistics tracking and question management.
Users can add 2 types of questions which are given a unique ID number and stored in a JSON file.
Users can reference question ID for enabling/disabling questions.
practice mode allows user to answer as many questions as they want with the stats being updated
test mode prompts thr user for a set amount of questions they want to answer and saves the results to a text file

## Requirements

To run the Learning Tool program, you need to have the following packages:

- Python 3.x
- `json`
- `re`
- `random`
- `datetime`
- `pytest`

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/TuringCollegeSubmissions/ginnes-FPCS.3.git

    Change to the project directory:

    bash

cd learning-tool

Run the program:

bash

    python learning_tool.py

## Usage

    Launch the program by running learning_tool.py
    Follow the on-screen instructions to interact with the Learning Tool.
    Use the different modes available (practice mode, test mode) to enhance your learning experience.
    View statistics and manage questions as needed.

## File Structure

The file structure of the Learning Tool project is as follows:

- `Learning_tool.py`: The main program file that provides the user interface for interacting with the Learning Tool.
- `question_handler.py` contains the classes for adding, loading and saving questions to the JSON file
- `questions.py`: Contains the classes for different types of questions (`Question`, `QuizQuestion`, `FreeFormQuestion` `QuestionModifier` (for enable/disable questions)).
- `modes.py`: Contains the classes for handling statistics related to questions (`Statistics`), the `TestMode` and `PracticeMode` classes.
- `test.py` for unit tests using pytest
- `questions.json` for storage of user added questions
- `results.txt` for storing the results of the test mode


regex pattern for at 3 matching words: r'^\w+(\s+\w+){2,}$'