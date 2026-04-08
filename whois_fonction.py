import whois

def clean(variable):
    if isinstance(variable,list):
        return list(set(variable))
    else:
        return variable

def fwhois(domain ,full=False):
    inforamtion=whois.whois(domain)
    resulet={
        "creation_date ":clean(inforamtion.creation_date),
        "expiration_date ":clean(inforamtion.expiration_date),
        "name_servers ":clean(inforamtion.name_servers),
        "org ":clean(inforamtion.org),
        "country ":clean(inforamtion.country),
        "status ":clean(inforamtion.status),
    }
    if full:
        resulet.update({
            "domain :":clean(inforamtion.domain_name),
            "registrar :":clean(inforamtion.registrar),
            "registrar_url :":clean(inforamtion.registrar_url),
            "whois_server :":clean(inforamtion.whois_server),
            "updated_date :":clean(inforamtion.updated_date),
            "emails :":clean(inforamtion.emails),
            "dnssec :":clean(inforamtion.dnssec),
        })
    
    return resulet
