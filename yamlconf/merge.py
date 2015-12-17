
def merge(d, *dicts):
    """
    Recursively merges dictionaries
    """

    for d_update in dicts:
        if not isinstance(d, dict):
            raise TypeError("{0} is not a dict".format(d))

        dict_merge_pair(d, d_update)

    return d


def dict_merge_pair(d1, d2):
    """
    Recursively merges values from d2 into d1.
    """
    for key in d2:
        if key in d1 and isinstance(d1[key], dict) and \
           isinstance(d2[key], dict):
            dict_merge_pair(d1[key], d2[key])
        else:
            d1[key] = d2[key]

    return d1
