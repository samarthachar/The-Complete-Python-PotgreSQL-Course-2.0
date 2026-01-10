from psycopg2 import sql

table_name = input("Enter table you want to search in: ")
column_name = input("Enter column you want to search by: ")
search_value = input("Enter what value you're looking for: ")

query = sql.SQL("SELECT * FROM {table} WHERE {column} = %s")
query = query.format(
    table=sql.Identifier(table_name),
    column=sql.Identifier(column_name)
) # type: ignore

fields_csv = input("Enter fields you wish to retrieve, seperated by commas: ")
fields = fields_csv.strip().split(",")
sql_fields =[sql.Identifier(field) for field in fields]

query = sql.SQL("SELECT {fields} FROM users")

query = query.format(
    fields=sql.SQL(",").join(sql_fields)
) # type: ignore 