import re

# Function to replace large exponents in variable names
# according to the mapping rules for the attack

def replace_exponents(line):
    
    pattern = r'(y\[\d+\])\^\d+'
    return re.sub(pattern, r'\1', line)

    return line

# Function to process an input file and write the processed output

def process_file(input_file, output_file):
    try:
        # Read all lines from the input file
        with open(input_file, 'r') as f_in:
            lines = f_in.readlines()

        # Write processed lines to the output file
        with open(output_file, 'w') as f_out:
            for line in lines:
                processed = replace_exponents(line)
                f_out.write(processed)

        print("File has been processed and saved as {}".format(output_file))

    except FileNotFoundError:
        print("Error: The file {} was not found.".format(input_file))
    except Exception as e:
        print("An error occurred: {}".format(e))



process_file('result.txt', 'result_without_exp.txt')