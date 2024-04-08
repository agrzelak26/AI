osoba(anna).
osoba(jozef).
osoba(karolina).
osoba(ewa).
osoba(maciej).
osoba(ela).
osoba(pawel).
osoba(danuta).
osoba(robert).
osoba(piotr).
osoba(ola).
osoba(marek).
osoba(sylwia).
osoba(arek).
osoba(eryk).
mezczyzna(jozef).
mezczyzna(maciej).
mezczyzna(pawel).
mezczyzna(robert).
mezczyzna(piotr).
mezczyzna(marek).
mezczyzna(arek).
mezczyzna(eryk).

rodzic(marek, karolina).
rodzic(marek, jozef).
rodzic(sylwia, anna).
rodzic(sylwia, piotr).
rodzic(arek, anna).
rodzic(arek, piotr).
rodzic(eryk, piotr).
rodzic(eryk, ola).
rodzic(jozef, ewa).
rodzic(jozef, maciej).
rodzic(anna, ewa).
rodzic(anna, maciej).
rodzic(piotr, ela).
rodzic(piotr, pawel).
rodzic(pawel, danuta).
rodzic(pawel, robert).


kobieta(X) :- \+mezczyzna(X).

ojciec(X, Y) :- rodzic(Y, X), mezczyzna(X).

matka(X, Y) :- rodzic(Y, X), kobieta(X).

corka(X, Y) :- rodzic(X, Y), kobieta(X).

brat_rodzony(X, Y) :- matka(A, X), matka(A, Y), ojciec(B, X), ojciec(B, Y), mezczyzna(X).

brat_przyrodni(X, Y) :- ojciec(OX, X), ojciec(OY, Y), matka(MX, X), matka(MY, Y), (   (   MX = MY, OX \= OY);(   MX \= MY, OX = OY)).

kuzyn(X, Y) :- rodzic(X, A), rodzic(Y, B), rodzic(A, C), rodzic(B, C), mezczyzna(X).

dziadek_od_strony_ojca(X, Y) :- ojciec(A, Y), ojciec(X, A).
    
dziadek_od_strony_matki(X, Y) :- matka(A, Y), ojciec(X, A).
    
dziadek(X, Y) :- rodzic(Y, A), ojciec(X, A).
    
babcia(X, Y) :- rodzic(Y, A), matka(X, A).
    
wnuczka(X, Y) :- kobieta(Y), rodzic(Y, Z), rodzic(Z, X).
    
przodek_do2pokolenia_wstecz(X, Y) :- rodzic(Y, X); rodzic(Y, Z), rodzic(Z, X).
    
przodek_do3pokolenia_wstecz(X, Y) :- rodzic(Y, X); (  rodzic(Y, Z), rodzic(Z, X)); (   rodzic(Y, A), rodzic(A, B), rodzic(B, X)).
