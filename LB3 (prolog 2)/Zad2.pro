rodzic(julek, anna).
mezczyzna(julek).

kobieta(X) :- \+mezczyzna(X).

ojciec(X, Y) :- rodzic(Y, X), mezczyzna(X).
