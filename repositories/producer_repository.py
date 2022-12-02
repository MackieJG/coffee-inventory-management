from db.run_sql import run_sql

from models.producer import Producer


def save(producer):
    sql = "INSERT INTO producers (name, location, description) VALUES (%s, %s, %s) RETURNING *"
    values = [producer.name, producer.location, producer.description]
    results = run_sql(sql, values)
    id = results[0]['id']
    producer.id = id
    return producer

def select_all():
    producers = []

    sql = "SELECT * FROM producers"
    results = run_sql(sql)

    for row in results:
        producer = Producer(row['name'], row['location'], row['description'])
        producers.append(producer)
    return producers

def select(id):
    producer = None
    sql = "SELECT * FROM producers WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        producer = Producer(result['name'], result['location'], result['description'])
    return producer

def delete_all():
    sql = "DELETE FROM producers"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM producers WHERE id = %s"
    values = [id]
    run_sql(sql, values)

