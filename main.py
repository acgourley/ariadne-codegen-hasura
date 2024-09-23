import time

start_time = time.time()
from gql_client import client
client_import_time = time.time() - start_time

start_time = time.time()
from gql_client import enums
enums_import_time = time.time() - start_time

start_time = time.time()
from gql_client import input_types
input_types_import_time = time.time() - start_time

print(f"Import times:")
print(f"gql_client.client: {client_import_time:.6f} seconds")
print(f"gql_client.enums: {enums_import_time:.6f} seconds")
print(f"gql_client.input_types: {input_types_import_time:.6f} seconds")
