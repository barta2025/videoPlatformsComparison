#!/usr/bin/env python3
"""
Generate PDF files from video platform comparison data
"""

import csv
import json
from pathlib import Path
from reportlab.lib.pagesizes import letter, A4, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT

def create_pdf_from_csv(csv_filename, pdf_filename, title="Video Platform Comparison"):
    """Create PDF from CSV data"""
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
    
    # Create PDF
    doc = SimpleDocTemplate(
        pdf_filename,
        pagesize=landscape(A4),
        rightMargin=0.5*inch,
        leftMargin=0.5*inch,
        topMargin=0.5*inch,
        bottomMargin=0.5*inch
    )
    
    # Create story (content)
    story = []
    styles = getSampleStyleSheet()
    
    # Add title
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=16,
        spaceAfter=20,
        alignment=TA_CENTER
    )
    story.append(Paragraph(title, title_style))
    story.append(Spacer(1, 12))
    
    # Create table
    table = Table(data)
    
    # Style the table
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 8),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 6),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.beige]),
    ])
    
    table.setStyle(style)
    story.append(table)
    
    # Build PDF
    doc.build(story)
    print(f"Created PDF: {pdf_filename}")

def create_summary_pdf():
    """Create a summary PDF with all comparison data"""
    doc = SimpleDocTemplate(
        "video_platform_comparison_summary.pdf",
        pagesize=A4,
        rightMargin=0.5*inch,
        leftMargin=0.5*inch,
        topMargin=0.5*inch,
        bottomMargin=0.5*inch
    )
    
    story = []
    styles = getSampleStyleSheet()
    
    # Add title
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=18,
        spaceAfter=20,
        alignment=TA_CENTER
    )
    story.append(Paragraph("Video Platform Comparison Summary", title_style))
    story.append(Spacer(1, 20))
    
    # Add summary content
    summary_text = """
    This document contains comprehensive comparisons of video calling platforms including:
    
    • Technical Settings (20 features)
    • UI/UX Features (100 features)
    • Platform Coverage: 15 major platforms
    • Additional Platforms: 40+ emerging and specialized platforms
    
    Platforms compared include:
    • Jitsi Meet, Google Meet, Zoom, Microsoft Teams, Cisco Webex
    • Discord, Slack, BlueJeans, RingCentral, 8x8
    • Whereby, Loom, and many more
    
    For detailed comparisons, see the individual CSV and JSON files.
    """
    
    normal_style = ParagraphStyle(
        'Normal',
        parent=styles['Normal'],
        fontSize=12,
        spaceAfter=12,
        alignment=TA_LEFT
    )
    
    story.append(Paragraph(summary_text, normal_style))
    story.append(Spacer(1, 20))
    
    # Add file list
    files = [
        "video_platform_comparison_table_1.csv - Technical Settings",
        "video_platform_comparison_table_2.csv - UI/UX Features",
        "video_platform_comparison_practical_table_1.csv - Technical Settings (Practical)",
        "video_platform_comparison_practical_table_2.csv - UI/UX Features (Practical)"
    ]
    
    for file_info in files:
        story.append(Paragraph(f"• {file_info}", normal_style))
    
    doc.build(story)
    print("Created PDF: video_platform_comparison_summary.pdf")

def main():
    # Create PDFs from CSV files
    csv_files = [
        ("video_platform_comparison_table_1.csv", "technical_comparison.pdf", "Technical Settings Comparison"),
        ("video_platform_comparison_table_2.csv", "uiux_comparison.pdf", "UI/UX Features Comparison"),
        ("video_platform_comparison_practical_table_1.csv", "technical_comparison_practical.pdf", "Technical Settings Comparison (Practical)"),
        ("video_platform_comparison_practical_table_2.csv", "uiux_comparison_practical.pdf", "UI/UX Features Comparison (Practical)")
    ]
    
    for csv_file, pdf_file, title in csv_files:
        if Path(csv_file).exists():
            create_pdf_from_csv(csv_file, pdf_file, title)
    
    # Create summary PDF
    create_summary_pdf()

if __name__ == "__main__":
    main()