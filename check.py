import os
import csv
from datetime import datetime

def parse_csv_files(folder_path, connector_name):
    ip_data = {}

    # Iterate through each file in the specified folder
    for filename in os.listdir(folder_path):
        if filename.endswith('.LOG'):
            with open(os.path.join(folder_path, filename), mode='r', encoding='utf-8') as file:
                reader = csv.reader(file)
                for i, row in enumerate(reader):
                    if i < 5:  # Skip first 5 lines
                        continue
                    # print(row)
                    if connector_name in row[1]:  # Check if the line is relevant
                        # print("Found relevant line")
                        ip = row[5].split(':')[0]  # Extract IP address
                        date_time = row[0]

                        if ip not in ip_data:
                            ip_data[ip] = {'count': 0, 'last_used': date_time}
                        ip_data[ip]['count'] += 1
                        if datetime.fromisoformat(date_time) > datetime.fromisoformat(ip_data[ip]['last_used']):
                            ip_data[ip]['last_used'] = date_time
    return ip_data

def output_summary(ip_data):
    for ip, data in ip_data.items():
        print(f"IP: {ip}, Total found {data['count']}, last used {data['last_used']}")

# Folder path + connector name
folder_path = '.\\csv'
connector_name = 'Relay-Extern-SVR-E-EX3'

# Parse CSV files and output summary
ip_data = parse_csv_files(folder_path, connector_name)
output_summary(ip_data)
