#!/usr/bin/env python3
"""
Create Excel-like files from video platform comparison data
"""

import csv
import json
from pathlib import Path

def create_formatted_csv(csv_filename, formatted_filename, title="Video Platform Comparison"):
    """Create a formatted CSV file with better structure"""
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
    
    # Create formatted CSV with better structure
    with open(formatted_filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        
        # Add title row
        writer.writerow([title])
        writer.writerow([])  # Empty row
        
        # Add headers
        writer.writerow(data[0])
        
        # Add separator line
        separator = ['---'] * len(data[0])
        writer.writerow(separator)
        
        # Add data rows
        for row in data[1:]:
            writer.writerow(row)
        
        # Add summary row
        writer.writerow([])
        writer.writerow(['Summary', 'Total Features', str(len(data)-1), '', '', '', '', '', '', '', '', '', '', '', '', '', ''])
    
    print(f"Created formatted CSV: {formatted_filename}")

def create_summary_csv():
    """Create a summary CSV file with all comparison data"""
    summary_data = [
        ['Video Platform Comparison Summary'],
        [''],
        ['Overview'],
        ['Feature Category', 'Count', 'Description'],
        ['---', '---', '---'],
        ['Technical Settings', '20', 'Backend languages, codecs, encryption, etc.'],
        ['UI/UX Features', '100', 'User interface and experience features'],
        ['Platforms Compared', '15', 'Major video calling platforms'],
        ['Additional Platforms', '40+', 'Emerging and specialized platforms'],
        [''],
        ['Platforms Included'],
        ['Platform', 'Type', 'Key Features'],
        ['---', '---', '---'],
        ['Jitsi Meet', 'Open Source', 'Self-hosted, WebRTC, Free'],
        ['Google Meet', 'Enterprise', 'Google Workspace integration'],
        ['Zoom', 'Commercial', 'Wide adoption, extensive features'],
        ['Microsoft Teams', 'Enterprise', 'Microsoft 365 integration'],
        ['Cisco Webex', 'Enterprise', 'Cisco ecosystem integration'],
        ['Discord', 'Community', 'Gaming and community focus'],
        ['Slack', 'Business', 'Team collaboration focus'],
        ['BlueJeans', 'Enterprise', 'Verizon enterprise platform'],
        ['RingCentral', 'Business', 'Unified communications'],
        ['8x8', 'Business', 'Cloud communications'],
        ['Whereby', 'Simple', 'Browser-based, easy to use'],
        ['Loom', 'Recording', 'Video messaging and screen recording'],
        [''],
        ['Generated Files'],
        ['File Type', 'Filename', 'Description'],
        ['---', '---', '---'],
        ['CSV', 'video_platform_comparison_table_1.csv', 'Technical Settings Comparison'],
        ['CSV', 'video_platform_comparison_table_2.csv', 'UI/UX Features Comparison'],
        ['CSV', 'video_platform_comparison_practical_table_1.csv', 'Technical Settings (Practical)'],
        ['CSV', 'video_platform_comparison_practical_table_2.csv', 'UI/UX Features (Practical)'],
        ['HTML', 'technical_comparison.html', 'Technical Settings (Printable)'],
        ['HTML', 'uiux_comparison.html', 'UI/UX Features (Printable)'],
        ['HTML', 'technical_comparison_practical.html', 'Technical Settings (Practical, Printable)'],
        ['HTML', 'uiux_comparison_practical.html', 'UI/UX Features (Practical, Printable)'],
        ['JSON', 'video_platform_comparison_table_1.json', 'Technical Settings (JSON format)'],
        ['JSON', 'video_platform_comparison_table_2.json', 'UI/UX Features (JSON format)'],
        ['JSON', 'video_platform_comparison_practical_table_1.json', 'Technical Settings (Practical, JSON)'],
        ['JSON', 'video_platform_comparison_practical_table_2.json', 'UI/UX Features (Practical, JSON)']
    ]
    
    with open("video_platform_comparison_summary.csv", 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        for row in summary_data:
            writer.writerow(row)
    
    print("Created CSV: video_platform_comparison_summary.csv")

def create_readme():
    """Create a README file with instructions"""
    readme_content = """# Video Platform Comparison Files

This directory contains comprehensive comparison files for video calling platforms.

## Files Generated

### CSV Files (Excel-compatible)
- `video_platform_comparison_table_1.csv` - Technical Settings Comparison
- `video_platform_comparison_table_2.csv` - UI/UX Features Comparison
- `video_platform_comparison_practical_table_1.csv` - Technical Settings (Practical)
- `video_platform_comparison_practical_table_2.csv` - UI/UX Features (Practical)
- `video_platform_comparison_summary.csv` - Summary and overview

### HTML Files (Printable)
- `technical_comparison.html` - Technical Settings Comparison (print to PDF)
- `uiux_comparison.html` - UI/UX Features Comparison (print to PDF)
- `technical_comparison_practical.html` - Technical Settings (Practical, print to PDF)
- `uiux_comparison_practical.html` - UI/UX Features (Practical, print to PDF)
- `video_platform_comparison_summary.html` - Summary and overview (print to PDF)

### JSON Files (Data format)
- `video_platform_comparison_table_1.json` - Technical Settings (JSON format)
- `video_platform_comparison_table_2.json` - UI/UX Features (JSON format)
- `video_platform_comparison_practical_table_1.json` - Technical Settings (Practical, JSON)
- `video_platform_comparison_practical_table_2.json` - UI/UX Features (Practical, JSON)

## Usage Instructions

### For Excel/Spreadsheet Users:
1. Open any `.csv` file in Excel, Google Sheets, or LibreOffice Calc
2. The data will be automatically formatted in a table
3. You can sort, filter, and analyze the data as needed

### For PDF Generation:
1. Open any `.html` file in a web browser
2. Use the browser's print function (Ctrl+P or Cmd+P)
3. Select "Save as PDF" as the destination
4. The HTML files are optimized for printing with proper formatting

### For Data Analysis:
1. Use the `.json` files for programmatic access
2. Import into data analysis tools like Python, R, or Tableau
3. The JSON format preserves all data structure

## Platforms Compared

### Major Platforms (15):
- Jitsi Meet, Google Meet, Zoom, Microsoft Teams, Cisco Webex
- Discord, Slack, BlueJeans, RingCentral, 8x8
- Whereby, Loom, and more

### Additional Platforms (40+):
- Emerging platforms: Calendly, Cal.com, Tandem, Gather, Spatial
- Enterprise platforms: Vonage, LogMeIn, TeamViewer, AnyDesk
- Specialized platforms: Doxy.me, TheraNest, SimplePractice (healthcare)

## Features Analyzed

### Technical Settings (20 features):
- Backend Language, Frontend Language, Bandwidth Adaptability
- Video Resolution, Codec, Encryption Used, External API Calls
- STUN Server Location, Mobile SDK Support, WebRTC Implementation
- Cloud Infrastructure, Recording Capability, Analytics & Monitoring
- SSO Integration, Compliance Standards, Multi-tenant Support
- Auto-scaling, Load Balancing, CDN Integration, Database Technology

### UI/UX Features (100 features):
- Meeting controls (mute, camera, waiting room)
- Collaboration features (chat, whiteboard, screen sharing)
- Integration options (calendar, API, SDK, webhooks)
- AI features (meeting assistant, smart summaries)
- Analytics and monitoring features
- Settings and configuration options

## Data Sources

The comparison is based on:
- Official platform documentation
- Technical specifications
- User experience analysis
- Industry reports and reviews

## Updates

This comparison is regularly updated to reflect:
- New platform features
- Emerging platforms
- Technology changes
- User feedback

For questions or suggestions, please refer to the main comparison document.
"""
    
    with open("README.md", 'w', encoding='utf-8') as readmefile:
        readmefile.write(readme_content)
    
    print("Created README: README.md")

def main():
    # Create formatted CSV files
    csv_files = [
        ("video_platform_comparison_table_1.csv", "technical_comparison_formatted.csv", "Technical Settings Comparison"),
        ("video_platform_comparison_table_2.csv", "uiux_comparison_formatted.csv", "UI/UX Features Comparison"),
        ("video_platform_comparison_practical_table_1.csv", "technical_comparison_practical_formatted.csv", "Technical Settings Comparison (Practical)"),
        ("video_platform_comparison_practical_table_2.csv", "uiux_comparison_practical_formatted.csv", "UI/UX Features Comparison (Practical)")
    ]
    
    for csv_file, formatted_file, title in csv_files:
        if Path(csv_file).exists():
            create_formatted_csv(csv_file, formatted_file, title)
    
    # Create summary files
    create_summary_csv()
    create_readme()

if __name__ == "__main__":
    main()