import matplotlib.pyplot as plt


zawodnicy = ["Anna", "Bartek", "Celina", "Dawid", "Ewa"]
bieg_100m = [14.2, 13.5, 15.1, 13.8, 14.5]
skok_w_dal = [3.8, 4.2, 3.5, 4.5, 4.0]
podbicia_pilka = [22, 25, 20, 28, 24]
punktacja = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
bcopy= bieg_100m.copy()
bcopy.sort()
pierwsze =bieg_100m.index(bcopy[0])
drugie =bieg_100m.index(bcopy[1])
trzecie =bieg_100m.index(bcopy[2])

for i in range(0,5):
    punktacja[i][1] = punktacja[i][0]

punktacja[pierwsze][0] = punktacja[pierwsze][0] + 5
punktacja[drugie][0] = punktacja[drugie][0] + 3
punktacja[trzecie][0] = punktacja[trzecie][0] + 2

plt.subplots_adjust(wspace= 0.4, hspace=0.5)
plt.subplot(2,2,1)
plt.title("Wyniki biegu na 100 metrów")
plt.bar(zawodnicy,  bieg_100m, color="green")


plt.xlabel('zawodnik')
plt.ylabel('Czas')
plt.grid(True)
bcopy= skok_w_dal.copy()
bcopy.sort(reverse=True)
pierwsze =skok_w_dal.index(bcopy[0])
drugie =skok_w_dal.index(bcopy[1])
trzecie =skok_w_dal.index(bcopy[2])
bcopy.sort(reverse=True)
for i in range(0,5):
    punktacja[i][1] = punktacja[i][0]

punktacja[pierwsze][1] = punktacja[pierwsze][1] + 5
punktacja[drugie][1] = punktacja[drugie][1] + 3
punktacja[trzecie][1] = punktacja[trzecie][1] + 2

plt.subplot(2,2,2)
plt.title("Skok w dal")
plt.bar(zawodnicy,skok_w_dal,color="yellow")
plt.grid(True)

plt.ylabel('Odległość')
plt.xlabel('Zawodnik')
plt.subplot(2,2,3)
plt.grid(True)
plt.title("Podbijanie piłką")


plt.bar(zawodnicy,podbicia_pilka, color="red")
plt.ylabel('ilosc')
plt.ylabel('zawodnik')
bcopy= podbicia_pilka.copy()
bcopy.sort(reverse=True)
pierwsze =podbicia_pilka.index(bcopy[0])
drugie =podbicia_pilka.index(bcopy[1])
trzecie =podbicia_pilka.index(bcopy[2])

for i in range(0,5):
    punktacja[i][2] = punktacja[i][1]


plt.subplot(2,2,4)
plt.ylabel('Pozycja')
plt.xlabel('Konkurencja')

punktacja[pierwsze][2] = punktacja[pierwsze][2] + 5
punktacja[drugie][2] = punktacja[drugie][2] + 3
punktacja[trzecie][2] = punktacja[trzecie][2] + 2
for i in range(0,5):
    plt.plot([1,2,3], punktacja[i], label='Wypełnione')



plt.show()

