import os
import csv


def main():
    gps_x_data_path = '../config/log/Graph1.txt'

    gps_x_data_values = get_data_from_csv(gps_x_data_path)
    if gps_x_data_values:
        # Calculate the standard deviation of GPS X values
        std_dev_gps_x = calculate_standard_deviation(gps_x_data_values)
        print(f'MeasuredStdDev_GPSPosXY: {std_dev_gps_x}')

    accel_x_data_path = '../config/log/Graph2.txt'
    accel_x_data_values = get_data_from_csv(accel_x_data_path)
    if accel_x_data_values:
        # Calculate the standard deviation of Accelerometer X values
        std_dev_accel_x = calculate_standard_deviation(accel_x_data_values)
        print(f'MeasuredStdDev_AccelXY: {std_dev_accel_x}')


def calculate_standard_deviation(data):
    # Calculate the mean of the data values
    mean_data = sum(data) / len(data)
    # Calculate the variance
    variance = sum((x - mean_data) ** 2 for x in data) / len(data)
    # Calculate the standard deviation
    std_dev = variance ** 0.5

    return std_dev


def get_data_from_csv(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            reader = csv.reader(f)
            data = list(reader)
            # Extract data value
            data_values = [float(row[1]) for row in data[1:]]  # Skip the first row {time, value}
            return data_values
    else:
        print(f'File does not exist: {file_path}')
        return None


if __name__ == '__main__':
    main()
