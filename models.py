from enum import Enum
from pydantic import BaseModel

class PromptEnum(str, Enum):
    Form1040 = "Form1040"
    Form1040SR = "Form1040SR"
    Form1040NR = "Form1040NR"
    Form1040X = "Form1040X"
    Schedule1 = "Schedule1"
    ScheduleA = "ScheduleA"
    ScheduleB = "ScheduleB"
    ScheduleC = "ScheduleC"
    ScheduleD = "ScheduleD"
    ScheduleE = "ScheduleE"
    ScheduleSE = "ScheduleSE"
    FormW2 = "FormW2"
    FormW4 = "FormW4"
    FormW9 = "FormW9"
    Form1099NEC = "Form1099NEC"
    Form1099INT = "Form1099INT"
    Form1099DIV = "Form1099DIV"
    Form1099R = "Form1099R"
    Form1098 = "Form1098"
    Form1098T = "Form1098T"
    Form1095A = "Form1095A"
    Form8962 = "Form8962"
    Form2441 = "Form2441"

class TaxForm(BaseModel):
    pdf_url: str

