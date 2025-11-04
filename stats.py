def get_num_words(book_text):
    return len(book_text.split()) 

def get_num_characters(book_text):
    characters = {}

    for word in book_text:
        for character in word:
            if character.lower() in characters:
                characters[character.lower()] += 1
            else:
                characters[character.lower()] = 1

    return characters

def sort_on(dictionary):
    return dictionary["num"]

def get_sorted_list(dictionary):
    list_dict = []
    
    for char in dictionary:
        list_dict.append({"char": char, "num": dictionary[char]})
    
    list_dict.sort(reverse=True, key=sort_on) 

    return list_dict
