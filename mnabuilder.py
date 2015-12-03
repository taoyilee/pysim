import logging
from Abpair import Abpair
import numpy as np 

logger = logging.getLogger(__name__)
ch = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

def mnabuilder(componentList):
	for comp in componentList:
		logger.debug(comp)
	Abp = Abpair(np.array([[3,1], [1,2]]),  np.array([9,8]))
	sol = Abp.solve()
	logger.debug(sol)
	return Abp

