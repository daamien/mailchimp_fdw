
CREATE EXTENSION multicorn;

CREATE SERVER mailchimp_fdw 
FOREIGN DATA WRAPPER multicorn
options (
  wrapper 'mailchimpfdw.MailchimpFDW'
);

CREATE SCHEMA IF NOT EXISTS mailchimp;

--
-- the complete list of fields is available here
-- https://apidocs.mailchimp.com/api/2.0/helper/account-details.php
--
CREATE FOREIGN TABLE mailchimp.details (
        username TEXT,
        user_id TEXT,
        is_trial TEXT,
        is_approved TEXT,
        has_activated TEXT,
        timezone    TEXT,
        plan_type   TEXT,
       -- plan_low    integer,
        --plan_high   integer,
        --emails_left TEXT,
        first_payment TEXT,
        last_payment   TEXT,
        times_logged_in TEXT,
        last_login  TEXT,
        affiliate_link  TEXT,
        industry  TEXT,
        contact TEXT
) server mailchimp_fdw options (
   key 'your_secret_api_key'
);

