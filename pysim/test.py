import parser
import logging
import mnabuilder

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
comp_list = parser.parse_netlist('netlist.net')

mnabuilder.mnabuilder(comp_list)
