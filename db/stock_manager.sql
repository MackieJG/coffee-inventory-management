DROP TABLE producers;
DROP TABLE coffees;
DROP TABLE equipment;

CREATE TABLE coffees (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    origin VARCHAR(255),
    description VARCHAR(255),
    producer_id INT REFERENCES producers(id) ON DELETE CASCADE,
    stock INT,
    buy_price INT,
    sell_price INT
);

CREATE TABLE equipment (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    description VARCHAR(255),
    producer_id INT REFERENCES producers(id) ON DELETE CASCADE,
    stock INT,
    buy_price INT,
    sell_price INT

);

CREATE TABLE producers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    location VARCHAR(255),
    description VARCHAR(255)
    
);
