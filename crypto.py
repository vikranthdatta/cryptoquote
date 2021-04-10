#Program for generating the Crypto Quote

# Import String to generate Alphabet Characters
import string

# Import Random to shuffle the List
import random

#Import Pretty Printing
import pprint
pp = pprint.PrettyPrinter(indent=4)

#Importing webbrowser module to open the html page from a browser
import webbrowser
import urllib


#======= Class Quote =============================
# Class for representing a single QUOTE
# id, quote, author, submitted_by
# _repr__ and __str__
class Quote:
    
    def __init__(self, id, quote, author, submitted_by):
        self.id = id
        self.quote = quote
        self.author = author
        self.submitted_by = submitted_by

    def __repr__(self):
        return "ID: " + self.id + " Quote: " + self.quote + " Author: " + self.author + " Submitted by: " + self.submitted_by

    def __str__(self):
        return "ID: " + self.id + " Quote: " + self.quote + " Author: " + self.author + " Submitted by: " + self.submitted_by    
   
    def writeToHTML(self):
        current_quote = self.quote
        file = open("random_quote.html", "w", encoding='iso-8859-15')
        file.write(current_quote)
        file.close()
        

#======= Class QuotesList =============================
#Class for representing all the quotes (quotes collection).
# This class represents a collection of quotes
# _repr__ and __str__
class QuotesList:


    # constructor method for creating a QuotesList object
    # The list of quotes should be constructed outside of the class
    def __init__(self, some_list_of_quotes):
        self.quotes_list = some_list_of_quotes
        

   
    # Another method for creating the  Quote object
    # This method takes the file name as the input
    # See https://stackoverflow.com/questions/44726196/how-to-implement-multiple-constructors-in-python
    # this method imports CSV module to ensure that we are processing the CSV correctly
    # as some quotes may contain commas.
    @classmethod
    def createWithFileName(cls, file_name):
        # create an empty list of quotes
        quotes_list = [ ]

        # now process the file
        file = open(file_name)
        import csv
        reader = csv.reader(file)
        for fields in reader:
            quote = Quote(fields[0], fields[1], fields[2], fields[3])
            quotes_list.append(quote)
        file.close()
        
        # now, return this 
        return cls(quotes_list)


    # We will now have a getMethod for other classes to get the quotes_list variable
    # from QuotesList object
    def getQuotesList(self):
         return self.quotes_list

    # This is a useful function to print the quotes_list
    # Can be called by different methods to validate that their methods are working
    def printQuotes(self):
        for x in self.quotes_list:
            print(x)
        


    # We will now have methods for __str, __ repr, and __ iter
    # these are the standard methods to print and iterate the object
    def __str__(self):
        return quotes_list.__str()

    def __repr__(self):
        return quotes_list.__str()

    def __iter__(self):
        self.x = 0
        return self

    def __next__(self):
        if (self.x < len(self.quotes_list)):
            current_quote = self.quotes_list[self.x]
            self.x = self.x+1
            return current_quote
        else:
            raise StopIteration

    #================= PLEASE READ ======================================
    # All the student's methods start here.
    # Please write the method number and your name as the first line comment
    # Proive the "purpose" of the function
    # Make sure that you are adding your method at the respective sequence
    # Please ensure that you are always working with the latest version of crypto.py
    # So please sync with the UPSTREAM every week
    #=====================================================================

    # ============= Method No: 2 (Nikhitha Gollamudi) ===============
    # Purpose: This method returns how many students (submitted_by) there are in the quotes collection 
    def getStudentCount(self):
        students = set()
        
        for x in self.quotes_list:
            students.add(x.submitted_by)
        return len(students)

    # ============= Method No: 3 (Nikhitha Gollamudi) ===============
    # Purpose: This method returns the student with the most quotes submitted 
    def getStudentWithMostQuotes(self):
        students_list = []
        student = ""
        count = 0
        for x in self.quotes_list:
            students_list.append(x.submitted_by)
            for x in students_list:
                freq = students_list.count(x)
                if freq > count:
                    count = freq
                    student = x
        return student
   

    # ============= Method No: 4 (Anjneya Kumar) ===============
    # Purpose: The method returns a mini-collection of quotes by a certain author (given by the user)
    #TODO: 1. you need to take the author as the input parameter to the method
    #TODO: 2. You need to build a mini collection and return it
    def getQuotesByAuthor(self):
        pass
       
     
    # ============= Method No: 6 (Eshaan Dhavala) ===============
    # Purpose: This method returns dictionary
    #  with author as the key, and count as the value
    def getAuthorAndQuoteCount(self):
        author_count_dict = {}       
        for x in self.quotes_list:
            author_name = x.author
            author_name = author_name.strip()
            
            if author_name in author_count_dict:
                current_count = author_count_dict[author_name]
                author_count_dict[author_name] = current_count + 1
            else:
                author_count_dict[author_name] = 1
            
            
        return author_count_dict

    # ============= Method No: 9 (Jaya Varanasi) ===============
    # Purpose: This method displays a random quote as HTML
    def showRandomQuoteInHTML(self):
        random_quote_object = random.choice(self.quotes_list)
        #print(random_quote_object)
        #random_quote = random_quote_object.quote
        #print(random_quote)

        # write random_quote to the file itself.
        random_quote_object.writeToHTML()

        # Now show the file name in a browser
        new = 2
        url = "random_quote.html"
        webbrowser.open(url,new=new)

        
    
    
    # ============= Method No: 11 (Karthik Uppala) ===============
    # Purpose: This method returns provide the list of "author"
    # (name of the authors) in sorted order
    def getSortedAuthors(self):
        # TODO
        # you have to operate on this variable self.quotes_list

        sorted_authors_list = ["a", "bx", "c", "jasthi"]
        return sorted_authors_list
    

    # ============= Method No: 13 (Nikhitha Gollamudi) ===============
    # Purpose: This method returns the words in the quotes sorted by frequency 
    def getWordListByFrequency(self):
        words_list = []
        word_dict = {}

        for x in self.quotes_list:
            quote_str = x.quote
            words_list = words_list + quote_str.split(" ")
          
        for word in words_list:
            if word != "":
                if word not in word_dict.keys():
                   word_dict[word] = 1
                else:
                    word_dict[word] = word_dict.get(word) + 1
        sorted_dict = {}
        sorted_keys = sorted(word_dict, key=word_dict.get, reverse=True)  

        for w in sorted_keys:
            sorted_dict[w] = word_dict[w]

        return sorted_dict

# ============= Method No: 14 (Shekar Motukuri) ===============
    # Purpose: This method returns count of Quotes submitted by students(him/her)
    
    def getCountOfQuotesByStudent(self, student_name):
        student_count = 0
        student_string=""
        student_name=""
        print('testing')
             
        for x in self.quotes_list:
            current_student = x.submitted_by
            student_string+=current_student+" ";
        #print('testing'+student_string)
        for x in self.quotes_list:
            current_student = x.submitted_by
            student_count1=student_string.count(current_student)
            if(student_count1>=student_count):
              student_count=student_count1
              student_name=current_student    
        print('testing'+student_name)
        print(student_count)  
        return student_name


    # ============= Method No: 15 (Pranav Manikonda) ===============
    # Purpose: This method returns a random quote from the collection of quotes
    def getRandomQuote(self):
        random_quote_object = random.choice(self.quotes_list)
        random_quote_str = random_quote_object.quote
        return random_quote_str



    # ============= Method No: 16 (Pranav) ===============
    # Purpose: This method returns the count of quotes submitted by the author
    def getCountOfQuotesByAuthor(self, author_name):
        quote_count = 0
        for x in self.quotes_list:
            p = x.author.strip()
            q = author_name.strip()
            if p==q:
                quote_count = quote_count + 1
        return quote_count


    # ============= Method No: 19 (Sahasra Tummala) ===============
    # Purpose: This method returns shortest quote in the quotes collection
    def getShortestQuote(self):
        shortest_quote = "abcdedfghijklmnopqrstuvwxyz"
        shortest_quote = shortest_quote * 100
        for x in self.quotes_list:
            current_quote = x.quote
            if len(current_quote) < len(shortest_quote):
                shortest_quote = current_quote  
        return shortest_quote


    # ============= Method No: 20 (Sai Akaksha Josylua) ===============
    # Purpose: This method returns the count of Authors in the quotes collection
    def getAuthorCount(self):
        authors = set()
        
        for x in self.quotes_list:
            current_author = x.author
            authors.add(current_author)

        count_of_authors = len(authors)
        return count_of_authors


    # ========= Sravamti Manikonda: Method # 22 ========================
    # Purpose: This method returns the single author who authored the most quotes
    def getAuthorWithMostQuotes(self):
        ## Call eshan's method to get author - count dictionary
        author_count_dictionary = self.getAuthorAndQuoteCount()
        ## Find the max key from the dictionary    
        max_key = max(author_count_dictionary, key=author_count_dictionary.get)
        ## Return the max key
        return max_key

    

    # ============= Method No: 21 (Shekar Motukuri) ===============
    # Purpose: This method returns longest quote in the quotes collection 
    def getLongestQuote(self):
        longest_quote = ""
             
        for x in self.quotes_list:
            current_quote = x.quote
            if len(current_quote) > len(longest_quote):
                longest_quote = current_quote         
                
        return longest_quote
    
    # ============= Method No: 26 (Vikranth Datta) ===============
    # Purpose: This method returns a list of students with no quotes
    # Algorithm:
    # 1. Get the set of students from the file (x)
    # 2. Get the set of students from the quotes_list (y)
    # 3. Find the difference (x) and (y) to find out the students who did not submit the quotes.
    # 4. Convert this difference set into list and return the list.
    def getStudentListWithNoQuotes(self):
        file=open("students_list.txt")
        lists=file.readlines()

        #create an empty set. we can not use { } because it will be treated as empty dictionary
        all_students_set = set()
        
        for i in range(len(lists)):
            student_name = lists[i].rstrip('\n')
            all_students_set.add(student_name)
        #print(all_students_set)

        students_with_quotes_set = set()
        for x in self.quotes_list:
             students_with_quotes_set.add(x.submitted_by)

        # find the intersection
        students_with_no_quotes_set = all_students_set.difference(students_with_quotes_set)

        # since the method contract says that we should return a list,
        # convert the set to a list and return it
        students_with_no_quotes_list = list(students_with_no_quotes_set)
        
        return students_with_no_quotes_list;




    # ============= Method No: 28 (Vishnu Vundamati) ===============
    # Purpose: The method allows you to update a quote in the collection/file
    def updateQuote(self, id, quote, author, submitted_by):

        #default
        updated_status = "The id you entered does not exist in the collection"

        #sorting through each quote to find the quote with the id the user entered
        for x in self.quotes_list:
            current_id = x.id
            current_quote = x.quote
            current_author = x.author
            current_submitted_by = x.submitted_by

            #updates the quote with user input values
            if (current_id == id):
                x.quote = quote
                x.author = author
                x.submitted_by = submitted_by
                #proof of update
                updated_status = "The quote has successfully been updated"

                #exiting loop
                break
        return updated_status

    # ============= Method No: 29 (Siva Jasthi) ===============
    # Purpose: The method returns a mini-collection of quotes containing the bad words
    # Reference: https://www.geeksforgeeks.org/python-test-if-string-contains-element-from-list/
    def getQuotesContainingBadWords(self):
        bad_word = ["heck", "damn"]
        #this need to be calculated
        quotes_list_containing_bad_words = []
        y = ""
        for x in self.quotes_list:
            for y in bad_word:
                word = " " + y.lower() + " "
                if word in str(x).lower():
                    quotes_list_containing_bad_words.append(x)
                    break

        # create a mini quotes collection 
        quotes_mini_collection = QuotesList(quotes_list_containing_bad_words)
        return quotes_mini_collection;
        



    # ============= Method No: 30 (Nikhitha Gollamudi) ===============
    # Purpose: The quotes collection may have been changed by add, update and delete methods.
    #          This method writes the contents of the quotes_list into the file
    def saveToFile(self):
        file = open("quotes_in_excel.csv", "w", encoding='iso-8859-15')
        file.write(str(self.quotes_list))
        file.close()
    
        
  

    # For adding a quote to the collection
    def add(self, quote):
        self.quotes_list.append(quote)
        
    # This method chooses a random quote from the collection
    # The quote is converted to the crypto quote
    # The crypto quote is shown on the HTML page
    # Author : Ishana D
    def showRandomCryptoInHTML(self):
        return self
        

    # Generates Crypto Quote for the input Quote
    def generateCryptoQuote(quote):
        upper_quote = quote.upper()
        quote_list = list(upper_quote)
        quote_list_temp = list(upper_quote)
    
        list_of_alphabets = []
        list_of_alphabets = list(string.ascii_uppercase)
    
        random_list_of_alphabets = list(list_of_alphabets)
        random.shuffle(random_list_of_alphabets)

        output_queue_pos = -1
        for quote_char in quote_list:
            output_queue_pos += 1
            if quote_char in list_of_alphabets:
                quote_char_alphbt_pos = list_of_alphabets.index(quote_char)
                replace_char = random_list_of_alphabets[quote_char_alphbt_pos]
                quote_list_temp[output_queue_pos] = replace_char

        cryptoquote = ''.join(quote_list_temp)

        return cryptoquote

    

#========================= STARTING POINT ==========================
# All the testing happens here
# Please ensure that you print some info about the method invocation and the results
# Please ensure that you put the method number, your name and method name in the print
#================= Starting Point ===============================
# This is the starting point for the program execution
#
# Step 1:  Create a QuotesList object from the input file
quotes_list_object = QuotesList.createWithFileName("quotes_in_excel.csv")

# Step 2:  Now, ask the quotes_list_object for its variable quotes_list
# quotes_list_x = quotes_list_object.getQuotesList()

# Step 3: Just for debugging, iterate through the quotes collection and print it
# We will comment it this line out during the demo
# for x in quotes_list_x:
#    print(x)

# Step 3: Invoke the helper function to print the quotes
print("=== Printing all the quotes:  printQuotes() method ========")
quotes_list_object.printQuotes()

# Step 4: Now let us exercise some methods in the QuotesList


# ========= Nikhitha Gollamudi: Method # 2 ========================
print("=== Method #2 (Nikhitha Gollamudi) getStudentCount( ) method ====")
student_count = quotes_list_object.getStudentCount()
print(student_count)

# ========= Nikhitha Gollamudi: Method # 3 ========================
print("=== Method #2 (Nikhitha Gollamudi) getStudentCount( ) method ====")
student_with_most_quotes = quotes_list_object.getStudentWithMostQuotes()
print(student_with_most_quotes)

# ========= Anjneya Kumar: Method # 4 ========================
print("=== Method #4 (Anjneya Kumar) def getQuotesByAuthor( ) method ====")
mini_quote_collection = quotes_list_object.getQuotesByAuthor()
#mini_quote_collection.printQuotes()



# ========= Eshaan Dhavala: Method # 6 ========================
print("=== Method #6 (Eshaan Dhavala) def getAuthorAndQuoteCount( ) method ====")
author_count_dictionary = quotes_list_object.getAuthorAndQuoteCount()
pp.pprint(author_count_dictionary)



# ========= Jaya Varanasi: Method # 9 ========================
print("=== Method #9 (Jaya Varanasi) def showRandomQuoteInHTML( )method ====")
quotes_list_object.showRandomQuoteInHTML( )

#Opening a html file directly from a web browser 
#new = 2
#url = "file://c:/users/onedrive/Documents/showRandomQuoteInHtml.html"
#webbrowser.open(url,new=new)


# ========= Karthik Uppala: Method # 11 ========================
print("=== Method #11 (Karthik Uppala) def getSortedAuthors( )method ====")
sorted_authors_list_x = quotes_list_object.getSortedAuthors( )
print(sorted_authors_list_x)

# ========= Nikhita Gollamudi: Method # 13 ========================
print("=== Method #13.2 (Nikhita Gollamudi) getWordListByFrequency( ) method ====")
word_frequency = quotes_list_object.getWordListByFrequency()
pp.pprint(word_frequency)


print("=== Method #13.2 (Nikhita Gollamudi) getWordListByFrequency( ) method ====")
q1 = Quote(1, "Hello", "A1", "S1")
q2 = Quote(2, "How are you?", "A1", "S1")
q3 = Quote(3, "OK", "A1", "S1")
q4 = Quote(4, "Great", "A1", "S1")
q5 = Quote(5, "Good to know", "A1", "S1")
q6 = Quote(6, "TTYL", "A1", "S1")
q7 = Quote(7, "Bye now", "A1", "S1")
q8 = Quote(8, "See ya!", "A1", "S1")
q9 = Quote(9, "Bye Bye!", "A2", "S2")
quotes_list = [q1,q2,q3,q4,q5,q6,q7,q8, q9]
nikhita_QuotesList_object = QuotesList(quotes_list)
word_frequency = nikhita_QuotesList_object.getWordListByFrequency()
pp.pprint(word_frequency)

# ========= Soma Modukuri: Method # 14 ========================
print("=== Method #14 (Soma Modukuri) getCountOfQuotesByStudent(student_name)method ====")
student_name = "Jasthi"
quote_count = quotes_list_object.getCountOfQuotesByStudent(student_name)
print(quote_count)

student_name = "ABC"
quote_count = quotes_list_object.getCountOfQuotesByStudent(student_name)
print(quote_count)

# =================pranav manikonda #15======================
print("=== Method #15.1 (Pranav Manikonda) getRandomQuote method ====")
random_quote_1 = quotes_list_object.getRandomQuote()
print(random_quote_1)


print("=== Method #15.2  (Pranav Manikonda) getRandomQuote method ====")
q1 = Quote(1, "Hello", "A1", "S1")
q2 = Quote(2, "How are you?", "A1", "S1")
q3 = Quote(3, "OK", "A1", "S1")
q4 = Quote(4, "Great", "A1", "S1")
q5 = Quote(5, "Good to know", "A1", "S1")
q6 = Quote(6, "TTYL", "A1", "S1")
q7 = Quote(7, "Bye now", "A1", "S1")
q8 = Quote(8, "See ya!", "A1", "S1")
quotes_list = [q1,q2,q3,q4,q5,q6,q7,q8]
pranav_QuotesList_object = QuotesList(quotes_list)
random_quote_2 = pranav_QuotesList_object.getRandomQuote()
print(random_quote_2)

# =================pranav mukkara #16======================
print("=== Method #16 (Pranav mukkara) getCountOfQuotesByAuthor(author_count)method ====")
author_name = "unknown"
quote_count = quotes_list_object.getCountOfQuotesByAuthor(author_name)
print(quote_count)


# ========== Sahasra Tummala: Method #19 =================
print("=== Method #19.1  (Sahasra Tummala) getShortestQuote( ) method ====")
shortest_quotation = quotes_list_object.getShortestQuote( )
print(shortest_quotation)

print("=== Method #19.2  (Sahasra Tummala) getShortestQuote( ) method ====")
q1 = Quote(1, "Hello", "A1", "S1")
q2 = Quote(2, "How are you?", "A1", "S1")
q3 = Quote(3, "OK", "A1", "S1")
q4 = Quote(4, "Great", "A1", "S1")
quotes_list = [q1,q2,q3,q4]
my_own_QuotesList_object = QuotesList(quotes_list)
shortest_quotation = my_own_QuotesList_object.getShortestQuote( )
print(shortest_quotation)

# ========== Happy Josyula: Method #20 =================
print("=== Method #20  (Happy Josyula) getAuthorCount( ) method ====")
author_count = quotes_list_object.getAuthorCount( )
print(author_count)



# ========== Soma MOdukuri: Method #21 =================
print("=== Method #21.1  (Soma Modukuri) getLongestQuote( ) method ====")
longest_quote = quotes_list_object.getLongestQuote( )
print(longest_quote)


print("=== Method #21.2  (Soma Modukuri) getLongestQuote( ) method ====")
q1 = Quote(1, "Hello", "A1", "S1")
q2 = Quote(2, "How are you?", "A1", "S1")
q3 = Quote(3, "OK", "A1", "S1")
q4 = Quote(4, "Great", "A1", "S1")
quotes_list = [q1,q2,q3,q4]
my_own_QuotesList_object = QuotesList(quotes_list)
longest_quotation = my_own_QuotesList_object.getLongestQuote( )
print(longest_quotation)


# ========== Sravamti Manikonda: Method #22 =================
print("=== Method #22.1 (Sravamti Manikonda) getAuthorWithMostQuotes( ) method ====")
author_with_most_quotes = quotes_list_object.getAuthorWithMostQuotes()    
print(author_with_most_quotes)

print("=== Method #22.2  (Sravamti Manikonda) getAuthorWithMostQuotes( ) method ====")
q1 = Quote(1, "Hello", "A1", "S1")
q2 = Quote(2, "How are you?", "A1", "S1")
q3 = Quote(3, "OK", "A2", "S1")
q4 = Quote(4, "Great", "A3", "S1")
q5 = Quote(5, "OK", "A2", "S1")
q6 = Quote(6, "OK", "A2", "S1")
quotes_list = [q1,q2,q3,q4,q5, q6]
sravanti_QuotesList_object = QuotesList(quotes_list)
author_with_most_quotes = sravanti_QuotesList_object.getAuthorWithMostQuotes( )
print(author_with_most_quotes)


# ========= Sumedh Ghatti: Method # 24 ========================
print("=== Sumedh Ghatti: Method #24; def getQuotesContainingWord(input_word) method ====")
#TODO: you need to pass in a string here
#quotes_mini_collection = quotes_list_object.getQuotesContainingWord()
#quotes_mini_collection.printQuotes()

# ========= Vishnu Vundamati: Method # 26 ========================
print("===  Method #26 (Vikrant Datta) def getStudentListWithNoQuotes()  method ====")
students_list_with_no_quotes = quotes_list_object.getStudentListWithNoQuotes()
print(students_list_with_no_quotes)

# ========= Vishnu Vundamati: Method # 28 ========================
print("===  Method #28 (Vishnu Vundamati) def updateQuote(self, id, quote, author, submitted_by)  method ====")
update_status = quotes_list_object.updateQuote(2, "test_quote", "test_author", "test_submitted_by")
print(update_status)

# ========= Nikhitha Gollamudi: Method # 29 ========================
print("===  Method #29 (Nikhitha Gollamudi) def getQuotesContainingBadWords()  method ====")
mini_collection_29 = quotes_list_object.getQuotesContainingBadWords()
#mini_collection_29.printQuotes()


# ========= Nikhita Gollamudi: Method # 30 ========================
print("=== Nikhita Gollamudi: Method #30; saveToFile( ) method ====")
#quotes_list_object.saveToFile()


    
