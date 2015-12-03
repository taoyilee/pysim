import re
import logging
import components.source as source

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

def parse_voltageSource(line):
	return match_g1(line, 'V', source.voltage_source)

def parse_currentSource(line):
	return match_g2(line, 'I', source.current_source)

def parse_resistor(line):
	return match_g2(line, 'R', source.resistor)

def parse_capacitor(line):
	return match_g2(line, 'C', source.capacitor)

def parse_inductor(line):
	return match_g1(line, 'L', source.inductor)

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
		dinst = re.match('(D\d+)\s+(\d+)\s+(\d+)',line)
		dinstval = re.match('(D\d+)\s+(\d+)\s+(\d+)\s+([\de\.]*)',line)
		
		qninstval = re.match('(QN\d+)\s+(d+)\s+(\d+)\s+(\d+)\s+([\de\.]*)',line)
		qpinstval = re.match('(QP\d+)\s+(d+)\s+(\d+)\s+(\d+)\s+([\de\.]*)',line)
		mninstval = re.match('(MN\d+)\s+(d+)\s+(\d+)\s+(\d+)\s+([\de\.]*)',line)
		mpinstval = re.match('(MP\d+)\s+(d+)\s+(\d+)\s+(\d+)\s+([\de\.]*)',line)

		qninst = re.match('(QN\d+)\s+(d+)\s+(\d+)\s+(\d+)\s+',line)
		qpinst = re.match('(QP\d+)\s+(d+)\s+(\d+)\s+(\d+)\s+',line)
		mninst = re.match('(MN\d+)\s+(d+)\s+(\d+)\s+(\d+)\s+',line)
		mpinst = re.match('(MP\d+)\s+(d+)\s+(\d+)\s+(\d+)\s+',line)

	logger.debug(dev_list)
