import lightning as L
import lightning.app.frontend as frontend
import streamlit as st
import requests

def your_streamlit_app(lightning_app_state):
    encounter_id = st.number_input('encounter_id')
    patient_nbr = st.number_input('patient_nbr')
    race_Caucasian = st.number_input('race_Caucasian')
    race_AfricanAmerican = st.number_input('race_AfricanAmerican')
    race_ = st.number_input('race_')
    race_Other = st.number_input('race_Other')
    race_Hispanic = st.number_input('race_Hispanic')
    race_Asian = st.number_input('race_Asian')
    gender = st.number_input('gender')
    age_50 = st.number_input('age_50')
    age_70 = st.number_input('age_70')
    age_80 = st.number_input('age_80')
    age_40 = st.number_input('age_40')
    age_60 = st.number_input('age_60')
    age_30 = st.number_input('age_30')
    age_90 = st.number_input('age_90')
    age_10 = st.number_input('age_10')
    age_20 = st.number_input('age_20')
    age_0 = st.number_input('age_0')
    weight_ = Fi = st.number_input('weight_')
    weight_75 = st.number_input('weight_75')
    weight_100 = st.number_input('weight_100')
    weight_50 = st.number_input('weight_50')
    weight_150 = st.number_input('weight_150')
    weight_125 = st.number_input('weight_125')
    weight_25 = st.number_input('weight_25')
    weight_0 = st.number_input('weight_0')
    weight_175 = st.number_input('weight_175')
    admission_type_id = st.number_input('admission_type_id')
    discharge_dispositi = st.number_input('discharge_dispositi')
    admission_source_id = st.number_input('admission_source_id')
    time_in_hospital = st.number_input('time_in_hospital')
    payer_code_ = st.number_input('payer_code_')
    payer_code_MC = st.number_input('payer_code_MC')
    payer_code_CM = st.number_input('payer_code_CM')
    payer_code_WC = st.number_input('payer_code_WC')
    payer_code_MD = st.number_input('payer_code_MD')
    payer_code_DM = st.number_input('payer_code_DM')
    payer_code_HM = st.number_input('payer_code_HM')
    payer_code_CP = st.number_input('payer_code_CP')
    payer_code_BC = st.number_input('payer_code_BC')
    payer_code_SP = st.number_input('payer_code_SP')
    payer_code_UN = st.number_input('payer_code_UN')
    payer_code_OG = st.number_input('payer_code_OG')
    payer_code_PO = st.number_input('payer_code_PO')
    payer_code_OT = st.number_input('payer_code_OT')
    payer_code_SI = st.number_input('payer_code_SI')
    payer_code_MP = st.number_input('payer_code_MP')
    payer_code_CH = st.number_input('payer_code_CH')
    medical_specialty = st.number_input('medical_specialty')
    num_lab_procedures = st.number_input('num_lab_procedures')
    num_procedures = st.number_input('num_procedures')
    num_medications = st.number_input('num_medications')
    number_outpatient = st.number_input('number_outpatient')
    number_emergency = st.number_input('number_emergency')
    number_inpatient = st.number_input('number_inpatient')
    diag_1 = st.number_input('diag_1')
    diag_2 = st.number_input('diag_2')
    diag_3 = st.number_input('diag_3')
    number_diagnoses  = st.number_input('number_diagnoses')
    max_glu_serum_None = st.number_input('max_glu_serum_None')
    max_glu_serum_Norm = st.number_input('max_glu_serum_Norm')
    max_glu_serum_300 = st.number_input('max_glu_serum_300')
    max_glu_serum_200 = st.number_input('max_glu_serum_200')
    A1Cresult_None  = st.number_input('A1Cresult_None')
    A1Cresult_7  = st.number_input('A1Cresult_7')
    A1Cresult_8  = st.number_input('A1Cresult_8')
    A1Cresult_Norm  = st.number_input('A1Cresult_Norm')
    metformin_No = st.number_input('metformin_No')
    metformin_Steady  = st.number_input('metformin_Steady')
    metformin_Down = st.number_input('metformin_Down')
    metformin_Up = st.number_input('metformin_Up')
    repaglinide_No = st.number_input('repaglinide_No')
    repaglinide_Steady = st.number_input('repaglinide_Steady')
    repaglinide_Up = st.number_input('repaglinide_Up')
    repaglinide_Down  = st.number_input('repaglinide_Down')
    nateglinide_No = st.number_input('nateglinide_No')
    nateglinide_Steady = st.number_input('nateglinide_Steady')
    nateglinide_Up = st.number_input('nateglinide_Up')
    chlorpropamide_No = st.number_input('chlorpropamide_No')
    chlorpropamide_Up = st.number_input('chlorpropamide_Up')
    chlorpropamide_Stea = st.number_input('chlorpropamide_Stea')
    glimepiride_No  = st.number_input('glimepiride_No')
    glimepiride_Steady = st.number_input('glimepiride_Steady')
    glimepiride_Up  = st.number_input('glimepiride_Up')
    glimepiride_Down  = st.number_input('glimepiride_Down')
    acetohexamide_No  = st.number_input('acetohexamide_No')
    glipizide_No = st.number_input('glipizide_No')
    glipizide_Steady  = st.number_input('glipizide_Steady')
    glipizide_Up = st.number_input('glipizide_Up')
    glipizide_Down  = st.number_input('glipizide_Down')
    glyburide_No = st.number_input('glyburide_No')
    glyburide_Up = st.number_input('glyburide_Up')
    glyburide_Steady  = st.number_input('glyburide_Steady')
    glyburide_Down  = st.number_input('glyburide_Down')
    tolbutamide  = st.number_input('tolbutamide')
    pioglitazone_No  = st.number_input('pioglitazone_No')
    pioglitazone_Steady = st.number_input('pioglitazone_Steady')
    pioglitazone_Up  = st.number_input('pioglitazone_Up')
    pioglitazone_Down = st.number_input('pioglitazone_Down')
    rosiglitazone_No  = st.number_input('rosiglitazone_No')
    rosiglitazone_Stead = st.number_input('rosiglitazone_Stead')
    rosiglitazone_Up  = st.number_input('rosiglitazone_Up')
    rosiglitazone_Down = st.number_input('rosiglitazone_Down')
    acarbose_No  = st.number_input('acarbose_No')
    acarbose_Steady  = st.number_input('acarbose_Steady')
    acarbose_Up  = st.number_input('acarbose_Up')
    miglitol  = st.number_input('miglitol')
    troglitazone_No  = st.number_input('troglitazone_No')
    tolazamide = st.number_input('tolazamide')
    examide_No = st.number_input('examide_No')
    citoglipton_No  = st.number_input('citoglipton_No')
    insulin_Steady  = st.number_input('insulin_Steady')
    insulin_No = st.number_input('insulin_No')
    insulin_Up = st.number_input('insulin_Up')
    insulin_Down = st.number_input('insulin_Down')
    glyburide_metformin = st.number_input('glyburide_metformin')
    glipizide_metformin = st.number_input('glipizide_metformin')
    glimepiride_pioglit = st.number_input('glimepiride_pioglit')
    metformin_rosiglita = st.number_input('metformin_rosiglita')
    metformin_pioglitaz = st.number_input('metformin_pioglitaz')
    change = st.number_input('change')
    diabetesMed = st.number_input('diabetesMed')
    data = {
                            "encounter_id": encounter_id, 
                            "patient_nbr": patient_nbr,
                            "race_Caucasian": race_Caucasian,
                            "race_AfricanAmerican": race_AfricanAmerican,
                            "race_": race_,
                            "race_Other": race_Other,
                            "race_Hispanic": 0,
                            "race_Asian": 0,
                            "gender": 1,
                            "age_50-60)": 0,
                            "age_70-80)": 0,
                            "age_80-90)": 0,
                            "age_40-50)": 0,
                            "age_60-70)": 0,
                            "age_30-40)": 0,
                            "age_90-100)": 0,
                            "age_10-20)": 0,
                            "age_20-30)": 0,
                            "age_0-10)": 1,
                            "weight_?": 1,
                            "weight_75-100)": 0,
                            "weight_100-125)": 0,
                            "weight_50-75)": 0,
                            "weight_150-175)": 0,
                            "weight_125-150)": 0,
                            "weight_25-50)": 0,
                            "weight_0-25)": 0,
                            "weight_175-200)": 0,
                            "admission_type_id": 6,
                            "discharge_disposition_id": 25,
                            "admission_source_id": 1,
                            "time_in_hospital": 1,
                            "payer_code_?": 1,
                            "payer_code_MC": 0,
                            "payer_code_CM": 0,
                            "payer_code_WC": 0,
                            "payer_code_MD": 0,
                            "payer_code_DM": 0,
                            "payer_code_HM": 0,
                            "payer_code_CP": 0,
                            "payer_code_BC": 0,
                            "payer_code_SP": 0,
                            "payer_code_UN": 0,
                            "payer_code_OG": 0,
                            "payer_code_PO": 0,
                            "payer_code_OT": 0,
                            "payer_code_SI": 0,
                            "payer_code_MP": 0,
                            "payer_code_CH": 0,
                            "medical_specialty": 1,
                            "num_lab_procedures": 41,
                            "num_procedures": 0,
                            "num_medications": 1,
                            "number_outpatient": 0,
                            "number_emergency": 0,
                            "number_inpatient": 0,
                            "diag_1": 250.83,
                            "diag_2": 0,
                            "diag_3": 0,
                            "number_diagnoses": 1,
                            "max_glu_serum_None": 1,
                            "max_glu_serum_Norm": 0,
                            "max_glu_serum_>300": 0,
                            "max_glu_serum_>200": 0,
                            "A1Cresult_None": 1,
                            "A1Cresult_>7": 0,
                            "A1Cresult_>8": 0,
                            "A1Cresult_Norm": 0,
                            "metformin_No": 1,
                            "metformin_Steady": 0,
                            "metformin_Down": 0,
                            "metformin_Up": 0,
                            "repaglinide_No": 1,
                            "repaglinide_Steady": 0,
                            "repaglinide_Up": 0,
                            "repaglinide_Down": 0,
                            "nateglinide_No": 1,
                            "nateglinide_Steady": 0,
                            "nateglinide_Up": 0,
                            "chlorpropamide_No": 1,
                            "chlorpropamide_Up": 0,
                            "chlorpropamide_Steady": 0,
                            "glimepiride_No": 1,
                            "glimepiride_Steady": 0,
                            "glimepiride_Up": 0,
                            "glimepiride_Down": 0,
                            "acetohexamide_No": 1,
                            "glipizide_No": 1,
                            "glipizide_Steady": 0,
                            "glipizide_Up": 0,
                            "glipizide_Down": 0,
                            "glyburide_No": 1,
                            "glyburide_Up": 0,
                            "glyburide_Steady": 0,
                            "glyburide_Down": 0,
                            "tolbutamide": 1,
                            "pioglitazone_No": 1,
                            "pioglitazone_Steady": 0,
                            "pioglitazone_Up": 0,
                            "pioglitazone_Down": 0,
                            "rosiglitazone_No": 1,
                            "rosiglitazone_Steady": 0,
                            "rosiglitazone_Up": 0,
                            "rosiglitazone_Down": 0,
                            "acarbose_No": 1,
                            "acarbose_Steady": 0,
                            "acarbose_Up": 0,
                            "miglitol": 1,
                            "troglitazone_No": 1,
                            "tolazamide": 1,
                            "examide_No": 1,
                            "citoglipton_No": 1,
                            "insulin_Steady": 0,
                            "insulin_No": 1,
                            "insulin_Up": 0,
                            "insulin_Down": 0,
                            "glyburide-metformin": 1,
                            "glipizide-metformin_No": 1,
                            "glipizide-metformin_Steady": 0,
                            "glimepiride-pioglitazone_No": 1,
                            "metformin-rosiglitazone_No": 1,
                            "metformin-pioglitazone_No": 1,
                            "change": 1,
                            "diabetesMed": 1
                            }
    if st.button('Inferir'):
        url = 'http://10.43.102.109:8000/do_inference/'
        r = requests.post(url, json=data)
        st.write(r.text)



class LitStreamlit(L.LightningFlow):
    def configure_layout(self):
        return frontend.StreamlitFrontend(render_fn=your_streamlit_app)

class LitApp(L.LightningFlow):
    def __init__(self):
        super().__init__()
        self.lit_streamlit = LitStreamlit()

    def run(self):
        self.lit_streamlit.run()

    def configure_layout(self):
        tab1 = {"name": "home", "content": self.lit_streamlit}
        return tab1

app = L.LightningApp(LitApp())

