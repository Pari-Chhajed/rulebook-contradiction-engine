import json
import os
from fpdf import FPDF

os.makedirs("data", exist_ok=True)
os.makedirs("eval", exist_ok=True)

# 1. Academic Regulations Markdown
academic_md = """# Institute of Technology & Science - Academic Ordinances

## Section 1: Degree Requirements and Credits
1.1 An undergraduate student must complete a minimum of 160 credits to be eligible for the award of a B.Tech degree.
1.2 The maximum duration permitted to complete the degree requirements is 6 consecutive academic years from initial enrollment.
1.3 Grade Point Average (GPA) is computed on a 10.0 scale. A minimum Cumulative Grade Point Average (CGPA) of 5.0 is required for graduation.
1.4 A student may register for a maximum of 26 credits in a regular semester, provided their previous SGPA is at least 7.5.
1.5 Audit courses do not carry academic credits and are graded on a Satisfactory/Unsatisfactory basis.

## Section 2: Attendance and Course Registration
2.1 Course registration must be completed within the first 5 working days of each semester. Late registration carries a fine of $50 per day up to day 10.
2.2 **Attendance Requirement (Clause 2.2):** A student must maintain a strict minimum attendance of 75% in every registered theory and lab course to be eligible to appear for the End-Semester Examination.
2.3 Any student falling below 75% attendance will receive an automatic 'FA' (Failed due to Attendance) grade and must repeat the course in a subsequent semester.
2.4 No instructor or department head is permitted to condone attendance shortages below 75% on academic or extracurricular grounds.

## Section 3: Grading, Supplementary Exams, and Re-evaluation
3.1 Mid-semester examinations carry 30% weightage, continuous assessments 20%, and End-Semester examinations 50%.
3.2 A student receiving an 'F' grade is eligible for one supplementary examination held during the summer term.
3.3 Supplementary examination grades shall be capped at a maximum of 'B' grade (7.0 equivalent on the GPA scale).
3.4 Re-evaluation requests must be submitted within 14 calendar days of result declaration accompanied by a non-refundable fee of $25 per course.
3.5 If a student misses a mid-term exam due to authorized official representation, a makeup test must be arranged within 10 days.

## Section 4: Academic Integrity and Plagiarism
4.1 Plagiarism exceeding 15% similarity index on final-year theses results in immediate thesis rejection and a mandatory 6-month extension.
4.2 Minor cheating offenses in mid-term tests result in zero marks for that specific test and a written warning.
4.3 Second-time integrity violations are referred to the Academic Disciplinary Committee for suspension consideration.

## Section 5: Course Drops and Program Withdrawals
5.1 A student may drop an elective course up to the 4th week of the semester without penalty or transcript notation.
5.2 Course withdrawals requested between week 5 and week 8 require formal Dean approval and will appear as 'W' on the permanent transcript.
5.3 Semester drop on medical grounds requires a verified certificate from the Chief Medical Officer within 14 days of incident.
"""

with open("data/academic_regulations.md", "w", encoding="utf-8") as f:
    f.write(academic_md)

# 2. Fee and Scholarship Schedule Markdown
fee_md = """# Schedule of Fees, Refunds, and Merit Scholarships

## Section 1: Tuition and Deadline Schedule
| Program | Semester Fee (USD) | Regular Deadline | Late Deadline (+Late Fee) |
|---|---|---|---|
| Undergraduate B.Tech | $4,500 | August 10 | August 25 ($150 late fee) |
| Postgraduate M.Tech | $3,800 | August 10 | August 25 ($150 late fee) |
| Doctoral Ph.D. | $1,200 | September 01 | September 15 ($50 late fee) |

## Section 2: Refund Policy
2.1 Withdrawal requested before orientation date: 100% tuition refund minus a $100 administrative processing charge.
2.2 Withdrawal within 15 calendar days of class commencement: 80% tuition refund.
2.3 Withdrawal after 30 calendar days of class commencement: No refund under any circumstances.

## Section 3: Merit Scholarships & Fee Waivers
3.1 Top 5% academic performers of each department receive a 50% tuition waiver for the subsequent semester.
3.2 **Fee Concession Committee Powers (Clause 3.2):** The Dean of Academic Affairs has discretionary authority to completely waive end-semester examination fees for any student experiencing documented family hardship.
3.3 Sibling discounts of 10% are applied to the second enrolled child from the same immediate household.
"""

with open("data/fee_and_scholarship_schedule.md", "w", encoding="utf-8") as f:
    f.write(fee_md)

# 3. PDF Generation (Updated for modern fpdf2)
pdf = FPDF()
pdf.add_page()
pdf.set_font("Helvetica", size=12)
pdf.cell(w=pdf.epw, h=10, text="Student Welfare, Medical, and Hostel Regulations", align="C", new_x="LMARGIN", new_y="NEXT")
pdf.ln(5)

pdf.set_font("Helvetica", size=10)

pdf_paragraphs = [
    "Section 10: Medical Exemption and Attendance Rules",
    "10.1 (PLANTED CONTRADICTION 1): Any student with certified medical hospitalization spanning more than 7 days is granted a mandatory attendance relaxation, permitting examination eligibility at 60% cumulative attendance.",
    "Section 11: Hostel Curfew and Late Entry",
    "11.1 All resident hostel students must swipe their biometric smart cards at the entrance before 10:00 PM on weekdays.",
    "11.2 (PLANTED CONTRADICTION 2): First-year undergraduate hostel residents have an unrestricted 24/7 library movement pass, allowing campus hostel entry at any hour without logging fines.",
    "Section 12: Examination Fee Exemption",
    "12.1 (PLANTED CONTRADICTION 3): All examination fees are non-waivable and must be paid in full by all enrolled candidates without exception. No officer of the university is authorized to grant fee waivers on examination testing."
]

for p in pdf_paragraphs:
    pdf.multi_cell(w=pdf.epw, h=8, text=p)
    pdf.ln(3)

pdf.output("data/hostel_and_medical_policy.pdf")

# 4. Planted Contradictions Log
contradictions_md = """# Planted Contradictions Log

### Contradiction 1: Minimum Attendance for Exam Eligibility
- **Source A:** `data/academic_regulations.md` -> Section 2, Clause 2.2 (Strict 75% mandatory, no exceptions, below 75% receives FA grade).
- **Source B:** `data/hostel_and_medical_policy.pdf` -> Section 10, Clause 10.1 (Hospitalization grants relaxation down to 60% attendance eligibility).

### Contradiction 2: First-Year Hostel Curfew Rules
- **Source A:** `data/hostel_and_medical_policy.pdf` -> Section 11, Clause 11.1 (Mandatory 10:00 PM smart card curfew for all resident hostel students).
- **Source B:** `data/hostel_and_medical_policy.pdf` -> Section 11, Clause 11.2 (First-year residents hold unrestricted 24/7 library movement passes).

### Contradiction 3: Authority to Waive Examination Fees
- **Source A:** `data/fee_and_scholarship_schedule.md` -> Section 3, Clause 3.2 (Dean of Academic Affairs can waive exam fees for hardship).
- **Source B:** `data/hostel_and_medical_policy.pdf` -> Section 12, Clause 12.1 (Examination fees are strictly non-waivable with zero administrative discretion).
"""

with open("eval/contradictions.md", "w", encoding="utf-8") as f:
    f.write(contradictions_md)

# 5. Test cases for eval
test_cases = [
    # 3 Contradictions
    {"id": "C1", "q": "What is the minimum attendance required to sit for exams if I was hospitalized?", "expected_state": "CONTRADICTION"},
    {"id": "C2", "q": "Can a first-year student enter the hostel after 10 PM with a library pass?", "expected_state": "CONTRADICTION"},
    {"id": "C3", "q": "Can the Dean waive my end-semester examination fee?", "expected_state": "CONTRADICTION"},
    
    # 5 Answerable Questions
    {"id": "A1", "q": "What is the fee for submitting a re-evaluation request?", "expected_state": "ANSWER"},
    {"id": "A2", "q": "What is the maximum duration allowed to complete a B.Tech degree?", "expected_state": "ANSWER"},
    {"id": "A3", "q": "What is the late registration fine per day after the first 5 days?", "expected_state": "ANSWER"},
    {"id": "A4", "q": "What happens if my final year thesis has 20% plagiarism?", "expected_state": "ANSWER"},
    {"id": "A5", "q": "What percentage refund do I get if I withdraw within 15 days of class commencement?", "expected_state": "ANSWER"},
    
    # 25 Hard Near-Misses (Document is silent -> Must REFUSE)
    {"id": "R01", "q": "Can I miss an exam because of my sister's wedding?", "expected_state": "REFUSAL"},
    {"id": "R02", "q": "Is electric kettle permitted inside the hostel room?", "expected_state": "REFUSAL"},
    {"id": "R03", "q": "What is the stipend provided for undergraduate teaching assistants?", "expected_state": "REFUSAL"},
    {"id": "R04", "q": "How many days of paternity leave can a postgraduate scholar take?", "expected_state": "REFUSAL"},
    {"id": "R05", "q": "Can I bring my pet dog to the campus grounds?", "expected_state": "REFUSAL"},
    {"id": "R06", "q": "What is the policy for converting a minor degree into an honors degree?", "expected_state": "REFUSAL"},
    {"id": "R07", "q": "Are students allowed to park four-wheeler cars in the campus parking lot?", "expected_state": "REFUSAL"},
    {"id": "R08", "q": "Is there a grace period for returning library books during summer break?", "expected_state": "REFUSAL"},
    {"id": "R09", "q": "How much fine is charged for losing the hostel smart card?", "expected_state": "REFUSAL"},
    {"id": "R10", "q": "Can two students from different branches swap their elective courses?", "expected_state": "REFUSAL"},
    {"id": "R11", "q": "What is the dress code required for the annual convocation ceremony?", "expected_state": "REFUSAL"},
    {"id": "R12", "q": "Does the university provide medical health insurance coverage for dental treatments?", "expected_state": "REFUSAL"},
    {"id": "R13", "q": "Are vegan meal options guaranteed during weekend dinners in the mess?", "expected_state": "REFUSAL"},
    {"id": "R14", "q": "How many attempts are permitted for clearing the campus sports proficiency test?", "expected_state": "REFUSAL"},
    {"id": "R15", "q": "Can an undergraduate student take a gap year to work at a venture-backed startup?", "expected_state": "REFUSAL"},
    {"id": "R16", "q": "What is the procedure to book the campus indoor badminton court for late night?", "expected_state": "REFUSAL"},
    {"id": "R17", "q": "Is there financial assistance available for publishing research papers in IEEE journals?", "expected_state": "REFUSAL"},
    {"id": "R18", "q": "Can a student audit a course without registering on the academic portal?", "expected_state": "REFUSAL"},
    {"id": "R19", "q": "What is the penalty for using loud speakers in the hostel common room after 8 PM?", "expected_state": "REFUSAL"},
    {"id": "R20", "q": "Does the tuition fee include subscription to online cloud platforms like AWS?", "expected_state": "REFUSAL"},
    {"id": "R21", "q": "What is the maximum number of times a student can change their hostel room?", "expected_state": "REFUSAL"},
    {"id": "R22", "q": "Can alumni retain access to the university gym facilities after graduating?", "expected_state": "REFUSAL"},
    {"id": "R23", "q": "Is there a fee reduction if a student completes the degree in 3.5 years?", "expected_state": "REFUSAL"},
    {"id": "R24", "q": "What are the rules regarding cooking induction plates inside hostel rooms?", "expected_state": "REFUSAL"},
    {"id": "R25", "q": "How many days in advance must a guest room in the visitor lodge be reserved?", "expected_state": "REFUSAL"}
]

with open("eval/test_cases.json", "w", encoding="utf-8") as f:
    json.dump(test_cases, f, indent=2)

print("Corpus, planted contradictions, and test suite generated successfully.")