import logging
import sys


def remove_include_module(name):
    logger = logging.getLogger("mayarepacker")

    module_list = [_ for _ in sys.modules]
    module_list.sort()

    logger.info("================================================")

    first_hit_parent_module = None
    for k in module_list:
        if k.startswith(name):
            if first_hit_parent_module is None:
                first_hit_parent_module = k

            del sys.modules[k]
            # send_message_list.append("remove module : {}".format(k))
            logger.info("remove module : {}".format(k))

    if first_hit_parent_module:
        exec("import {}".format(first_hit_parent_module))
        logger.info("reloaded : {}".format(first_hit_parent_module))

    logger.info("================================================")
