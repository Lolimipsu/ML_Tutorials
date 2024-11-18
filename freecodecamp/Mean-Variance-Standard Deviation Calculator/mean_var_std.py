import numpy as np

def calculate(list):
    # Check if list contains nine numbers, raise an error if it's less than 9 numbers
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    matrix = np.reshape(list, (3, 3))
    # Initialization
    calculations = {}

    name_of_lists = ['mean', 'variance', 'standard deviation', 'max', 'min', 'sum']
    functions = [np.mean, np.var, np.std, np.max, np.min, np.sum]

    for name_of_lists, function in zip(name_of_lists, functions):
        calculations[name_of_lists] = [
            function(matrix, axis=0).tolist(),
            function(matrix, axis=1).tolist(),
            function(matrix)
        ]

    return calculations
