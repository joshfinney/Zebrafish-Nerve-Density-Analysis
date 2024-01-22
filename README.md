# Zebrafish Pancreatic Islet Analysis

## Overview
The `Zebrafish-Pancreatic-Islet-Analysis` repository presents a sophisticated Python project designed to investigate nerve density in Zebrafish pancreatic islets. This work is pivotal for understanding the intricate biological processes in Zebrafish, serving as a model organism for developmental studies. The project encompasses data loading and validation, preprocessing, statistical analysis, and visual representation of the findings.

## Key Features
- **Data Validation and Loading**: Ensuring the integrity and availability of essential data columns.
- **Data Preprocessing**: Tailoring the dataset for analysis, including handling of missing values and data transformation.
- **Statistical Analysis**: Utilising t-tests to understand the significance of differences between various groups.
- **Data Visualisation**: Creating insightful boxplots and scatter plots to visually represent the analysis outcomes.

## Prerequisites
To run this project, the following Python libraries are required:
- pandas
- matplotlib
- seaborn
- scipy

## Usage
1. **Data Loading and Validation**: The script begins by loading data from a CSV file, ensuring that all required columns are present.
2. **Data Preprocessing**: The data is then preprocessed to split and clean specific columns for analysis.
3. **Statistical Analysis**:
   - The mean and standard deviation for each group are computed.
   - T-tests are performed to assess the statistical differences between groups.
4. **Visualisation**:
   - A boxplot is generated to visualise the nerve density across different treatment types and stages.
   - Scatter plots are created to showcase the results of the t-tests, including both T-statistics and P-values.
