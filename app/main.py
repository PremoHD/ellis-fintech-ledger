from fastapi import FastAPI, HTTPException
from sqlalchemy.orm import Session
from .database import Base, engine, get_db
from .models import Account, Transaction, LedgerEntry, AuditLog, BalanceSnapshot
from .utils import parse_micr
import datetime

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Ellis Fintech Ledger")

@app.post("/ledger/post")
def post_transaction(event: dict, db: Session = next(get_db())):
    txn_id = event.get("transaction_id")
    amount = event.get("amount")
    from_acc_name = event.get("from_account")
    to_acc_name = event.get("to_account")

    from_acc = db.query(Account).filter(Account.name==from_acc_name).first()
    to_acc = db.query(Account).filter(Account.name==to_acc_name).first()

    if not from_acc or not to_acc:
        raise HTTPException(status_code=400, detail="Account not found")

    # Create transaction
    txn = Transaction(txn_type=event.get("type"), amount=amount, status="posted", source=event.get("entity"))
    db.add(txn)
    db.commit()
    db.refresh(txn)

    # Ledger entries (double-entry)
    debit_entry = LedgerEntry(txn_id=txn.txn_id, account_id=to_acc.account_id, debit=amount)
    credit_entry = LedgerEntry(txn_id=txn.txn_id, account_id=from_acc.account_id, credit=amount)
    db.add_all([debit_entry, credit_entry])

    # Update balances
    to_acc.balance += amount
    from_acc.balance -= amount

    # Audit log
    audit = AuditLog(action="post_transaction", actor="system", txn_ref=txn.txn_id, payload=event)
    db.add(audit)

    # Balance snapshot
    snapshot_to = BalanceSnapshot(account_id=to_acc.account_id, balance=to_acc.balance)
    snapshot_from = BalanceSnapshot(account_id=from_acc.account_id, balance=from_acc.balance)
    db.add_all([snapshot_to, snapshot_from])

    db.commit()
    return {"status": "success", "txn_id": txn.txn_id}