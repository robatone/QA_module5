import pandas as pd

# Read CSV file
sys_book_df = pd.read_csv('03_Library Systembook.csv')
sys_cust_df = pd.read_csv('03_Library SystemCustomers.csv')

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
    sys_book_df.dropna(subset=["Books"], inplace=True)
    sys_cust_df.dropna(inplace=True)

def fixDateFormat():
    # alter 32/05/23 to 31/05/23 stip " from bookCheckout and convert to datetime
    sys_book_df.loc[16, "BookCheckout"] = '"31/05/2023"'
    sys_book_df.loc[6, "BookCheckout"] = '"10/04/2023"'
    sys_book_df["BookCheckout"] = sys_book_df["BookCheckout"].str.strip('"')
    sys_book_df["BookCheckout"] = pd.to_datetime(sys_book_df["BookCheckout"])
    
    # convert BookReturned to datetime
    sys_book_df["BookReturned"] = pd.to_datetime(sys_book_df["BookReturned"])

def checkoutCheck(df, Checkout, Returned):
    if sys_book_df["BookCheckout"] > sys_book_df["BookReturned"]:
        tempcheckout = sys_book_df["BookCheckout"]
        sys_book_df["BookCheckout"] = sys_book_df["BookReturned"]
        sys_book_df["BookReturned"] = tempcheckout

    # # replace spelling mistake in Books column
    # sys_book_df.loc[2,"Books"] = "Lord of the rings the return of the king"

def WeeksToDays(df,col):
    # change days allowed to borrow to an INT and cast cloumn to an INT
    df[col] = df[col].dt.days
  

def daysOnLoan(df, col1, col2, new_col):
    df[new_col] = (df[col1] - df[col2]).dt.days   

def cleanBookCSV():   
    pascalCase()
    removeNA()
    fixDateFormat()
    # WeeksToDays(sys_book_df, "DaysAllowedToBorrow")
    daysOnLoan(sys_book_df, "BookReturned", "BookCheckout", "DaysOnLoan" )

    sys_book_df.to_csv("/app/data/generic_storage/system_book_cleaned.csv", index=False)
    sys_cust_df.to_csv("/app/data/generic_storage/system_customer_cleaned.csv", index=False)
    

if __name__ == "__main__":
    cleanBookCSV()

