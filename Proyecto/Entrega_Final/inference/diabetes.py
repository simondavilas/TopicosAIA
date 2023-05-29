from pydantic import BaseModel, Field
class Diabetes(BaseModel):
  encounter_id: float = 2278392
  patient_nbr: float = 8222157
  race_Caucasian: float = 1
  race_AfricanAmerican: float = 0
  race_: float = Field(alias="race_?", default=0)
  race_Other: float = 0
  race_Hispanic: float = 0
  race_Asian: float = 0
  gender: float = 1
  age_50: float = Field(alias="age_50-60)", default=0)
  age_70: float = Field(alias="age_70-80)", default=0)
  age_80: float = Field(alias="age_80-90)", default=0)
  age_40: float = Field(alias="age_40-50)", default=0)
  age_60: float = Field(alias="age_60-70)", default=0)
  age_30: float = Field(alias="age_30-40)", default=0)
  age_90: float = Field(alias="age_90-100)", default=0)
  age_10: float = Field(alias="age_10-20)", default=0)
  age_20: float = Field(alias="age_20-30)", default=0)
  age_0: float = Field(alias="age_0-10)", default=1)
  weight_: float = Field(alias="weight_?", default=1)
  weight_75: float = Field(alias="weight_75-100)", default=0)
  weight_100: float = Field(alias="weight_100-125)", default=0)
  weight_50: float = Field(alias="weight_50-75)", default=0)
  weight_150: float = Field(alias="weight_150-175)", default=0)
  weight_125: float = Field(alias="weight_125-150)", default=0)
  weight_25: float = Field(alias="weight_25-50)", default=0)
  weight_0: float = Field(alias="weight_0-25)", default=0)
  weight_175: float = Field(alias="weight_175-200)", default=0)
  admission_type_id: float = 6
  discharge_disposition_id: float = 25
  admission_source_id: float = 1
  time_in_hospital: float = 1
  payer_code_: float = Field(alias="payer_code_?", default=1)
  payer_code_MC: float = 0
  payer_code_CM: float = 0
  payer_code_WC: float = 0
  payer_code_MD: float = 0
  payer_code_DM: float = 0
  payer_code_HM: float = 0
  payer_code_CP: float = 0
  payer_code_BC: float = 0
  payer_code_SP: float = 0
  payer_code_UN: float = 0
  payer_code_OG: float = 0
  payer_code_PO: float = 0
  payer_code_OT: float = 0
  payer_code_SI: float = 0
  payer_code_MP: float = 0
  payer_code_CH: float = 0
  medical_specialty: float = 1
  num_lab_procedures: float = 41
  num_procedures: float = 0
  num_medications: float = 1
  number_outpatient: float = 0
  number_emergency: float = 0
  number_inpatient: float = 0
  diag_1: float = 250.83
  diag_2: float = 0
  diag_3: float = 0
  number_diagnoses: float = 1
  max_glu_serum_None: float = 1
  max_glu_serum_Norm: float = 0
  max_glu_serum_300: float = Field(alias="max_glu_serum_>300", default=0)
  max_glu_serum_200: float = Field(alias="max_glu_serum_>200", default=0)
  A1Cresult_None: float = 1
  A1Cresult_7: float = Field(alias="A1Cresult_>7", default=0)
  A1Cresult_8: float = Field(alias="A1Cresult_>8", default=0)
  A1Cresult_Norm: float = 0
  metformin_No: float = 1
  metformin_Steady: float = 0
  metformin_Down: float = 0
  metformin_Up: float = 0
  repaglinide_No: float  = 1
  repaglinide_Steady: float = 0
  repaglinide_Up: float = 0
  repaglinide_Down: float = 0
  nateglinide_No: float = 1
  nateglinide_Steady: float = 0
  nateglinide_Up: float = 0
  chlorpropamide_No: float = 1
  chlorpropamide_Up: float = 0
  chlorpropamide_Steady: float = 0
  glimepiride_No: float = 1
  glimepiride_Steady: float = 0
  glimepiride_Up: float = 0
  glimepiride_Down: float = 0
  acetohexamide_No: float = 1
  glipizide_No: float = 1
  glipizide_Steady: float = 0
  glipizide_Up: float = 0
  glipizide_Down: float = 0
  glyburide_No: float = 1
  glyburide_Up: float = 0
  glyburide_Steady: float = 0
  glyburide_Down: float = 0
  tolbutamide: float = 1
  pioglitazone_No: float = 1
  pioglitazone_Steady: float = 0
  pioglitazone_Up: float = 0
  pioglitazone_Down: float = 0
  rosiglitazone_No: float = 1
  rosiglitazone_Steady: float = 0
  rosiglitazone_Up: float = 0
  rosiglitazone_Down: float = 0
  acarbose_No: float = 1
  acarbose_Steady: float = 0
  acarbose_Up: float = 0
  miglitol: float = 1
  troglitazone_No: float = 1
  tolazamide: float = 1
  examide_No: float = 1
  citoglipton_No: float = 1
  insulin_Steady: float = 0  
  insulin_No: float = 1
  insulin_Up: float = 0
  insulin_Down: float = 0
  glyburide_metformin: float = Field(alias="glyburide-metformin", default=1)
  glipizide_metformin_No: float = Field(alias="glipizide-metformin_No", default=1)
  glipizide_metformin_Steady: float = Field(alias="glipizide-metformin_Steady", default=0)
  glimepiride_pioglitazone_No: float = Field(alias="glimepiride-pioglitazone_No", default=1)
  metformin_rosiglitazone_No: float = Field(alias="metformin-rosiglitazone_No", default=1)
  metformin_pioglitazone_No: float = Field(alias="metformin-pioglitazone_No", default=1)
  change: float = 1
  diabetesMed: float = 1