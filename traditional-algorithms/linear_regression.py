# My Observations:
# Loop holes:
# If given more than 10 hours the score goes beyond 100 lol
# Fixes: Capping hours OP values

# With the current scores: Near perfect predictions
# Mean Squared Error: 0.0
# R-squared: 1.0

# If given this scores:
# y = np.array([42, 50, 52, 50, 62, 75, 80, 82, 91, 82])  # Exam scores
# Mean Squared Error: 56.08169178434402
# R-squared: -0.5578247717873337   - worse

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# 1: Sample data (Study hours vs Exam hours)

X = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape(-1, 1)  # Study hours (reshape converts the array into a 2D array with one column)
# this will give a 2D array like this
# [[ 1], [ 2], [ 3], [ 4], .... [10]]
# I Can manually also give it
y = np.array([50, 55, 60, 65, 70, 75, 80, 85, 90, 95])  # Exam scores

print("Shape of X:", X.shape)
print("Shape of y:", y.shape)

# 2. Split the data into training and test sets (80% train, 20% test)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=40)
# I have given randomly for now

# 3. Initiate the Linear Regression Model
model = LinearRegression()

# 4. Train the model on the training data
model.fit(X_train, y_train)

# 5. Make prdictions on test data
y_pred = model.predict(X_test)

# 66. Evaluate the model

# (For my understanding)
# Calculate Mean Squared Error (MSE) to
# evaluate the average squared difference
# between actual and predicted values
# Lower is better.
mse = mean_squared_error(y_test, y_pred)
# R-squared (R²): Tells you how much of the variance
# in the data is explained by the model.
# 1.0 means perfect fit.
# If it's closer to 0, the model doesn't explain much.
r2 = r2_score(y_test, y_pred)

# 7. Plotting the results
plt.scatter(X, y, color='blue', label='Actual Data')
plt.plot(X, model.predict(X), color='red', label='Regression Line')
plt.title('Linear Regression: Study Hours vs Exam Scores')
plt.xlabel('Study Hours')
plt.ylabel('Exam Scores')
plt.legend()
# plt.show() # Not showing graph for now

# 8.Output the results
print(f"Mean Squared Error: {mse}")
print(f"R-squared: {r2}")

# 9. Make predictions based on new input
new_study_hours = np.array([[10.5]])  # Reshape to 2D array
predicted_score = model.predict(new_study_hours)

print(f"Predicted exam score for {new_study_hours[0][0]} study hours: {predicted_score[0]}")

