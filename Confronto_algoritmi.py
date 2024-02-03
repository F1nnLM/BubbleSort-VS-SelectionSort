import array_colf as ml 
import time
import timeit
import matplotlib.pyplot as plt

#Stampa su schermo dell grafico
def stampaGrafico(tempi_bs, tempi_ss):
    plt.plot(tempi_bs, label = "Bubble sort", color = "purple")
    plt.plot(tempi_ss, label = "Selection Sort", color = "orange")
    plt.title('Tempi di esecuzione di Bubble Sort e Selection Sort')
    plt.xlabel('Iterazioni e grandezza array')
    plt.ylabel('Tempo')
    plt.legend()
    plt.show()

'''Crea un grafico che raffiguara il tempo di esecuzione dei due algoritmi 
che ordinano ad ogni ciclo un array casuale che cambia e aumenta di un indice ad ogni ciclo;'''
def grafico(iterazioni, tipo):
    tempi_bs = []  
    tempi_ss = []
    print("Creazione grafico...")
    #campionamento
    for i in range(iterazioni + 1):
        #creazione array casuale
        array = ml.RandomArray(i)
        #scelta del tipo di campionamento
        if tipo == 1:
             #campionamento del tempo di bubble sort
            time_start = time.perf_counter()
            ml.BubbleSort(array)
            time_end = time.perf_counter()

            delta = time_end - time_start 
            #registrazione di delta del ciclo
            tempi_bs.append(delta)

            #campionamento del tempo di Selection sort
            time_start = time.perf_counter()
            ml.SelectionSort(array)
            time_end = time.perf_counter()
            delta = time_end - time_start 
            #registrazione di delta del ciclo
            tempi_ss.append(delta)
        elif tipo == 2:
            #campionamento del tempo di bubble sort
            time_start = time.time()
            ml.BubbleSort(array)
            time_end = time.time()
            delta = time_end - time_start
            #registrazione di delta del ciclo
            tempi_bs.append(delta)

            #campionamento del tempo di bubble sort
            time_start = time.time()
            ml.SelectionSort(array)
            time_end = time.time()
            delta = time_end - time_start
            #registrazione di delta del ciclo
            tempi_ss.append(delta)
        elif tipo == 3:
            #campionamento del tempo di bubble sort
            delta = timeit.timeit(stmt=lambda: ml.BubbleSort(array), number=500)
            #registrazione di delta del ciclo
            tempi_bs.append(delta)

            #campionamento del tempo di Selection sort
            delta = timeit.timeit(stmt=lambda: ml.BubbleSort(array), number=500)
            #registrazione di delta del ciclo
            tempi_ss.append(delta)


    #stampa su schermo del grafico
    plt.plot(tempi_bs, label = "Bubble sort", color = "purple")
    plt.plot(tempi_ss, label = "Selection Sort", color = "orange")
    plt.title('Tempi di esecuzione di Bubble Sort e Selection Sort')
    plt.xlabel('Iterazioni e grandezza array')
    plt.ylabel('Tempo')
    plt.legend()
    plt.show()

#Confronta I due algoritmi con uno stesso array casuale iterandoli un determinato numero di volte scelto dall'utente;
def confronto1(iterazioni, lungezza_array):
        #creazione array casuale
        array = ml.RandomArray(lungezza_array)
        print("array creato")

        #calcolo media dei campionamenti di bubble sort
        media_bs = timeit.timeit(stmt=lambda: ml.BubbleSort(array), number=iterazioni)
        print("Bubble sort terminato")

        #calcolo media dei campionamenti di selection sort
        media_ss = timeit.timeit(stmt=lambda: ml.SelectionSort(array), number=iterazioni) 
        print("Selection sort terminato")

        #comparazione
        if media_bs < media_ss:
            veloce = "Bubble sort"
        else: 
            veloce = "Selection sort"
        
        #stampa su schermo
        print("Bubble sort: {:.10f}s".format(media_bs))
        print("Selection sort: {:.10f}s".format(media_ss))
        print(f"il {veloce} è il più veloce\n") 
        
#Confronta I due algoritmi con uno stesso array casuale;
def confronto2(lungezza_array):
        #creazione array casuale
        array = ml.RandomArray(lungezza_array)
        #bubble sort
        time_start = time.perf_counter()
        ml.BubbleSort(array)
        time_end = time.perf_counter()
        delta_bs = time_end - time_start

        #selection sort
        time_start = time.perf_counter()
        ml.SelectionSort(array)
        time_end = time.perf_counter()
        delta_ss = time_end - time_start

        #comparazione
        if delta_bs < delta_ss:
            veloce = "Bubble sort"
        else: 
            veloce = "Selection sort"
        
        #stampa su schermo
        print("Bubble sort: {:.10f}s".format(delta_bs))
        print("Selection sort: {:.10f}s".format(delta_ss))
        print(f"il {veloce} è il più veloce\n")


#main
inp = 0
while inp != 4:

#menu
    print('''
BubbleSort vs SelectionSort
1) Crea un grafico che raffiguara il tempo di esecuzione dei due algoritmi che ordinano
   ad ogni ciclo un array casuale che cambia e aumenta di un indice ad ogni ciclo;
2) Confronta I due algoritmi con uno stesso array casuale iterandoli un determinato numero di volte scelto dall'utente;
3) Confronta I due algoritmi con uno stesso array casuale;
4) Esci.
''')
    
    inp = int(input("Inserisci scelta: "))
    if inp == 1:
        #grafico
        #scelta del tipo di campionamento grafico
        print('''
Scegli il tipo di campionamento:
1) time.perf_counter() 
2) time.time()
3) timeit.timeit() (500 iterazioni)
''')
    
        tipo = int(input("Inserisci scelta: "))

        while tipo != 1 and tipo != 2 and tipo != 3:
            #verifica dell'input
            tipo = int(input("Inserimento non valido, inserisci scelta: "))
        grafico(100, tipo)
    elif inp == 2:
        #confronto 1 
        iterazioni = int(input("Inserisci numero di iterazioni: "))
        lungezza_array = int(input("Inserisci la lunghezza dell'array: "))
        confronto1(iterazioni, lungezza_array)
    elif inp == 3:
        #confronto 2
        lungezza_array = int(input("Inserisci la lunghezza dell'array: "))
        confronto2(lungezza_array)
    elif inp == 4:
        print("Chiusura programma...")
    else:
        print("Inserimento non valido")