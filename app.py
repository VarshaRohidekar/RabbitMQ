from flask import Flask, request, jsonify

app = Flask(__name__)

# Health Check Endpoint
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'ok'})

# # CRUD Operations Endpoints (sample implementation)
# inventory = []

# @app.route('/inventory', methods=['GET'])
# def get_inventory():
#     return jsonify(inventory)

# @app.route('/inventory/<int:product_id>', methods=['GET'])
# def get_product(product_id):
#     product = next((item for item in inventory if item['product_id'] == product_id), None)
#     if product:
#         return jsonify(product)
#     else:
#         return jsonify({'error': 'Product not found'}), 404

# @app.route('/inventory', methods=['POST'])
# def add_product():
#     data = request.json
#     inventory.append(data)
#     return jsonify({'message': 'Product added successfully'}), 201

# @app.route('/inventory/<int:product_id>', methods=['PUT'])
# def update_product(product_id):
#     data = request.json
#     for item in inventory:
#         if item['product_id'] == product_id:
#             item.update(data)
#             return jsonify({'message': 'Product updated successfully'})
#     return jsonify({'error': 'Product not found'}), 404

# @app.route('/inventory/<int:product_id>', methods=['DELETE'])
# def delete_product(product_id):
#     global inventory
#     inventory = [item for item in inventory if item['product_id'] != product_id]
#     return jsonify({'message': 'Product deleted successfully'})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
