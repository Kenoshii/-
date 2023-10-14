# TODO Найдите количество книг, которое можно разместить на дискете
inf = 1.44
stran = 100
strok = 50
simv = 25
onesimv = 4
kniga1 = (simv * strok * stran * onesimv) / 1024**2 #объём книги в Мб
vsego = inf // kniga1
print("Количество книг, помещающихся на дискету:", round(vsego))
