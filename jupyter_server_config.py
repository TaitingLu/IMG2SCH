# jupyter_server_config.py
c = get_config()

# don’t pop open a browser
c.ServerApp.open_browser = False

# disable any token or password prompt
c.ServerApp.token = ''
c.ServerApp.password = ''

# allow VS Code (and any origin) to talk to the server
c.ServerApp.allow_origin = '*'
c.ServerApp.allow_credentials = True
c.ServerApp.allow_remote_access = True

# (you still need this to stop the XSRF checks)
c.ServerApp.disable_check_xsrf = True
