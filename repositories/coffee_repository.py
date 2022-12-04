from db.run_sql import run_sql

from models.producer import Producer
from models.coffee import Coffee

import repositories.producer_repository as producer_repository

def save(coffee):
    sql = "INSERT INTO coffees (name, origin, description, producer_id, stock, buy_price, sell_price) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING *"
    values = [coffee.name, coffee.origin, coffee.description, coffee.producer.id, coffee.stock, coffee.buy_price, coffee.sell_price]
    result = run_sql(sql, values)[0]
    result_id = result['id']
    coffee.id = result_id
    return coffee

def select_all():
    coffees = []
    sql = "SELECT * FROM coffees"
    results = run_sql(sql)

    for row in results:
        producer = producer_repository.select(row['producer_id'])
        coffee = Coffee(row['name'], row['origin'], row['description'], producer, row['stock'], row['buy_price'], row['sell_price'])
        coffees.append(coffee)
    return coffees

def select(id):
    coffee = None
    sql = "SELECT * FROM coffees WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)


    if results:
        result = results[0]
        producer = producer_repository.select(result['producer_id'])
        coffee = Coffee(result['name'], result['origin'], result['description'], producer, result['buy_price'], result['sell_price'])
    return coffee

def delete_all():
    sql = "DELETE FROM coffees"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM coffees where id = %s"
    values = [id]
    run_sql(sql, values)


def update(coffee):
    sql = "UPDATE coffees SET (name, origin, description, producer_id, buy_price, sell_price) = (%s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [coffee.name, coffee.origin, coffee.description, coffee.producer.id, coffee.buy_price, coffee.sell_price, coffee.id]
    run_sql(sql, values)
