################################
# Creating re-usable function #
###############################


def upper_case_name(name):
    return name.upper()


# this will only run if this file is the current file been run
if __name__ == "__main__":
    print(upper_case_name("Yemi"))
    print(f"dunder name {__name__}")
