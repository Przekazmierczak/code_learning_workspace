import csv
import sys

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

TEST_SIZE = 0.4


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python shopping.py data")

    # Load data from spreadsheet and split into train and test sets
    evidence, labels = load_data(sys.argv[1])
    X_train, X_test, y_train, y_test = train_test_split(
        evidence, labels, test_size=TEST_SIZE
    )

    # Train model and make predictions
    model = train_model(X_train, y_train)
    predictions = model.predict(X_test)
    sensitivity, specificity = evaluate(y_test, predictions)

    # Print results
    print(f"Correct: {(y_test == predictions).sum()}")
    print(f"Incorrect: {(y_test != predictions).sum()}")
    print(f"True Positive Rate: {100 * sensitivity:.2f}%")
    print(f"True Negative Rate: {100 * specificity:.2f}%")


def load_data(filename):
    """
    Load shopping data from a CSV file `filename` and convert into a list of
    evidence lists and a list of labels. Return a tuple (evidence, labels).

    evidence should be a list of lists, where each list contains the
    following values, in order:
        - Administrative, an integer
        - Administrative_Duration, a floating point number
        - Informational, an integer
        - Informational_Duration, a floating point number
        - ProductRelated, an integer
        - ProductRelated_Duration, a floating point number
        - BounceRates, a floating point number
        - ExitRates, a floating point number
        - PageValues, a floating point number
        - SpecialDay, a floating point number
        - Month, an index from 0 (January) to 11 (December)
        - OperatingSystems, an integer
        - Browser, an integer
        - Region, an integer
        - TrafficType, an integer
        - VisitorType, an integer 0 (not returning) or 1 (returning)
        - Weekend, an integer 0 (if false) or 1 (if true)

    labels should be the corresponding list of labels, where each label
    is 1 if Revenue is true, and 0 otherwise.
    """
    # List of months and format
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    formats = [int, float, int, float, int, float, float, float, float, float, int, int, int, int, int, int, int, int]
    
    # Create list off all evidence and labels
    evidence_list = []
    labels_list = []
    
    # Open and read the CSV file
    with open (filename, newline="") as csvfile:
        reader = csv.reader(csvfile)
        
        # Iterate through rows in the CSV file
        for count, row in enumerate(reader):
            # Skip the first row (title row)
            if count != 0:
                # Create variables for evidence and labels for one user
                evidence_element = []
                labels_element = -1

                # Iterate through elements in the row
                for index, element in enumerate(row):
                    # Change months into their numerical representation
                    if element in months:
                        month_index = months.index(element)
                        row[index] = str(month_index)
                    # Convert certain string values into integers
                    if element == "Returning_Visitor" or element == "TRUE":
                        row[index] = "1"
                    elif element == "New_Visitor" or element == "Other" or element == "FALSE":
                        row[index] = "0"
                    # Change the format of input
                    row[index] = formats[index](row[index])
                    # Add elements to the evidence or labels variable
                    if index < 16:
                        evidence_element.append(row[index])
                    else:
                        labels_element = row[index]
                
                # Add evidence and labels elements to the list of all evidences and labels
                evidence_list.append(evidence_element)
                labels_list.append(labels_element)
    
    # Return a tuple containing the evidence and labels lists
    return (evidence_list, labels_list)


def train_model(evidence, labels):
    """
    Given a list of evidence lists and a list of labels, return a
    fitted k-nearest neighbor model (k=1) trained on the data.
    """
    model = KNeighborsClassifier(n_neighbors=1)
    return model.fit(evidence, labels)


def evaluate(labels, predictions):
    """
    Given a list of actual labels and a list of predicted labels,
    return a tuple (sensitivity, specificity).

    Assume each label is either a 1 (positive) or 0 (negative).

    `sensitivity` should be a floating-point value from 0 to 1
    representing the "true positive rate": the proportion of
    actual positive labels that were accurately identified.

    `specificity` should be a floating-point value from 0 to 1
    representing the "true negative rate": the proportion of
    actual negative labels that were accurately identified.
    """
    # Create empty lists for sensitivity and specificity values
    true_sensitivity = []
    false_sensitivity = []
    true_specificity = []
    false_specificity = []

    # Iterate throught elements in labels
    for count, element in enumerate(labels):
        # Check if element in labels is positive
        if element == True:
            # Count actual positive labels that were correctly identified
            if element == predictions[count]:
                true_sensitivity.append(element)
            # Count actual positive labels that were incorrectly identified
            else:
                false_sensitivity.append(element)
        # Check if element in labels is negative
        else:
            # Count actual negative labels that were correctly identified
            if element == predictions[count]:
                true_specificity.append(element)
            # Count actual negative labels that were incorrectly identified
            else:
                false_specificity.append(element)

    # Calculate sensitivity: TP / (TP + FN)
    # where TP is the count of true positives and FN is the count of false negatives.
    sensitivity = len(true_sensitivity) / (len(true_sensitivity) + len(false_sensitivity))
    # Calculate specificity: TN / (TN + FP)
    # where TN is the count of true negatives and FP is the count of false positives.
    specificity = len(true_specificity) / (len(true_specificity) + len(false_specificity))

    return (sensitivity, specificity)


if __name__ == "__main__":
    main()
