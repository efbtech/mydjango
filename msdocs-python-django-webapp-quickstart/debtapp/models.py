from django.db import models
from django.db import connection

class MY_UTIL():
    def get_companies(self, uid):
        cursor = connection.cursor()
        ret = cursor.callproc("MY_UTIL.CBIS_SP_SelectCompanyList", (uid))# calls PROCEDURE named LOG_MESSAGE which resides in MY_UTIL Package
        cursor.close()
        return ret
