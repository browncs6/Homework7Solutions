from visuals import stages

# Don't touch this function
def load_words(file_name, word_len):
    """Given the name/path to a text file of words (one word per line), saves all
    words of length `word_len` to returned set.
    
    Arguments:
        file_name {string} -- path to text file of words
        word_len {int} -- length of words to take from text file; must be > 3
    
    Returns:
        set[string] -- all words of length `word_len` from the file at `file_name`
    """
    ret = set()
    with open(file_name) as f:
        for l in f:
            l = l.strip()
            if len(l) == word_len and len(l) > 3:
                ret.add(l.upper())
    return ret


def print_output_decorator(func):
    """This function is a decorator that takes `func` and wraps it such that
    the returned decorated function takes the output of `func`, prints that
    output, then returns that output.
    
    Arguments:
        func {function} -- function to apply this decorator to
    
    Returns:
        function -- a decorated version of `func`
    """

    def wrapped_func(*original_args, **original_kwargs):
        output = func(*original_args, **original_kwargs)
        print(output)
        return output

    return wrapped_func
