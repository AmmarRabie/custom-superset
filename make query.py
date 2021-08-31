import psycopg2


conn = psycopg2.connect(
    host="localhost", database="elrabie", user="postgres", password="159753"
)


def getColumnsOfTable(tableName, schema="public"):
    with conn.cursor() as cursor:
        cursor.execute(
            f"select column_name from information_schema.columns where table_schema = '{schema}' and table_name='{tableName}'"
        )
        return [row[0] for row in cursor]


def addTableSignature(tableName, columns):
    # return list(filter(lambda c: c != "id", columns))
    return map(lambda c: f"{tableName}_{c}", columns)

def removeUnimportantCols(columns):
    return list(filter(lambda c: c not in [
        "deleted_at",
        "password",
        "notes",
        "answers",
    ], columns))

"""

"""

tables = [
    ("areas", "a"),
    ("sub_areas", "sa"),
    ("merchants", "m"),
    ("purchase_orders", "po"),
    ("purchase_order_items", "poi"),
    ("products", "p"),
    ("users", "u"),
    # ("salesperson", "sp"),
    # ("area_manager", "am"),
    # ("visits", "visits"),
    # ("expenses", "expenses"),
    # ("expenses_types", "expenses_types"),
]

selectClauses = []
i = 0
for tableName, tableNameAlias in tables:
    columns = getColumnsOfTable(tableName)
    columns = removeUnimportantCols(columns)
    columnsWithTableSig = addTableSignature(tableNameAlias, columns)
    selectClauses.append([])
    for columnName, columnNameAlias in zip(columns, columnsWithTableSig):
        selectClauses[i].append(f"{tableNameAlias}.{columnName} as {columnNameAlias}")
    i += 1
queryTxt = "\n".join(", ".join(item) for item in selectClauses)
print(queryTxt)
with open("query.txt", "w") as f:
    f.write(queryTxt)
