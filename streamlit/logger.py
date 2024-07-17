import logging
import os

# Ruta de la carpeta de logs
src_dir = os.path.dirname(os.path.dirname(__file__))
log_dir = os.path.join(src_dir, 'src', 'logs')

# Crea la carpeta si no existe
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

log_file = os.path.join(log_dir, 'log_escuela.log')

def creador_logs():
    logger = logging.getLogger(__name__)

    logging.basicConfig(level=logging.DEBUG, 
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S',
                    filename = log_file, 
                    filemode = 'a')

    return logger

logger = creador_logs()