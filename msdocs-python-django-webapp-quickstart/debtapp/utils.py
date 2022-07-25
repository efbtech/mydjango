import sys
import datetime
from django.db import connection

def getSPCall(name,param):
    if(name == 'company'):
        st = "{CALL [dbo].[CBIS_SP_SelectCompanyList](%s)}"
    if(name == 'memberlist'):
        st = "{CALL [dbo].[CBIS_SP_SelectMemberListByClassID_ParentOnly](%s,%s,%s)}"
    if(name == 'memberdetail'):
        st = "{CALL [dbo].[CBIS_SP_SelectAllDetailsForMemberID](%s,%s)}"
    if(name == 'agingsummary'):
        st = "{CALL [dbo].[CBIS_SP_SelectMemberAgeingSummaryByID](%s,%s)}"
    if(name == 'latestdetail'):
        st = "{CALL [dbo].[CBIS_SP_SelectLatestDetailsByMemberID](%s,%s)}"
    if(name == 'systemparam'):
        st = "{CALL [dbo].[CBIS_SP_SelectSystemParameter](%s,%s)}"
    if (name == 'supplier'):
        st = "{CALL [dbo].[CBIS_SP_SelectSupplierForMemberTransaction](%s,%s,%s)}"
    if(name == 'transaction_open'):
        st = "{CALL [dbo].[CBIS_SP_SelectTransByAgingIDAndMemberID](%s,%s,%s,%s,%s)}"
    if(name == 'defaultsystem'):
        st = "{CALL [dbo].[CBIS_SP_SelectSystemDefaults](%s)}"
    if(name == 'selecttemplate'):
        st = "{CALL [dbo].[CBIS_SP_SelectTemplateDetails](%s,%s,%s,%s)}"
    if(name == 'suppliercontact'):
        st = "{CALL [dbo].[CBIS_SP_SelectSupplierContacts](%s,%s)}"

        
    cursor = connection.cursor()
    try:
        #cursor.execute("{call dbo.CBIS_SP_SelectCompanyList %,'sjayaraman'}")
        #cursor.execute("[dbo].[CBIS_SP_SelectCompanyList] %", ['sjayaraman'])
        cursor.execute(st,param)
        result_set = cursor.fetchall()
    finally:
        cursor.close()
    return result_set