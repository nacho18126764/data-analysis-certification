import pandas as pd

def analyze_data():
    # Cargar el archivo CSV
    df = pd.read_csv('census_data.csv')
    
    # 1. ¿Cuántas personas de cada raza están representadas en este set de datos?
    race_counts = df['race'].value_counts()
    print("Número de personas por raza:\n", race_counts)
    
    # 2. ¿Cuál es la edad promedio de los hombres?
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)
    print(f"Edad promedio de los hombres: {average_age_men} años")
    
    # 3. ¿Cuál es el porcentaje de personas que tienen un grado de licenciatura?
    bachelor_percentage = round((df[df['education'] == 'Bachelors'].shape[0] / df.shape[0]) * 100, 1)
    print(f"Porcentaje de personas con grado de licenciatura: {bachelor_percentage}%")
    
    # 4. ¿Qué porcentaje de personas con educación avanzada (Bachelors, Masters o Doctorate) generan más de 50k?
    advanced_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    advanced_education_high_salary_percentage = round((advanced_education[advanced_education['salary'] == '>50K'].shape[0] / advanced_education.shape[0]) * 100, 1)
    print(f"Porcentaje de personas con educación avanzada que ganan más de 50k: {advanced_education_high_salary_percentage}%")
    
    # 5. ¿Qué porcentaje de personas sin una educación avanzada generan más de 50k?
    non_advanced_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    non_advanced_education_high_salary_percentage = round((non_advanced_education[non_advanced_education['salary'] == '>50K'].shape[0] / non_advanced_education.shape[0]) * 100, 1)
    print(f"Porcentaje de personas sin educación avanzada que ganan más de 50k: {non_advanced_education_high_salary_percentage}%")
    
    # 6. ¿Cuál es el mínimo número de horas que una persona trabaja por semana?
    min_hours_per_week = df['hours-per-week'].min()
    print(f"El mínimo número de horas trabajadas por semana: {min_hours_per_week} horas")
    
    # 7. ¿Qué porcentaje de personas que trabajan el mínimo de horas por semana tienen un salario de más de 50k?
    min_hours_high_salary_percentage = round((df[df['hours-per-week'] == min_hours_per_week][df['salary'] == '>50K'].shape[0] / df[df['hours-per-week'] == min_hours_per_week].shape[0]) * 100, 1)
    print(f"Porcentaje de personas que trabajan el mínimo de horas por semana y ganan más de 50k: {min_hours_high_salary_percentage}%")
    
    # 8. ¿Qué país tiene el más alto porcentaje de personas que ganan >50k y cuál es ese porcentaje?
    country_salary_percentage = df.groupby('native-country').apply(lambda x: (x[x['salary'] == '>50K'].shape[0] / x.shape[0]) * 100)
    highest_salary_country = country_salary_percentage.idxmax()
    highest_salary_percentage = round(country_salary_percentage.max(), 1)
    print(f"El país con el mayor porcentaje de personas que ganan >50k es {highest_salary_country} con un {highest_salary_percentage}%")
    
    # 9. Identifica la ocupación más popular de aquellos que ganan >50k en India.
    india_high_salary = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    most_popular_occupation_india = india_high_salary['occupation'].mode()[0]
    print(f"La ocupación más popular de aquellos que ganan >50k en India es: {most_popular_occupation_india}")

# Llamar a la función de análisis de datos
analyze_data()
