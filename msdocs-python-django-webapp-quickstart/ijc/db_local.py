DATABASES = {
    "default": {
        "ENGINE": "sql_server.pyodbc",
        "NAME": "CBIS_HO_TST",
        "USER": "CBIS_HO_NonPro",
        "PASSWORD": "House1Of2As!",
        "HOST": "onebillingsql-nonprod.database.windows.net",
        'PORT': '',
        "OPTIONS": {
            "driver": "ODBC Driver 17 for SQL Server",
        },
    },
}