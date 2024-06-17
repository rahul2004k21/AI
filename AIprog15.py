from sklearn.tree import DecisionTreeClassifier

# Sample dataset - features and labels
# Imagine you have some data about customers and whether they bought a product (1) or not (0)
# Features: [Age, Income, Gender]
# Labels: [Bought_Product]
X = [
    [25, 50000, 'Male'],
    [30, 70000, 'Female'],
    [35, 90000, 'Male'],
    [20, 30000, 'Female'],
    [40, 100000, 'Male'],
    [45, 120000, 'Female']
]
y = [0, 1, 1, 0, 1, 1]

# Convert categorical variables to numerical using one-hot encoding
X_encoded = []
for sample in X:
    encoded_sample = []
    # Age and Income remain unchanged
    encoded_sample.extend(sample[:2])
    # Convert gender to numerical
    if sample[2] == 'Male':
        encoded_sample.append(0)
    else:
        encoded_sample.append(1)
    X_encoded.append(encoded_sample)

# Train Decision Tree Classifier
clf = DecisionTreeClassifier()
clf.fit(X_encoded, y)

# Now, let's make a decision for a new customer
# For example, a 28-year-old male with an income of $60,000
new_customer = [[28, 60000, 'Male']]
new_customer_encoded = []
for sample in new_customer:
    encoded_sample = []
    encoded_sample.extend(sample[:2])
    if sample[2] == 'Male':
        encoded_sample.append(0)
    else:
        encoded_sample.append(1)
    new_customer_encoded.append(encoded_sample)

# Predict whether the new customer will buy the product or not
prediction = clf.predict(new_customer_encoded)

if prediction[0] == 1:
    print("The new customer is likely to buy the product.")
else:
    print("The new customer is unlikely to buy the product.")
