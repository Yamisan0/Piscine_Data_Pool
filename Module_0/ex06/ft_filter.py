def ft_filter(iterate, func)->list:
    """
    creates a filtered list of elements for which one the func returns true
    iterate: iterable in which you want to iterate
    func: function to apply to each element of the iterable
    """
    try:
        iterator = iter(iterate)
    except TypeError as te:
        print(iterate, 'is not iterable')
    
    return [element for element in iterate if func(element)]
