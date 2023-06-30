# Lazy Classification

Lazy Classification is a machine learning project that focuses on predicting whether a student is lazy or not based on their performance in Math, Physics, and Chemistry subjects.

## Overview

The project utilizes various machine learning algorithms to perform classification on the given dataset. The code performs the following steps:

1. **Importing Libraries**: Necessary libraries such as pandas, numpy, seaborn, scikit-learn, and matplotlib are imported.

2. **Reading the Dataset**: The dataset, named "Student.csv", is read into a pandas DataFrame.

3. **Data Preprocessing**: Null values are removed from the dataset.

4. **Data Visualization**: The distribution of marks in the subjects (Maths, Physics, and Chemistry) is visualized using histograms. Outliers are identified using box plots.

5. **Data Splitting**: The dataset is split into training and testing sets.

6. **Feature Scaling**: Numerical features are scaled using StandardScaler.

7. **Model Training**: Several classification algorithms are trained on the training data, including Logistic Regression, Naive Bayes, Support Vector Machines (SVM), K-Nearest Neighbor (KNN), and Decision Tree.

8. **Model Evaluation**: The trained models are evaluated by calculating accuracy scores and confusion matrices on the testing data.

9. **Decision Tree Pruning**: The Decision Tree model is pruned using cost complexity pruning, and the optimal alpha value is chosen based on validation scores.

10. **Model Saving**: The trained Decision Tree model is saved using pickle.

11. **Model Loading and Prediction**: The saved model is loaded, and predictions are made on new data.

## Usage

1. Install the required libraries mentioned in the `requirements.txt` file.

2. Ensure that the dataset file, "Student.csv", is in the same directory.

3. Run the code in a Python environment, such as Jupyter Notebook or any Python IDE.

4. The trained models can be evaluated, and predictions can be made on new data.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or suggestions, please feel free to reach out to me at [your-sathishkavimass@gmail.com](mailto:sathishkavimass@gmail.com).
