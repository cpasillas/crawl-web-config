import logging
try:
    from collections import OrderedDict
except ImportError:
    from ordereddict import OrderedDict

dgl_mode = True

bind_nonsecure = True # Set to false to only use SSL
#bind_address = ""
#bind_port = 8080
# Or listen on multiple address/port pairs (overriding the above) with:
bind_pairs = (
    ("", 8080),
    ("", 80),
)

logging_config = {
    "filename": "/data/webtiles.log",
    "level": logging.INFO,
    "format": "%(asctime)s %(levelname)s: %(message)s"
}

password_db = "/data/passwd.db3"

static_path = "/root/crawl/crawl-ref/source/webserver/static"
template_path = "./webserver/templates/"

# Path for server-side unix sockets (to be used to communicate with crawl)
server_socket_path = None # Uses global temp dir

# Server name, so far only used in the ttyrec metadata
server_id = ""

# Disable caching of game data files
game_data_no_cache = True

# Watch socket dirs for games not started by the server
watch_socket_dirs = False


VERSION_PATH = "/data/rcs/%s/"
BASE_CONF_DICT = {
    "client_path": "./webserver/game_data/",
    "morgue_url": None,
    "send_json_options": True}


def GameConfTuples(version, conf_tuple_list):
  conf_dict = BASE_CONF_DICT.copy()
  rc_path = VERSION_PATH % version
  conf_dict["rcfile_path"] = rc_path
  conf_dict["macro_path"] = rc_path
  conf_dict["morgue_path"] = rc_path + '%n'
  conf_dict["inprogress_path"] = rc_path + 'running'
  conf_dict["ttyrec_path"] = rc_path + 'ttyrecs/%n'
  conf_dict["socket_path"] = rc_path
  conf_dict['name'] = "DCSS " + version
  conf_dict['crawl_binary'] = "/root/crawlout/%s/crawl" % version
  webconf = ("dcss-" + version, conf_dict)
  #tut_dict = conf_dict.copy()
  #tut_dict['name'] = "Tutorial " + version
  #tut_dict['options'] = ['-tutorial']
  #tutconf = ("tut-web-" + version, tut_dict)
  #sprint_dict = conf_dict.copy()
  #sprint_dict['name'] = "Sprint " + version
  #sprint_dict['options'] = ['-sprint']
  #sprintconf = ("sprint-web-" + version, sprint_dict)
  conf_tuple_list.append(webconf)
  #conf_tuple_list.append(tutconf)
  #conf_tuple_list.append(sprintconf)

conf_tuple_list = []
trunk_confs = GameConfTuples('trunk', conf_tuple_list)
zero_one_nine_confs = GameConfTuples('0.19', conf_tuple_list)

# Game configs
# %n in paths and urls is replaced by the current username
# morgue_url is for a publicly available URL to access morgue_path
games = OrderedDict(conf_tuple_list)

dgl_status_file = "/data/rcs/status"

# Set to None not to read milestones
milestone_file = "./milestones"

status_file_update_rate = 5

recording_term_size = (80, 24)

max_connections = 100

# Script to initialize a user, e.g. make sure the paths
# and the rc file exist. This is not done by the server
# at the moment.
init_player_program = "./util/webtiles-init-player.sh"

ssl_options = None # No SSL
#ssl_options = {
#    "certfile": "./webserver/localhost.crt",
#    "keyfile": "./webserver/localhost.key"
#}
ssl_address = ""
ssl_port = 8081
# Or listen on multiple address/port pairs (overriding the above) with:
# ssl_bind_pairs = (
#     ("127.0.0.1", 8081),
#     ("localhost", 8083),
# )

connection_timeout = 600
max_idle_time = 5 * 60 * 60

# Seconds until stale HTTP connections are closed
# This needs a patch currently not in mainline tornado.
http_connection_timeout = None

kill_timeout = 10 # Seconds until crawl is killed after HUP is sent

nick_regex = r"^[a-zA-Z0-9]{3,20}$"
max_passwd_length = 20

# crypt() algorithm, e.g. "1" for MD5 or "6" for SHA-512; see crypt(3). If
# false, use traditional DES (but then only the first eight characters of the
# password are significant). If set to "broken", use traditional DES with
# the password itself as the salt; this is necessary for compatibility with
# dgamelaunch, but should be avoided if possible because it leaks the first
# two characters of the password's plaintext.
crypt_algorithm = "broken"

# The length of the salt string to use. If crypt_algorithm is false, this
# setting is ignored and the salt is two characters.
crypt_salt_length = 16

login_token_lifetime = 7 # Days

uid = None  # If this is not None, the server will setuid to that (numeric) id
gid = None  # after binding its sockets.

umask = None # e.g. 0077

chroot = None

pidfile = None
daemon = False # If true, the server will detach from the session after startup

# Set to a URL with %s where lowercased player name should go in order to
# hyperlink WebTiles spectator names to their player pages.
# For example: "http://crawl.akrasiac.org/scoring/players/%s.html"
# Set to None to disable player page hyperlinks
player_url = None

# Only for development:
# Disable caching of static files which are not part of game data.
no_cache = False
# Automatically log in all users with the username given here.
autologin = None
