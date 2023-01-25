import streamlit
import requests
import json
        
def run():
    streamlit.title("Placement prediction")
    sl_no = streamlit.text_input("Serial Number")
    ssc_p = streamlit.text_input("SSC (10th) Percentage")
    hsc_p = streamlit.text_input("HSC (12th) percentage")
    degree_p = streamlit.text_input("Degree Percentage")
    etest_p = streamlit.text_input("employability test percentage (conducted by the college)")
    mba_p = streamlit.text_input("MBA percentage")
    gender = streamlit.selectbox("Gender", ['M', 'F'])
    ssc_b = streamlit.selectbox("SSC Board of Education", ['Central', 'Others'])
    hsc_b = streamlit.selectbox("HSC Board of Education", ['Central', 'Others'])
    hsc_s = streamlit.selectbox("Specialization in HSC", ['Commerce', 'Science', 'Arts'])
    degree_t = streamlit.selectbox("Under Graduation (Degree type)", ['Sci&Tech', 'Comm&Mgmt'])
    workex = streamlit.selectbox("Work Experience", ['Yes', 'No'])
    specialisation = streamlit.selectbox("Post Graduation(MBA)- Specialization", ['Mkt&HR', 'Mkt&Fin'])
    
    data = { 
        'sl_no': sl_no,
        'ssc_p': ssc_p,
        'hsc_p': hsc_p,
        'degree_p': degree_p,
        'etest_p': etest_p,
        'mba_p': mba_p,
        'gender': gender,
        'ssc_b': ssc_b,
        'hsc_b': hsc_b,
        'hsc_s': hsc_s,
        'degree_t': degree_t,
        'workex': workex,
        'specialisation': specialisation 
        }

    if streamlit.button("Predict"):

        response = requests.post('http://127.0.0.1:8000/predict', json=data)
        prediction =(response.text)[16:-3]

        streamlit.success(f"Placement prediction: {prediction}")



if __name__ == '__main__':
    run()