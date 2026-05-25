from io import BytesIO
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import (
    getSampleStyleSheet,
    ParagraphStyle,
)

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    Image,
)


def generate_pdf_report(
    prediction: str,
    confidence: float,
    report_sections: dict,
    original_mri_path: str,
    gradcam_local_path: str,
):

    # --------------------------------
    # Normalize Paths
    # --------------------------------

    original_mri_path = str(
        Path(original_mri_path).resolve()
    )

    gradcam_local_path = str(
        Path(gradcam_local_path).resolve()
    )

    # --------------------------------
    # PDF Buffer
    # --------------------------------

    buffer = BytesIO()

    doc = SimpleDocTemplate(
        buffer,
        pagesize=letter,

        rightMargin=40,
        leftMargin=40,

        topMargin=40,
        bottomMargin=30,
    )

    styles = getSampleStyleSheet()

    # --------------------------------
    # Custom Styles
    # --------------------------------

    section_heading_style = ParagraphStyle(
        "SectionHeading",

        parent=styles["Heading2"],

        fontSize=16,
        leading=22,

        spaceAfter=14,

        textColor=colors.HexColor(
            "#1f2937"
        ),
    )

    body_style = ParagraphStyle(
        "BodyStyle",

        parent=styles["BodyText"],

        fontSize=11,

        leading=16,

        spaceAfter=12,
    )

    impression_style = ParagraphStyle(
        "ImpressionStyle",

        parent=styles["BodyText"],

        fontSize=11,

        leading=16,

        backColor=colors.HexColor(
            "#f3f4f6"
        ),

        borderPadding=12,

        spaceAfter=18,
    )

    footer_style = ParagraphStyle(
        "FooterStyle",

        parent=styles["Italic"],

        alignment=1,

        textColor=colors.grey,
    )

    elements = []

    # --------------------------------
    # Extract Report Sections
    # --------------------------------

    exam_info = report_sections[
        "exam_information"
    ]

    clinical_context = report_sections[
        "clinical_context"
    ]

    imaging_technique = report_sections[
        "imaging_technique"
    ]

    findings = report_sections[
        "findings"
    ]

    impression = report_sections[
        "impression"
    ]

    confidence_assessment = report_sections[
        "confidence_assessment"
    ]

    recommendations = report_sections[
        "recommendations"
    ]

    disclaimer = report_sections[
        "disclaimer"
    ]

    # --------------------------------
    # Title
    # --------------------------------

    title = Paragraph(
        """
        <font size=24>
        <b>CerebroVision AI</b>
        </font>

        <br/>

        <font size=14>
        AI-Assisted Radiology Report
        </font>
        """,

        styles["Title"],
    )

    elements.append(title)

    elements.append(
        Spacer(1, 28)
    )

    # --------------------------------
    # Exam Information Table
    # --------------------------------

    exam_data = [

        [
            "Modality",
            exam_info["modality"],
        ],

        [
            "Analysis Type",
            exam_info["analysis_type"],
        ],

        [
            "Generated On",
            exam_info["generated_on"],
        ],

        [
            "Prediction",
            prediction.upper(),
        ],

        [
            "Confidence",
            f"{confidence}%",
        ],
    ]

    exam_table = Table(
        exam_data,

        colWidths=[180, 300],
    )

    exam_table.setStyle(
        TableStyle([

            (
                "BACKGROUND",
                (0, 0),
                (0, -1),

                colors.HexColor(
                    "#e5e7eb"
                ),
            ),

            (
                "TEXTCOLOR",
                (0, 0),
                (-1, -1),

                colors.black,
            ),

            (
                "GRID",
                (0, 0),
                (-1, -1),

                1,

                colors.HexColor(
                    "#d1d5db"
                ),
            ),

            (
                "FONTNAME",
                (0, 0),
                (-1, -1),

                "Helvetica",
            ),

            (
                "BOTTOMPADDING",
                (0, 0),
                (-1, -1),

                10,
            ),
        ])
    )

    elements.append(
        exam_table
    )

    elements.append(
        Spacer(1, 30)
    )

    # --------------------------------
    # Section Helper
    # --------------------------------

    def add_section(
        title,
        content,
        style=body_style,
    ):

        elements.append(
            Paragraph(
                f"<b>{title}</b>",
                section_heading_style,
            )
        )

        elements.append(
            Paragraph(
                content,
                style,
            )
        )

        elements.append(
            Spacer(1, 12)
        )

    # --------------------------------
    # Clinical Sections
    # --------------------------------

    add_section(
        "Clinical Context",
        clinical_context,
    )

    add_section(
        "Imaging Technique",
        imaging_technique,
    )

    # --------------------------------
    # MRI + GradCAM Images
    # --------------------------------

    elements.append(
        Paragraph(
            "<b>MRI & Grad-CAM Comparison</b>",
            section_heading_style,
        )
    )

    elements.append(
        Spacer(1, 6)
    )

    mri_image = Image(
        original_mri_path,

        width=180,
        height=180,
    )

    gradcam_image = Image(
        gradcam_local_path,

        width=220,
        height=220,
    )

    comparison_table = Table([
        [
            mri_image,
            gradcam_image,
        ]
    ])

    comparison_table.setStyle(
        TableStyle([

            (
                "VALIGN",
                (0, 0),
                (-1, -1),

                "MIDDLE",
            ),

            (
                "ALIGN",
                (0, 0),
                (-1, -1),

                "CENTER",
            ),
        ])
    )

    elements.append(
        comparison_table
    )

    elements.append(
        Spacer(1, 15)
    )

    # --------------------------------
    # Findings & Impression
    # --------------------------------

    add_section(
        "AI Findings",
        findings,
    )

    add_section(
        "Impression",
        impression,
        impression_style,
    )

    # --------------------------------
    # Confidence Assessment
    # --------------------------------

    elements.append(
        Paragraph(
            "<b>Confidence Assessment</b>",
            section_heading_style,
        )
    )

    confidence_data = [

        [
            "Prediction",
            confidence_assessment[
                "prediction"
            ],
        ],

        [
            "Confidence Score",
            confidence_assessment[
                "confidence_score"
            ],
        ],

        [
            "Confidence Level",
            confidence_assessment[
                "confidence_level"
            ],
        ],
    ]

    confidence_table = Table(
        confidence_data,

        colWidths=[220, 260],
    )

    confidence_table.setStyle(
        TableStyle([

            (
                "BACKGROUND",
                (0, 0),
                (0, -1),

                colors.HexColor(
                    "#f3f4f6"
                ),
            ),

            (
                "GRID",
                (0, 0),
                (-1, -1),

                1,

                colors.HexColor(
                    "#d1d5db"
                ),
            ),

            (
                "BOTTOMPADDING",
                (0, 0),
                (-1, -1),

                10,
            ),
        ])
    )

    elements.append(
        confidence_table
    )

    elements.append(
        Spacer(1, 28)
    )

    # --------------------------------
    # Recommendations
    # --------------------------------

    add_section(
        "Recommendations",
        recommendations,
    )

    # --------------------------------
    # Disclaimer
    # --------------------------------

    add_section(
        "Disclaimer",
        disclaimer,
    )

    # --------------------------------
    # Footer
    # --------------------------------

    elements.append(
        Spacer(1, 30)
    )

    footer = Paragraph(
        """
        Generated by CerebroVision AI
        <br/>
        Experimental Educational AI System
        """,

        footer_style,
    )

    elements.append(
        footer
    )

    # --------------------------------
    # Build PDF
    # --------------------------------

    doc.build(elements)

    buffer.seek(0)

    return buffer