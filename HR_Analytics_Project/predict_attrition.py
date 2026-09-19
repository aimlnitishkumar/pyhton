import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import os

def build_prediction_model():
    print("Loading cleaned dataset...")
    input_path = 'data/clean/cleaned_hr_dataset.csv'
    
    if not os.path.exists(input_path):
        print(f"Error: Could not find {input_path}.")
        return

    df = pd.read_csv(input_path)
    
    print("Preparing data for Machine Learning...")
    # 1. Select numeric features
    features = ['Age', 'Salary', 'PerformanceRating', 'TrainingHours', 
                'AttendancePercent', 'LeaveDays', 'OvertimeHours', 'JobSatisfaction']
    
    # 2. Encode categorical features
    cat_features = pd.get_dummies(df[['Department', 'JobRole', 'WorkMode']])
    
    X = pd.concat([df[features], cat_features], axis=1)
    y = df['AttritionFlag']
    
    # 3. Split the data into Training and Testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    print("Training Random Forest Classifier...\n")
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # 4. Evaluate the model
    predictions = model.predict(X_test)
    print("--- Model Evaluation ---")
    print(classification_report(y_test, predictions, target_names=['Stayed', 'Left'], zero_division=0))
    
    # 5. Extract Top Feature Importances (What drives attrition?)
    importances = pd.Series(model.feature_importances_, index=X.columns).sort_values(ascending=False).head(5)
    print("--- Top 5 Drivers of Attrition ---")
    print(importances.to_string())
    print("\n")
    
    # 6. Predict flight risk for currently ACTIVE employees
    print("Generating Flight Risk Report for active employees...")
    active_emp = df[df['Attrition'] == 'No'].copy()
    
    if not active_emp.empty:
        X_active = pd.concat([active_emp[features], pd.get_dummies(active_emp[['Department', 'JobRole', 'WorkMode']])], axis=1)
        
        # Ensure columns match the training data exactly
        X_active = X_active.reindex(columns=X.columns, fill_value=0)
        
        # Get probability of leaving (Class 1)
        active_emp['FlightRiskProb'] = model.predict_proba(X_active)[:, 1]
        
        # Filter employees with > 30% risk of leaving
        high_risk = active_emp[active_emp['FlightRiskProb'] > 0.3].sort_values(by='FlightRiskProb', ascending=False)
        
        os.makedirs('dashboards/reports', exist_ok=True)
        output_path = 'dashboards/reports/high_flight_risk_employees.csv'
        
        # Save the report for management
        report_columns = ['EmployeeID', 'EmployeeName', 'Department', 'JobRole', 'Salary', 'FlightRiskProb']
        high_risk[report_columns].to_csv(output_path, index=False)
        
        print(f"✅ Found {len(high_risk)} active employees at risk of leaving.")
        print(f"✅ Saved High Flight Risk Report to: {output_path}")

if __name__ == "__main__":
    build_prediction_model()