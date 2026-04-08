import dns.resolver

def StringObject (v):
    if isinstance(v,str):
        return v
    else:
        result=[]
        for r in v:
            result.append(str(r))
        return result

def resolve_dns(domain,record_type):
    try:
        result=dns.resolver.resolve(domain,record_type)
        return StringObject(result)
    except Exception as e:
        return [f"erreur : {e}"]
    



def fdns(domain,full=False):
    try:
        result={
            "A":StringObject(resolve_dns(domain,"A")),
            "MX":StringObject(resolve_dns(domain,"MX")),
            "NS":StringObject(resolve_dns(domain,"NS")),
        }
        if full:
            result.update({
                "TXT":StringObject(resolve_dns(domain,"TXT")),
                "CNAME": StringObject(resolve_dns(domain,"CNAME")),
                "AAAA": StringObject(resolve_dns(domain, "AAAA")),
                "SOA": StringObject(resolve_dns(domain, "SOA")),
            })
    except Exception as e:
        print(f"erreur : {e}")
        return {}
    else:
        return result