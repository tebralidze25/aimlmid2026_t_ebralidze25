# AI and ML for Cybersecurity – Midterm Exam

Student: Tornike Ebralidze  
Repository: aimlmid2026_t_ebralidze25

---

## Finding the Correlation

The data for this task was obtained from the provided interactive graph.  
The blue data points were manually extracted by hovering over each point and recording its (x, y) coordinates.

Using the extracted values, Pearson’s correlation coefficient was calculated in Python using the scipy library.

The resulting correlation coefficient indicates a strong negative linear relationship between the variables.

A scatter plot was generated to visually confirm this relationship.

The source code for this task is available in:
- `correlation.py`

---

## Spam Email Detection

### Dataset

The dataset used for spam email detection is provided as a CSV file and is included in this repository:
- `data/t_ebralidze25_36714.csv`

The dataset contains numerical email features and a class label indicating whether an email is spam or legitimate.

---

### Data Loading and Processing

The dataset was loaded using the pandas library.  
Feature columns were separated from the target class column.

The data was split into:
- 70% training data
- 30% testing data

This split was performed using the `train_test_split` function from scikit-learn.

---

### Model

A Logistic Regression model was used to classify emails as spam or legitimate.

The model was trained on the training dataset.  
The learned coefficients represent the importance of each feature in the classification process.

The source code for training and evaluating the model is available in:
- `spam_classifier.py`

---

### Model Evaluation

The trained model was evaluated on the test dataset.

The following evaluation metrics were calculated:
- Confusion Matrix
- Accuracy score

These metrics provide insight into the performance of the spam classification model.

---

### Email Classification Capability

The application is capable of evaluating new email inputs by extracting the same features used in the dataset and applying the trained Logistic Regression model.

---

### Manually Composed Email Examples

#### Spam Email Example


Congratulations! You have won a free prize.
Click now to claim your reward before the offer expires.



This email was intentionally created to resemble spam by including promotional language, urgency, and incentives.

---

#### Legitimate Email Example

Dear Team,

Please find attached the agenda for tomorrow’s meeting.

Best regards.


This email represents a legitimate message with a professional tone and no spam-related content.

---

### Visualizations

The following visualizations were generated as part of this assignment:

- Scatter plot showing the correlation between X and Y values
- Class distribution chart for spam and legitimate emails
- Confusion matrix heatmap illustrating model performance
