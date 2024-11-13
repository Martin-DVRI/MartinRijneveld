import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from scipy.optimize import fsolve

# Functie om de catenary-vergelijking te berekenen
def catenary(x, a, c):
    return a * np.cosh(x / a) + c

# Streamlit invoer voor de ophangpunten en trekkracht
#st.title("Hangende Kabel Berekening")
x1 = st.number_input("Geef ophangpunt links (x1):", value=0.0)
y1 = st.number_input("Geef ophangpunt links (y1):", value=8.0)
x2 = st.number_input("Geef ophangpunt rechts (x2):", value=50.0)
y2 = st.number_input("Geef ophangpunt rechts (y2):", value=8.0)
H = st.number_input("Geef de horizontale trekkracht (H) in Newton:", value=20000.0)
w = st.number_input("Geef het gewicht per eenheid lengte (w) in N/m:", value=100.0)

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
Lowest_point_place = round(np.argmin(y_values)*((x2-x1)/500),2)
st.write('the lowest point is at ', Lowest_point_place,'m with a heigth of ',Lowest_point,'m.')
