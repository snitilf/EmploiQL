#!/bin/bash
# sync local EmploiQL data to supabase

set -e  # exit on error

SUPABASE_URL='postgresql://postgres.rorpgotiiesksietltru:%2558A0d%2AF%5EBEiJKQ@aws-0-us-west-2.pooler.supabase.com:6543/postgres'

echo "Exporting local data..."
pg_dump -h localhost -d EmploiQL --data-only --inserts > data_export.sql

echo "Clearing supabase data..."
psql "$SUPABASE_URL" -c "
SET search_path TO public;
TRUNCATE TABLE job_skills, raw_postings, jobs, skills, companies RESTART IDENTITY CASCADE;
"

echo "Importing to supabase..."
psql "$SUPABASE_URL" -c "SET search_path TO public;" -f data_export.sql

echo "Done! Reboot your Streamlit app to see changes."