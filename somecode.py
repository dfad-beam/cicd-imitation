#-----------------------|
# Import Python Modules |
#-----------------------|
import sys
from optparse import OptionParser

#--------------------------|
# Main Program Starts Here |
#--------------------------|
# Command Line Arguments Parser
cmd_parser = OptionParser(version = "%prog 0.2")
cmd_parser.add_option("-C", "--core", action = "store", dest = "core", help = "Set the Core")
cmd_parser.add_option("-q", "--qps", action = "store_true", dest = "qps", help = "Get QPS information of the SOLR Server")
cmd_parser.add_option("-r", "--requesttime", action = "store_true", dest = "tpr", help = "Get Average Time Per Requests")
cmd_parser.add_option("-d", "--doc", action = "store_true", dest = "doc", help = "Get Docs information of the SOLR Server", default = True)
cmd_parser.add_option("-H", "--host", type = "string", action = "store", dest = "solr_server", help = "SOLR Server IPADDRESS")
cmd_parser.add_option("-p", "--port", type = "string", action = "store", dest = "solr_server_port", help = "SOLR Server port", default = 8983)
cmd_parser.add_option("-w", "--warning", type = "float", action = "store", dest = "warning_per",
                      help = "Exit with WARNING status if higher than the PERCENT of CPU Usage", metavar = "Warning Percentage")
cmd_parser.add_option("-c", "--critical", type = "float", action = "store", dest = "critical_per",
                      help = "Exit with CRITICAL status if higher than the PERCENT of CPU Usage", metavar = "Critical Percentage")
(cmd_options, cmd_args) = cmd_parser.parse_args()
# Check the Command syntax
if not (cmd_options.warning_per and cmd_options.critical_per and cmd_options.solr_server and cmd_options.solr_server_port):
    cmd_parser.print_help()
    sys.exit(3)



