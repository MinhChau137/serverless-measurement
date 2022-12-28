IMAGE_NAME = "29061999/knative-video-detection:v1.2"
STATUS_PULL_COMPLETE = "Pull complete"
SLEEP_TIME = 0.1

# HOST IP
MASTER_HOST = "192.168.101.100"
MASTER_USERNAME = "controller"
MASTER_PASSWORD = "1"
PI_IP = "192.168.101.105"
PI_USERNAME = "pi4knative"
PI_PASSWORD = "1"

SERVER_HOSTNAME = "server"
SERVER_INSTANCE = "192.168.101.101"

# PORT
PROMETHEUS_PORT = "9090"

# Common
COLON = ":"
SLASH = "/"
TEST_MODE = False

# Network interfacte
NETWORK_INTERFACE = "ens33"

PROMETHEUS_DOMAIN = "http://"+ MASTER_HOST + COLON + PROMETHEUS_PORT +"/api/v1/query?query="
SERVICE_DOMAIN = "http://detection.default.svc.cluster.local"

# QUERY
VALUES_CPU_QUERY = "100-(avg%20by%20(instance,job)(irate(node_cpu_seconds_total{mode='idle',job='node_exporter',instance='"+SERVER_INSTANCE+":9100'}[30s])*100))"
VALUES_MEMORY_QUERY = "((node_memory_MemTotal_bytes{job='node_exporter',instance='"+SERVER_INSTANCE+":9100'}-node_memory_MemAvailable_bytes{job='node_exporter',instance='"+SERVER_INSTANCE+":9100'})/(node_memory_MemTotal_bytes{job='node_exporter',instance='"+SERVER_INSTANCE+":9100'}))*100"
VALUES_NETWORK_RECEIVE_QUERY = "rate(node_network_receive_bytes_total{device='"+NETWORK_INTERFACE+"',instance='"+SERVER_INSTANCE+":9100'}[1m])/(1024*1024)"

# FOLDER
PULLING_FOLDER = "pulling"

# FILE NAME
DATA_PULLING_IMAGE_FILENAME = "data_pulling_image_{}_{}_{}_server.csv"

# DIRECTORIES
DATA_DIRECTORY = "run_on_server/data/"
DATA_PULLING_IMAGE_FILE_DIRECTORY = DATA_DIRECTORY + SLASH + PULLING_FOLDER + SLASH + DATA_PULLING_IMAGE_FILENAME



