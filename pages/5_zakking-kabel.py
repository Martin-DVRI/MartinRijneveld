import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from scipy.optimize import fsolve

# Functie om de catenary-vergelijking te berekenen
def catenary(x, a, c):
    return a * np.cosh(x / a) + c

# Streamlit invoer voor de ophangpunten en trekkracht
st.title("Catenary equation")

col1,col2,col3=st.columns([1,1,1])

with col1:
    y1 = st.number_input("Geef ophanghoogte links:", value=8.5)

with col2:
    x2 = st.number_input("Geef veldlengte:", value=50.0)

with col3:
    y2 = st.number_input("Geef ophanghoogte rechts:", value=8.5)

# Informatie in tekstvorm
st.write("""
De trekkracht en het gewicht van de kabel bepalen de zakking. Zie hieronder voor wat bekende waardes:
""")

# Bekende waardes in een tabel
data = [
    {'Type Kabel': 'Draagkabel 150 (10C)', 'Trekkracht (N)': 10800, 'Gewicht per eenheid lengte (N/m)': 13.12},
    {'Type Kabel': 'Draagkabel 150 (-20C)', 'Trekkracht (N)': 17300, 'Gewicht per eenheid lengte (N/m)': 13.12},
    {'Type Kabel': 'Draagkabel 70 (10C)', 'Trekkracht (N)': 9400, 'Gewicht per eenheid lengte (N/m)': 5.85},
    {'Type Kabel': 'Draagkabel 70 (-20C)', 'Trekkracht (N)': 12700, 'Gewicht per eenheid lengte (N/m)': 5.85},
    {'Type Kabel': 'Draagkabel 150 b1-net(10C)', 'Trekkracht (N)': 10800, 'Gewicht per eenheid lengte (N/m)': 30.56},
    {'Type Kabel': 'Draagkabel 70 b1-net(10C)', 'Trekkracht (N)': 9400, 'Gewicht per eenheid lengte (N/m)': 19.15},
    {'Type Kabel': 'VL(10C)', 'Trekkracht (N)': 6500, 'Gewicht per eenheid lengte (N/m)': 13.12},
    {'Type Kabel': 'VL(-20C)', 'Trekkracht (N)': 13500, 'Gewicht per eenheid lengte (N/m)': 13.12},
    {'Type Kabel': 'rijdraad 2x100(10C)', 'Trekkracht (N)': 20000, 'Gewicht per eenheid lengte (N/m)': 17.44}
]

# Tabel tonen
st.table(data)

col4,col5=st.columns([1,1])

with col4:
    H = st.number_input("Geef de horizontale trekkracht in Newton:", value=10800.0)

with col5:
    w = st.number_input("Geef het gewicht per eenheid lengte in N/m:", value=13.12)

x1 = 0.0


# Bereken de constante a
a = H / w

# Functie om de verschuiving x0 te berekenen
def find_x0(a, x1, y1, x2, y2):
    def equations(x0):
        return a * np.cosh((x1 - x0) / a) - y1, a * np.cosh((x2 - x0) / a) - y2
    x0_initial_guess = (x1 + x2) / 2
    x0_solution = fsolve(lambda x0: equations(x0)[0] - equations(x0)[1], x0_initial_guess)
    return x0_solution[0]

# Bereken x0
x0 = find_x0(a, x1, y1, x2, y2)

# Bereken de constante c
c = y1 - a * np.cosh((x1 - x0) / a)

# Bereken de y-waarden voor x-waarden tussen x1 en x2
x_values = np.linspace(x1, x2, 500)
y_values = catenary(x_values - x0, a, c)

# Plot de catenary
plt.figure(figsize=(10, 5))
plt.plot(x_values, y_values, label='Hangende kabel')
plt.scatter([x1, x2], [y1, y2], color='red', zorder=5)  # Ophangpunten
plt.title('Hangende kabel tussen twee punten')
plt.xlabel('Horizontale positie (m)')
plt.ylabel('Hoogte (m)')
plt.axhline(y=y1, color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.grid(True)
st.pyplot(plt)
#plt.show()

st.write('---')
#print(y_values)
Lowest_point = round(min(y_values),2)
Lowest_point_place = round((np.argmin(y_values)+1)*((x2-x1)/500),2)
st.write(f'Het laagste punt is op {Lowest_point_place}m met een hoogte van {Lowest_point}m.')

col6,col7=st.columns([1,2])
with col6:
    distance = st.number_input("Geef afstand gewenste hoogte [m]:", value=Lowest_point_place, step=0.5)
with col7:
    Xpoint=int(distance/x2*499)
    hoogte=y_values[Xpoint]
    st.write('de kabelhoogte op ingegeven afstand:')
    st.write(f"{hoogte:.3} m")
