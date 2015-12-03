import re
import logging
from components.voltage_source import voltage_source
from components.current_source import current_source
from components.resistor import resistor
from components.capacitor import capacitor
from components.inductor import inductor
from components.diode import diode
from components.mosfet import mosfet
from components.bjt import bjt

logger = logging.getLogger(__name__)
ch = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

def match_g1(line, prefix, class_header):
	inst = re.match('(' + prefix + '\d+)\s+(\d+)\s+(\d+)\s+([\de\.]*)',line)
	if inst:
		logger.debug('match('+ prefix +')->' + inst.group(1))
		return	class_header(inst.group(1),inst.group(2),inst.group(3),inst.group(4))
	else:
		return None

def match_g2(line, prefix, class_header):
	instg1 = re.match('(' + prefix + '\d+)\s+(\d+)\s+(\d+)\s+([\de\.]*)',line)
	instg2 = re.match('(' + prefix +'\d+)\s+(\d+)\s+(\d+)\s+([\de\.]*)\s+G2',line)
	if instg1:
		if instg2:
			logger.debug('match(' + prefix +'G2)->' + instg2.group(1))
			return	class_header(instg2.group(1),instg2.group(2),instg2.group(3),instg2.group(4), 1)
		else:
			logger.debug('match(' + prefix + ')->' + instg1.group(1))
			return	class_header(instg1.group(1),instg1.group(2),instg1.group(3),instg1.group(4), 0)
	else:
		return None

def match_g3(line, prefix, class_header):
	inst = re.match('(' + prefix + '\d+)\s+(\d+)\s+(\d+)\s+',line)
	instval = re.match('(' + prefix + '\d+)\s+(\d+)\s+(\d+)\s+([\de\.]*)',line)
	if inst:
		if instval:
			logger.debug('match('+ prefix +')->' + instval.group(1))
			return	class_header(instval.group(1),instval.group(2),instval.group(3),instval.group(4))
		else:
			logger.debug('match('+ prefix +')->' + inst.group(1))
			return	class_header(inst.group(1),inst.group(2),inst.group(3),None)
	else:
		return None

def match_g4(line, prefix, class_header):
	inst = re.match('(' + prefix + ')(\w)(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+',line)
	instval = re.match('(' + prefix + ')(\w)(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+([\de\.]*)',line)
	if inst:
		if instval:
			logger.debug('match('+ prefix +')->' + instval.group(1) + instval.group(2)+ instval.group(3))
			return	class_header(instval.group(1)+ instval.group(2)+ instval.group(3), 
				instval.group(2),instval.group(4),instval.group(5),instval.group(6))
		else:
			logger.debug('match('+ prefix +')->' + inst.group(1))
			return	class_header(inst.group(1)+ instval.group(2)+ instval.group(3),
				inst.group(4),inst.group(5),instval.group(4),None)
	else:
		return None

def parse_voltageSource(line):
	return match_g1(line, 'V', voltage_source)

def parse_currentSource(line):
	return match_g2(line, 'I', current_source)

def parse_resistor(line):
	return match_g2(line, 'R', resistor)

def parse_capacitor(line):
	return match_g2(line, 'C', capacitor)

def parse_inductor(line):
	return match_g1(line, 'L', inductor)

def parse_diode(line):
	return match_g3(line, 'D', diode)

def parse_mosfet(line):
	return match_g4(line, 'M', mosfet)

def parse_bjt(line):
	return match_g4(line, 'Q', bjt)

def parse_netlist(file_name):
	f = open(file_name, 'r')
	dev_list = []

	for line in f:
		logger.debug(line.rstrip())	
		vinst = parse_voltageSource(line)
		if vinst:
			dev_list.append(vinst)	

		iinst = parse_currentSource(line)
		if iinst:
			dev_list.append(iinst)	

		cinst = parse_capacitor(line)
		if cinst:
			dev_list.append(cinst)	

		rinst = parse_resistor(line)
		if rinst:
			dev_list.append(rinst)	

		linst = parse_inductor(line)
		if linst:
			dev_list.append(linst)	

		dinst = parse_diode(line)
		if dinst:
			dev_list.append(dinst)	

		qinst = parse_bjt(line)
		if qinst:
			dev_list.append(qinst)	

		minst = parse_mosfet(line)
		if qinst:
			dev_list.append(minst)	

	logger.debug(dev_list)
