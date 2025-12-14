from .models import Account
from .database import get_db

def seed_accounts(db):
    accounts = [
        Account(name="Ellis Care Inc. Main", type="checking", entity="Ellis Care, Inc."),
        Account(name="Pending Deposits", type="suspense", entity="Ellis Care, Inc."),
        Account(name="Check Clearing", type="clearing", entity="Ellis Care, Inc."),
    ]
    db.add_all(accounts)
    db.commit()