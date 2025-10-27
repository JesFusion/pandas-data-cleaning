import pandas as pd
from test_code import practice_emp_Dset


practice_dataset = pd.DataFrame(practice_emp_Dset)

print(f'''
============================= Original dataset =============================

{practice_dataset.sample(6)}


============================= dataset info =============================
''')

practice_dataset.info()


practice_dataset["Avg_team_Sal"] = (practice_dataset.groupby("Department")["Salary"].transform("mean")).round(2)


print(f'''
============================= using .transform() to add "Avg_Team_Sal" =============================
      
{practice_dataset.sample(10)}
''')

practice_dataset["Sal difference"] = practice_dataset["Salary"] - practice_dataset["Avg_team_Sal"]

print(f'''
============================= Comapring Employee Salary with average salary =============================
      
{practice_dataset.sample(7)}
''')



print(f'''
============================= using .filter() to find high-Earning departments =============================
      
{practice_dataset.groupby("Department").filter(
    lambda the_dataframe: the_dataframe["Salary"].mean() > 83000
).sample(7)}
''')





