import whois

def clean(variable):
    if isinstance(variable,list):
        return list(set(variable))
    else:
        return variable

def fwhois(domain ,full=False):
    information=whois.whois(domain)
    result={
        "creation_date":clean(information.creation_date),
        "expiration_date":clean(information.expiration_date),
        "name_servers":clean(information.name_servers),
        "org":clean(information.org),
        "country":clean(information.country),
        "status":clean(information.status),
    }
    if full:
        result.update({
            "domain":clean(information.domain_name),
            "registrar":clean(information.registrar),
            "registrar_url":clean(information.registrar_url),
            "whois_server":clean(information.whois_server),
            "updated_date":clean(information.updated_date),
            "emails":clean(information.emails),
            "dnssec":clean(information.dnssec),
        })
    
    return result
