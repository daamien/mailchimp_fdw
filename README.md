# mailchimp_fdw
a PostgreSQL Foreign Data Wrapper for Maichimp




## INSTALL

```
sudo apt-get install postgresql-9.3-python3-multicorn  python-pip
pip install mailchimp
git clone  https://github.com/daamien/mailchimp_fdw
cd mailchimp_fdw
sudo python setup.py install
sudo service postgresql restart
```

## USE

```sql
CREATE EXTENSION multicorn;

CREATE SERVER mailchimp_fdw
FOREIGN DATA WRAPPER multicorn
options (
  wrapper 'mailchimpfdw.MailchimpFDW'
);


CREATE FOREIGN TABLE members (
        id TEXT,
        email TEXT,
        email_type TEXT,
        merges  TEXT,
        status  TEXT
) server mailchimp_fdw options (
   key 'your_mailchimp_api_key',
   list_name 'your_mailchimp_mailing_list'
);

SELECT * from members;


```
