def passports():
    try:
        while True:
            line = input()
            d = dict()
            while len(line.strip()) != 0: # empty line
                fields = line.split()
                d.update(dict(field.split(':') for field in fields))
                line = input() # will fail for last pasport
            yield d
    except EOFError:
        yield d # last passport 
        return

def valid(passport):
    if any(key not in passport for key in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]): return False
    byr, iyr, eyr, hgt, hcl, ecl, pid = (passport[key] for key in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])
    byr_valid = len(byr) == 4 and 1920 <= int(byr) <= 2002
    iyr_valid = len(iyr) == 4 and 2010 <= int(iyr) <= 2020
    eyr_valid = len(eyr) == 4 and 2020 <= int(eyr) <= 2030
    hgt_valid = (
        150 <= int(hgt[:-2]) <= 193 if hgt.endswith("cm") else 
        59 <= int(hgt[:-2]) <= 76 if hgt.endswith("in") else
        False
        )
    try: hcl_valid = hcl.startswith("#") and len(hcl[1:]) == 6; int(hcl[1:], base=16)
    except: hcl_valid = False
    ecl_valid = ecl in "amb blu brn gry grn hzl oth".split()
    try: pid_valid = len(pid) == 9; int(pid)
    except: pid_valid = False
    
    return byr_valid and iyr_valid and eyr_valid and hgt_valid and hcl_valid and ecl_valid and pid_valid



print(sum(valid(passport) for passport in passports()))


