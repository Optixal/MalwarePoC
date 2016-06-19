#!/usr/bin/python
# Optixal, 13 Jun 2016

import subprocess, sys, optparse, argparse
import coloredstatus as cs

def nmap_network(subnet_bits = None, port = None, state = None):

    subnet_bits = "/" + subnet_bits

    get_ip = "hostname -I"
    process_ip = subprocess.Popen(get_ip, shell=True, stdout=subprocess.PIPE)
    (ip, error) = process_ip.communicate()
    subnet = ip.strip() + subnet_bits

    if port == None:
        nmap_cmd = "nmap -T4 -n -sn -oG - " + subnet + " | grep -v \\# | awk '{print $2}'"
    else:
        nmap_cmd = "nmap -T4 -n -p " + port + " -oG - " + subnet + " | grep " + port + "/" + state + " | awk '{print $2}'"

    process_nmap = subprocess.Popen(nmap_cmd, shell=True, stdout=subprocess.PIPE)
    (nmap_result, error) = process_nmap.communicate()
    return nmap_result

def main():
    parser = argparse.ArgumentParser(description="Speed scans a network subnet for online hosts with nmap")
    parser.add_argument("-b", "--subnetbits", help="Subnet bit to use for scan (e.g. 24)", metavar="", default="24")
    parser.add_argument("-p", "--port", help="Port to scan for (e.g. 443)", metavar="",)
    parser.add_argument("-s", "--state", help="Port state to look for (e.g. open, filtered or closed)", choices=["open", "filtered", "closed"], metavar="", default="open")
    parser.add_argument("-o", "--output", help="Output file location (e.g. scan.txt)", metavar="",)
    args = parser.parse_args()

    cs.print_status("Scanning network subnet for online machines...")

    if args.output:
        output_file = open(args.output, 'w')
        output_file.write(nmap_network(port=args.port, state=args.state, subnet_bits=args.subnetbits))
        output_file.close()
        cs.print_good("Successfully saved targets to " +  args.output)
    else:
        result = nmap_network(port=args.port, state=args.state, subnet_bits=args.subnetbits)
        print "\n" + result
        cs.print_good("Successful, found a total of " + str(len(result.splitlines())) + " online machines.")

if __name__ == "__main__":
    main()