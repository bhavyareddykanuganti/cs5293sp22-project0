# -*- coding: utf-8 -*-
# Example main.py
import argparse

import project0


def main(url):
    # Download data
    incident_data = project0.fetchincidents(url)

    # Extract data
    incidents0,incidents1,incidents2,incidents3,incidents4,x,count = project0.extractincidents(incident_data)


    # Create new database
    db = project0.createdb()

    # Insert data
    project0.populatedb(db, incidents0,incidents1,incidents2,incidents3,incidents4,x)

    # Print incident counts
    records = project0.status(db,count)
    for i in range(0,len(records)):
        print(records[i][0],"|",records[i][1])
    print('z-Null', '|', count)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--incidents", type=str, required=True,
                        help="Incident summary url.")

    args = parser.parse_args()
    if args.incidents:
        main(args.incidents)
