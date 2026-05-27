import pandas as pd
import matplotlib.pyplot as plt

# Wczytanie danych

df = pd.read_csv('gym_members_exercise_tracking.csv')

# --- WIZUALIZACJA 1: Rozkład klas ---

experience_counts = df['Experience_Level'].value_counts().sort_index()
plt.figure()
plt.bar(experience_counts.index.astype(str), experience_counts.values, color='skyblue', edgecolor='black')
plt.title('Rozkład poziomu doświadczenia')
plt.xlabel('Poziom doświadczenia')
plt.ylabel('Liczba osób')
plt.tight_layout()
plt.show()

# --- WIZUALIZACJA 2: Macierz korelacji ---

plt.figure(figsize=(10, 8))
numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
corr = df[numeric_cols].corr()
plt.imshow(corr, cmap='coolwarm')
plt.colorbar()
plt.xticks(range(len(corr.columns)), corr.columns, rotation=90)
plt.yticks(range(len(corr.columns)), corr.columns)
plt.title('Macierz korelacji', pad=20)
plt.tight_layout()
plt.show()

# --- WIZUALIZACJA 3: Zależność czasu i kalorii, do średniego tętna ---

plt.figure()
scatter = plt.scatter(df['Session_Duration (hours)'], df['Calories_Burned'], c=df['Avg_BPM'], cmap='plasma', edgecolor='k')
plt.title('Zależność spalonych kalorii od czasu sesji')
plt.xlabel('Czas trwania sesji (godziny)')
plt.ylabel('Spalone kalorie')
plt.colorbar(scatter, label='Średnie tętno (BPM)')
plt.tight_layout()
plt.show()

# --- WIZUALIZACJA 4: Wykrywanie wartości odstających ---

df.boxplot(column='Age', by='Workout_Type', figsize=(10, 6))
plt.title('Rozkład wieku a typ treningu')
plt.suptitle('')
plt.xlabel('Typ treningu')
plt.ylabel('Wiek')
plt.tight_layout()
plt.show()

# --- WIZUALIZACJA 5: Rozkład procentu tkanki tłuszczowej ---

plt.figure()
plt.hist(df['Fat_Percentage'], bins=20, color='coral', edgecolor='black')
plt.title('Rozkład procentu tkanki tłuszczowej')
plt.xlabel('Procent tkanki tłuszczowej (%)')
plt.ylabel('Liczba osób')
plt.axvline(df['Fat_Percentage'].mean(), color='red', label='Średnia')
plt.legend()
plt.tight_layout()
plt.show()