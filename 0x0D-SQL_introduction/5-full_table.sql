-- Print the full description of the table first_table from the database hbtn_0c_0
SELECT column_name, data_type, character_maximum_length
FROM information_schema.columns
WHERE table_name = 'first_table';
