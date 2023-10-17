import pandas as pd
import streamlit as st

courses = {'GNS111':2,'GNS112':2,'GNS114':1,'ABE263':3,'CHE241':3,'CVE253':3,'ELE201':3,'ELE275':1,'GNS211':2,
           'MEE217':2,'MEE235':2,'WEE283':2,'ABE206':2,'CHE242':3,'CHE264':3,'CVE254':3,'ELE202':3,
           'ELE276':2,'GNS212':2,'GSE202':2,'MEE218':2,'MEE272':2,'WEE284':2,'WEE222':6,'WEE341':3, 'CVE351':3,
           'CVE363':2,'CVE365':2,'WEE383':1,'GEM217':1,'GEM319':3,'GNS311':2,'GSE301':2,'MEE361':3,'ABE306':2,
           'ABE376':1,'CVE322':3,'CVE352':3,'CVE362':3,'CVE366':2,'CHM328':2,'WEE384':1,'MEE362':3,'ABE463':2,
           'CHM415':2,'CVE473':3,'WEE411':3,'WEE425':2,'WEE431':3,'WEE433':2,'WEE471':2,'WEE481':2,'WEE485':2,
           'ABE501':3,'ABE573':1,'WEE511':2,'WEE521':3,'WEE515':3,'WEE517':2,'WEE519':2,'WEE593':4,'BUL506':3,
           'WEE516':3,'WEE524':3,'WEE526':3,'WEE528':2,'WEE584':2,'WEE594':4}

grade_equ = {'A': 5, 'B': 4, 'C': 3, 'D': 2, 'E': 1, 'F': 0}   

def get_info(level):
    list_course, units = [], []
    if time == 'Session':
        if level == 100:
            for key,value in courses.items():
                if key[3] == '1':
                    list_course.append(key)
                    units.append(value)
        elif level == 200:
            for key,value in courses.items():
                if key[3] == '2' and 'gem' not in key[:3].lower():
                    list_course.append(key)
                    units.append(value)
        elif level == 300:
            for key,value in courses.items():
                if key[3] == '3' or 'gem' in key[:3].lower():
                    list_course.append(key)
                    units.append(value)
        elif level == 400:
            for key,value in courses.items():
                if key[3] == '4':
                    list_course.append(key)
                    units.append(value)
        else:
            for key,value in courses.items():
                if key[3] == '5':
                    list_course.append(key)
                    units.append(value)
    else:
        num_sem = st.sidebar.selectbox(f'First/Second Semester?', [1, 2])
        if level == 100:
            if num_sem == 1:
                for key,value in courses.items():
                    if ((key[3] == '1' ) & (int(key[5])%2 != 0)):
                        list_course.append(key)
                        units.append(value)
            else:
                for key,value in courses.items():
                    if ((key[3] == '1') & (int(key[5])%2 == 0)):
                        list_course.append(key)
                        units.append(value)
        elif level == 200:
            if num_sem == 1:
                for key,value in courses.items():
                    if ((key[3] == '2') & (int(key[5])%2 != 0) & ('gem' not in key[:3].lower())):
                        list_course.append(key)
                        units.append(value)
            else:
                for key,value in courses.items():
                    if ((key[3] == '2') & (int(key[5])%2 == 0) & ('gem' not in key[:3].lower())):
                        list_course.append(key)
                        units.append(value)
        elif level == 300:
            if num_sem == 1:
                for key,value in courses.items():
                    if ((key[3] == '3') & (int(key[5])%2 != 0)) or ('gem' in key[:3].lower()):
                        list_course.append(key)
                        units.append(value)
            else:
                for key,value in courses.items():
                    if ((key[3] == '3') & (int(key[5])%2 == 0)) or ('gem' in key[:3].lower()):
                        list_course.append(key)
                        units.append(value)
        elif level == 400:
            if num_sem == 1:
                for key,value in courses.items():
                    if ((key[3] == '4') & (int(key[5])%2 != 0)):
                        list_course.append(key)
                        units.append(value)
            else:
                for key,value in courses.items():
                    if ((key[3] == '4') & (int(key[5])%2 == 0)):
                        list_course.append(key)
                        units.append(value)
        else:
            if num_sem == 1:
                for key,value in courses.items():
                    if ((key[3] == '5') & (int(key[5])%2 != 0)):
                        list_course.append(key)
                        units.append(value)
            else:
                for key,value in courses.items():
                    if ((key[3] == '5') & (int(key[5])%2 == 0)):
                        list_course.append(key)
                        units.append(value)
    return list_course, units

def class_rank(value):
    if value >= 4.5:
        st.balloons()
        return st.markdown('***🔥🔥 Congratulation! You are in First Class 🚀🚀.***')
    elif 3.5 <= value < 4.5:
        st.balloons()
        return st.markdown('***Amazing!🎉🎉You are in Second Class Upper.***')
    elif 2.4 <= value < 3.5:
        return st.markdown("***You are in Second Class Lower. Sky isn't the limit, you can go above it 💪.***")
    elif 1.5 <= value < 2.4:
        return st.markdown("***You are in Third Class.***")
    elif 1.0 <= value < 1.5:
        return st.markdown("***You Pass.***")
    else:
        return st.markdown('***You Fail.***')


img_path = 'https://th.bing.com/th/id/OIP.rQJ9bzWPW3xCaS2wcx_DTgAAAA?pid=ImgDet&rs=1'
st.sidebar.image(img_path, use_column_width=False)
st.sidebar.title('WEE CGPA/GPA CALCULATOR')
st.sidebar.markdown('Customise Your Calculator: ')
calc_cgpa = st.sidebar.selectbox(f'GPA/CGPA?', 
                                 ['GPA', 'CGPA'])
level = st.sidebar.selectbox(f'Select Level', [100,200,300,400,500])
st.title('Select your grade for each course:')
if calc_cgpa == 'GPA':
    time = st.sidebar.selectbox(f'Per Semester/Session?', ['Semester', 'Session'])
    list_course, units = get_info(level)
    df = pd.DataFrame({'Courses':list_course, 'Units':units})
    
    grades, points = [], []
    for course in list_course:
        st.write(course)
        grade = st.selectbox(f'Grade', list(grade_equ.keys()), key=course)
        grades.append(grade)
        points.append(grade_equ[grade])
    
    df['Grades'], df['Grade Index'] = grades, points
    if st.button('Calculate GPA'):
        st.spinner()
        st.write('Your results:', df)
        df['Points'] = df['Units'] * df['Grade Index']
        total_unit = df['Units'].sum()
        user_total_point = df['Points'].sum()
        gpa = round((user_total_point / total_unit), 2)    
        supposed_total_point = 5 * total_unit
        
        st.write(f'Total Unit: {total_unit}')
        st.write(f'Total point: {user_total_point} out of {supposed_total_point}')
        st.write(f'GPA: {gpa}')
        class_rank(value = gpa)

else:
    list_course, units = [], []
    if level == 100:
        for key,value in courses.items():
            if int(key[3]) <= 1:
                list_course.append(key)
                units.append(value)
    
    elif level == 200:
        for key,value in courses.items():
            if ((int(key[3]) <= 2) & ('gem' not in key[:3].lower())):
                list_course.append(key)
                units.append(value)
        
    elif level == 300:
        for key,value in courses.items():
            if ((int(key[3]) <= 3) | ('gem' in key[:3].lower())):
                list_course.append(key)
                units.append(value)
 
    elif level == 400:
        for key,value in courses.items():
            if int(key[3]) <= 4:
                list_course.append(key)
                units.append(value)
     
    else:
        for key,value in courses.items():
            if int(key[3]) <= 5:
                list_course.append(key)
                units.append(value)
    
    df = pd.DataFrame({'Courses':list_course, 'Units':units})
    
    grades, points = [], []
    for course in list_course:
        st.write(course)
        grade = st.selectbox(f'Grade', list(grade_equ.keys()), key=course)
        grades.append(grade)
        points.append(grade_equ[grade])
    
    df['Grades'], df['Grade Index'] = grades, points
    if st.button('Calculate CGPA'):
        st.spinner()
        st.write('Your results:', df)
        df['Points'] = df['Units'] * df['Grade Index']
        total_unit = df['Units'].sum()
        user_total_point = df['Points'].sum()
        cgpa = round((user_total_point / total_unit), 2)
        supposed_total_point = 5 * total_unit
        
        st.write(f'Total Unit: {total_unit}')
        st.write(f'Total point: {user_total_point} out of {supposed_total_point}')
        st.write(f'CGPA: {cgpa}')
        class_rank(value = cgpa)