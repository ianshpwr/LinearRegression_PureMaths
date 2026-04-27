# Linear Regression from Scratch

This project implements a simple linear regression model from scratch using Python. The model is trained using gradient descent to predict student scores based on the number of hours they studied.

## Project Overview

The script `LinearRegression.py` performs the following steps:
1.  Loads the student scores data from `score_updated.csv`.
2.  Initializes the model parameters (slope `m` and y-intercept `b`).
3.  Implements a loss function (Mean Squared Error).
4.  Uses gradient descent to minimize the loss and find the best values for `m` and `b`.
5.  Visualizes the original data points and the final regression line using `matplotlib`.

## Dataset

The dataset used is `score_updated.csv`, which contains two columns:
-   `Hours`: The number of hours a student studied.
-   `Scores`: The score obtained by the student.

## Requirements

The project requires the following Python libraries:
-   pandas
-   matplotlib

## Getting Started

### Prerequisites

Make sure you have Python installed on your system.

### Installation

1.  Clone the repository or download the source code.
2.  Install the required packages using pip:
    ```bash
    pip install -r requirements.txt
    ```

### Running the script

To run the linear regression model, execute the following command in your terminal:
```bash
python LinearRegression.py
```
The script will print the final values for the slope (`m`) and y-intercept (`b`) and then display a plot showing the data points and the fitted regression line.
