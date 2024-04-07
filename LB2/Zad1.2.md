rodzic(maria, anna).
rodzic(franek, anna).
rodzic(franek, jozef).
rodzic(alicja, marian).
rodzic(alicja, eleonora).
rodzic(dorota, franek).
rodzic(dorota, alicja).
rodzic(ola, marian).
rodzic(ola, felicja).
rodzic(dominik, ola).
rodzic(dominik, mirek).
rodzic(kasia, ola).
rodzic(arek, kasia).
rodzic(arek, mirek).

wnuk(X, Z) :- dziecko(X, Y), dziecko(Y, Z).

dziecko(X, Y) :- rodzic(Y, X).

rodzenstwo(X, Y) :- rodzic(X, A), rodzic(X, B), rodzic(Y, A), rodzic(Y, B).

kuzynostwo(X, Y) :- rodzic(X, A), rodzic(Y, B), rodzic(A, Z), rodzic(B, Z).

wspolny_wnuk(X, Y) :- dziecko(X, A), dziecko(Y, B), dziecko(A, WNUK), dziecko(B, WNUK).

ojczym_macocha(X, Y) :- dziecko(A, X), dziecko(A, B), rodzic(B, Y).

rodzenstwo_przyrodnie(X, Y) :- rodzic(X, WSPOLNY), rodzic(Y, WSPOLNY), rodzic(X, A), rodzic(Y, B), \+rodzenstwo(A, B). 

szwagier(X, Y) :- rodzic(DZIECKO, X), rodzic(DZIECKO, M), rodzenstwo(M, Y).

brat_wujek_jednoczesnie(X, Y) :- rodzic(X, A), rodzic(X, B), rodzenstwo(A, Y), rodzic(Y, B).
