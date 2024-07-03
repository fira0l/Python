def FormatName(fname,lname):
    f_name = fname
    l_name = lname
    
    full_name = f_name + " " +l_name
    
    return full_name.title()

fullName = FormatName("FIRAOL","ANBESSA")
print(fullName)