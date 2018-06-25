#!/bin/bash

python generate.py > data.csv
rm data.db
sqlite3 data.db <<EOF 
create table salaries(idnumber INTEGER,
                          name TEXT,
                        salary INTEGER,
                    department TEXT,
                     join_date DATE);
.mode csv
.import data.csv salaries
.quit
EOF
