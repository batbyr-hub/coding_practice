from typing import List
import pandas as pd

# 2877. Create a DataFrame from List
def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    df = pd.DataFrame(student_data, columns=['student_id', 'age'])
    return df

# 2878. Get the Size of a DataFrame
def getDataframeSize(players: pd.DataFrame) -> List[int]:
    return list(players.shape)

# 2879. Display the First Three Rows
def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.head(3)

# 2880. Select Data
def selectData(students: pd.DataFrame) -> pd.DataFrame:
    return students[students["student_id"] == 101].drop("student_id", axis=1)

# 2881. Create a New Column
def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees["bonus"] = employees["salary"] * 2
    return employees

# 2882. Drop Duplicate Rows
def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    return customers.drop_duplicates(subset=["email"])

# 2883. Drop Missing Data
def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    return students.dropna(subset=["name"], axis=0)

# 2884. Modify Columns
def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees["salary"] = employees["salary"] * 2
    return employees

# 2885. Rename Columns
def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    students = students.rename(columns={"id": "student_id"})
    students = students.rename(columns={"first": "first_name"})
    students = students.rename(columns={"last": "last_name"})
    students = students.rename(columns={"age": "age_in_years"})
    return students

# 2886. Change Data Type
def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    students["grade"] = students["grade"].astype(int)
    return students

# 2887. Fill Missing Data
def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    products["quantity"] = products["quantity"].fillna(0)
    return products

# 2888. Reshape Data: Concatenate
def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    return pd.merge(df1, df2, on=["student_id", "name", "age"], how="outer")

# 2889. Reshape Data: Pivot
def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    return weather.groupby(["month", "city"])["temperature"].sum().reset_index().pivot(index="month", columns="city", values="temperature")

# 2890. Reshape Data: Melt
def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    return pd.melt(report, id_vars=["product"], var_name="quarter", value_name="sales")

# 2891. Method Chaining
def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    return animals[animals["weight"] > 100].sort_values("weight", ascending=False).drop(["species", "age", "weight"], axis=1)