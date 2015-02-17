"""

"""

from multicorn import ForeignDataWrapper
import mailchimp


class MailchimpFDW(ForeignDataWrapper):

    def __init__(self,options,columns):
        super(MailchimpFDW,self).__init__(options,columns)
        self.key=options.get('key',None)
        self.list_name=options.get('list_name',None)

        # the list.member cannot return more than 100 result at once
        self.page_size =  100

        # chimp is the global object
        self.chimp=mailchimp.Mailchimp(self.key)

        # extract id from name
        the_list = self.chimp.lists.list({"list_name": self.list_name})
        self.list_id = the_list['data'][0]['id']

        self.columns=columns


    def execute(self, quals, columns):

        total = self.chimp.lists.members(self.list_id)['total']
        start_page = 0

        # Fetch the members, page by page
        while start_page * self.page_size <= total :
            filters = {'start' : start_page, 'limit': self.page_size} 
            page=self.chimp.lists.members(self.list_id,'',filters)['data']
            for member in page:
                line = {}
                for column_name in self.columns:
                    line[column_name] = member[column_name]
                yield line
            # Next page
            start_page += 1 
