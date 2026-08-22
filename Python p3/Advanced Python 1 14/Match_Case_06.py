# MATCH CASE - COMPLETE REFERENCE
# =================================
# WHAT: Match case is a cleaner alternative to if elif else
# WHEN: Use when you have many conditions on same variable
#       Match case was introduced in Python 3.10 and above
# HOW:  match variable then case for each value
#       case _ is default case - runs when nothing else matches


def http_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Error Found"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unknown Status"


print(http_status(500))
