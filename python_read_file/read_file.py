from calendar import prcal


class _file:
    def __init__(self):         # we read the file and extract the words.We create a list and throw it into it.


        with open("readme.txt","r",encoding="UTF-8") as file:


            file_content=file.read()
            words=file_content.split()
            self.just_words= list()


            for i in words:
                i=i.strip("\n")
                i=i.strip(",")
                i=i.strip(" ")
                i=i.strip(".")
                
                self.just_words.append(i)
            

    def all_words(self):
        word_set=set()
        
        for i in self.just_words:
            word_set.add(i)
        
        _word=input("enter the searched word (for exit, type exit): ")
        while(_word!="exit"):
            if(_word in word_set):
                print("The searched word is here.")
                _word=input("enter the searched word (for exit, type exit): ")
                if(_word=="exit"):
                    break
            else:
                print("The searched word is not here.")
                _word=input("enter the searched word (for exit, type exit): ")
                if(_word=="exit"):
                    break
                
                

    





dosya=_file()

dosya.all_words()

        
    
    