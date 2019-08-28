from enum import Enum


class RecordStatus(Enum):
    ACTIVE = 'ACTIVE'
    INACTIVE = 'INACTIVE'
    DELETED = 'DELETED'


class AccountAccessStatus(Enum):
    ACTIVE = 'ACTIVE'
    INACTIVE = 'BLOCKED'
    DEACTIVATED = 'DEACTIVATED'
    SUSPENDED = 'SUSPENDED'


class RoleConstant(Enum):
    ADMIN = 'ADMIN'
    USER = 'USER'

