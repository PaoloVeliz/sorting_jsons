def KeysAndValues(dictionary):
    # sort alphabetically the dictionary items (sorted by key) and save the new dictionary into the "sorted_dictionary" variable
    sorted_dictionary = dict(sorted(dictionary.items()))
    result = []
    # insert the keys seperated from the values, and then i insert the values xd
    result.append(list(sorted_dictionary.keys()))
    result.append(list(sorted_dictionary.values()))
    # final result its supposed to be pretty similar to the pdf example
    return result



test = {
    "Paolo" : "valor1",
    "Bryan" : "valor2",
    "Tato" : "valor3",
    "Angela" : "valor4",
    "Maria" : "valor5",
    "llave6" : "valor6",
    "llave7" : "valor7",
    "llave8" : "valor8",
    "llave10": "valor10",
    "llave9" : "valor9",
}

def run():
    # you can test here a lot of different dictionaries to, just put them as a variable a then pass them into the split_dictionary function
    print(KeysAndValues(test))

if __name__ == '__main__':
    run()