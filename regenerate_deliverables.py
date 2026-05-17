from pathlib import Path

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.util import Inches, Pt
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import (
    ListFlowable,
    ListItem,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parent
PPTX_PATH = ROOT / "LoanEvaluator_Quality_Diagnostic.pptx"
PDF_PATH = ROOT / "raport_testare.pdf"


def set_run_style(run, *, size=24, bold=False, color=(255, 255, 255)):
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.color.rgb = RGBColor(*color)


def add_title_slide(prs, title, subtitle):
    slide = prs.slides.add_slide(prs.slide_layouts[0])
    bg = slide.background.fill
    bg.solid()
    bg.fore_color.rgb = RGBColor(18, 52, 86)

    title_box = slide.shapes.title
    title_box.text = title
    for paragraph in title_box.text_frame.paragraphs:
        for run in paragraph.runs:
            set_run_style(run, size=30, bold=True)

    subtitle_box = slide.placeholders[1]
    subtitle_box.text = subtitle
    for paragraph in subtitle_box.text_frame.paragraphs:
        for run in paragraph.runs:
            set_run_style(run, size=16, color=(230, 235, 242))


def add_bullet_slide(prs, title, bullets, footer=None):
    slide = prs.slides.add_slide(prs.slide_layouts[5])
    bg = slide.background.fill
    bg.solid()
    bg.fore_color.rgb = RGBColor(248, 250, 252)

    title_shape = slide.shapes.title
    title_shape.text = title
    for paragraph in title_shape.text_frame.paragraphs:
        for run in paragraph.runs:
            run.font.size = Pt(28)
            run.font.bold = True
            run.font.color.rgb = RGBColor(18, 52, 86)

    box = slide.shapes.add_textbox(Inches(0.8), Inches(1.6), Inches(11.8), Inches(5.2))
    tf = box.text_frame
    tf.word_wrap = True
    tf.margin_left = Pt(4)
    tf.margin_right = Pt(4)
    tf.clear()

    for index, item in enumerate(bullets):
        paragraph = tf.paragraphs[0] if index == 0 else tf.add_paragraph()
        if isinstance(item, tuple):
            text, level = item
        else:
            text, level = item, 0
        paragraph.text = text
        paragraph.level = level
        paragraph.font.size = Pt(20 if level == 0 else 18)
        paragraph.font.color.rgb = RGBColor(35, 35, 35)

    if footer:
        footer_box = slide.shapes.add_textbox(Inches(0.8), Inches(6.8), Inches(11.5), Inches(0.4))
        footer_tf = footer_box.text_frame
        footer_tf.text = footer
        footer_paragraph = footer_tf.paragraphs[0]
        footer_paragraph.alignment = PP_ALIGN.RIGHT
        for run in footer_paragraph.runs:
            run.font.size = Pt(11)
            run.font.color.rgb = RGBColor(90, 90, 90)


def build_pptx():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)

    # Remove the default first slide so the generated deck is fully controlled.
    while prs.slides:
        r_id = prs.slides._sldIdLst[0].rId
        prs.part.drop_rel(r_id)
        del prs.slides._sldIdLst[0]

    add_title_slide(
        prs,
        "LoanEvaluator - diagnostic de calitate",
        "Testare unitara, frontiere, basis path si mutation testing",
    )

    add_bullet_slide(
        prs,
        "1. Obiective",
        [
            "Aplicarea tehnicilor cerute la disciplina Testarea Sistemelor Software.",
            "Construirea unei suite de teste formale pentru clasa LoanEvaluator.",
            "Compararea unei suite proiectate manual cu o suita generata automat de Claude.",
            "Justificarea utilizarii mutmut fata de un generator didactic de mutanti.",
        ],
        "README.md si rapoartele asociate au fost aliniate la aceasta versiune.",
    )

    add_bullet_slide(
        prs,
        "2. Componenta testata",
        [
            "validate_loan_amount: valideaza intervalul [1000, 50000] si intoarce small, medium sau large.",
            "calculate_interest_rate: aplica reguli de dobanda in functie de suma, perioada si contul de salariu.",
            "evaluate_application: decide approved, manual_review sau rejected.",
            "Diagrama pentru evaluate_application este folosita pentru cursul 2 si traseele independente.",
        ],
        "Numar total de teste in proiect: 53.",
    )

    add_bullet_slide(
        prs,
        "3. Tehnici de testare",
        [
            "Clase de echivalenta: valori sub minim, intervale valide si valori peste maxim.",
            "Frontiere: 999/1000/1001, 5000/5001, 20000/20001, 49999/50000/50001.",
            "Acoperire la nivel de instructiune, decizie si conditie.",
            "Basis path pentru evaluate_application, cu noduri numerotate in graf.",
        ],
    )

    add_bullet_slide(
        prs,
        "4. Graful de control",
        [
            "1. validarea valorilor negative",
            "2. calculul raportului de indatorare",
            "3. pragul credit_score < 550",
            "4. ramura de venit mare",
            "5. aprobarea finala prin scor sau codebitor",
            "6. ramura de venit mediu",
            "7. respingerea implicita",
        ],
        "Diagrama SVG din diagrams/flowchart_evaluate_application.svg a fost numerotata pentru cursul 2.",
    )

    add_bullet_slide(
        prs,
        "5. Mutation testing",
        [
            "mutmut este preferat fiindca genereaza mutanti direct din codul real.",
            "Instrumentul este mai robust si mai repetabil decat un generator manual de mutanti.",
            "mutation_runner.py ramane util doar ca suport didactic si comparativ.",
            "Pentru mutmut este recomandat un mediu virtual local.",
        ],
    )

    add_bullet_slide(
        prs,
        "6. Structura testelor",
        [
            "tests/test_loan_evaluator_core.py: 15 teste de baza.",
            "tests/test_loan_evaluator_additional.py: 2 teste suplimentare.",
            "tests/test_loan_evaluator_ai_generated.py: 16 teste generate de Claude.",
            "tests/test_loan_evaluator_mutmut.py: 20 teste derivate din analiza mutmut.",
        ],
        "Total verificat prin unittest: 53 teste, toate OK.",
    )

    add_bullet_slide(
        prs,
        "7. Rezultate",
        [
            "Suita manuala acopera sistematic frontierele si traseele sensibile.",
            "Claude ofera rapid un schelet util, dar nu inlocuieste proiectarea formala.",
            "Testele suplimentare au inchis golurile identificate de mutanti.",
            "Rezultatul final este o suita stabila si mai puternica la regresii.",
        ],
    )

    add_bullet_slide(
        prs,
        "8. Referinte",
        [
            "Python Software Foundation - unittest.",
            "A. J. Offutt - Introduction to Software Testing.",
            "ISTQB Foundation Level Syllabus - Test Design Techniques.",
            "mutmut - mutation testing tool.",
        ],
    )

    prs.save(PPTX_PATH)


def build_pdf():
    doc = SimpleDocTemplate(
        str(PDF_PATH),
        pagesize=A4,
        rightMargin=2 * cm,
        leftMargin=2 * cm,
        topMargin=1.8 * cm,
        bottomMargin=1.8 * cm,
    )

    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        "CustomTitle",
        parent=styles["Title"],
        fontName="Helvetica-Bold",
        fontSize=20,
        leading=24,
        textColor=colors.HexColor("#123456"),
        spaceAfter=12,
    )
    heading_style = ParagraphStyle(
        "CustomHeading",
        parent=styles["Heading2"],
        fontName="Helvetica-Bold",
        fontSize=13,
        leading=16,
        textColor=colors.HexColor("#123456"),
        spaceBefore=8,
        spaceAfter=6,
    )
    body_style = ParagraphStyle(
        "CustomBody",
        parent=styles["BodyText"],
        fontName="Helvetica",
        fontSize=10.5,
        leading=14,
        spaceAfter=4,
    )

    story = []
    story.append(Paragraph("Raport de testare si aliniere deliverabile", title_style))
    story.append(Paragraph("1. Obiectiv", heading_style))
    story.append(Paragraph(
        "Documentul sintetizeaza proiectarea si verificarea suitei de teste pentru clasa LoanEvaluator, precum si justificarea utilizarii mutmut in locul unui generator manual de mutanti.",
        body_style,
    ))

    story.append(Paragraph("2. Componenta testata", heading_style))
    story.append(ListFlowable(
        [
            ListItem(Paragraph("validate_loan_amount: intervalul [1000, 50000] si clasificarea small/medium/large.", body_style)),
            ListItem(Paragraph("calculate_interest_rate: reguli pentru suma, perioada si contul de salariu.", body_style)),
            ListItem(Paragraph("evaluate_application: aprobarea, review-ul manual si respingerea.", body_style)),
        ],
        bulletType="bullet",
    ))

    story.append(Paragraph("3. Tehnici de testare", heading_style))
    data = [
        ["Tehnica", "Elemente acoperite"],
        ["Clase de echivalenta", "sub minim, intervale valide, peste maxim"],
        ["Frontiere", "999/1000/1001, 5000/5001, 20000/20001, 49999/50000/50001"],
        ["Acoperire", "statement, decision, condition"],
        ["Basis path", "trasee independente pentru evaluate_application"],
    ]
    table = Table(data, colWidths=[4.0 * cm, 10.5 * cm])
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#d9e6f2")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.black),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("FONTSIZE", (0, 0), (-1, -1), 9.5),
                ("LEADING", (0, 0), (-1, -1), 12),
                ("GRID", (0, 0), (-1, -1), 0.4, colors.grey),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.whitesmoke, colors.lightgrey]),
            ]
        )
    )
    story.append(table)

    story.append(Paragraph("4. Mutation testing", heading_style))
    story.append(Paragraph(
        "mutmut este preferat fiindca genereaza mutanti direct din codul real, este repetabil si scaleaza mai bine decat un generator manual. mutation_runner.py ramane util doar ca instrument didactic.",
        body_style,
    ))

    story.append(Paragraph("5. Structura testelor", heading_style))
    story.append(ListFlowable(
        [
            ListItem(Paragraph("tests/test_loan_evaluator_core.py - 15 teste de baza.", body_style)),
            ListItem(Paragraph("tests/test_loan_evaluator_additional.py - 2 teste suplimentare.", body_style)),
            ListItem(Paragraph("tests/test_loan_evaluator_ai_generated.py - 16 teste generate de Claude.", body_style)),
            ListItem(Paragraph("tests/test_loan_evaluator_mutmut.py - 20 teste derivate din mutmut.", body_style)),
        ],
        bulletType="bullet",
    ))

    story.append(Paragraph("6. Rezultate", heading_style))
    story.append(ListFlowable(
        [
            ListItem(Paragraph("Total verificat prin unittest: 53 teste, toate OK.", body_style)),
            ListItem(Paragraph("Numerotarea grafului pentru evaluate_application este folosita pentru cursul 2.", body_style)),
            ListItem(Paragraph("Diagrama SVG din diagrams/flowchart_evaluate_application.svg a fost aliniata vizual.", body_style)),
        ],
        bulletType="bullet",
    ))

    story.append(Paragraph("7. Concluzie", heading_style))
    story.append(Paragraph(
        "Rezultatul final este o suita stabila, formala si mai puternica la regresii, completata de documentatie aliniata si de o prezentare coerenta.",
        body_style,
    ))

    story.append(Paragraph("8. Referinte", heading_style))
    story.append(ListFlowable(
        [
            ListItem(Paragraph("Python Software Foundation - unittest.", body_style)),
            ListItem(Paragraph("A. J. Offutt - Introduction to Software Testing.", body_style)),
            ListItem(Paragraph("ISTQB Foundation Level Syllabus - Test Design Techniques.", body_style)),
            ListItem(Paragraph("mutmut - mutation testing tool.", body_style)),
        ],
        bulletType="bullet",
    ))

    doc.build(story)


if __name__ == "__main__":
    build_pptx()
    build_pdf()
    print(f"Wrote {PPTX_PATH}")
    print(f"Wrote {PDF_PATH}")