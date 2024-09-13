import pandas as pd
import re

def phone1_check(df):
    phone_pattern=r'^01(\d{3})-(\d{6}$)'
    match=re.match(phone_pattern,df.phone1)
    if match:
        return df.phone1
    else:
        return ''
    


def phone2_check(df):
    phone_pattern=r'^01(\d{3})-(\d{6}$)'
    match=re.match(phone_pattern,df.phone2)
    if match:
        return df.phone2
    else:
        return ''
    


def mail_check(df):
    mail_pattern=r'^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$'
    match=re.match(mail_pattern,df.email)
    if match:
        return df.email
    else:
        return ''

def data_cleaning(df):
    data=['Employee Name','Company','Employee Address','Phone','Employee Email','Web']
    
    df2=pd.DataFrame(columns=data)
    
    df2['Employee Name']=df['first_name']+' '+df['last_name']
    
    df2['Company']=df['company_name']

    df2['Employee Address']=df['address']+','+df['city']+','+df['county']+','+df['postal']
    
    df2['Phone']=df.apply(phone1_check,axis=1)+','+df.apply(phone2_check,axis=1)

    df2['Employee Email']=df.apply(mail_check,axis=1)

    df2['Web']=df['web']

    return df2

def cleaned_file(input_file,output_file):
    df=pd.read_csv(input_file)
    cleaned_df=data_cleaning(df)
    cleaned_df.to_csv(output_file)
    return output_file


