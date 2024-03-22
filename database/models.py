from datetime import datetime
from typing import List, Dict, Optional, Any


class UserModel:

  def __init__(self,
               customer_id: str,
               email: str = '',
               phone: str = '',
               interaction_history: Optional[List[Dict[Any, Any]]] = None):
    self.customer_id = customer_id
    self.email = email
    self.phone = phone
    self.interaction_history = (interaction_history
                                if interaction_history is not None else [])
    self.created_at = datetime.now()

  def to_dict(self):
    return {
        "customer_id": self.customer_id,
        "email": self.email,
        "phone": self.phone,
        "interaction_history": self.interaction_history,
        "created_at": self.created_at
    }

  @staticmethod
  def from_dict(source):
    if not source or not isinstance(source, dict):
      raise ValueError("Invalid source data for UserModel")

    # Provide a default empty string if customer_id is not found
    customer_id = source.get("customer_id", '')
    if not isinstance(customer_id, str):
      raise ValueError("customer_id must be a string")

    return UserModel(customer_id=customer_id,
                     email=source.get("email", ''),
                     phone=source.get("phone", ''),
                     interaction_history=source.get("interaction_history", []))

  def add_interaction(self, interaction: Dict):
    if not isinstance(interaction, dict):
      raise ValueError("Invalid interaction data")
    self.interaction_history.append(interaction)
