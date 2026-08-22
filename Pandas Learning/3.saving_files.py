import pandas as pd

# Create our own DataFrame from Python data.
my_data = {
    "Name": ["Moiz", "Junaid", "Shoaib"],
    "Age": [21, 18, 14],
    "Class": ["15th", "11th", "8th"],
}

df = pd.DataFrame(my_data)
print(df)

# Save the DataFrame in different file formats.
df.to_csv("save_in.csv", index=False)
df.to_excel("save_in.xlsx", index=False)
df.to_html("save_in.html", index=False)
df.to_json("save_in.json", index=False)


# Important notes
# pd.DataFrame() creates a DataFrame from our own Python data.
# After manipulating or cleaning data, we can save/export the DataFrame into different file formats.
# to_csv() → saves as CSV.
# to_excel() → saves as Excel.
# to_json() → saves as JSON.
# to_html() → saves the DataFrame as an HTML table.
# index=False means Pandas does not save the DataFrame's row index (0, 1, 2...) into the file.

# 🧠 One-line concept to remember

# Read file → work/clean/manipulate DataFrame → save/export DataFrame using to_...()
