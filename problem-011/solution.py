def possible_string(query_string, possible_strings):
    """
    Filter possible_strings that has prefix of the query_string.
    """
    return [string for string in possible_strings if string.startswith(query_string)]


assert possible_string("de", ["dog", "deer", "deal"]) == ["deer", "deal"]
