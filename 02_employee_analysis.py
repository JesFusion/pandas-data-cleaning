import pandas as pd


data = {
    'Employee': ['John', 'Mary', 'Peter', 'Jane', 'Tom', 'Lisa'],
    'Department': ['Sales', 'Engineering', 'Sales', 'Engineering', 'Marketing', 'Marketing'],
    'Status': ['Full-Time', 'Part-Time', 'Full-Time', 'Full-Time', 'Part-Time', 'Full-Time'],
    'Salary': [90000, 80000, 95000, 110000, 60000, 75000],
    'Projects': [5, 3, 7, 6, 4, 5]
}



d_set = pd.DataFrame(data = data)


print(f'''
============================= original dataset =============================
      
{d_set}


============================= average salary for each department =============================

{d_set.groupby("Department").mean(numeric_only = True).drop("Projects", axis = 1)}


============================= employees per Status =============================

{d_set.groupby("Status").sum()}
''')


agg_algorithm = d_set.groupby("Department").agg(

    Total_Projects = (
        "Projects", "sum"
    ),

    Max_Salary = (
        "Salary", "max"
    )
)


print(f'''
============================= finding total number of projects and maximum salary, grouped by Department =============================
      
{agg_algorithm}
''')

