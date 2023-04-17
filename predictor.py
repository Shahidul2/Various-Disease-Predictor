import pickle
import streamlit as st
from streamlit_option_menu import option_menu

#loading the saved models
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))
breast_cancer_model = pickle.load(open('breast_cancer_model.sav', 'rb'))


#sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Various Health Condition Predictor',
                           
                           ['Diabetes Classifier',
                           'Heart Disease Classifier',
                           'Parkinsons Classifier',
                           'Breast Cancer Classifier'],
                           
                           default_index=0)
    
#Diabetes Classifier
if (selected == 'Diabetes Classifier'):
    
    #page title
    st.title('Diabetes Classification using ML')
    
    #columns for input fields
    col1, col2, col3 = st.columns(3)
    
    #getting input values from user
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose Level')
    with col3:
        BloodPressure = st.text_input('Blood Pressure Value')
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    with col2:
        Insulin = st.text_input('Insulin Level')
    with col3:
        BMI = st.text_input('BMI value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function Value')
    with col2:
        Age = st.text_input('Age of the person')
    
    #code for prediction
    diab_diagnosis = ''
    
    #creating a button for prediction
    if st.button('Diabetes Test Result'):
        diab_pred = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
    
        if diab_diagnosis[0] == 1:
            diab_diagnosis = 'The person is Diabetic'
        else:
            diab_diagnosis = 'The person is Not Diabetic'
            
    st.success(diab_diagnosis)
    
    
    
    
    

#Heart disease classifier
if (selected == 'Heart Disease Classifier'):
    
    #page title
    st.title('Heart Disease Classification using ML')
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')     
    with col2:
        sex = st.text_input('Sex')       
    with col3:
        cp = st.text_input('Chest Pain types')       
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')       
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')       
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')      
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')       
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')       
    with col3:
        exang = st.text_input('Exercise Induced Angina')        
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')        
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')        
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')      
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        

    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)
    
    
    
    

#Parkinsons classifier
if (selected == 'Parkinsons Classifier'):
    
    #page title
    st.title('Parkinsons Classification using ML')
    
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')       
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')       
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')       
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')       
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')       
    with col1:
        RAP = st.text_input('MDVP:RAP')    
    with col2:
        PPQ = st.text_input('MDVP:PPQ')     
    with col3:
        DDP = st.text_input('Jitter:DDP')     
    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')      
    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')      
    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')      
    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')     
    with col3:
        APQ = st.text_input('MDVP:APQ')     
    with col4:
        DDA = st.text_input('Shimmer:DDA')      
    with col5:
        NHR = st.text_input('NHR')     
    with col1:
        HNR = st.text_input('HNR')     
    with col2:
        RPDE = st.text_input('RPDE')    
    with col3:
        DFA = st.text_input('DFA')    
    with col4:
        spread1 = st.text_input('spread1')    
    with col5:
        spread2 = st.text_input('spread2')    
    with col1:
        D2 = st.text_input('D2')    
    with col2:
        PPE = st.text_input('PPE')
         
    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
        
        if (parkinsons_prediction[0] == 1):
          parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
          parkinsons_diagnosis = "The person does not have Parkinson's disease"
        
    st.success(parkinsons_diagnosis)
    

#Breast cancer classifier
if (selected == 'Breast Cancer Classifier'):
    
    #page title
    st.title('Breast Cancer Classification using ML')
    
    col1, col2, col3, col4, col5 = st.columns(5)
    
    #taking input from users
    with col1:
        MeanRadius = st.text_input('Mean Radius')
    with col2:
        MeanTexture = st.text_input('Mean Texture')
    with col3:
        MeanPerimeter = st.text_input('Mean Perimeter')
    with col4:
        MeanArea = st.text_input('Mean Area')
    with col5:
        MeanSmoothness = st.text_input('Mean Smoothness')
    with col1:
        MeanCompactness = st.text_input('Mean Compactness')
    with col2:
        MeanConcavity = st.text_input('Mean Concavity')
    with col3:
        MeanConcavepoints = st.text_input('Mean Concace Points')
    with col4:
        MeanSymmetry = st.text_input('Mean Symmetry')
    with col5:
        MeanFractaldimension = st.text_input('Mean Fractal Dimension')
    with col1:
        RadiusError = st.text_input('Radius Error')
    with col2:
        TextureError = st.text_input('Texture Error')
    with col3:
        PerimeterError = st.text_input('Perimeter Error')
    with col4:
        AreaError = st.text_input('Area Error')
    with col5:
        SmoothnessError = st.text_input('Smoothness Error')
    with col1:
        CompactnessError = st.text_input('Compactness Error')
    with col2:
        ConcavityError = st.text_input('Concavity Error')
    with col3: 
        ConcavepointsError = st.text_input('Concave Points Error')
    with col4:
        SymmetryError = st.text_input('Symmetry Error')
    with col5:
        FractaldimensionError = st.text_input('Fractal Dimension Error')
    with col1:
        WorstRadius = st.text_input('Worst Radius')
    with col2:
        WorstTexture = st.text_input('Worst Texture')
    with col3:
        WorstPerimeter = st.text_input('Worst Perimeter')
    with col4:
        WorstArea = st.text_input('Worst Area')
    with col5:
        WorstSmoothness = st.text_input('Worst Smoothness')
    with col1:
        WorstCompactness = st.text_input('Worst Compactness')
    with col2:
        WorstConcavity = st.text_input('Worst Concavity')
    with col3:
        WorstConcavepoints = st.text_input('Worst Concave points')
    with col4:
        WorstSymmetry = st.text_input('Worst Symmetry')
    with col5:
        WorstFractaldimension = st.text_input('Worst Fractal Dimension')
    
    # code for Prediction
    breast_cancer_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Breast Cancer Test Result"):
        breast_cancer_prediction = breast_cancer_model([[MeanRadius, MeanTexture, MeanPerimeter, MeanArea, MeanSmoothness, MeanCompactness, MeanConcavity, MeanConcavepoints, MeanSymmetry, MeanFractaldimension, RadiusError, TextureError, PerimeterError, AreaError, SmoothnessError, CompactnessError, ConcavityError, ConcavepointsError, SymmetryError, FractaldimensionError, WorstRadius, WorstTexture, WorstPerimeter, WorstArea, WorstSmoothness, WorstCompactness, WorstConcavity, WorstConcavepoints, WorstSymmetry, WorstFractaldimension]])
    
        if (breast_cancer_prediction[0] == 1):
          breast_cancer_diagnosis = "The person has Breast Cancer"
        else:
          breast_cancer_diagnosis = "The person does not have Breast Cancer"
    
    st.success(breast_cancer_diagnosis)