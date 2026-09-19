import pandas as pd
import os

def clean_and_prepare_data():
    print("Loading raw dataset...")
    input_path = 'data/raw/hr_dataset.csv'
    
    if not os.path.exists(input_path):
        print(f"Error: Could not find {input_path}. Make sure you are in the right directory.")
        return

    df = pd.read_csv(input_path)

    print("Applying data transformations and feature engineering...")
    
    # 1. Create Attrition Flag (Numeric 1/0 for easy KPI math)
    df['AttritionFlag'] = df['Attrition'].apply(lambda x: 1 if x == 'Yes' else 0)
    
    # 2. Create Age Groups
    bins_age = [0, 29, 39, 49, 100]
    labels_age = ['<30 (Gen Z/Young Millennial)', '30-39', '40-49', '50+']
    df['AgeGroup'] = pd.cut(df['Age'], bins=bins_age, labels=labels_age)
    
    # 3. Create Salary Bands
    # Assuming salaries range from ~40k to ~160k based on our generator
    bins_salary = [0, 70000, 120000, 250000]
    labels_salary = ['Low (<$70k)', 'Medium ($70k-$120k)', 'High (>$120k)']
    df['SalaryBand'] = pd.cut(df['Salary'], bins=bins_salary, labels=labels_salary)
    
    # 4. Create Attendance Status
    df['AttendanceStatus'] = df['AttendancePercent'].apply(
        lambda x: 'Needs Attention' if x < 85.0 else ('Excellent' if x >= 95.0 else 'Good')
    )
    
    # 5. Leave Balance Category
    bins_leave = [-1, 5, 15, 50]
    labels_leave = ['Low (<5 days)', 'Medium (5-15 days)', 'High (>15 days)']
    df['LeaveCategory'] = pd.cut(df['LeaveDays'], bins=bins_leave, labels=labels_leave)

    # Ensure the clean directory exists
    os.makedirs('data/clean', exist_ok=True)
    
    # Save the cleaned dataset
    output_path = 'data/clean/cleaned_hr_dataset.csv'
    df.to_csv(output_path, index=False)
    
    print(f"Success! Cleaned data with new features saved to: {output_path}")
    print(f"Total rows: {len(df)}, Total columns: {len(df.columns)}")

if __name__ == "__main__":
    clean_and_prepare_data()