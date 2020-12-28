'''
Autorzy: Jan Rygulski s16724, Dominika Stryjewska s16722
Program ma za zadanie polecić filmy, które warto
było by obejrzeć na podstawie ocen innych użytkowników w pliku .json.
w momencie gdyby nie podano dla którego użytkownika mamy
przeprowadzić rekomendacji ,odbędzie się rekomendacja dla Pana Pawła.
Dla wyboru uzytkowników na podstawie których przeprowadzona
została rekomendacja wykorzystaliśmy współczynnil Pearsdona
'''

import json
import numpy as np


def pearson_score(dataset, user1, user2):
    '''metoda oblicząjąca współczynnnik Pearsona na podstawie podanego uzytkownika(user1) względem reszty
    użytkowników dostepnych w piliku .json'''

    # porównuje wspólnie ocenione filmy
    common_movies = {}

    for item in dataset[user1]:
        if item in dataset[user2]:
            common_movies[item] = 1

    num_ratings = len(common_movies)

    # w momencie braku wspolnych filmów wynik wyniesie 0
    if num_ratings == 0:
        return 0

    # obliczamy sumę wszystkich wspólnych filmów

    user1_sum = np.sum([dataset[user1][item]
                        for item in common_movies])
    user2_sum = np.sum([dataset[user2][item]
                        for item in common_movies])

    # oceny wspólnych filmów zostają podniesione do kwadratu
    user1_squared_sum = np.sum([np.square(dataset[user1][item])
                                for item in common_movies])
    user2_squared_sum = np.sum([np.square(dataset[user2][item])
                                for item in common_movies])

    # obliczanie sumy czesci wspolnych
    product_sum = np.sum([dataset[user1][item] * dataset[user2][item]
                          for item in common_movies])

    # liczymy wartosci koncowe dla wspolczynnika Pearsona
    Sxy = product_sum - (user1_sum * user2_sum / num_ratings)
    Sxx = user1_squared_sum - np.square(user1_sum) / num_ratings
    Syy = user2_squared_sum - np.square(user2_sum) / num_ratings

    if Sxx * Syy == 0:
        return 0

    return Sxy / np.sqrt(Sxx * Syy)


def best_users_from_data(user1, data):
    '''metoda ma za zadonie odnalezienie najlepiej
    pasujących użytkowników i posortowanie ich od nalepszego do najgorszego
     na podstawie wspolczynnika'''

    scores = np.array([[user2, pearson_score(data, user1, user2)]
                       for user2 in data if user1 != user2])
    scores1 = scores[scores[:, 1].argsort()[::-1]]
    best_users = scores1[0:5]

    return best_users


def recommendations(data, user1, best_user):
    '''Metoda otrzymuje pieciu użytkowników którzy
     najbardziej pasują do wykorzystania w rekomendacji,
      po czym zwraca listę filmów '''
    for x in best_user:
        user2 = x[0]
        scores = pearson_score(data, user1, user2)

        total = {}
        similarity = {}

        for item in [x for x in data[user2]
                     if x not in data[user1] or data[user1][x] == 0]:
            total.update({item: data[user2][item] * scores})
            similarity.update({item: scores})

    if len(total) == 0:
        return ['Brak możliwych rekomendacji']

    # Tworzy listę
    rank = np.array([[total / similarity[item], item]
                     for item, total in total.items()])

    # Sortuje wzgędem pierwszej kolumny
    rank = rank[np.argsort(rank[:, 0].astype(np.float))][::-1]

    # Propozycja filmów
    recom = [movie for _, movie in rank]

    return recom


if __name__ == '__main__':

    # podajemy imię i nazwisko osoby na której przeprowadzimy rekomendacje
    user1 = input("Podaj osobę, na którym przerowadzimy rekomendacje. . . \n "
                  "Jesli wciśniesz odrazu Enter przeprowadzona zostanie rekomendacja dla  Pana Pawła\n"
                  "==>")
    if user1 is "":
        user1 = "Pawel Czapiewski"
    rating_file = 'list.json'
    with open(rating_file, 'r', encoding='utf-8') as f:
        data = json.loads(f.read())
    if user1 not in data:
        raise TypeError(user1 + ' - kto to taki ??')
    else:
        best_users = best_users_from_data(user1, data)
        print("\nPolecamy:")
        list = recommendations(data, user1, best_users)
        for i, movie in enumerate(list[:7], start=1):
            print(str(i) + ". " + movie)
        print("\nNie polecamy: ")
        for i, movie in enumerate(list[-7:], start=1):
            print(str(i) + ". " + movie)
