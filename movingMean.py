import numpy as np
import pandas as pd
def read_2d_array_from_file(file_name):
    """
    Reads a 2D array from a text file where rows are separated by newline characters
    and columns are separated by whitespace.
    """
    with open(file_name, 'r') as file:
        lines = file.readlines()
    
    # Split each line into a list of numbers and store them in a 2D list.
    array = [list(map(float, line.strip().split())) for line in lines]
    
    return array

def sliding_average(matrix, window_size):
    """
    Calculates the sliding average for each element in a 2D matrix using a specified window size
    without accumulating the mean.
    """
    result = []

    # for i in range(len(matrix)):
    #     row = []
    #     for j in range(len(matrix[i])):
    #         # Initialize variables to keep track of the total and count within the window
    #         total = 0
    #         count = 0

    #         for r in range(max(0, i - window_size // 2), min(len(matrix), i + window_size // 2 + 1)):
    #             for c in range(max(0, j - window_size // 2), min(len(matrix[i]), j + window_size // 2 + 1)):
    #                 # Increment the total and count only if the current cell is within the window
    #                 total += matrix[r][c]
    #                 count += 1

    #         # Calculate the average and append it to the row
    #         row.append(total / count)

    #     result.append(row)

    # Program to calculate moving average using numpy
  
    matrix = np.array(matrix)
    arr = matrix[:,1]
    
    
    i = 0
    # Initialize an empty list to store moving averages
    moving_averages = []
    
    # Loop through the array t o
    #consider every window of size 3
    while i < len(arr) - window_size + 1:
    
        # Calculate the average of current window
        window_average = np.mean(arr[
        i:i+window_size])
        
        # Store the average of current
        # window in moving average list
        moving_averages.append(window_average)
        
        # Shift window to right by one position
        i += 1
    
    
    
    return moving_averages


def write_2d_array_to_file(matrix, file_name):
    """
    Writes a 2D matrix to a text file.
    """
    with open(file_name, 'w') as file:
        for row in matrix:
            file.write(" ".join(map(str, row)) + "\n")

if __name__ == "__main__":
    input_file = "VACzeta10ns_modifunzoomed1"
    output_file = input_file + "_smooth"
    window_size = 50  # Adjust the window size as needed
    
    # Read the input 2D array from the file
    input_matrix = read_2d_array_from_file(input_file)
    input_matrix = np.array(input_matrix)
    # Calculate the sliding average
    result_matrix = sliding_average(input_matrix, window_size)
    
    dt=0.001
    outputName = 'smooth'
    np.savetxt(outputName, np.c_[[t*dt for t in range(len(result_matrix))], result_matrix], fmt='%1.8E')

    numbers_series = pd.Series(input_matrix[:,1])
  
    windows = numbers_series.rolling(window_size)
  
    # Create a series of moving
    # averages of each window
    moving_averages = windows.mean()
    
    # Convert pandas series back to list
    moving_averages_list = moving_averages.tolist()
    
    # Remove null entries from the list
    final_list = moving_averages_list[window_size - 1:]
    outputName2 = 'smoothPandas'
    np.savetxt(outputName2, np.c_[[t*dt for t in range(len(final_list))], final_list], fmt='%1.8E')

    exit()
    # Write the result to the output file
    write_2d_array_to_file(result_matrix, output_file)




