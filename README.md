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

Setup: 

git clone https://github.com/your-username/BMI-Analysis-Project.git

cd BMI-Analysis-Project

Install required libraries 

run the BMI-age-height visualization.py

Technologies used: 
Python:
  Libraries: Pandas, Matplotlib, Seaborn, Scikit-learn

Visualization of data: 

Distribution of BMI: 

<img width="1059" alt="Screenshot 2023-09-29 at 7 59 00 PM" src="https://github.com/AbulkhairT/BMI-analysis-project/assets/125773898/101532ad-4b3d-48d8-a6ed-7b8836d8a2af">


Age vs BMI: 

<img width="991" alt="Screenshot 2023-09-29 at 8 10 10 PM" src="https://github.com/AbulkhairT/BMI-analysis-project/assets/125773898/4c634e81-c098-4fe1-8b69-e047b5248e79">


Height vs Weight: 

<img width="1111" alt="Screenshot 2023-09-29 at 8 07 56 PM" src="https://github.com/AbulkhairT/BMI-analysis-project/assets/125773898/34f11caf-ad46-4dc3-a5de-687bc08b7110">

Distribution acroess BMI classes: 

<img width="1124" alt="Screenshot 2023-09-29 at 8 08 33 PM" src="https://github.com/AbulkhairT/BMI-analysis-project/assets/125773898/310f468a-1e83-47ac-836a-1598e60c60ec">

Average BMI across age groups: 

<img width="1117" alt="Screenshot 2023-09-29 at 8 09 00 PM" src="https://github.com/AbulkhairT/BMI-analysis-project/assets/125773898/26ed74cf-559e-4e9e-a01e-9f5ff41b1ee9">

Blox Plot of BMI: 

<img width="1007" alt="Screenshot 2023-09-29 at 8 09 23 PM" src="https://github.com/AbulkhairT/BMI-analysis-project/assets/125773898/a92a08a1-4601-4593-a67c-60401a1548bd">

Weight distribution across age groups: 

<img width="1007" alt="Screenshot 2023-09-29 at 8 09 50 PM" src="https://github.com/AbulkhairT/BMI-analysis-project/assets/125773898/a56d4583-ad6f-4fc5-938f-67fc30ee58d2">


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






