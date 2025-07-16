import pandas as pd

# --- IMPORTANT: Make sure 'varsity_50_free_times.csv' is in the same directory as your script,
# --- or provide the full path to the file. ---
csv_file_path = 'varsity_50_free_times.csv'

try:
    # 1. Load your actual CSV file into a Pandas DataFrame
    df = pd.read_csv(csv_file_path)
    print(f"Successfully loaded data from '{csv_file_path}'")
    print("First 5 rows of your DataFrame:")
    print(df.head())

except FileNotFoundError:
    print(f"Error: The file '{csv_file_path}' was not found.")
    print("Please ensure the CSV file is in the correct directory or provide the full path.")
    exit()
except Exception as e:
    print(f"An error occurred while loading the CSV: {e}")
    exit()

# List of names to filter by
target_names = [
    "Lian, Ziruo",
    "Methuku, Hasini R",
    "Vance, Isabelle A",
    "Lee, Harmonie",
    "Jiang, Nancy",
    "Wong, Kiely",
    "Olalia, Hailey Anne",
    "Sonawane, Saatvika Sachin",
    "Cao, Grace",
    "Chan, Grace",
    "Wan, Julia",
    "Cheng, Jessica",
    "Kottapalli, Ansha Tan",
    "Vaish, Aadya",
    "Pawar, Shreya S",
    "Tran, Madyson",
    "Ip, Crystal",
    "Diala, Jewliana",
    "Bhushan, Sara",
    "Bharti, Jiya"
]

# Ensure the required columns exist and handle potential non-numeric data
# Updated: 'name' is now the column for swimmer names
required_columns = ['earliest_50y_free_time', 'name']

if not all(col in df.columns for col in required_columns):
    missing_cols = [col for col in required_columns if col not in df.columns]
    print(f"Error: One or more required columns ({', '.join(missing_cols)}) not found in the DataFrame.")
    print("Please ensure your CSV file contains 'earliest_50y_free_time' and 'name' columns (case-sensitive).")
else:
    # Convert 'earliest_50y_free_time' to numeric, coercing errors to NaN
    df['earliest_50y_free_time'] = pd.to_numeric(df['earliest_50y_free_time'], errors='coerce')

    # Drop rows where 'earliest_50y_free_time' is NaN
    df_cleaned = df.dropna(subset=['earliest_50y_free_time']).copy()

    # Filter the DataFrame for the target names
    # Updated: Filtering by the 'name' column
    filtered_times = df_cleaned[df_cleaned['name'].isin(target_names)]

    # Sort the filtered data by 'earliest_50y_free_time' in ascending order (lowest to highest)
    sorted_times = filtered_times.sort_values(by='earliest_50y_free_time', ascending=True) # Changed to True

    if not sorted_times.empty:
        print("\n--- Earliest 50-Yard Free Times (Lowest to Highest) for Selected Swimmers ---") # Updated title
        # Display only the relevant columns
        # Updated: Displaying 'name' and 'earliest_50y_free_time'
        print(sorted_times[['name', 'earliest_50y_free_time']])
    else:
        print("\nNo matching swimmers found or no valid times for the specified swimmers.")
        print("Please check the 'name' column in your CSV and the list of target names.")
