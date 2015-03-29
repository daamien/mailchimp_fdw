
CREATE EXTENSION multicorn;

CREATE SERVER mailchimp_lists_fdw 
FOREIGN DATA WRAPPER multicorn
options (
  wrapper 'mailchimpfdw.MailchimpListsFDW'
);

CREATE SCHEMA IF NOT EXISTS mailchimp;

--
-- the complete list of fields is available here
-- https://apidocs.mailchimp.com/api/2.0/lists/list.php
--

CREATE FOREIGN TABLE mailchimp.lists (
        id TEXT,
        name TEXT,
        date_created TEXT,
        email_type_option  TEXT,
        list_rating  TEXT 
) server mailchimp_lists_fdw options (
      key 'your_secret_api_key'
);


