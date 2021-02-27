#Program for generating the Crypto Quote

# Define a Class to represent a single QUOTE
class Quote:
    
    def __init__(self, id, quote, author, submitted_by):
        self.id = id
        self.quote = quote
        self.author = author
        self.submitted_by = submitted_by

    def __repr__(self):
        return 'Quote(id=%s, quote=%s, author=%s, submitted_by=%s)' % (self.id, self.quote, self.author, self.submitted_by)
    
    def __str__(self):
        return 'Quote(id=%s, quote=%s, author=%s, submitted_by=%s)' % (self.id, self.quote, self.author, self.submitted_by)


# Define a Class to represent the list of quotes (quotes collection).
class QuotesList:

    def __init__(self):
        self.quotes_list = []
        
    def __str__(self):
        return 'QuotesList(quotes_list=%s)' % (self.quotes_list)

    def __repr__(self):
        return 'QuotesList(quotes_list=%s)' % (self.quotes_list)

    def add(self, quote):
        self.quotes_list.append(quote)


# Read the Quotes excel, build the Quote object for each quote in the excel and build the Quotes List object
def process_file(file_name):

    quotes_list = QuotesList();
    
    in_file = open(file_name, "rt")
    quote_lines_list = in_file.readlines()

    for each_quote_line in quote_lines_list[1:]:
        
        quote_line_edit = each_quote_line.replace(",\n" , "")
        fields_list = quote_line_edit.split(',')
        
        id = fields_list[0]
        quote = fields_list[1]
        author = fields_list[2]
        submitted_by = fields_list[3]
        
        quote_line_details = Quote(id, quote, author, submitted_by)
        
        quotes_list.add(quote_line_details)
    
    in_file.close()
    
    return quotes_list
        
# Read the .csv file with list of Quotes
quotes_list = process_file("quotes_in_excel.csv")
print(quotes_list)
    
