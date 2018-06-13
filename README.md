# mailchimp_fdw
A PostgreSQL Foreign Data Wrapper for [MailChimp](https://mailchimp.com/)




## INSTALL

Assuming your using debian and the apt.postgresql.org repositories.

```
sudo apt-get install postgresql-9.5-python3-multicorn python3-setuptools
sudo easy_install3 pip
sudo pip-3.2 install mailchimp
git clone  https://github.com/daamien/mailchimp_fdw
cd mailchimp_fdw
sudo python3 setup.py install
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
