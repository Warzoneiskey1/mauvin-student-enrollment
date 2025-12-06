# Mauvin Student Enrollment Analysis - Jeffrey Godwin (Warzoneiskey1)
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('mauvin_students.csv')
df['enrollment_date'] = pd.to_datetime(df['enrollment_date'])
df['month'] = df['enrollment_date'].dt.month

print("Dataset loaded:", df.shape)
print(df.head())

# 1. Monthly enrollment trend
monthly = df['month'].value_counts().sort_index()
monthly.plot(kind='bar', title='Monthly Student Enrollments', color='teal')
plt.xlabel('Month')
plt.ylabel('Students')
plt.show()

# 2. Retention by gender
retention = df.groupby('gender')['retention'].mean() * 100
print("\nRetention by gender (%):")
print(retention)

# 3. Course popularity
print("\nCourse distribution:")
print(df['course'].value_counts())

print("\n✅ Analysis complete! Key insights in plots above.")
