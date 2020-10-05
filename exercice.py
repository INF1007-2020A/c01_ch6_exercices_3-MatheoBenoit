#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint
from structs import Queue, Stack


def reverse_data(data: list = None):
    # TODO: Demander 10 valeurs à l'utilisateur,
    # les stocker dans une structure de données,
    # et les retourner en ordre inverse, sans utiliser de liste.

    reversed_data = Stack()

    if data is None:
        data = [input("Veuillez entre une valeur") for _ in range(10)]

    reversed_data.put_many(data)

    liste = []
    for _ in range(len(reversed_data)):
        liste.append(reversed_data.get())

    #ou simplement return [reversed_data.get() for _ in range(len(reversed_data))]

    return liste


def delete_nth_from_stack(data: Stack, position: int) -> Stack:
    # TODO: Supprimer le énième (position) élément de data et retourner la nouvelle structure de données.
    #Voir solutions screenshots du 5 octobre
    x = Stack()
    y = len(data)
    for i in range(len(data)):
        if i == y - position - 1:
            data.get()
        else:
            x.put(data.get())

    return [x.get() for _ in range(len(x))]


def delete_nth_from_queue(data: Queue, position: int) -> Queue:
    # TODO: Supprimer le énième (position) élément de data et retourner la nouvelle structure de données.
    x = Queue()
    for i in range(len(data)):
        if i == position:
            data.get()
        else:
            x.put(data.get())

    return x
    return Queue()


def sort_stack(data: Stack) -> Stack:
    # TODO: Retourner la séquence triée
    x = Stack()
    values = []
    for i in range(len(data)):
        values.append(data.get())

    x.put_many(sorted(values))

    return x


def sort_queue(data: Queue) -> Queue:
    # TODO: Retourner la séquence triée
    x = Queue()
    values = []
    for i in range(len(data)):
        values.append(data.get())

    x.put_many(sorted(values))

    return x


def string_and_structs(string: str) -> tuple:
    # TODO: Parcourez la chaîne de caractères.
    # Si le caractère est une lettre, on l'ajoute dans fifo.
    # Sinon, on retire un élément de fifo pour l'insérer dans lifo.

    fifo, lifo = Queue(), Stack()

    for i in string:
        if i.isalpha():
            fifo.put(i)
        else:
            lifo.put(fifo.get())


    return fifo, lifo


def main() -> None:
    print("On inverse des données...")
    print(f"Résultat: {reverse_data()}")

    n = 4
    lifo = Stack()
    lifo.put_many([i for i in range(20)])
    print(f"On retire l'élément à la position {n} de la pile et on obtient: {delete_nth_from_stack(lifo, n)}")

    n = 6
    fifo = Queue()
    fifo.put_many([i for i in range(20)])
    print(f"On retire l'élément à la position {n} de la file et on obtient: {delete_nth_from_queue(fifo, n)}")

    lifo = Stack()
    lifo.put_many([randint(0, 1000) for _ in range(20)])
    print(f"On ordonne une file: {sort_stack(lifo)}")

    fifo = Queue()
    fifo.put_many([randint(0, 1000) for _ in range(20)])
    print(f"On ordonne une file: {sort_queue(fifo)}")

    sequence = "te!eYy.E6e/T"
    print(f"Le résulat de la manipulation de la séquence: {string_and_structs(sequence)}")


if __name__ == '__main__':
    main()
