import logging
import sys

import maya

from functools import partial


def remove_include_module(name):
    logger = logging.getLogger("mayarepacker")

    module_list = [_ for _ in sys.modules]
    module_list.sort()

    # send_message_list = []
    # send_message_list.append("================================================")
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
        # send_message_list.append("reloaded : {}".format(first_hit_parent_module))
        logger.info("reloaded : {}".format(first_hit_parent_module))

    # send_message_list.append("================================================")
    logger.info("================================================")

    # send_message_list.reverse()

    # for send_message in send_message_list:
    #     maya.utils.executeDeferred(partial(logger.info, send_message))
