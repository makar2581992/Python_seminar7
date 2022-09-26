import input
import impo
import export
import log



def start():
    if input.mod() == '1':
        if input.get_data() == '1':
            info = input.exp()
            export.get_data(info)
        else:
            info = input.name()
            export.get_data(info)
            log.log_info(info)
    else:
        info = input.inpp()
        impo.impo(info)
        log.log_info(info)