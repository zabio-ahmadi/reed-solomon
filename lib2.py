
import re
class polynom:
    def __init__(self, polstr) -> None:
        self.polstr = polstr
        self.monoms = self.eval_monoms()
    
    def eval_monoms(self):

        start = 0
        end = 0
        lst = list()
        for ch in self.polstr:
            if ch == '+' or ch == '-':
                lst.append(self.polstr[start:end])
                start = end
            end +=1
        lst.append(self.polstr[start:end])

        monom_list = list()
        for monom in lst:
                       
            monom = monom.replace(" ", "")

        
            if monom.find("+") == -1 and monom.find('-') == -1 and len(monom) > 0:
                monom = "+" + monom

            splited = re.split("[x-z].{1}", monom)


            dic = dict() 
            if len(splited) == 2:

                if len(splited[0]) == 1:
                    dic["coef"] = splited[0] + '1'

                if len(splited[0]) > 1:
                    dic["coef"] = splited[0]

                dic["pow"] = splited[1]
            if len(splited) == 1 and len(splited[0]) > 0:
                
                dic["coef"] = splited[0]
                dic["pow"] = 0

            if len(dic) > 0:
                monom_list.append(dic) 
            

        monom_list = sorted(monom_list, key=lambda x: int(x["pow"]), reverse=True)
        return monom_list
    

def pol_to_str(dict_pol):
    result = ''
    for mon in dict_pol:
        if mon["pow"]  == '0':
            result += str(mon["coef"])
        else : 
            result += str(mon["coef"]) + 'x' + '^' + str(mon["pow"])

    return result


def add_tow_polynomes(str_pol1, str_pol2):

    pol1 = polynom(str_pol1)
    pol1_monoms = pol1.monoms


    pol2 = polynom(str_pol2)
    pol2_monoms = pol2.monoms


    new_list = list()
    for i in pol1_monoms:

        for j in pol2_monoms:

            if i["pow"] == j['pow']:
                dic = dict()
                new_coef = int(i["coef"]) + int(j["coef"])
                dic["coef"] = new_coef
                dic["pow"]  = i["pow"]
                new_list.append(dic)
    

    lst = []
    for monom in new_list:
        lst.append(int(monom['pow']))

    filtered_pol1monoms = list(filter(lambda monoms: int(monoms["pow"]) not in lst, pol1_monoms))

    
    filtered_pol2monoms = list(filter(lambda monoms: int(monoms["pow"]) not in lst, pol2_monoms))


    new_list = new_list + filtered_pol1monoms + filtered_pol2monoms # combine 

    new_list = sorted(new_list, key=lambda x: int(x["pow"]), reverse=True)# sort

    return new_list





def sub_tow_polynomes(str_pol1, str_pol2):

    pol1 = polynom(str_pol1)
    pol1_monoms = pol1.monoms


    pol2 = polynom(str_pol2)
    pol2_monoms = pol2.monoms


    new_list = list()
    for i in pol1_monoms:

        for j in pol2_monoms:

            if i["pow"] == j['pow']:
                dic = dict()
                new_coef = int(i["coef"]) - int(j["coef"])
                dic["coef"] = new_coef
                dic["pow"]  = i["pow"]
                new_list.append(dic)
    

    lst = []
    for monom in new_list:
        lst.append(int(monom['pow']))

    filtered_pol1monoms = list(filter(lambda monoms: int(monoms["pow"]) not in lst, pol1_monoms))

    
    filtered_pol2monoms = list(filter(lambda monoms: int(monoms["pow"]) not in lst, pol2_monoms))


    new_list = new_list + filtered_pol1monoms + filtered_pol2monoms # combine 

    new_list = sorted(new_list, key=lambda x: int(x["pow"]), reverse=True)# sort

    return new_list


def multiply_tow_polynomes(str_pol1, str_pol2):

    pol1 = polynom(str_pol1)
    pol1_monoms = pol1.monoms


    pol2 = polynom(str_pol2)
    pol2_monoms = pol2.monoms

    new_list = list()
    for i in pol1_monoms:
        for j in pol2_monoms:

            i_coef = int(i["coef"])
            j_coef = int(j["coef"])
            if i["pow"] == '0':
                i_pow = 1
            else : 
                i_pow = int(i["pow"])
            
            if j['pow'] == '0':
                j_pow = 1
            else:
                j_pow = int(j["pow"])

            dic = dict()
            dic["coef"] = i_coef * j_coef
            dic["pow"] = i_pow + j_pow
            new_list.append(dic)

    new_list = sorted(new_list, key=lambda x: int(x["pow"]), reverse=True)# sort
    return new_list

            
        


        
mult = multiply_tow_polynomes('2x^3 - x^2','3x^2')

result = pol_to_str(mult)

print(result)

# print(rr)