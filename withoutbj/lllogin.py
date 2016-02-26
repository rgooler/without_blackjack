# vim:fileencoding=utf8

class LLLogin():

	"""
	* Make a connection to a grid.
	* @param uri The 'well known and published' authentication URL.
	* @param credentials LLSD data that contians the credentials.
	* *NOTE:Mani The credential data can vary depending upon the authentication
	* method used. The current interface matches the values passed to
	* the XMLRPC login request.
	{
		method			:	string, 
		first			:	string,
		last			:	string,
		passwd			:	string,
		start			:	string,
		skipoptional	:	bool,
		agree_to_tos	:	bool,
		read_critical	:	bool,
		last_exec_event	:	int,
		version			:	string,
		channel			:	string,
		mac				:	string,
		id0				:	string,
		options			:   [ strings ]
	}
	 """

	method = ""
	first = ""
	last = ""
	passwd = ""
	start = ""
	skipoptional = False
	agree_to_tos = False
	read_critical = False
	last_exec_event = 0
	version = ""
	channel = ""
	mac = ""
	id0 = ""
	options = []

	def __init__(self):
		pass

	def connect(uri, credentials):
		pass

	def disconnect():
		pass

	def getEventPump():
		"""
		Event API

		LLLogin will issue multiple events to it pump to indicate the 
		progression of states through login. The most important 
		states are "offline" and "online" which indicate auth failure 
		and auth success respectively.

		pump: login (tweaked)
		These are the events posted to the 'login' 
		event pump from the login module.
		{
			state		:	string, // See below for the list of states.
			progress	:   real // for progress bar.
			data		:   LLSD // Dependent upon state.
		}
		
		States for method 'login_to_simulator'
		offline - set initially state and upon failure. data is the server response.
		srvrequest - upon uri rewrite request. no data.
		authenticating - upon auth request. data, 'attempt' number and 'request' llsd.
		downloading - upon ack from auth server, before completion. no data
		online - upon auth success. data is server response.


		Dependencies:
		pump: LLAres 
		LLLogin makes a request for a SRV record from the uri provided by the connect method.
		The following event pump should exist to service that request.
		pump name: LLAres
		request = {
			op : "rewriteURI"
			uri : string
			reply : string

		pump: LLXMLRPCListener
		The request merely passes the credentials LLSD along, with one additional 
		member, 'reply', which is the string name of the event pump to reply on. 
		"""
		pass

	

if __name__ == "__main__":
    pass
