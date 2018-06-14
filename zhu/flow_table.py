#!/mininet/custom/python
# coding: utf-8

import httplib  
import json
  
class StaticFlowPusher(object):  
  
    def __init__(self, server):  
        self.server = server  
  
    def get(self, data):  
        ret = self.rest_call({}, 'GET')  
        return json.loads(ret[2])  
  
    def set(self, data):  
        ret = self.rest_call(data, 'POST')  
        return ret[0] == 200  
  
    def remove(self, objtype, data):  
        ret = self.rest_call(data, 'DELETE')  
        return ret[0] == 200  
  
    def rest_call(self, data, action):  
        #path = '/wm/staticflowentrypusher/json'
        path = '/wm/staticflowpusher/json'
        #path = '/wm/staticentrypusher/json'  
        headers = {  
            'Content-type': 'application/json',  
            'Accept': 'application/json',  
            }  
        body = json.dumps(data)  
        conn = httplib.HTTPConnection(self.server, 8080)
        print conn  
        conn.request(action, path, body, headers)  
        response = conn.getresponse()  
        ret = (response.status, response.reason, response.read())  
        print ret  
        conn.close()  
        return ret  
  
pusher = StaticFlowPusher('127.0.0.1')  #控制器ip  

#this instruction_goto_table can work

#s1--------------------------------------------------------------------
en_flow_a11 = {  #bei fen liu biao
    'switch':"00:00:00:00:00:00:00:01",  
    "name":"en_flow-mod-arp11",  
    "cookie":"0",  
    "table":"0",
    "eth_type":"0x0806",
    "eth_src":"00:00:00:00:00:01",
    "priority":"2",  
    "active":"true",
    "actions":"output=flood"
    }
en_flow_a12 = {  #bei fen liu biao
    'switch':"00:00:00:00:00:00:00:01",  
    "name":"en_flow-mod-arp12",  
    "cookie":"0",  
    "table":"0",
    "eth_type":"0x0806",
    "eth_src":"00:00:00:00:00:02",
    "priority":"2",  
    "active":"true",
    "actions":"output=flood"
    }
en_flow_a13 = {  #bei fen liu biao
    'switch':"00:00:00:00:00:00:00:01",  
    "name":"en_flow-mod-arp13",  
    "cookie":"0",  
    "table":"0",
    "eth_type":"0x0806",
    "eth_src":"00:00:00:00:00:03",
    "priority":"2",  
    "active":"true",
    "actions":"output=flood"
    }
en_flow_a14 = {  #bei fen liu biao
    'switch':"00:00:00:00:00:00:00:01",  
    "name":"en_flow-mod-arp14",  
    "cookie":"0",  
    "table":"0",
    "eth_type":"0x0806",
    "eth_src":"00:00:00:00:00:04",
    "priority":"2",  
    "active":"true",
    "actions":"output=flood"
    }


en_flow_11 = {  #bei fen liu biao 
    'switch':"00:00:00:00:00:00:00:01",
    "name":"en_flow-mod-11",
    "cookie":"0",
    "table":"0",
    "eth_type":"0x0800",
    "ipv4_dst":"10.0.0.1",
    "priority":"2",
    "active":"true",
    "actions":"output=1"
    }
en_flow_12 = {  #bei fen liu biao 
    'switch':"00:00:00:00:00:00:00:01",
    "name":"en_flow-mod-12",
    "cookie":"0",
    "table":"0",
    "eth_type":"0x0800",
    "ipv4_dst":"10.0.0.2",
    "priority":"2",
    "active":"true",
    "actions":"output=2"
    }
en_flow_13 = {  #bei fen liu biao 
    'switch':"00:00:00:00:00:00:00:01",
    "name":"en_flow-mod-13",
    "cookie":"0",
    "table":"0",
    "eth_type":"0x0800",
    "ipv4_dst":"10.0.0.3",
    "priority":"2",
    "active":"true",
    "actions":"output=4"
    }
en_flow_14 = {  #bei fen liu biao 
    'switch':"00:00:00:00:00:00:00:01",
    "name":"en_flow-mod-14",
    "cookie":"0",
    "table":"0",
    "eth_type":"0x0800",
    "ipv4_dst":"10.0.0.4",
    "priority":"2",
    "active":"true",
    "actions":"output=4"
    }

#s1--------------------------------------------------------------------

#s2--------------------------------------------------------------------
en_flow_21 = {  #bei fen liu biao 
    'switch':"00:00:00:00:00:00:00:02",
    "name":"en_flow-mod-21",
    "cookie":"0",  
    "table":"0",
    "in_port":"1",
    "priority":"2",
    "active":"true",
    "actions":"output=2"
    }
en_flow_22 = {  #bei fen liu biao 
    'switch':"00:00:00:00:00:00:00:02",
    "name":"en_flow-mod-22",
    "cookie":"0",
    "table":"0",
    "in_port":"2",
    "priority":"2",
    "active":"true",
    "actions":"output=1"
    }

#s2--------------------------------------------------------------------

#s3--------------------------------------------------------------------
en_flow_31 = {  #bei fen liu biao 
    'switch':"00:00:00:00:00:00:00:03",
    "name":"en_flow-mod-31",
    "cookie":"0",
    "table":"0",
    "in_port":"1",
    "priority":"2",
    "active":"true",
    "actions":"output=2"
    }
en_flow_32 = {  #bei fen liu biao 
    'switch':"00:00:00:00:00:00:00:03",
    "name":"en_flow-mod-32",
    "cookie":"0",
    "table":"0",
    "in_port":"2",
    "priority":"2",
    "active":"true",
    "actions":"output=1"
    }


#s3--------------------------------------------------------------------

#s4--------------------------------------------------------------------
en_flow_a41 = {  #bei fen liu biao
    'switch':"00:00:00:00:00:00:00:04",  
    "name":"en_flow-mod-arp41",  
    "cookie":"0",  
    "table":"0",
    "eth_type":"0x0806",
    "eth_src":"00:00:00:00:00:01",
    "priority":"2",  
    "active":"true",
    "actions":"output=flood"
    }
en_flow_a42 = {  #bei fen liu biao
    'switch':"00:00:00:00:00:00:00:04",  
    "name":"en_flow-mod-arp42",  
    "cookie":"0",  
    "table":"0",
    "eth_type":"0x0806",
    "eth_src":"00:00:00:00:00:02",
    "priority":"2",  
    "active":"true",
    "actions":"output=flood"
    }
en_flow_a43 = {  #bei fen liu biao
    'switch':"00:00:00:00:00:00:00:04",  
    "name":"en_flow-mod-arp43",  
    "cookie":"0",  
    "table":"0",
    "eth_type":"0x0806",
    "eth_src":"00:00:00:00:00:03",
    "priority":"2",  
    "active":"true",
    "actions":"output=flood"
    }
en_flow_a44 = {  #bei fen liu biao
    'switch':"00:00:00:00:00:00:00:04",  
    "name":"en_flow-mod-arp44",  
    "cookie":"0",  
    "table":"0",
    "eth_type":"0x0806",
    "eth_src":"00:00:00:00:00:04",
    "priority":"2",  
    "active":"true",
    "actions":"output=flood"
    }


en_flow_41 = {  #bei fen liu biao 
    'switch':"00:00:00:00:00:00:00:04",
    "name":"en_flow-mod-41",
    "cookie":"0",
    "table":"0",
    "eth_type":"0x0800",
    "ipv4_dst":"10.0.0.1",
    "priority":"2",
    "active":"true",
    "actions":"output=1"
    }
en_flow_42 = {  #bei fen liu biao 
    'switch':"00:00:00:00:00:00:00:04",
    "name":"en_flow-mod-42",
    "cookie":"0",
    "table":"0",
    "eth_type":"0x0800",
    "ipv4_dst":"10.0.0.2",
    "priority":"2",
    "active":"true",
    "actions":"output=1"
    }
en_flow_43 = {  #bei fen liu biao 
    'switch':"00:00:00:00:00:00:00:04",
    "name":"en_flow-mod-43",
    "cookie":"0",
    "table":"0",
    "eth_type":"0x0800",
    "ipv4_dst":"10.0.0.3",
    "priority":"2",
    "active":"true",
     "actions":"output=3"
    }
en_flow_44 = {  #bei fen liu biao 
    'switch':"00:00:00:00:00:00:00:04",
    "name":"en_flow-mod-44",
    "cookie":"0",
    "table":"0",
    "eth_type":"0x0800",
    "ipv4_dst":"10.0.0.4",
    "priority":"2",
    "active":"true",
    "actions":"output=4"
    }

#s4--------------------------------------------------------------------


pusher.set(en_flow_a11)
pusher.set(en_flow_a12)
pusher.set(en_flow_a13)
pusher.set(en_flow_a14)
pusher.set(en_flow_11)
pusher.set(en_flow_12)
pusher.set(en_flow_13)
pusher.set(en_flow_14)


pusher.set(en_flow_21)
pusher.set(en_flow_22)

pusher.set(en_flow_31)
pusher.set(en_flow_32)

pusher.set(en_flow_a41)
pusher.set(en_flow_a42)
pusher.set(en_flow_a43)
pusher.set(en_flow_a44)
pusher.set(en_flow_41)
pusher.set(en_flow_42)
pusher.set(en_flow_43)
pusher.set(en_flow_44)

