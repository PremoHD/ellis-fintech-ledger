from sqlalchemy import Column, Integer, String, Numeric, JSON, TIMESTAMP
from .database import Base
import datetime

class Account(Base):
    __tablename__ = "accounts"
    account_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    type = Column(String)
    entity = Column(String)
    balance = Column(Numeric(18,2), default=0.00)
    created_at = Column(TIMESTAMP, default=datetime.datetime.utcnow)

class Transaction(Base):
    __tablename__ = "transactions"
    txn_id = Column(Integer, primary_key=True)
    txn_type = Column(String)
    amount = Column(Numeric(18,2))
    status = Column(String)
    source = Column(String)
    created_at = Column(TIMESTAMP, default=datetime.datetime.utcnow)

class LedgerEntry(Base):
    __tablename__ = "ledger_entries"
    entry_id = Column(Integer, primary_key=True)
    txn_id = Column(Integer)
    account_id = Column(Integer)
    debit = Column(Numeric(18,2), default=0)
    credit = Column(Numeric(18,2), default=0)
    created_at = Column(TIMESTAMP, default=datetime.datetime.utcnow)

class AuditLog(Base):
    __tablename__ = "audit_logs"
    audit_id = Column(Integer, primary_key=True)
    action = Column(String)
    actor = Column(String)
    txn_ref = Column(Integer)
    payload = Column(JSON)
    timestamp = Column(TIMESTAMP, default=datetime.datetime.utcnow)

class BalanceSnapshot(Base):
    __tablename__ = "balance_snapshots"
    snapshot_id = Column(Integer, primary_key=True)
    account_id = Column(Integer)
    balance = Column(Numeric(18,2))
    snapshot_time = Column(TIMESTAMP, default=datetime.datetime.utcnow)