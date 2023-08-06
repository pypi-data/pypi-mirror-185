"""
Help text strings for pygnssutils CLI utilities

Created on 26 May 2022

:author: semuadmin
:copyright: SEMU Consulting © 2022
:license: BSD 3-Clause
"""
# pylint: disable=line-too-long

from platform import system
from pygnssutils._version import __version__ as VERSION

# console escape sequences don't work on standard Windows terminal
RED = ""
GREEN = ""
BLUE = ""
YELLOW = ""
MAGENTA = ""
CYAN = ""
BOLD = ""
NORMAL = ""
if system() != "Windows":
    RED = "\033[31m"
    GREEN = "\033[32m"
    BLUE = "\033[34m"
    YELLOW = "\033[33m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    BOLD = "\033[1m"
    NORMAL = "\033[0m"

COMMON = (
    "  baudrate: serial baud rate (9600)\n"
    + "  timeout: serial timeout in seconds (3)\n"
    + "  protfilter - 1 = NMEA, 2 = UBX, 4 = RTCM3 (7 - ALL)\n"
    + "  msgfilter - comma-separated list of required message identities e.g. NAV-PVT,GNGSA (None)\n"
    + "  limit - maximum number of messages to read (0 = unlimited)\n"
    + "  format - output format; 1 = parsed, 2 = binary (raw), 4 = hex, 8 = tabular hex, 16 = parsed as string, 32 = JSON (can be OR'd)\n"
    + "  quitonerror - 0 = ignore errors,  1 = log errors and continue, 2 = (re)raise errors (1)\n"
    + "  validate - 1 = validate message checksum, 0 = ignore invalid checksum (1)\n"
    + "  msgmode - 0 = GET, 1 = SET, 2 = POLL (0)\n"
    + "  parsebitfield - boolean True = parse UBX 'X' type attributes as bitfields, False = leave as bytes (True)\n"
)

LICENSE = (
    f"{CYAN}© 2022 SEMU Consulting BSD 3-Clause license\n"
    + "https://github.com/semuconsulting/pygnssutils/\n\n"
)

LOGOPTIONS = (
    "  verbosity - log message verbosity 0 = low, 1 = medium, 2 = high (1)\n"
    + "  logtofile - 0 = log to stdout, 1 = log to file (0)\n"
    + "  logpath - fully qualified path to logfile folder ('.')\n\n"
)

GNSSDUMP_HELP = (
    f"\n\n{RED}{BOLD}GNSSDUMP v{VERSION}\n"
    + f"=================={NORMAL}\n\n"
    + f"{BOLD}gnssdump{NORMAL} is a command line utility, provided with the"
    + f" {MAGENTA}{BOLD}pygnssutils{NORMAL} Python library, which parses the output"
    + " of a GNSS receiver to stdout (e.g. terminal), to an output file, or to a"
    + " designated external output handler.\n\n"
    + "gnssdump is capable of parsing NMEA, UBX and RTCM3 protocols.\n\n"
    + f"{GREEN}Usage (either stream, port, socket or filename must be specified):{NORMAL}\n\n"
    + "  Serial stream: gnssdump port=/dev/ttyACM0 baudrate=9600 timeout=3, **kwargs\n"
    + "  File stream: gnssdump filename=gpslog.bin, **kwargs\n"
    + "  Socket stream: gnssdump socket=192.168.0.72:50007, **kwargs\n"
    + "  Other stream object: gnssdump stream=stream, **kwargs\n"
    + f"{GREEN}Help:{NORMAL}\n\n gnssdump -h\n\n"
    + f"{GREEN}Optional keyword arguments (default):{NORMAL}\n\n"
    + COMMON
    + "  outfile - fully qualified path to output file (None)\n"
    + LOGOPTIONS
    + f"{GREEN}\nThe following optional output handlers can either be instances of writeable output"
    + f" media (serial, file, socket or queue), or evaluable Python expressions{NORMAL}:\n\n"
    + "  outputhandler - output handler (None)\n"
    + "  errorhandler - error message handler (None)\n\n"
    + f"{GREEN}Type Ctrl-C to terminate.{NORMAL}\n\n"
    + LICENSE
)

GNSSSERVER_HELP = (
    f"\n\n{RED}{BOLD}GNSSSERVER v{VERSION}\n"
    + f"===================={NORMAL}\n\n"
    + f"{BOLD}gnssserver{NORMAL} is a command line utility, provided with the"
    + f" {MAGENTA}{BOLD}pygnssutils{NORMAL} Python library, which acts as a TCP"
    + " Socket Server or NTRIP Server/Caster for GNSS data streams.\n\n"
    + "gnssserver is capable of broadcasting NMEA, UBX, RTCM3 and NTRIP protocols.\n\n"
    + f"{GREEN}Usage examples:{NORMAL}\n\n"
    + "Normal Mode:\n"
    + "  gnssserver inport=/dev/ttyACM0 hostip=192.168.0.20 outport=50010\n\n"
    + "NTRIP Server/Caster Mode:\n"
    + "  gnssserver inport=COM3 hostip=192.168.0.56 outport=2101 ntripmode=1 protfilter=4\n\n"
    + f"{GREEN}Help:{NORMAL}\n\n  gnssserver -h\n\n"
    + f"{GREEN}Optional keyword arguments (default):{NORMAL}\n\n"
    + "  ntripmode - 0 = open TCP socket server, 1 = authenticated NTRIP server (0)\n"
    + "  inport - serial port of host-connected receiver (/dev/ttyACM1)\n"
    + "  hostip - host IP address to bind to (0.0.0.0 i.e. all available IP addresses)\n"
    + "  outport - host TCP port (50010, or 2101 in NTRIP mode)\n"
    + COMMON
    + "  waittime - response wait time in seconds (1)\n"
    + LOGOPTIONS
    + f"{GREEN}Client login credentials for NTRIP Server mode are set via host environment variables "
    + f"{MAGENTA}PYGPSCLIENT_USER{GREEN} and {MAGENTA}PYGPSCLIENT_PASSWORD{NORMAL}\n\n"
    + f"{GREEN}Type Ctrl-C to terminate.{NORMAL}\n\n"
    + LICENSE
)

GNSSNTRIPCLIENT_HELP = (
    f"\n\n{RED}{BOLD}GNSS NTRIP CLIENT v{VERSION}\n"
    + f"========================={NORMAL}\n\n"
    + f"{BOLD}gnssntripclient{NORMAL} is a command line utility, provided with the"
    + f" {MAGENTA}{BOLD}pygnssutils{NORMAL} Python library, which acts as an NTRIP"
    + " client for RTCM3 RTK correction data streams.\n\n"
    + f"{GREEN}Usage examples:{NORMAL}\n\n"
    + "Get Sourcetable (leave mountpoint blank):\n"
    + "  gnssntripclient server=rtk2go.com port=2101\n\n"
    + "Get Correction Data (specify mountpoint):\n"
    + "  gnssntripclient server=rtk2go.com port=2101 mountpoint=WEBBPARTNERS\n\n"
    + f"{GREEN}Help:{NORMAL}\n\n  gnssntripclient -h\n\n"
    + f"{GREEN}Keyword arguments (default):{NORMAL}\n\n"
    + "  server - (mandatory) NTRIP server URL ('')\n"
    + "  port - NTRIP port (2101)\n"
    + "  mountpoint - NTRIP mountpoint (blank)\n"
    + "  version - NTRIP protocol version (2.0)\n"
    + "  user - NTRIP server login user (anon)\n"
    + "  password - NTRIP server login password (password)\n"
    + "  ggainterval - GGA sentence transmission interval in seconds (-1 = None)\n"
    + "  ggamode - GGA position source; 0 = receiver, 1 = fixed reference coordinates (0)\n"
    + "  reflat - reference latitude (0.0)\n"
    + "  reflon - reference longitude (0.0)\n"
    + "  refalt - reference altitude meters (0.0)\n"
    + "  refsep - reference separation from geoid meters (0.0)\n"
    + "  waittime - response wait time in seconds (3)\n"
    + LOGOPTIONS
    + f"{GREEN}Client login credentials for NTRIP Server can be set via host environment variables "
    + f"{MAGENTA}NTRIP_USER{GREEN} and {MAGENTA}NTRIP_PASSWORD{NORMAL}\n\n"
    + f"{GREEN}Type Ctrl-C to terminate.{NORMAL}\n\n"
    + LICENSE
)

UBXSETRATE_HELP = (
    f"\n\n{RED}{BOLD}UBXSETRATE v{VERSION}\n"
    + f"=================={NORMAL}\n\n"
    + f"{BOLD}ubxsetrate{NORMAL} is a simple command line utility, provided with the"
    + f" {MAGENTA}{BOLD}pygnssutils{NORMAL} Python library, which sets"
    + " NMEA or UBX message rates for u-blox GNSS receivers.\n\n"
    + f"{GREEN}Usage examples:{NORMAL}\n\n"
    + "  ubxsetrate port=/dev/ttyACM0 baudrate=38400 timeout=3 msgClass=0x01 msgID=0x14 rate=1\n\n"
    + "  ubxsetrate port=COM4 msgClass=allnmea\n\n"
    + f"{GREEN}Help:{NORMAL}\n\n  ubxsetrate -h\n\n"
    + f"{GREEN}Keyword arguments (default):{NORMAL}\n\n"
    + "  port - serial port e.g. /dev/ttyACM0 (None)\n"
    + "  baudrate - baudrate e.g. 38400 (9600)\n"
    + "  timeout - serial port timeout in secs (3)\n"
    + "  msgClass - UBX message class from pyubx2.UBX_CLASSES (e.g. 1 or 0x01), OR one of the following group values:\n"
    + "    'allubx' - all available UBX messages\n"
    + "    'minubx' - a minimum set of UBX messages (NAV-PVT, NAV-SAT)\n"
    + "    'allnmea' - all available NMEA messages\n"
    + "    'minnmea' - a minimum set of NMEA messages (GGA, GSA, GSV, RMC, VTG)\n"
    + "  msgID - UBX message ID from pyubx2.UBX_MSGIDS[1:] e.g. 20 or 0x14 (None)\n"
    + "  rate - message rate per navigation solution, 0 = off (1)\n\n"
    + LICENSE
)

UBXLOAD_HELP = (
    f"\n\n{RED}{BOLD}UBXLOAD v{VERSION}\n"
    + f"=================={NORMAL}\n\n"
    + f"{MAGENTA}{BOLD}ubxload{NORMAL} is a command line utility, provided with the"
    + f" {MAGENTA}{BOLD}pygnssutils{NORMAL} Python library, which reads binary UBX"
    + " configuration (CFG-VALSET) data from a file and loads this into a compatible"
    + " UBX device via its serial port. It then confirms that the data load has been"
    + " successfully acknowledged by the device, or reports any errors.\n\n"
    + f"{BOLD}NB:{NORMAL} For Generation 9+ UBX devices only (e.g. NEO-M9N or ZED-F9P)\n\n"
    + f"A suitable binary file can be created using the companion {MAGENTA}{BOLD}ubxsave{NORMAL} utility.\n\n"
    + f"{GREEN}Usage example:{NORMAL}\n\n"
    + "  ubxload port=/dev/ttyACM0 baudrate=38400 timeout=3 infile=ubxconfig.ubx verbosity=1 waittime=3\n\n"
    + f"{GREEN}Help:{NORMAL}\n\n  ubxload -h\n\n"
    + f"{GREEN}Keyword arguments (default):{NORMAL}\n\n"
    + "  port - serial port e.g. /dev/tty.usbmodem101 (/dev/ttyACM0)\n"
    + "  baudrate - baudrate e.g. 38400 (9600)\n"
    + "  timeout - serial port timeout in secs (3)\n"
    + "  infile - full path to binary input file (ubxconfig.ubx)\n"
    + "  verbosity - 0 = low, 1 = medium, 2 = high (1)\n"
    + "  waittime - acknowledgement wait time in secs (5)\n\n"
    + LICENSE
)

UBXSAVE_HELP = (
    f"\n\n{RED}{BOLD}UBXSAVE v{VERSION}\n"
    + f"=================={NORMAL}\n\n"
    + f"{MAGENTA}{BOLD}ubxsave{NORMAL} is a command line utility, provided with the"
    + f" {MAGENTA}{BOLD}pygnssutils{NORMAL} Python library, which polls a complete set"
    + " of configuration (CFG-VALGET) data from a UBX device and saves it to a file.\n\n"
    + f"The data can be reloaded to any compatible UBX device using the companion "
    + f"{MAGENTA}{BOLD}ubxload{NORMAL} utility.\n\n"
    + f"{BOLD}NB:{NORMAL} For Generation 9+ UBX devices only (e.g. NEO-M9N or ZED-F9P)\n\n"
    + f"{GREEN}Usage example:{NORMAL}\n\n"
    + "  ubxsave port=/dev/ttyACM0 baudrate=38400 timeout=3 outfile=ubxconfig.ubx verbosity=1\n\n"
    + f"{GREEN}Help:{NORMAL}\n\n  ubxsave -h\n\n"
    + f"{GREEN}Keyword arguments (default):{NORMAL}\n\n"
    + "  port - serial port e.g. /dev/tty.usbmodem101 (/dev/ttyACM0)\n"
    + "  baudrate - baudrate e.g. 38400 (9600)\n"
    + "  timeout - serial port timeout in secs (3)\n"
    + "  outfile - full path to binary output file (ubxconfig-YYMMDDhhmmss.ubx)\n"
    + "  verbosity - 0 = low, 1 = medium, 2 = high (1)\n\n"
    + LICENSE
)
