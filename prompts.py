def Form1040() : return "Form1040"
def Form1040SR() : return "Form1040SR"
def Form1040NR() : return "Form1040NR"
def Form1040X() : return "Form1040X"
def Schedule1() : return "Schedule1"
def ScheduleA() : return "ScheduleA"
def ScheduleB() : return "ScheduleB"
def ScheduleC() : return "ScheduleC"
def ScheduleD() : return "ScheduleD"
def ScheduleE() : return "ScheduleE"
def ScheduleSE() : return "ScheduleSE"

def FormW2() : return """
    Analyze the document or image, extract the data in the format given below. 
    For empty values use default value either empty string or 0.00 for numeric value. 
    Always keep data clean and formatted.
    {
        "form_title": "Form W-2",
        "form_desc": "Wage and Tax Statement",
        "tax_year": 2025,
        "employee_social_security_number": "",
        "employer_identification_number": "",
        "employer_details": "",
        "control_number": "",
        "employee_first_name": "",
        "employee_last_name": "",
        "employee_initial": "",
        "employee_suffix": "",
        "employee_address": "",
        "employee_zip_code": "",
        "omb_number": "",
        "wages_tips_compensation": 0.00,
        "federal_income_tax_withheld": 0.00,
        "social_security_wages": 0.00,
        "social_security_tax_withheld": 0.00,
        "medicare_wages_tips": 0.00,
        "medicare_tax_withheld": 0.00,
        "social_security_tips": 0.00,
        "allocated_tips": 0.00,
        "dependent_care_benefits": 0.00,
        "nonqualified_plans": 0.00,
        "box12a": 0.00,
        "box12b": 0.00,
        "box12c": 0.00,
        "box12d": 0.00,
        "box13": {
            "Statutory Employee": false,
            "Retirement Plan": false,
            "Third-party Sick Pay": false
        },
        "others": "",
        "state_code": "VA",
        "employer_state_id_number": "",
        "state_wages_tips_etc": 0.00,
        "state_income_tax": 0.00,
        "local_wages_tips": 0.00,
        "local_income_tax": 0.00,
        "locality_name": ""
    }
    """

def FormW4() : return "FormW4"
def FormW9() : return "FormW9"
def Form1099NEC() : return "Form1099NEC"
def Form1099INT() : return "Form1099INT"
def Form1099DIV() : return "Form1099DIV"
def Form1099R() : return "Form1099R"
def Form1098() : return "Form1098"
def Form1098T() : return "Form1098T"
def Form1095A() : return "Form1095A"
def Form8962() : return "Form8962"
def Form2441() : return "Form2441"