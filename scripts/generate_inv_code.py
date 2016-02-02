# encoding=utf8

import logging

from application.models import Session, InvCode
from application.common import util


def generate_inv_code():
    sess = Session()
    inv_code = util.generate_inv_code()
    while sess.query(InvCode).filter(InvCode.code == inv_code).first():
        inv_code = util.generate_inv_code()
    sess.add(InvCode(inv_code))
    sess.commit()
    return inv_code


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    logging.info(generate_inv_code())
