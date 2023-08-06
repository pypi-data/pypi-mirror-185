# cedict
A Chinese English dictionary.

csv file from https://github.com/1eez/103976

## How to use
    from cedict.cedict import DictionaryData, search
    dict_db = DictionaryData()
    print(search("apple", dict_db)) # ('apple', 'n.苹果,似苹果的果实')
