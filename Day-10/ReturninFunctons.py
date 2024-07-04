def FormatName(fname,lname):
    if fname == "" or lname == "":
        return "You didnt provide valid input"
    
    f_name = fname
    l_name = lname
    
    full_name = f_name + " " +l_name
    
    return full_name.title()

fullName = FormatName("FIRAOL","ANBESSA")
print(fullName)