

# Import necessary libraries
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import MinMaxScaler
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

# Impute missing values using SimpleImputer
imputer = SimpleImputer(strategy='mean')
data_imputed = imputer.fit_transform(data)

# Rescale the data using MinMaxScaler
scaler = MinMaxScaler()
data_scaled = scaler.fit_transform(data_imputed)

# Perform feature engineering using SelectKBest and chi2
X = data_scaled[:,:-1]
y = data_scaled[:,-1]
bestfeatures = SelectKBest(score_func=chi2, k=10)
fit = bestfeatures.fit(X,y)


