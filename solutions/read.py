def read_input(filename):
    complete_filename = '../inputs/' + filename
    data = []
    with open(complete_filename) as f:
        data = f.read().splitlines()
    return data
