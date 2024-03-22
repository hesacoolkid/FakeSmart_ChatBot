class InventoryManager:

  def __init__(self, db):
    self.db = db

  def check_inventory(self, product_id):
    if not product_id:
      raise ValueError("Product ID is required for inventory check.")

    try:
      product_data = self.db.get_product_data(product_id)
      if product_data:
        return product_data.get('stock', 0)
      else:
        print(f"Product {product_id} not found.")
        return 0
    except Exception as e:
      print(f"Error checking inventory for {product_id}: {e}")
      return None

  def update_inventory(self, product_id, quantity):
    if not product_id or quantity is None:
      raise ValueError(
          "Product ID and quantity are required for updating inventory.")

    try:
      current_stock = self.check_inventory(product_id)
      if current_stock is not None:
        new_stock = current_stock - quantity
        self.db.update_product_data(product_id, {'stock': new_stock})
        print(
            f"Inventory updated for product {product_id}. New stock level: {new_stock}"
        )
    except Exception as e:
      print(f"Error updating inventory for {product_id}: {e}")
