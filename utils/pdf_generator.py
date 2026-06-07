from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)

from reportlab.lib import colors


class PDFGenerator:

    def __init__(self):

        self.styles = (
            getSampleStyleSheet()
        )

    # ==================================
    # Generate Resume PDF
    # ==================================

    def generate_resume(

        self,

        filename,

        name,

        email,

        phone,

        linkedin,

        github,

        objective,

        education,

        skills,

        projects,

        experience,

        certifications,

        achievements

    ):

        doc = SimpleDocTemplate(
            filename
        )

        elements = []

        title_style = (
            self.styles["Title"]
        )

        heading_style = (
            self.styles["Heading2"]
        )

        body_style = (
            self.styles["BodyText"]
        )

        # ==========================
        # Header
        # ==========================

        elements.append(
            Paragraph(
                name,
                title_style
            )
        )

        elements.append(
            Paragraph(
                f"""
                Email: {email}<br/>
                Phone: {phone}<br/>
                LinkedIn: {linkedin}<br/>
                GitHub: {github}
                """,
                body_style
            )
        )

        elements.append(
            Spacer(1, 20)
        )

        # ==========================
        # Objective
        # ==========================

        elements.append(
            Paragraph(
                "Career Objective",
                heading_style
            )
        )

        elements.append(
            Paragraph(
                objective,
                body_style
            )
        )

        elements.append(
            Spacer(1, 15)
        )

        # ==========================
        # Education
        # ==========================

        elements.append(
            Paragraph(
                "Education",
                heading_style
            )
        )

        elements.append(
            Paragraph(
                education,
                body_style
            )
        )

        elements.append(
            Spacer(1, 15)
        )

        # ==========================
        # Skills
        # =================