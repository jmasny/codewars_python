# You have to extract a portion of the file name as follows:
#
#     Assume it will start with date represented as long number
#     Followed by an underscore
#     You'll have then a filename with an extension
#     it will always have an extra extension at the end
#
# Inputs:
#
# 1231231223123131_FILE_NAME.EXTENSION.OTHEREXTENSION
#
# 1_This_is_an_otherExample.mpg.OTHEREXTENSIONadasdassdassds34
#
# 1231231223123131_myFile.tar.gz2
#
# Outputs
#
# FILE_NAME.EXTENSION
#
# This_is_an_otherExample.mpg
#
# myFile.tar
#
# Acceptable characters for random tests:
#
# abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-0123456789
#
# The recommended way to solve it is using RegEx and specifically groups.

class FileNameExtractor:
    def extract_file_name(self, dirty_file_name):

        underscore = dirty_file_name.find('_')
        dirty_file_name = dirty_file_name[underscore+1:]

        dot_one = dirty_file_name.find('.')
        first = dirty_file_name[:dot_one]
        dirty_file_name = dirty_file_name[dot_one+1:]

        dot_two = dirty_file_name.find('.')
        second = dirty_file_name[:dot_two]

        return first + '.' + second


fnx = FileNameExtractor()
print(fnx.extract_file_name("1_FILE_NAME.EXTENSION.OTHEREXTENSIONadasdassdassds34"))  #"FILE_NAME.EXTENSION"
