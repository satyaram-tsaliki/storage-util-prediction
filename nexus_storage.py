import pandas as pd
import re
import os
import matplotlib.pyplot as plt

def parse_log_line(line):
    pattern = r'(?P<timestamp>\S+\s\S+)\s(?P<log_level>\S+)\s(?P<repo_name>\S+)\s(?P<artifact_size>\d+)\s(?P<message>.*)'
    match = re.match(pattern, line)
    if match:
        return match.groupdict()
    return None

def load_log_file(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Log file {file_path} not found.")
    
    log_data = []
    
    with open(file_path, 'r') as file:
        for line in file:
            parsed_line = parse_log_line(line)
            if parsed_line:
                log_data.append(parsed_line)

    return pd.DataFrame(log_data)

def cleanse_log_data(df):
    df.dropna(subset=['timestamp', 'log_level', 'repo_name', 'artifact_size'], inplace=True)
    df['log_level'] = df['log_level'].str.lower()
    df['artifact_size'] = df['artifact_size'].astype(int)
    df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')

    return df

def calculate_total_size(df):
    df['date'] = df['timestamp'].dt.date
    df['week'] = df['timestamp'].dt.isocalendar().week
    df['month'] = df['timestamp'].dt.month

    daily_size = df.groupby('date')['artifact_size'].sum()
    weekly_size = df.groupby('week')['artifact_size'].sum()
    monthly_size = df.groupby('month')['artifact_size'].sum()

    return daily_size, weekly_size, monthly_size

def plot_sizes(daily_size, weekly_size, monthly_size):
    plt.figure(figsize=(10,6))
    
    plt.subplot(3, 1, 1)
    daily_size.plot(kind='bar', title='Total Artifact Size Uploaded per Day')
    plt.ylabel('Size (bytes)')
    
    plt.subplot(3, 1, 2)
    weekly_size.plot(kind='bar', title='Total Artifact Size Uploaded per Week')
    plt.ylabel('Size (bytes)')
    
    plt.subplot(3, 1, 3)
    monthly_size.plot(kind='bar', title='Total Artifact Size Uploaded per Month')
    plt.ylabel('Size (bytes)')

    plt.tight_layout()
    plt.show()

file_path = '*******nexus_log.txt'
log_df = load_log_file(file_path)
clean_df = cleanse_log_data(log_df)
daily_size, weekly_size, monthly_size = calculate_total_size(clean_df)
plot_sizes(daily_size, weekly_size, monthly_size)
