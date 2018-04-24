from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        ## Hosts
        
        host11 = self.addHost( 'h11',mac='00:00:00:00:00:11',ip='10.1.0.1/8' )
        host12 = self.addHost( 'h12',mac='00:00:00:00:00:12',ip='10.1.0.2/8' )
        host13 = self.addHost( 'h13',mac='00:00:00:00:00:13',ip='10.1.0.3/8' )
        host14 = self.addHost( 'h14',mac='00:00:00:00:00:14',ip='10.1.0.4/8' )
        
        host21 = self.addHost( 'h21',mac='00:00:00:00:00:21',ip='10.2.0.1/8' )
        host22 = self.addHost( 'h22',mac='00:00:00:00:00:22',ip='10.2.0.2/8' )
        host23 = self.addHost( 'h23',mac='00:00:00:00:00:23',ip='10.2.0.3/8' )
        host24 = self.addHost( 'h24',mac='00:00:00:00:00:24',ip='10.2.0.4/8' )
        
        ## Switches
        switch01 = self.addSwitch( 's01' )
        switch02 = self.addSwitch( 's02' )
        switch03 = self.addSwitch( 's03' )
        switch04 = self.addSwitch( 's04' )

        switch11 = self.addSwitch( 's11' )
        switch12 = self.addSwitch( 's12' )
        switch13 = self.addSwitch( 's13' )
        switch14 = self.addSwitch( 's14' )

        switch21 = self.addSwitch( 's21' )
        switch22 = self.addSwitch( 's22' )
        switch23 = self.addSwitch( 's23' )
        switch24 = self.addSwitch( 's24' )

        # Add links
        self.addLink( switch01, switch11 )
        self.addLink( switch01, switch13 )
        
        self.addLink( switch02, switch11 )
        self.addLink( switch02, switch13 )
        
        self.addLink( switch03, switch12 )
        self.addLink( switch03, switch14 )
        
        self.addLink( switch04, switch12 )
        self.addLink( switch04, switch14 )

        ##################################

        self.addLink( switch11, switch21 )
        self.addLink( switch11, switch22 )
        self.addLink( switch12, switch21 )
        self.addLink( switch12, switch22 )

        self.addLink( switch13, switch23 )
        self.addLink( switch13, switch24 )
        self.addLink( switch14, switch23 )
        self.addLink( switch14, switch24 )


        ##################################

        self.addLink( host11, switch21 )
        self.addLink( host12, switch21 )
        self.addLink( host13, switch22 )
        self.addLink( host14, switch22 )

        self.addLink( host21, switch23 )
        self.addLink( host22, switch23 )
        self.addLink( host23, switch24 )
        self.addLink( host24, switch24 )

topos = { 'mytopo': ( lambda: MyTopo() ) }
