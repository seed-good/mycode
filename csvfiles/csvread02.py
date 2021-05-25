import csv

def main():
    with open('superbirthday.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                # print(f'Column names are {", ".join(row)}') # python3.6 way
                                                              ## to do things
                print('Column names are {}'.format(", ".join(row)))
                line_count += 1
            # print(f'\t{row["name"]} aka {row["heroname"]} was born in {row["birthday month"]}.')
            # above is the python3.6+ way to do things
            print('\t{} aka {} was born in {}.'.format(row["name"],row["heroname"],row["birthday month"]))
            line_count += 1
    # print(f'Processed {line_count} lines.') # python3.6 way to do things
    print('Processed {} lines.'.format(line_count))

    # Code customization - write to a file without 1 field
    with open('regularbirthday.csv', mode='w') as out_file:
        with open("superbirthday.csv", mode='r') as in_file:
            csv_reader = csv.DictReader(in_file)
            print(type(csv_reader))
            line_count = 0
            for row in csv_reader:
                headers = csv_reader.keys().remove('heroname')
                print(headers)
                writer = csv.DictWriter(out_file, fieldnames=headers)
                if line_count == 0:
                    writer.writeheader()
                    line_count += 1
                writer.writerow(row.pop('heroname'))

if __name__ == "__main__":
    main()

