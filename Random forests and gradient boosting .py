# Import necessary libraries
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import classification_report

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# Build and train Random Forest model
rfc = RandomForestClassifier(n_estimators=100)
rfc.fit(X_train, y_train)

# Evaluate Random Forest model
y_pred_rfc = rfc.predict(X_test)
print(classification_report(y_test, y_pred_rfc))

# Build and train Gradient Boosting model
gbc = GradientBoostingClassifier(n_estimators=100)
gbc.fit(X_train, y_train)

# Evaluate Gradient Boosting model
y_pred_gbc = gbc.predict(X_test)
print(classification_report(y_test, y_pred_gbc))

