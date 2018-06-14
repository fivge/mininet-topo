"""Custom topology example

Two directly connected switches plus a host for each switch:

   host --- switch --- switch --- host

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import CPULimitedHost
from mininet.link import TCLink
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        host1 = self.addHost( 'h1',mac='00:00:00:00:00:01',ip='10.0.0.1/24' )
        host2 = self.addHost( 'h2',mac='00:00:00:00:00:02',ip='10.0.0.2/24' )
        host3 = self.addHost( 'h3',mac='00:00:00:00:00:03',ip='10.0.0.3/24' )
        host4 = self.addHost( 'h4',mac='00:00:00:00:00:04',ip='10.0.0.4/24' )

        switch1 = self.addSwitch( 's1' , protocols='OpenFlow13')
        switch2 = self.addSwitch( 's2' , protocols='OpenFlow13')
        switch3 = self.addSwitch( 's3' , protocols='OpenFlow13')
        switch4 = self.addSwitch( 's4' , protocols='OpenFlow13')

        # Add links
        self.addLink( host1, switch1, 0, 1)
        self.addLink( host2, switch1, 0, 2)
        self.addLink( switch1, switch2, 3, 1)
        self.addLink( switch1, switch3, 4, 1)
        self.addLink( switch3, switch4, 2, 1)
        self.addLink( switch2, switch4, 2, 2)
        self.addLink( host3, switch4, 0, 3)
        self.addLink( host4, switch4, 0, 4)


topos = { 'mytopo': ( lambda: MyTopo() ) }
