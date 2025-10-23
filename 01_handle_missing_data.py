import numpy as np, pandas as pd


data = {
    'Name': ['Alice', 'Bob', 'Carol', 'David', 'Emily'],
    'Age': [25, 30, np.nan, 22, 35],
    'Salary': [50000, 65000, 70000, np.nan, 90000]
}

p_dataset = pd.DataFrame(data = data)

print(f'''
============================= original dataset =============================
      
{p_dataset}
''')


mean_age = p_dataset["Age"].mean()


p_dataset["Age"], p_dataset["Salary"] = p_dataset["Age"].fillna(mean_age), p_dataset["Salary"].fillna(0)


# print("\n", p_dataset, "\n")







