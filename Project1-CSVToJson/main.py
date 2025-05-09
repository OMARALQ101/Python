import json

def main():

    csv_filename = input("Enter the file name of the CSV: ")
    json_filename = input("Enter the file name of where you would like to save your JSON to: ")

    with open(csv_filename, "r") as f:
        line = f.readline()
        headers = line.strip("\n").split(",")
        data = []

        line = f.readline()
        for line in f:
            token = line.strip("\n").split(",")
            d = {headers[0]: token[0], 
                 headers[1]: token [1], 
                 headers[2]: token [2], 
                 headers[3]: token [3]}
            data.append(d)

        final = json.dumps(data, indent=2)

    with open(json_filename, "w") as f: 
        f.write(final)

    print(f"JSON saved to {json_filename}")

main()