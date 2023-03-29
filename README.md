# CSGO-Round-Winner-Prediction
Task-6 Kaiburr Assessment
---
### 1. Problem Statement 
####  To predict the Rounder winner of CSGO either it can be Terrorist or Counter Terrorist
---
### 2. DataSet
#### DataSet Link : https://raw.githubusercontent.com/insignificantGuy/Kaggle-Datasets/main/csgo_round_snapshots.csv
The dataset consists of round snapshots from about 700 demos from high level tournament play in 2019 and 2020. Warmup rounds and restarts have been filtered, and for the remaining live rounds a round snapshot has been recorded every 20 seconds until the round is decided. Following its initial publication, It has been pre-processed and flattened to improve readability and make it easier for algorithms to process. The total number of snapshots is 122411. Snapshots are i.i.d and should be treated as individual data points, not as part of a match.These features or values includes time_left, ct_score, bomb_planted, ct_armor, t_armor,etc. Total of 96 Feature are given to predict the round Winner
---
### 3. Requirement
1. Google Collab for Online
2. Jupyter Notebook and python for running the project locally on the machine
---
### 4. Method
The methodology consists roughly of two chronological steps. First the data is thoroughly explored and dimensionality reduction is applied. Secondly a suitable and  optimized model is applied to our problem. The work-flow of these two steps are carried out in the python-notebooks mentioned above.
---
### 4.1 Data exploration
Initial exploration and analysis of the dataset.Features and Labels are extracted.
---
### 4.2 Distributions and relationship
First the distributions of the different attributes and their relationship to the target are inspected by the means of histograms and correlation.
---
### 4.3 Splitting and standardize the data
---
At this stage we drop missing data and preprocess the data for efficient performance and best results, We use Standard Scaler from sklearn.preprocessing library to scale the data.Using this mode standarization normal distribution is achieved.Then the  data is separated into an training set and a test set in ratio 80:20. The test set wont be used at any point, this set will eventually simulate new data used to evaluate the final model.
---
### 5. Model Selection
KNN (K nearest Neighbour) model is selected.
---
### 6. Evaluate models using Confusion Matrixes and validation data
Confusion matrix is generated to closely observe the performace of the model.
---
### 7. Test
Finally we test the final model on the held out test-set.
---
### Result
Accuracy of 84 percent is achieved
---
