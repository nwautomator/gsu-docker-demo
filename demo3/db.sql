CREATE TABLE messages (
    message_id int NOT NULL AUTO_INCREMENT,
    first_name varchar(255),
    last_name varchar(255),
    message varchar(255),
    PRIMARY KEY (message_id)
);

INSERT INTO messages (first_name, last_name, message) VALUES ('Bob', 'Smith', 'Hello GSU!');
INSERT INTO messages (first_name, last_name, message) VALUES ('Jane', 'Smith', 'Hello EBCS!');
