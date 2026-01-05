#!/bin/bash

# creates the EmploiQL database and runs the schema
# usage: ./scripts/setup_db.sh

set -e

database_name="EmploiQL"
script_dir="$(dirname "$0")"
project_root="$script_dir/.."
schema_file="$project_root/schema.sql"

print_status() {
    echo -e "\033[1;34m==>\033[0m $1"
}

print_success() {
    echo -e "\033[1;32m==>\033[0m $1"
}

print_error() {
    echo -e "\033[1;31mERROR:\033[0m $1" >&2
}

# check postgresql is installed
if ! command -v psql >/dev/null 2>&1; then
    print_error "postgresql is not installed"
    echo "  mac: brew install postgresql@16"
    echo "  ubuntu: sudo apt install postgresql"
    exit 1
fi

if [ ! -f "$schema_file" ]; then
    print_error "schema.sql not found at: $schema_file"
    exit 1
fi

# check if database exists, offer to recreate
if psql -lqt | cut -d \| -f 1 | grep -qw "$database_name"; then
    print_status "database '$database_name' already exists"
    read -p "drop and recreate? this will DELETE ALL DATA [y/N]: " -r response
    
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
psql -d "$database_name" -f "$schema_file" -v ON_ERROR_STOP=1

# verify tables were created
table_count=$(psql -d "$database_name" -t -c "\dt" | grep -c "public")

if [ "$table_count" -eq 5 ]; then
    print_success "all 5 tables created successfully!"
else
    print_error "expected 5 tables but found $table_count"
    exit 1
fi

echo ""
print_status "tables in $database_name:"
psql -d "$database_name" -c "\dt"

echo ""
print_success "database setup complete!"