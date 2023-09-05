import pandas as pd
from sklearn.impute import KNNImputer

def interpolate_missing_values(data):
    """Interpolate missing values using pandas."""
    series = pd.Series(data)
    return series.interpolate(method='linear', limit_direction='both').tolist()

def impute_with_knn(data, n_neighbors=3):
    """Impute missing values using KNNImputer."""
    imputer = KNNImputer(n_neighbors=n_neighbors)
    return imputer.fit_transform(data)

def handle_missing_values(data):
    """Handle missing values using interpolation and KNN."""
    # Step 1: Interpolation
    for row in data:
        row[:] = interpolate_missing_values(row)
    
    # Step 2: KNN Imputation
    data[:] = impute_with_knn(data).tolist()
    return data

final_row_list = row_int
final_row_list = handle_missing_values(final_row_list)
