import csv

temp = []
pressure = []
num_of_lines_to_process = 10000
smallestNumber = 0
with open('temperature_full.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
            
        else:
          #Set biggest number to the first row of data
          if(line_count == 1):
            biggestNumber = float(row[1])
            smallestNumber = float(row[1])
          #print(f'Pressure: \t{row[1]}')
          temp.append([row[1],row[3]])
          #If the current value of the data is bigger than the previous biggestNumber, set biggestNumber equal to the new data value.
          if(biggestNumber<float(row[1])):
            biggestNumber = float(row[1])


          line_count += 1
          #if(line_count > num_of_lines_to_process):
          #  break
    print(f'Processed {line_count} lines.')
with open('pressure_full.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
            
        else:
          #Set biggest number to the first row of data
          if(line_count == 1):
            biggestPNumber = float(row[1])
            smallestPNumber = float(row[1])
          #print(f'Pressure: \t{row[1]}')
          pressure.append([row[1],row[3]])
          #If the current value of the data is bigger than the previous biggestNumber, set biggestNumber equal to the new data value.
          if(biggestPNumber<float(row[1])):
            biggestPNumber = float(row[1])


          line_count += 1
          #if(line_count > num_of_lines_to_process):
          #  break
    print(f'Processed {line_count} lines.')
print(len(temp))
print('Temperature')
print(f' The highest temperature is {biggestNumber} *Celsius.')
print(f' The lowest temperature is {smallestNumber} *Celsius.')
print(f'temperature is {temp[0][0]} at {temp[0][1]}' )
print('Pressure')
print(f' The highest pressure is {biggestPNumber}.')
print(f' The lowest pressure is {smallestPNumber}.')
print(f'pressure is {pressure[0][0]} at {pressure[0][1]}' )
