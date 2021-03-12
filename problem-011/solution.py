def possible_string(query_string, possible_strings):
    return [string for string in possible_strings if string.startswith(query_string)]

assert possible_string("de", ["dog", "deer", "deal"]) == ["deer", "deal"]
