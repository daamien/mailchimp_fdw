
CREATE EXTENSION multicorn;

CREATE SERVER mailchimp_members_fdw 
FOREIGN DATA WRAPPER multicorn
options (
  wrapper 'mailchimpfdw.MailchimpMembersFDW'
);

CREATE SCHEMA IF NOT EXISTS mailchimp;

--
-- The complete list of fields is available here
-- https://apidocs.mailchimp.com/api/2.0/lists/members.php
--
CREATE FOREIGN TABLE mailchimp.members (
	id TEXT,
	email TEXT,
	email_type TEXT,
	merges	TEXT,
	status	TEXT 
) server mailchimp_members_fdw options (
   key 'your_secret_api_key',
   list_name 'your_list_name' 
);


