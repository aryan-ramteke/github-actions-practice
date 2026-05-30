import requests
import pandas as pd

response = requests.get("https://api.github.com")

print("GitHub API Status:", response.status_code)

data = {
    "Name": ["Aaryan", "John", "Alice"],
    "Score": [95, 88, 92]
}

df = pd.DataFrame(data)

print("\nDataFrame:")
print(df)

print("\nAverage Score:", df["Score"].mean())
