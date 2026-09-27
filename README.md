# Healthcare Data Analysis using Python

## Project Overview

This project analyzes a healthcare dataset using Python, Pandas, and Matplotlib.

The analysis focuses on patient demographics, medical conditions, admission types, and billing information.

## Objectives

- Understand the healthcare dataset
- Check for missing values and duplicate records
- Clean the dataset
- Analyze patient medical conditions
- Analyze average billing amounts
- Analyze admission types
- Analyze average patient age
- Create visualizations to understand the data

## Tools & Technologies

- Python
- Pandas
- Matplotlib

## Dataset

The dataset contains 55,500 healthcare records with information including:

- Age
- Gender
- Blood Type
- Medical Condition
- Date of Admission
- Hospital
- Insurance Provider
- Billing Amount
- Admission Type
- Medication
- Test Results

## Data Cleaning

The dataset was checked for missing values and duplicate records.

- Missing values: 0
- Duplicate records identified: 534
- Duplicate records removed: 534
- Records remaining for analysis: 54,966

## Analysis Performed

### 1. Patients by Medical Condition

Analyzed the number of patients across different medical conditions.

### 2. Average Billing Amount by Medical Condition

Calculated the average billing amount for each medical condition.

### 3. Patients by Admission Type

Analyzed the distribution of patients across different admission types.

### 4. Average Age by Medical Condition

Calculated and visualized the average age of patients for each medical condition.

## Key Skills Demonstrated

- Python programming
- Pandas DataFrame handling
- Data cleaning
- Duplicate removal
- `value_counts()`
- `groupby()`
- Descriptive analysis
- Data visualization
- Matplotlib

## Project Structure

Healthcare_Data_Analysis/

├── analysis.py  
├── healthcare_dataset.csv  
├── requirements.txt  
└── README.md

## How to Run

Install the required libraries:

```bash
pip install -r requirements.txt