# BMI-analysis-project
This project dives deep into the relationship between an individual's age, height, weight, and BMI, aiming to unravel potential patterns and insights from a dataset of diverse individuals.

Dataset Description: 
bmi.csv from kaggle : https://www.kaggle.com/datasets/rukenmissonnier/age-weight-height-bmi-analysis/
The dataset in question comprises 741 individual records, each meticulously documented with the following attributes:

Age (in years): This field quantifies the age of each individual, denominated in years. It serves as a chronological reference for the dataset.
Height (in meters): The "Height" column provides measurements of the subjects' stature in meters. This standardized unit allows for precise representation and comparison of individuals' heights.
Weight (in kilograms): In the "Weight" column, the weights of the subjects are quantified in kilograms. This unit ensures consistency and accuracy in measuring the subjects' mass.
BMI (Body Mass Index): Derived from the height and weight columns, the BMI column computes the Body Mass Index of each individual. The calculation utilizes the formula: BMI = (Weight in kg) / (Height in m^2). BMI is a vital numerical indicator used for categorizing individuals based on their weight relative to their height. It is expressed as a continuous variable.
BmiClass: The "BmiClass" column categorizes individuals based on their calculated BMI values. The categories include "Obese Class 1," "Overweight," "Underweight," among others. These classifications are instrumental in health and weight analysis.


Technologies used: 
Python:
  Libraries: Pandas, Matplotlib, Seaborn, Scikit-learn
FastAPI


Key Findings:

BMI Distribution: The majority of the dataset lies in the "Normal" BMI range, but there is a significant proportion of individuals who are "Overweight".
Age and BMI: There's a slight trend indicating that BMI tends to increase with age up to a certain point, after which it plateaus.
Height and Weight Correlation: As expected, there's a positive correlation between height and weight. Taller individuals tend to weigh more.

BMI Classes Distribution:

Underweight: 5%
Normal: 55%
Overweight: 25%
Obese: 15%
Average BMI Across Age Groups:

10-20 years: 21 (Normal)
20-30 years: 23 (Normal)
30-40 years: 25 (Overweight)

Potential Outliers: There are a few individuals with extremely high BMI values that may be considered outliers.

Weight Distribution Across Age Groups: The spread of weight tends to increase with age, peaking in the 40-50 age range and then gradually declining.
