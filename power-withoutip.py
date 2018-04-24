from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        ## Hosts
        
        host11 = self.addHost( 'h11',mac='00:00:00:00:00:11' )
        host12 = self.addHost( 'h12',mac='00:00:00:00:00:12' )
        host13 = self.addHost( 'h13',mac='00:00:00:00:00:13' )
        host14 = self.addHost( 'h14',mac='00:00:00:00:00:14' )
        
        host21 = self.addHost( 'h21',mac='00:00:00:00:00:21' )
        host22 = self.addHost( 'h22',mac='00:00:00:00:00:22' )
        host23 = self.addHost( 'h23',mac='00:00:00:00:00:23' )
        host24 = self.addHost( 'h24',mac='00:00:00:00:00:24' )
        
        host31 = self.addHost( 'h31',mac='00:00:00:00:00:31' )
        host32 = self.addHost( 'h32',mac='00:00:00:00:00:32' )
        host33 = self.addHost( 'h33',mac='00:00:00:00:00:33' )
        host34 = self.addHost( 'h34',mac='00:00:00:00:00:34' )
        
        host41 = self.addHost( 'h41',mac='00:00:00:00:00:41' )
        host42 = self.addHost( 'h42',mac='00:00:00:00:00:42' )
        host43 = self.addHost( 'h43',mac='00:00:00:00:00:43' )
        host44 = self.addHost( 'h44',mac='00:00:00:00:00:44' )
        ## Switches
        switch01 = self.addSwitch( 's01' )
        switch02 = self.addSwitch( 's02' )
        switch03 = self.addSwitch( 's03' )
        switch04 = self.addSwitch( 's04' )

        switch11 = self.addSwitch( 's11' )
        switch12 = self.addSwitch( 's12' )
        switch13 = self.addSwitch( 's13' )
        switch14 = self.addSwitch( 's14' )
        switch15 = self.addSwitch( 's15' )
        switch16 = self.addSwitch( 's16' )
        switch17 = self.addSwitch( 's17' )
        switch18 = self.addSwitch( 's18' )

        switch21 = self.addSwitch( 's21' )
        switch22 = self.addSwitch( 's22' )
        switch23 = self.addSwitch( 's23' )
        switch24 = self.addSwitch( 's24' )
        switch25 = self.addSwitch( 's25' )
        switch26 = self.addSwitch( 's26' )
        switch27 = self.addSwitch( 's27' )
        switch28 = self.addSwitch( 's28' )

        # Add links
        self.addLink( switch01, switch11 )
        self.addLink( switch01, switch13 )
        self.addLink( switch01, switch15 )
        self.addLink( switch01, switch17 )
        
        self.addLink( switch02, switch11 )
        self.addLink( switch02, switch13 )
        self.addLink( switch02, switch15 )
        self.addLink( switch02, switch17 )
        
        self.addLink( switch03, switch12 )
        self.addLink( switch03, switch14 )
        self.addLink( switch03, switch16 )
        self.addLink( switch03, switch18 )
        
        self.addLink( switch04, switch12 )
        self.addLink( switch04, switch14 )
        self.addLink( switch04, switch16 )
        self.addLink( switch04, switch18 )

        ##################################

        self.addLink( switch11, switch21 )
        self.addLink( switch11, switch22 )
        self.addLink( switch12, switch21 )
        self.addLink( switch12, switch22 )

        self.addLink( switch13, switch23 )
        self.addLink( switch13, switch24 )
        self.addLink( switch14, switch23 )
        self.addLink( switch14, switch24 )

        self.addLink( switch15, switch25 )
        self.addLink( switch15, switch26 )
        self.addLink( switch16, switch25 )
        self.addLink( switch16, switch26 )

        self.addLink( switch17, switch27 )
        self.addLink( switch17, switch28 )
        self.addLink( switch18, switch27 )
        self.addLink( switch18, switch28 )

        ##################################

        self.addLink( host11, switch21 )
        self.addLink( host12, switch21 )
        self.addLink( host13, switch22 )
        self.addLink( host14, switch22 )

        self.addLink( host21, switch23 )
        self.addLink( host22, switch23 )
        self.addLink( host23, switch24 )
        self.addLink( host24, switch24 )

        self.addLink( host31, switch25 )
        self.addLink( host32, switch25 )
        self.addLink( host33, switch26 )
        self.addLink( host34, switch26 )

        self.addLink( host41, switch27 )
        self.addLink( host42, switch27 )
        self.addLink( host43, switch28 )
        self.addLink( host44, switch28 )



topos = { 'mytopo': ( lambda: MyTopo() ) }
