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

if __name__ == "__main__":
    pass
