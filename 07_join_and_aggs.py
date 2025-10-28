import pandas as pd



emp_data = pd.DataFrame(
    {
    'Name': ['Alice', 'Bob', 'Carol', 'David'],
    'Department': ['Sales', 'Engineering', 'Sales', 'Engineering']
    }, index=['e101', 'e102', 'e103', 'e104']
)

perf_data = pd.DataFrame(
    {
    'Performance_Score': [8.5, 9.0, 7.8],
    'Projects': [5, 3, 6]
    }, index=['e101', 'e102', 'e105']
)

emp_data.index.name, perf_data.index.name = "Employee ID", "Employee ID"

print(f'''
============================= Employee table (Index is Employee ID) =============================
      
{emp_data}


============================= Performance table (Index is Employee ID) =============================

{perf_data}
''')

joined_data = emp_data.join(perf_data)


print(f'''
============================= .join() Result (Left join on Index) =============================

{joined_data}
''')


joined_data["Performance_Score"] = joined_data["Performance_Score"].fillna(2.6)

dept_avg_score = joined_data.groupby("Department")["Performance_Score"].transform("mean")

joined_data["Dept. Total Score"] = joined_data.groupby("Department")["Performance_Score"].transform("sum")

joined_data["Avg. Score [D]"] = dept_avg_score

joined_data["Score vs. Dept."] = joined_data["Performance_Score"] - joined_data["Avg. Score [D]"]

print(f'''
============================= using .transform() to find Department total and average score =============================

{joined_data}
''')



joined_data['Projects'] = joined_data["Projects"].fillna(joined_data["Projects"].mean())

joined_data = joined_data.drop(list(joined_data.columns)[4:], axis = 1)

joined_data["Dept. Total Projects"] = joined_data.groupby("Department")["Projects"].transform("sum")

joined_data["Avg. Proj. [D]"] = joined_data.groupby("Department")["Projects"].transform("mean")

joined_data["Proj. vs.  Dept."] = joined_data["Projects"] - joined_data["Avg. Proj. [D]"]


print(f'''
============================= using .transform() to find Department total and average Projects =============================

{joined_data}
''')


high_perfromers_data = joined_data.groupby("Department").filter(
    lambda Dept: Dept["Projects"].mean() < 3.6
)

print(f'''
============================= Using .filter() to find "high-performing" Departments =============================
      
{high_perfromers_data}
''')
