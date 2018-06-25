#!/bin/bash

python generate.py > data.csv
rm data.db
sqlite3 data.db <<EOF 
create table salaries(idnumber integer,
                          name string,
                               salary integer,
                               department string,
                               join_date date);
.mode csv
.import data.csv salaries
.quit
EOF
