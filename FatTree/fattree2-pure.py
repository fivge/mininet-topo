from mininet.topo import Topo
import logging
import os

# logging.basicConfig(filename='./fattree.log', level=logging.DEBUG)
# logger = logging.getLogger(__name__)

class FatTree( Topo ):
  
    CoreSwitchList = []
    AggSwitchList = []
    EdgeSwitchList = []
    HostList = []
 
    def __init__( self, k):
        " Create Fat Tree topo."
        self.pod = k
        self.iCoreLayerSwitch = (k/2)**2
        self.iAggLayerSwitch = k*k/2
        self.iEdgeLayerSwitch = k*k/2
        self.density = k/2
        self.iHost = self.iEdgeLayerSwitch * self.density
        
        self.bw_c2a = 0.2
        self.bw_a2e = 0.1
        self.bw_h2a = 0.05

        # Init Topo
        Topo.__init__(self)
  
        self.createTopo()
        # logger.debug("Finished topology creation!")

        self.createLink( bw_c2a=self.bw_c2a, 
                         bw_a2e=self.bw_a2e, 
                         bw_h2a=self.bw_h2a)
        # logger.debug("Finished adding links!")

    #    self.set_ovs_protocol_13()
    #    logger.debug("OF is set to version 1.3!")  
    
    def createTopo(self):
        self.createCoreLayerSwitch(self.iCoreLayerSwitch)
        self.createAggLayerSwitch(self.iAggLayerSwitch)
        self.createEdgeLayerSwitch(self.iEdgeLayerSwitch)
        self.createHost(self.iHost)

    """
    Create Switch and Host
    """

    def _addSwitch(self, number, level, switch_list):
        for x in xrange(1, number+1):
            PREFIX = str(level) + "00"
            if x >= int(10):
                PREFIX = str(level) + "0"
            switch_list.append(self.addSwitch('s' + PREFIX + str(x)))

    def createCoreLayerSwitch(self, NUMBER):
        self._addSwitch(NUMBER, 1, self.CoreSwitchList)

    def createAggLayerSwitch(self, NUMBER):
        self._addSwitch(NUMBER, 2, self.AggSwitchList)

    def createEdgeLayerSwitch(self, NUMBER):
        self._addSwitch(NUMBER, 3, self.EdgeSwitchList)

    def createHost(self, NUMBER):
        for x in xrange(1, NUMBER+1):
            PREFIX = "h00"
            if x >= int(10):
                PREFIX = "h0"
            elif x >= int(100):
                PREFIX = "h"
            self.HostList.append(self.addHost(PREFIX + str(x)))

    """
    Add Link
    """
    def createLink(self, bw_c2a=1024, bw_a2e=200, bw_h2a=100):
        # logger.debug("Add link Core to Agg.")
        end = self.pod/2
        for x in xrange(0, self.iAggLayerSwitch, end):
            for i in xrange(0, end):
                for j in xrange(0, end):
                    self.addLink(
                        self.CoreSwitchList[i*end+j],
                        self.AggSwitchList[x+i])

        # logger.debug("Add link Agg to Edge.")
        for x in xrange(0, self.iAggLayerSwitch, end):
            for i in xrange(0, end):
                for j in xrange(0, end): 
                    self.addLink(
                        self.AggSwitchList[x+i], self.EdgeSwitchList[x+j])

        # logger.debug("Add link Edge to Host.")
        for x in xrange(0, self.iEdgeLayerSwitch):
            for i in xrange(0, self.density):
                self.addLink(
                    self.EdgeSwitchList[x],
                    self.HostList[self.density * x + i])
        
topos = { 'fattree' : ( lambda k : FatTree(k)) }

