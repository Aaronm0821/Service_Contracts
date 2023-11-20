from sqlalchemy.orm import Session

from models import models
from pydantic_schemas import contracts_schemas


def get_contract_by_id(db: Session, contract_id: int):
    return db.query(models.Contracts).filter(models.Contracts.id == contract_id).first()


def create_contract(db: Session, contract: contracts_schemas.ContractsBase):
    db_contract = models.Contracts(
        service_contract=contract.service_contract,
        start_date=contract.start_date,
        end_date=contract.end_date,
        last_pm=contract.last_PM,
        next_pm=contract.next_PM,
        machin_id=contract.machine_id
    )
    db.add(db_contract)
    db.commit()
    db.refresh(db_contract)



