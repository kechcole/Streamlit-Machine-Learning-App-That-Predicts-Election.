import pandas as pd
import geopandas as gpd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import pickle




def create_model(data):
    
    # Select predictor and target columns 
    X = data.select_dtypes(include=['int64', 'float']).drop('voter_turnout_2020', axis=1)
    y = data['voter_turnout_2020']

    # Scale predictors
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # Create the dataframe
    X = pd.DataFrame(X_scaled, columns=X.columns)


    # split the data 
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


    # Initialize Random Forest Regressor model with specified parameters
    model = RandomForestRegressor(
        max_depth=30,
        max_features='log2',
        n_estimators=200,
        random_state=42
    )

    # Fit the model
    model.fit(X_train, y_train)

    # Predict on test data
    y_pred = model.predict(X_test)

    # Evaluate the model
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print("Mean Squared Error:", mse)
    print("R² Score:", r2)   


    return model, scaler


# Read and clean data 
def fetch_clean_data():
    
    data = gpd.read_file('Data/Contigous_US_County_Election_Results.gpkg', layer='simplified')
 
    # Drop unwanted columns 
    data.drop(columns=['population', 'state_abbr', 'state_fips', 'state_name', 'region', 'geometry'], inplace=True)

    return data


def main():
    data = fetch_clean_data()
    model, scaler = create_model(data)

    # Save the model, 1.Predict US Election - ML App Streamlit\Model
    with open('Model/model.pkl', 'wb') as f:
        pickle.dump(model, f)
    # Save the scaler
    with open('Model/scaler.pkl', 'wb') as f:
        pickle.dump(scaler, f)
    # Open a file in write-binary mode and save the data
    with open('Model/data.pkl', 'wb') as f:
        pickle.dump(data, f)



if __name__ == '__main__':
    main()