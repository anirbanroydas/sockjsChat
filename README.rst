========================
sockjsChat
========================

A sockJS based Chat-Server/Chat-System primary using SockJS protocol.

-------
Details
-------

:Author: Anirban Roy Das
:Email: anirban.nick@gmail.com
:Copyright(C): 2016, Anirban Roy Das <anirban.nick@gmail.com>

Check sockjsChat/LICENSE file for full Copyright notice.

--------
Overview
--------

sockjsChat is a very basic Chat Server which can be set up locally to chat in your LAN. It supports both public chat among all participants at a time and also private chat between those participants.

It uses the sockjs protocol to implement the real time message passing system. SockJS is implemented in many languages, primarily javascript to talk to servers in real time using its protocol, which tries to create a duplex bi-directional connectin between the client (browser) and the server. It first tries to create websocket connection, and if it fails then it fallbacks to other transport mechanisms, such as ajax, long polling, etc.

You can read more about the sockjs `here <https://github.com/sockjs/sockjs-client>`_

---------------
Technical Specs
---------------

:sockjs-client:  Advance Websocket Javascript Client
:Tornado: async python web server
:sockjs-tornado: sockjs websocket server implementation for Tornado

------------
Installation
------------

`````````````
Prerequisites
`````````````

1. python 2.7+
2. tornado
3. sockjs-tornado
4. sockjs-client

::
        pip install sockjsChat

If dependencies do not get installed by the above command already, then use the below steps to install them one by one.

````````````````````
Step 1 - Install pip
````````````````````

Follow the below methods for installing pip. One of them may help you to install pip in your system.

* **Method 1 -**  https://pip.pypa.io/en/stable/installing/
* **Method 2 -** http://ask.xmodulo.com/install-pip-linux.html
* **Method 3 -** If you installed python on MAC OS X via ``brew install python``, then pip is already installed along with python.



``````
Step 2
``````
::
        pip install tornado






