from enum import StrEnum


class ClientsEnum(StrEnum):
    PF = 'pf'
    PJ = 'pj'


class ClientsTypePK(StrEnum):
    CPF = 'cpf'
    CNPJ = 'cnpj'


def cpf_format(cpf):
    cpf_f = "{}.{}.{}/{}-{}".format(cpf[:3], cpf[3:6], cpf[6:9], cpf[9:12], cpf[12:])
    return cpf_f


def cnpj_format(cnpj):
    cnpj_f = "{}.{}.{}/{}-{}".format(cnpj[:2], cnpj[2:5], cnpj[5:8], cnpj[8:12], cnpj[12:])
    return cnpj_f
