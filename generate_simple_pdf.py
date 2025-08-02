#!/usr/bin/env python3
"""
Generate simple PDF files from video platform comparison data using basic libraries
"""

import csv
import json
from pathlib import Path

def create_html_from_csv(csv_filename, html_filename, title="Video Platform Comparison"):
    """Create HTML file from CSV data that can be converted to PDF"""
    if not Path(csv_filename).exists():
        print(f"CSV file not found: {csv_filename}")
        return
    
    # Read CSV data
    data = []
    with open(csv_filename, 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)
    
    if not data:
        print(f"No data found in {csv_filename}")
        return
    
    # Create HTML content
    html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>{title}</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 20px;
            font-size: 10px;
        }}
        h1 {{
            text-align: center;
            color: #333;
            margin-bottom: 20px;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 20px;
            font-size: 8px;
        }}
        th, td {{
            border: 1px solid #ddd;
            padding: 4px;
            text-align: center;
            vertical-align: middle;
        }}
        th {{
            background-color: #f2f2f2;
            font-weight: bold;
        }}
        tr:nth-child(even) {{
            background-color: #f9f9f9;
        }}
        .feature-name {{
            text-align: left;
            font-weight: bold;
        }}
        .platform {{
            font-weight: bold;
            background-color: #e6f3ff;
        }}
        @media print {{
            body {{
                font-size: 8px;
            }}
            table {{
                font-size: 6px;
            }}
        }}
    </style>
</head>
<body>
    <h1>{title}</h1>
    <table>
        <thead>
            <tr>
"""
    
    # Add headers
    for header in data[0]:
        html_content += f'                <th>{header}</th>\n'
    
    html_content += "            </tr>\n        </thead>\n        <tbody>\n"
    
    # Add data rows
    for i, row in enumerate(data[1:], 1):
        html_content += "            <tr>\n"
        for j, cell in enumerate(row):
            if j == 0:  # First column (feature name)
                html_content += f'                <td class="feature-name">{cell}</td>\n'
            elif j == 1:  # Second column (serial number)
                html_content += f'                <td>{cell}</td>\n'
            else:  # Platform columns
                html_content += f'                <td class="platform">{cell}</td>\n'
        html_content += "            </tr>\n"
    
    html_content += """
        </tbody>
    </table>
</body>
</html>
"""
    
    # Write HTML file
    with open(html_filename, 'w', encoding='utf-8') as htmlfile:
        htmlfile.write(html_content)
    
    print(f"Created HTML: {html_filename}")

def create_summary_html():
    """Create a summary HTML file"""
    html_content = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Video Platform Comparison Summary</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 40px;
            line-height: 1.6;
        }
        h1 {
            text-align: center;
            color: #333;
            margin-bottom: 30px;
        }
        h2 {
            color: #555;
            border-bottom: 2px solid #ddd;
            padding-bottom: 10px;
        }
        .summary-box {
            background-color: #f9f9f9;
            padding: 20px;
            border-radius: 5px;
            margin: 20px 0;
        }
        .file-list {
            background-color: #e6f3ff;
            padding: 15px;
            border-radius: 5px;
            margin: 20px 0;
        }
        .platform-list {
            columns: 2;
            column-gap: 40px;
        }
        ul {
            margin: 10px 0;
        }
        li {
            margin: 5px 0;
        }
    </style>
</head>
<body>
    <h1>Video Platform Comparison Summary</h1>
    
    <div class="summary-box">
        <h2>Overview</h2>
        <p>This document contains comprehensive comparisons of video calling platforms including:</p>
        <ul>
            <li><strong>Technical Settings:</strong> 20 features analyzed</li>
            <li><strong>UI/UX Features:</strong> 100 features compared</li>
            <li><strong>Platform Coverage:</strong> 15 major platforms</li>
            <li><strong>Additional Platforms:</strong> 40+ emerging and specialized platforms</li>
        </ul>
    </div>
    
    <div class="summary-box">
        <h2>Platforms Compared</h2>
        <div class="platform-list">
            <ul>
                <li>Jitsi Meet</li>
                <li>Google Meet</li>
                <li>Zoom</li>
                <li>Microsoft Teams</li>
                <li>Cisco Webex</li>
                <li>Discord</li>
                <li>Slack</li>
                <li>BlueJeans</li>
                <li>RingCentral</li>
                <li>8x8</li>
                <li>Whereby</li>
                <li>Loom</li>
            </ul>
        </div>
    </div>
    
    <div class="file-list">
        <h2>Generated Files</h2>
        <ul>
            <li><strong>CSV Files:</strong>
                <ul>
                    <li>video_platform_comparison_table_1.csv - Technical Settings</li>
                    <li>video_platform_comparison_table_2.csv - UI/UX Features</li>
                    <li>video_platform_comparison_practical_table_1.csv - Technical Settings (Practical)</li>
                    <li>video_platform_comparison_practical_table_2.csv - UI/UX Features (Practical)</li>
                </ul>
            </li>
            <li><strong>HTML Files:</strong>
                <ul>
                    <li>technical_comparison.html - Technical Settings Comparison</li>
                    <li>uiux_comparison.html - UI/UX Features Comparison</li>
                    <li>technical_comparison_practical.html - Technical Settings (Practical)</li>
                    <li>uiux_comparison_practical.html - UI/UX Features (Practical)</li>
                </ul>
            </li>
            <li><strong>JSON Files:</strong>
                <ul>
                    <li>video_platform_comparison_table_1.json - Technical Settings (JSON format)</li>
                    <li>video_platform_comparison_table_2.json - UI/UX Features (JSON format)</li>
                    <li>video_platform_comparison_practical_table_1.json - Technical Settings (Practical, JSON)</li>
                    <li>video_platform_comparison_practical_table_2.json - UI/UX Features (Practical, JSON)</li>
                </ul>
            </li>
        </ul>
    </div>
    
    <div class="summary-box">
        <h2>Usage Instructions</h2>
        <ul>
            <li><strong>CSV Files:</strong> Open in Excel, Google Sheets, or any spreadsheet application</li>
            <li><strong>HTML Files:</strong> Open in a web browser and print to PDF</li>
            <li><strong>JSON Files:</strong> Use for data analysis or integration with other tools</li>
        </ul>
    </div>
</body>
</html>
"""
    
    with open("video_platform_comparison_summary.html", 'w', encoding='utf-8') as htmlfile:
        htmlfile.write(html_content)
    
    print("Created HTML: video_platform_comparison_summary.html")

def main():
    # Create HTML files from CSV files
    csv_files = [
        ("video_platform_comparison_table_1.csv", "technical_comparison.html", "Technical Settings Comparison"),
        ("video_platform_comparison_table_2.csv", "uiux_comparison.html", "UI/UX Features Comparison"),
        ("video_platform_comparison_practical_table_1.csv", "technical_comparison_practical.html", "Technical Settings Comparison (Practical)"),
        ("video_platform_comparison_practical_table_2.csv", "uiux_comparison_practical.html", "UI/UX Features Comparison (Practical)")
    ]
    
    for csv_file, html_file, title in csv_files:
        if Path(csv_file).exists():
            create_html_from_csv(csv_file, html_file, title)
    
    # Create summary HTML
    create_summary_html()

if __name__ == "__main__":
    main()