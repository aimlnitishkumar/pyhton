import pandas as pd
import numpy as np

def generate_hr_data():
    print("Generating mock HR dataset...")
    np.random.seed(42)
    num_employees = 1000

    # Define categorical choices
    departments = ['Sales', 'IT', 'HR', 'Finance', 'Operations']
    job_roles = ['Analyst', 'Manager', 'Director', 'Specialist', 'Executive']
    work_modes = ['Remote', 'Hybrid', 'On-site']
    recruitment_sources = ['LinkedIn', 'Referral', 'Agency', 'Website']

    # Generate data
    data = {
        'EmployeeID': [f"EMP{str(i).zfill(4)}" for i in range(1, num_employees + 1)],
        'EmployeeName': [f"Employee_{i}" for i in range(1, num_employees + 1)],
        'Gender': np.random.choice(['Male', 'Female', 'Non-Binary'], num_employees, p=[0.52, 0.45, 0.03]),
        'Age': np.random.randint(22, 60, num_employees),
        'Department': np.random.choice(departments, num_employees),
        'JobRole': np.random.choice(job_roles, num_employees),
        'Salary': np.random.randint(40000, 160000, num_employees),
        'Bonus': np.random.randint(0, 20000, num_employees),
        'PerformanceRating': np.random.choice([1, 2, 3, 4, 5], num_employees, p=[0.05, 0.10, 0.60, 0.20, 0.05]),
        'TrainingHours': np.random.randint(10, 100, num_employees),
        'AttendancePercent': np.random.uniform(75.0, 100.0, num_employees).round(1),
        'LeaveDays': np.random.randint(0, 30, num_employees),
        'OvertimeHours': np.random.randint(0, 40, num_employees),
        'WorkMode': np.random.choice(work_modes, num_employees),
        'RecruitmentSource': np.random.choice(recruitment_sources, num_employees),
        'JobSatisfaction': np.random.choice([1, 2, 3, 4, 5], num_employees),
        'Attrition': np.random.choice(['Yes', 'No'], num_employees, p=[0.18, 0.82])
    }

    # Create the DataFrame
    df = pd.DataFrame(data)

    # Save to the raw data folder
    output_path = 'data/raw/hr_dataset.csv'
    df.to_csv(output_path, index=False)
    print(f"Success! Dataset with {num_employees} records saved to: {output_path}")

if __name__ == "__main__":
    generate_hr_data()
