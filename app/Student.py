from pydantic import BaseModel


class Student(BaseModel):
    sl_no: int
    ssc_p: float
    hsc_p: float
    degree_p: float
    etest_p: float
    mba_p: float
    gender: str
    ssc_b: str
    hsc_b: str
    hsc_s: str
    degree_t: str
    workex: str
    specialisation: str