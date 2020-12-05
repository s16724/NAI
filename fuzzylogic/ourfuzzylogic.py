# Autorzy : Dominika Stryjewska , Jan Rygulski

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

''' 
Program ma za zadanie ocenić składkę OC w skali 
100 - stopniowej na podstawie trzech podanych cech, które
uzależniaja znacząco wysokość składki. Im wyższa 
skala tym lepsza oferta składki OC. Zakresy wieku, doświadczenia, 
ilość mieszkańców zaciągneliśmy z publikacji motoryzacjnych, które starały się wyjaśnic zależności,
które wykorzystujemy, a składką OC
 
 '''

'''
Użytkownik na samym początku podaję swoje dane jak wiek, 
długość czas posiadanego prawa jazdy i ilość mieszkańców 
, w którym żyje.
'''
age_val = int(input("Podaj swój wiek  : "))
experience_val = int(input("Ile lat posiadasz swoje prawo jazdy? : "))
city_populacion_val = int(input("Podaj ilość mieszkańców twojego miasta : "))

'''
Określenie danych wejściowych i wyjściowych wygląda  następująco:
- wiek w zakresię od 18 do 56 lat. Powyżej tego zakresu składka je staję się niezmiennia 
- czas posiadania prawa jazdy, który mieści się w zakresie do 31 lat   
- (wyjście) skala od 0 do 100. Im możliwie korzystne ubecpieczenie tym blizej 100 .
'''

# definiujemy membership funcions zaczynając od danyczah wejściowych i kończąc na wyjściowych
age = ctrl.Antecedent(np.arange(18, 56, 1), 'age')
experience = ctrl.Antecedent(np.arange(0, 31, 1), 'experience')
city_populacion = ctrl.Antecedent(np.arange(0, 500001, 1), 'city_populacion')
indicator = ctrl.Consequent(np.arange(0, 101, 1), 'indicator')

# definiujemy kształt naszych funkcji wejściowych. Dzielimy  wiek na :
# young, adult, old
age['young'] = fuzz.trimf(age.universe, [18, 25, 35])
age['adult'] = fuzz.trimf(age.universe, [25, 35, 45])
age['old'] = fuzz.trimf(age.universe, [35, 45, 55])

experience['beginner'] = fuzz.trimf(experience.universe, [0, 0, 15])
experience['intermediate'] = fuzz.trimf(experience.universe, [0, 15, 30])
experience['advanced'] = fuzz.trimf(experience.universe, [15, 30, 30])

city_populacion['small'] = fuzz.trimf(city_populacion.universe, [0, 0, 20000])
city_populacion['medium'] = fuzz.trimf(city_populacion.universe, [0, 20000, 100000])
city_populacion['big'] = fuzz.trimf(city_populacion.universe, [20000, 100000, 500000])
city_populacion['very_big'] = fuzz.trimf(city_populacion.universe, [100000, 500000, 500000])

indicator['low'] = fuzz.trimf(indicator.universe, [0, 25, 50])
indicator['medium'] = fuzz.trimf(indicator.universe, [25, 50, 75])
indicator['high'] = fuzz.trimf(indicator.universe, [50, 75, 100])

# Określenie reguł:
# 1 Jeśli młody wiek lub początkujący (doświadczenie) lub duże miasto to skala na poziomie "niski"
# 2 Jeśli stary albo doświadczenie zaawansowane lub małe miasto to skala na poziomie "wysoki"
# 3 Jeśli dorosły albo doświadczenie średnie to skala na poziomie "średni"
# 4 Jeśli stary lub doświadczenie początkujące to skala na poziomie "średni"
rule1 = ctrl.Rule(age['young'] | experience['beginner'] | city_populacion['very_big'], indicator['low'])
rule2 = ctrl.Rule(age['old'] | experience['advanced'] | city_populacion['small'], indicator['high'])
rule3 = ctrl.Rule(age['adult'] & experience['intermediate'], indicator['medium'])
rule4 = ctrl.Rule(age['old'] & experience['beginner'], indicator['medium'])

# Agregacja reguł
tipping_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4])

tipping = ctrl.ControlSystemSimulation(tipping_ctrl)

# Liczymy nową wartość określoną dla poszczególnych parametrów
tipping.input['age'] = age_val
tipping.input['experience'] = experience_val
tipping.input['city_populacion'] = city_populacion_val

tipping.compute()

# Wyświetlamy wynik
print("po podanych kryteriach skladka OC jest na " + str(
    int(tipping.output['indicator'])) + " poziomie w skali stustopniowej")
