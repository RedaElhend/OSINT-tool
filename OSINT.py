#start 4/6/2026
# end  

import whois
import argparse
# libreri to use re.match and r' '
import re
# check if the domain is valide by tek the domain entre bby the user
# and comperte to pattern 
def check_validition_domain(domain):
    pattern = r'^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(pattern,domain):
        raise ValueError(f"errer :\' {domain} \' is not a doain name ")
    return domain
#------------------------------------------------------------------
# CLI code 
parser = argparse.ArgumentParser(
    description="port scaning"
)
parser.add_argument(
    '-d' , '--domain'  ,
    required=True       ,
    help="domain whant to scan"
)
parser.add_argument(
    '-f','--full'   ,
    action="",
    help="scan evrything "
)
parser.add_argument(
    "--output",
    help="were you want to save the result"
)
args = parser.parse_args()
#------------------------------------------------------------------
# check if the domain is writhe
