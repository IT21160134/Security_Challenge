

log_file_path = 'log.txt' #path to firewall log file

with open(log_file_path, 'r') as log_file: # Open the log file and read its lines
       for line in log_file:# Iterate through each line in the log file
           if 'block' in line.lower():# Check if the line contains "block"
             print(line.strip()) # Print the line if it contains a block action
