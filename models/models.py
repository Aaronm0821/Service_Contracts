from typing import Optional, List, Text
from sqlalchemy import ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import mapped_column, Mapped, relationship
from datetime import datetime
from apps import db




class Reps(db.Model):
    __tablename__ = "reps"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, unique=True, autoincrement=True)
    rep_first_name: Mapped[str] = mapped_column(String, index=True, nullable=False)
    rep_last_name: Mapped[str] = mapped_column(String, index=True, nullable=False)
    rep_email: Mapped[str] = mapped_column(String, index=True, nullable=False)

    customers: Mapped[List["Customer"]] = relationship(back_populates="reps")


class Customer(db.Model):
    __tablename__ = "customer"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, unique=True, autoincrement=True)
    customer_name: Mapped[str] = mapped_column(String, index=True, nullable=False)
    department: Mapped[str] = mapped_column(String, index=True, nullable=True)
    location: Mapped[str] = mapped_column(String, index=True, nullable=False)

    rep_id: Mapped[int] = mapped_column(Integer, ForeignKey("reps.id"))

    machines: Mapped[List["Machines"]] = relationship(back_populates="customers")
    reps: Mapped["Reps"] = relationship(back_populates="customers")


class Machines(db.Model):
    __tablename__ = "machines"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, unique=True, autoincrement=True)
    machine_type: Mapped[str] = mapped_column(String, index=True, nullable=False)
    serial_number: Mapped[str] = mapped_column(String, index=True, nullable=True)
    install_date: Mapped[datetime] = mapped_column(DateTime, index=True, nullable=True)
    site_survey_OCC: Mapped[str] = mapped_column(String, index=True, nullable=True)
    install_OCC: Mapped[str] = mapped_column(String, index=True, nullable=True)

    customer_id: Mapped[int] = mapped_column(Integer, ForeignKey("customer.id"))

    notes: Mapped[Optional["Notes"]] = relationship(back_populates="machines")
    customers: Mapped["Customer"] = relationship(back_populates="machines")
    contracts: Mapped[List["Contracts"]] = relationship(back_populates="machines", uselist=False)

    def as_dict(self):
        return {
            "machine_type": self.machine_type,
            "serial_number": self.serial_number,
            "install_date": self.install_date,
            "site_survey_OCC": self.site_survey_OCC,
            "customer_name": self.customers.customer_name,
            "department": self.customers.department,
            "location": self.customers.location,
            "rep_id": self.customers.rep_id,
            "service_contract": self.contracts.service_contract,
            "start_date": self.contracts.start_date,
            "end_date": self.contracts.end_date,
            "last_PM": self.contracts.last_PM,
            "next_PM": self.contracts.next_PM,
            "machine_id": self.contracts.machine_id,
            "notes": self.notes.note
        }

    @classmethod
    def get_machines(cls):
        return [i.as_dict() for i in db.session.query(cls).all()]



class Contracts(db.Model):
    __tablename__ = "contracts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, unique=True, autoincrement=True)
    service_contract: Mapped[str] = mapped_column(String, index=True, nullable=False)
    start_date: Mapped[datetime] = mapped_column(DateTime, index=True, nullable=True)
    end_date: Mapped[datetime] = mapped_column(DateTime, index=True, nullable=True)
    last_PM: Mapped[datetime] = mapped_column(DateTime, index=True, nullable=True)
    next_PM: Mapped[datetime] = mapped_column(DateTime, index=True, nullable=True)

    machine_id: Mapped[int] = mapped_column(Integer, ForeignKey("machines.id"))

    machines: Mapped["Machines"] = relationship(back_populates="contracts")


class Notes(db.Model):
    __tablename__ = "notes"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, unique=True, autoincrement=True)
    note: Mapped[str] = mapped_column(String, index=True, nullable=True)

    machines_id: Mapped[int] = mapped_column(Integer, ForeignKey("machines.id"))

    machines: Mapped["Machines"] = relationship(back_populates="notes")













