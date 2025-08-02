#!/usr/bin/env python3
"""
Generate Excel files from video platform comparison data
"""

import csv
import json
import re
from pathlib import Path

def parse_markdown_table(content):
    """Parse markdown table and return structured data"""
    lines = content.split('\n')
    tables = []
    current_table = []
    in_table = False
    
    for line in lines:
        if line.strip().startswith('|') and '|' in line:
            if not in_table:
                in_table = True
            current_table.append(line)
        elif in_table:
            if line.strip() == '' or not line.strip().startswith('|'):
                if current_table:
                    tables.append(parse_single_table(current_table))
                    current_table = []
                in_table = False
    
    if current_table:
        tables.append(parse_single_table(current_table))
    
    return tables

def parse_single_table(table_lines):
    """Parse a single markdown table"""
    if len(table_lines) < 3:
        return None
    
    # Parse headers
    header_line = table_lines[0]
    headers = [h.strip() for h in header_line.split('|')[1:-1]]
    
    # Parse separator line (second line)
    separator_line = table_lines[1]
    
    # Parse data rows
    data_rows = []
    for line in table_lines[2:]:
        if line.strip() and '|' in line:
            cells = [cell.strip() for cell in line.split('|')[1:-1]]
            if len(cells) == len(headers):
                data_rows.append(cells)
    
    return {
        'headers': headers,
        'data': data_rows
    }

def create_csv_from_table(table_data, filename):
    """Create CSV file from table data"""
    if not table_data:
        return
    
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(table_data['headers'])
        writer.writerows(table_data['data'])
    
    print(f"Created CSV: {filename}")

def create_json_from_table(table_data, filename):
    """Create JSON file from table data"""
    if not table_data:
        return
    
    # Convert to list of dictionaries
    json_data = []
    for row in table_data['data']:
        row_dict = {}
        for i, header in enumerate(table_data['headers']):
            if i < len(row):
                row_dict[header] = row[i]
        json_data.append(row_dict)
    
    with open(filename, 'w', encoding='utf-8') as jsonfile:
        json.dump(json_data, jsonfile, indent=2, ensure_ascii=False)
    
    print(f"Created JSON: {filename}")

def main():
    # Read the markdown files
    files = [
        'video_platform_comparison.md',
        'video_platform_comparison_practical.md'
    ]
    
    for filename in files:
        if not Path(filename).exists():
            print(f"File not found: {filename}")
            continue
        
        print(f"\nProcessing: {filename}")
        
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Parse tables
        tables = parse_markdown_table(content)
        
        # Create output files for each table
        base_name = Path(filename).stem
        
        for i, table in enumerate(tables):
            if table:
                # Create CSV
                csv_filename = f"{base_name}_table_{i+1}.csv"
                create_csv_from_table(table, csv_filename)
                
                # Create JSON
                json_filename = f"{base_name}_table_{i+1}.json"
                create_json_from_table(table, json_filename)

if __name__ == "__main__":
    main()