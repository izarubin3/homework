def cats_and_hats(cats: int, rounds: int) -> list:
    cats_with_hats = []
    for i in range(1, rounds + 1):
        for j in range(1, cats + 1):
            if j % i == 0 and j not in cats_with_hats:
                cats_with_hats.append(j)
            elif j % i == 0 and j in cats_with_hats:
                cats_with_hats.remove(j)
    return cats_with_hats



def cats_and_hats():
    return [i*i for i in range(1, 11)]

    yolof123