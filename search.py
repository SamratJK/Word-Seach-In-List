

list_strings= ['Mary had a little lamb','Its fleece was white as snow, yeah.',"Everywhere the child went,","The little lamb was sure to go, yeah","He followed her to school one day"]


#in order to save every words and there poistion in index
words_and_position={}

def SearchList(term):
    # get required variable which are out-of-scope
    global list_strings
    global words_and_position

    # capitalizing search term in order to make it case-insensitive
    term= term.upper()
    
    # if no value in words_and_ position dictionary run this once
    if not words_and_position:
        for i in list_strings:
            x = i.split(' ')
            for j in x:
                # if same word found in dicitonary add its index into value of the found word(in list)
                if j.upper() in words_and_position:
                    words_and_position[j.upper()].append(list_strings.index(i))
                # if new words in the list add as new key value pair
                else:
                    # only adding words as key
                    getVals = list([val for val in j if val.isalpha() or val.isnumeric()])
                    result = "".join(getVals)

                    words_and_position[result.upper()]=[list_strings.index(i)]
        
        is_function_acessed= True 
    
    #checking if given word is in dicitonary or not it checks provided words with hash value of key so O(1)
    if term in words_and_position:
        return words_and_position[term]
    else:
        return []

y=SearchList('everywhere')
if y:

    for index_ in y:
        print(list_strings[index_])
else:
    print("Sentence not found.")
z=SearchList('snOw')
if z:

    for index_ in z:
        print(list_strings[index_])
else:
    print("Sentence not found.")


