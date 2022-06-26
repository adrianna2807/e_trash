# jeżeli użytkownik wybiera datę i godzinę to filtrowana jest lista recyclerów, którzy są dostępni w danym terminie
#
# Dostępni w danym terminie to znaczy, że w danym przedziale czasowym ilość zamówień przypisanych do recyclera nie przekracza capacity
#
# recycler agregate count orders po tym będziemy filtrować -> count orders w danej godzinie
#
# Potem z tej listy recyclerów możemy zrobić random albo first i przekażemy go do order objects create