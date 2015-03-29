"""

"""

from multicorn import ForeignDataWrapper
from multicorn.utils import log_to_postgres
import mailchimp


class MailchimpFDW(ForeignDataWrapper):

    def __init__(self,options,columns):
        super(MailchimpFDW,self).__init__(options,columns)
        self.key=options.get('key',None)

        # the Mailchimp API cannot return more than 100 result at once
        self.page_size =  100

        # chimp is the global object
        self.chimp=mailchimp.Mailchimp(self.key)

        self.columns=columns

        # DEBUG
        #log_to_postgres("Mailchimp FDW loaded : %s" % __file__)

    def fetch(self) :
        data = []
        data.append(self.chimp.helper.account_details())

        # account_details returns a dict, transform it into a list before return
        return data

    def execute(self, quals, columns):
        for item in self.fetch():
            output = {}
            for column_name in self.columns:
                output[column_name] = item[column_name]
            yield output



class MailchimpListsFDW(MailchimpFDW):

    def __init__(self,options,columns):
        super(MailchimpListsFDW,self).__init__(options,columns)


    def fetch(self):

        data = []
        total = self.chimp.lists.list()['total']
        start_page = 0

        # Fetch the members, page by page
        while start_page * self.page_size <= total :
            filters = {'start' : start_page, 'limit': self.page_size} 
            data += self.chimp.lists.list(filters)['data']
            # Next page
            start_page += 1 

        return data

class MailchimpMembersFDW(MailchimpFDW):

    def __init__(self,options,columns):
        super(MailchimpMembersFDW,self).__init__(options,columns)
        
        self.list_name=options.get('list_name',None)

        # extract id from name
        the_list = self.chimp.lists.list({"list_name": self.list_name})
        self.list_id = the_list['data'][0]['id']


    def fetch(self):
        data=[]

        total = self.chimp.lists.members(self.list_id)['total']
        start_page = 0

        # Fetch the members, page by page
        while start_page * self.page_size <= total :
            filters = {'start' : start_page, 'limit': self.page_size} 
            data =self.chimp.lists.members(self.list_id,'subscribed',filters)['data']
            data+=self.chimp.lists.members(self.list_id,'cleaned',filters)['data']
            data+=self.chimp.lists.members(self.list_id,'unsubscribed',filters)['data']
            # Next page
            start_page += 1 

        return data
