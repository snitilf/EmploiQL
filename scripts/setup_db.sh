#!/bin/bash

# creates the EmploiQL database and runs the schema
# usage: ./scripts/setup_db.sh

# exit on error (non zero code returned)
set -e

database_name="EmploiQL"
# runs command and captures output
# $0 = path to this script, dirname extracts the directory part
script_dir="$(dirname "$0")"
project_root="$script_dir/.."
schema_file="$project_root/schema.sql"

print_status() {
    # -e enables \033 escape sequences, \033[1;34m = bold blue, \033[0m = reset
    echo -e "\033[1;34m==>\033[0m $1"
}

print_success() {
    # \033[1;32m = bold green
    echo -e "\033[1;32m==>\033[0m $1"
}

print_error() {
    # \033[1;31m = bold red, >&2 redirects to stderr instead of stdout
    echo -e "\033[1;31mERROR:\033[0m $1" >&2
}

# check postgresql is installed
# -v checks if command exists in PATH
# >/dev/null discards stdout, 2>&1 sends stderr to same place so also discarded
if ! command -v psql >/dev/null 2>&1; then
    print_error "postgresql is not installed"
    echo "  mac: brew install postgresql@16"
    exit 1
fi

# if file exists and is regular file
# ! this checks if file does not exist
if [ ! -f "$schema_file" ]; then
    print_error "schema.sql not found at: $schema_file"
    exit 1
fi

# check if database exists, offer to recreate
# psql -l = list databases, -q = quiet, -t = tuples only (no headers)
# cut -d \| -f 1 = split by pipe char, take field 1
# grep -q = quiet (exit code only), -w = whole word match
if psql -lqt | cut -d \| -f 1 | grep -qw "$database_name"; then
    print_status "database '$database_name' already exists"
    # read -p = show prompt, -r = raw input (don't interpret backslashes)
    read -p "drop and recreate? this will DELETE ALL DATA [y/N]: " -r response
    # [[ =~ ]] = regex match, ^ = start, $ = end, [Yy] = char class
    # ([Ee][Ss])? = optional group, matches "es" case-insensitive
    # matches: y, Y, yes, Yes, YES, etc. rejects: yeah, yep, yes please
    if [[ "$response" =~ ^[Yy]([Ee][Ss])?$ ]]; then
        print_status "dropping and recreating database..."
        dropdb "$database_name"
        createdb "$database_name"
    else
        print_status "keeping existing database, re-running schema..."
    fi
else
    print_status "creating database '$database_name'..."
    createdb "$database_name"
fi

print_status "running schema.sql..."
# -d = database, -f = file to execute, -v = set psql variable
psql -d "$database_name" -f "$schema_file" -v ON_ERROR_STOP=1

# verify tables were created
# -t = tuples only, -c = execute command, \dt = describe tables
# grep -c = count matching lines
table_count=$(psql -d "$database_name" -t -c "\dt" | grep -c "public")

# [ -eq ] = numeric equality test ( = for strings, -eq for numbers)
if [ "$table_count" -eq 5 ]; then
    print_success "all 5 tables created successfully!"
else
    print_error "expected 5 tables but found $table_count"
    exit 1
fi

echo ""
print_status "tables in $database_name:"
# VAR=value cmd = set env var for just this one command
# PAGER=cat prevents psql from opening less/more for output
PAGER=cat psql -d "$database_name" -c "\dt"

echo ""
print_success "database setup complete!"