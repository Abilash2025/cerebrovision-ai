
from pydantic import BaseModel


class PDFRequest(
    BaseModel
):
    prediction : str
    confidence : float
    report_sections : dict
    original_mri_path : str
    gradcam_local_path : str
    
    