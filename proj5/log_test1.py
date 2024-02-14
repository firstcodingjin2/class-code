import logging
import logging.config

# 모듈 호출 : logging
# Logger 생성
logging.config.fileConfig('logging.conf')
logger = logging.getLogger()

# 로깅 정보 출력
# logger.error('ERROR occurred')
# logger.info('HERE WE ARE')
# logger.debug('TEST finished')
