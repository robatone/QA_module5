import pandas as pd

# Read CSV file
sys_book_df = pd.read_csv('03_Library Systembook.csv')
sys_cust_df = pd.read_csv('03_Library SystemCustomers.csv')

# log changes for tracking dashboard
book_change_logs = {}
cust_change_logs = {}

changedrows = sys_book_df

def pascalCase():
    # rename headers to pascal case
    sys_book_df.rename(columns = {"Book checkout" : "BookCheckout",
                                     "Book Returned" : "BookReturned",
                                     "Days allowed to borrow": "DaysAllowedToBorrow",
                                     "Customer ID" : "CustomerID"
                                     }, inplace= True)
    #  change headers to pascal case
    sys_cust_df.rename(columns = {"Customer ID" : "CustomerID",
                                "Customer Name" : "CustomerName"}, inplace=True)

def removeNA():
    # remove null rows in the book column
    bookbefore = len(sys_book_df)
    custbefore = len(sys_cust_df)
    # sys_book_df.dropna(subset=["Books"], inplace=True)
    sys_cust_df.dropna(inplace=True)
    #  tracking changes
    book_change_logs["blank records dropped"] = (bookbefore - len(sys_book_df))
    cust_change_logs["blank records dropped"] = (custbefore - len(sys_cust_df))

    naRows = sys_book_df["Books"].isna()
    sys_book_df["NaDataIssue"] = naRows
   
    


def fixDateFormat():
    # alter 32/05/23 to 31/05/23 stip " from bookCheckout and convert to datetime
    # sys_book_df.loc[16, "BookCheckout"] = '"31/05/2023"'
    
    sys_book_df["BookCheckout"] = sys_book_df["BookCheckout"].str.strip('"')
    sys_book_df["BookCheckout"] = pd.to_datetime(sys_book_df["BookCheckout"], errors="coerce", dayfirst=True)
    naRows = sys_book_df["BookCheckout"].isna()
    sys_book_df["DateIssue"] = naRows

    # convert BookReturned to datetime
    sys_book_df["BookReturned"] = pd.to_datetime(sys_book_df["BookReturned"], dayfirst=True)

     #  tracking changes
    book_change_logs["dates corected"] = 2

# def checkoutCheck(df, Checkout, Returned):
#     if sys_book_df["BookCheckout"] > sys_book_df["BookReturned"]:
#         tempcheckout = sys_book_df["BookCheckout"]
#         sys_book_df["BookCheckout"] = sys_book_df["BookReturned"]
#         sys_book_df["BookReturned"] = tempcheckout

    # # replace spelling mistake in Books column
    # sys_book_df.loc[2,"Books"] = "Lord of the rings the return of the king"

def WeeksToDays(df,col):
    # change days allowed to borrow to an INT and cast cloumn to an INT
    df[col] = df[col].dt.days
  

def daysOnLoan(df, col1, col2, new_col):
    df[new_col] = (df[col1] - df[col2]).dt.days   
    sys_book_df["DaysOnLoanIssue"] = df[new_col] <= 0

def datasplit():
    masking = sys_book_df[["NaDataIssue","DateIssue","DaysOnLoanIssue"]].any(axis=1)
    issues_df = sys_book_df[masking]
    sys_book_df = sys_book_df[~masking]
    issues_df.to_csv("issues_log.csv", index=False)
    


def cleanBookCSV():   
    pascalCase()
    removeNA()
    fixDateFormat()
    # WeeksToDays(sys_book_df, "DaysAllowedToBorrow")
    daysOnLoan(sys_book_df, "BookReturned", "BookCheckout", "DaysOnLoan" )
    datasplit()
    sys_book_df.to_csv("system_book_cleaned.csv", index=False)
    sys_cust_df.to_csv("system_customer_cleaned.csv", index=False)

    print(book_change_logs)
    print(cust_change_logs)    
    print(sys_book_df)
    

if __name__ == "__main__":
    cleanBookCSV()

