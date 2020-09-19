import re 
import argparse

class INI_parser:
    def __init__(self, path):
        file_type = re.split(r'[.]', path)[-1]
        try:
            if file_type != 'ini':
                raise Exception()

            self.path_ = path
        except:
            print("Wrong file format")
    

    def Read_INI(self):
        try:
            if self.path_ != 0:
                f = open(self.path_)
            else:
                raise IOError()
            text = f.read().split('\n\n' )
        
        
            all_sect = {}

            for sect in text:
                sect_name = ''
                options = {}
                sect_parsed = sect.split('\n')
                for el in sect_parsed:
                    
                    #finding section name
                    res = re.split(r'[;]', el, maxsplit=1)[0]  
                    sect_name_tmp = re.findall(r'\[([A-Za-z0-9_]+)\]', res)

                    if sect_name_tmp:
                        sect_name = sect_name_tmp
                    elif res:

                        if sect_name == '' and res != '':
                            print(res)
                            raise Exception()

                        #separating option and value
                        option_n, value = re.split(r'=', res, maxsplit=1)
                        option_n = option_n.strip()
                        value = value.strip()

                        #defining type
                        if re.search(r'^(-?\d+)$', value) != None:
                            value = int(value)
                        elif re.search(r'^(-?\d+\.\d+)$', value) != None:
                            value = float(value)

                        if option_n:
                            options[option_n] = value

                if sect_name:
                    all_sect[sect_name[0]] = options
            
            self.sections_ = all_sect
            
        except IOError:
            print("File that you are trying to find doesn't exist")
        except Exception:
            print("File that you are trying to read has wrong structure.")
        

    def Get_Val(self, sect_name, opt_name, dtype):
        try:
            val = self.sections_[sect_name][opt_name]
            try:
                if str(type(val)) != f"<class '{dtype}'>":
                    raise Exception()

                return val
            except Exception:
                print("Value with data type that you are trying to get doesn't exist")

        except KeyError:
            print("Section or option that you are trying to find doesn't exist")

        

    path_ = 0 
    sections_ = {}


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--path-for-ini-file", required=True, type=str)
    parser.add_argument("-s", "--section", required=True, type=str)
    parser.add_argument("-o", "--option", required=True, type=str)
    parser.add_argument("-t", "--type", required=True, type=str)
    return parser.parse_args()

    
args = parse_args()

ini_pars = INI_parser(args.path_for_ini_file)
ini_pars.Read_INI()
val = ini_pars.Get_Val(args.section, args.option, args.type)
print(val)


# regular expression for section parsing
# otion out of section
