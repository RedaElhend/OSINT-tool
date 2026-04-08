#start 4/6/2026
# end  
import whois_fonction
import argparse
# libreri to use re.match and r' '
import re


# check if the domain is valide by tek the domain entre by the user
# and comperte to pattern 
def check_validition_domain(domain):
    pattern = r'^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(pattern,domain):
        raise argparse.ArgumentTypeError(f"errer :\' {domain} \' is not a doain name ")
    return domain
#------------------------------------------------------------------
# CLI code 
parser = argparse.ArgumentParser(
    description="port scaning"
)
parser.add_argument(
    '-d' , '--domain'  ,
    required=True       ,
    # type mean before storing this value, run it through this function first
    type=check_validition_domain,
    help="domain whant to scan",
)
parser.add_argument(
    '-f','--full'   ,
    # action mean if he writhe arg.full == TRUE if not arg.full == False
    action='store_true' ,
    help="scan evrything "
)
parser.add_argument(
    "--output",
    help="were you want to save the result"
)
args = parser.parse_args()
#------------------------------------------------------------------
#print the information with whois libreri
try:
   information =whois_fonction.fwhois(args.domain,args.full)
   for key , value in  information.items():
       print(f"{key:15} : {value}" ,end="\n\n")
except Exception as e :
    print(e)



