import parser
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

parser.parse_netlist('netlist.net')
