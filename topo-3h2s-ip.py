from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        host1 = self.addHost( 'h1',mac='00:00:00:00:00:01',ip='10.0.0.1/8' )
        host2 = self.addHost( 'h2',mac='00:00:00:00:00:02',ip='10.0.0.2/8' )
        host3 = self.addHost( 'h3',mac='00:00:00:00:00:03',ip='10.0.0.3/8' )
        switch1 = self.addSwitch( 's1' )
        switch2 = self.addSwitch( 's2' )

        # Add links
        self.addLink( host1, switch1 )
        self.addLink( host2, switch1 )
        self.addLink( host3, switch2 )
        self.addLink( switch1, switch2 )


topos = { 'mytopo': ( lambda: MyTopo() ) }
