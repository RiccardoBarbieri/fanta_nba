import pandas as pd

# Caricamento dei file CSV
file1 = 'fv_2021-22.csv'
file2 = 'fv_2022-23.csv'
file3 = 'fv_2023-24.csv'

# Lettura dei file in DataFrame
df1 = pd.read_csv(file1)
df2 = pd.read_csv(file2)
df3 = pd.read_csv(file3)

# Concatenazione dei DataFrame
df = pd.concat([df1, df2, df3])

# Conversione della colonna 'date' in datetime
df['date'] = pd.to_datetime(df['date'])

# Ordinamento per data
df = df.sort_values(by='date')

# Salvataggio del nuovo file CSV
df.to_csv('final.csv', index=False)

print("File CSV uniti e ordinati per data salvato come 'merged_sorted_file.csv'")
